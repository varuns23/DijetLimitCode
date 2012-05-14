#include <iostream>
#include <cmath>
#include <cassert>
#include <sstream>

#include <TGraph.h>
#include <TFile.h>
#include <TH1D.h>
#include <TCanvas.h>
#include <TF1.h>
#include <TMath.h>
#include <TROOT.h>
#include <TMatrixD.h>

#include "binneddata.hh"
#include "fit.hh"
#include "statistics.hh"

using namespace std;

////////////////////////////////////////////////////////////////////////////////
// magic numbers
////////////////////////////////////////////////////////////////////////////////

// number of pseudoexperiments
const int NPES=0; // 100

// number of samples of nuisance parameters for Bayesian MC integration
const int NSAMPLES=0; // 1000

// alpha (1-alpha=confidence interval)
const double ALPHA=0.05;

// left side tail
const double LEFTSIDETAIL=0.0;

// output file name
const string OUTPUTFILE="stats.root";

// input files vector
vector<string> INPUTFILES;

// histogram binning
const int NBINS=39;
double BOUNDARIES[NBINS] = {  890,  944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530,
                             1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546,
                             2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058 };

// parameters
double SIGMASS=0;
const int NPARS=9;
const int POIINDEX=0; // which parameter is "of interest"
const char* PAR_NAMES[9]    = { "xs", "lumi", "jes", "jer", "eff",  "bkg norm",        "p1",        "p2",         "p3" };
      double PAR_GUESSES[9] = {  0.1,  4976.,   1.0,   1.0,   0.4, 9.61568e-03, 6.58057e+00, 6.14410e+00,  1.59594e-01 };
const double PAR_MIN[9]     = {  0.0,    0.0,   0.0,   0.0,   0.0,      -9999.,      -9999.,      -9999.,       -9999. };
const double PAR_MAX[9]     = { 1.E6,  6000.,   2.0,   2.0,   1.0,       9999.,       9999.,       9999.,        9999. };
      double PAR_ERR[9]     = { 0.01,   110.,  0.03,  0.10,  0.04,      1e-02,        1e-01,       1e-01,        1e-02 };
const int PAR_TYPE[9]       = {    1,      1,     1,     1,     1,          0,            0,           0,            0 }; // 1 = signal, 0 = background
const int PAR_NUIS[9]       = {    0,      1,     1,     1,     1,          1,            0,           0,            0 }; // 1 = nuisance parameter, 0 = not varied (the POI is not a nuisance parameter)

// turn on/off the use of diagonal basis
int USE_DIAG_BASIS = 0;

// background fit parameters in diagonal basis
//                                      "p0'"       "p1'"       "p2'"        "p3'"
const double PAR_DIAG[4]     = {       8.554,      4.514,      1.343,       -1.121 };
const double PAR_ERR_DIAG[4] = {   0.0747718,  0.0147702, 0.00355092,  0.000258098 };

// branching ratio for bbbar final state (calculated wrt to the branching ratio for jet-jet final state)
double BR = 1.;

// light flavor resonance shape
string LFRS = "gg";

// CSVM 0- and 2-tag efficienies and efficieny erros for heavy and light flavor final states
double masses_eff[5] = {500.0, 700.0, 1200.0, 2000.0, 3500.0};
double eff0_h[5] = {0.16798716163169919, 0.21224111240704921, 0.39341468290622961, 0.60489840598104605, 0.71507983127742547};
double eff2_h[5] = {0.34639831542457067, 0.2894846919788272, 0.13766108321114659, 0.047756211824172577, 0.024802922727369742};
double eff0_l[5] = {0.9463027926797538, 0.9365073030766431, 0.918217090004583, 0.8945947299900272, 0.8354228549520759};
double eff2_l[5] = {0.0006734326117105626, 0.0012648521715485266, 0.00189397840672012, 0.0035695287821486833, 0.0068609139082176675};
// errors are from CSVL
double eff0_err_h[5] = {0.010219706183534143, 0.012473030851601145, 0.019620181633986555, 0.040560602922774504, 0.039263984277089076};
double eff2_err_h[5] = {0.02697328322836535, 0.027583170855405945, 0.02628211062017828, 0.030936028907094185, 0.020878956880156428};
double eff0_err_l[5] = {0.029358140867892124, 0.03115511213973088, 0.027825440734214335, 0.049341830230287376, 0.053193566695665884};
double eff2_err_l[5] = {0.004479227093928947, 0.0021581241053966384, 0.0038998893349127817, 0.010703628288447613, 0.016813324716293876};

TGraph *g_eff0_h = new TGraph(5, masses_eff, eff0_h);
TGraph *g_eff2_h = new TGraph(5, masses_eff, eff2_h);
TGraph *g_eff0_l = new TGraph(5, masses_eff, eff0_l);
TGraph *g_eff2_l = new TGraph(5, masses_eff, eff2_l);

TGraph *g_eff0_err_h = new TGraph(5, masses_eff, eff0_err_h);
TGraph *g_eff2_err_h = new TGraph(5, masses_eff, eff2_err_h);
TGraph *g_eff0_err_l = new TGraph(5, masses_eff, eff0_err_l);
TGraph *g_eff2_err_l = new TGraph(5, masses_eff, eff2_err_l);


TH1D* HISTCDF=0; // signal CDF


////////////////////////////////////////////////////////////////////////////////
// function integral
////////////////////////////////////////////////////////////////////////////////
double INTEGRAL(double *x0, double *xf, double *par)
{
  double xs=par[0];
  double lumi=par[1];
  double jes=par[2];
  double jer=par[3];
  double eff=par[4];
  double norm=par[5];
  double p1=par[6];
  double p2=par[7];
  double p3=par[8];

  if( USE_DIAG_BASIS )
  {
    double data[] = {
        0.04095,     -0.1166,     -0.4859,     -0.8652,
          0.998,    -0.02439,     0.05418,      0.0201,
        0.01794,      0.9548,      0.1853,     -0.2319,
        0.04399,      0.2725,     -0.8524,      0.4441
    };

    TMatrixD T = TMatrixD(4,4);
    T.SetMatrixArray(data);

    norm = T(0,0)*par[5] + T(0,1)*par[6] + T(0,2)*par[7] + T(0,3)*par[8];
    p1   = T(1,0)*par[5] + T(1,1)*par[6] + T(1,2)*par[7] + T(1,3)*par[8];
    p2   = T(2,0)*par[5] + T(2,1)*par[6] + T(2,2)*par[7] + T(2,3)*par[8];
    p3   = T(3,0)*par[5] + T(3,1)*par[6] + T(3,2)*par[7] + T(3,3)*par[8];
  }

  // uses Simpson's 3/8th rule to compute the background integral over a short interval
  // also use a power series expansion to determine the intermediate intervals since the pow() call is expensive

  double dx=(xf[0]-x0[0])/3./7000.;
  double x=x0[0]/7000.0;
  double logx=log(x);

  double a=pow(1-x,p1)/pow(x,p2+p3*logx);
  double b=dx*a/x/(x-1)*(p2+p1*x-p2*x-2*p3*(x-1)*logx);
  double c=0.5*dx*dx*a*( (p1-1)*p1/(x-1)/(x-1) - 2*p1*(p2+2*p3*logx)/(x-1)/x + (p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/x/x );
  double d=0.166666667*dx*dx*dx*a*( (p1-2)*(p1-1)*p1/(x-1)/(x-1)/(x-1) - 3*(p1-1)*p1*(p2+2*p3*logx)/(x-1)/(x-1)/x - (1+p2+2*p3*logx)*(p2*(2+p2) - 6*p3 + 4*p3*logx*(1+p2*p3*logx))/x/x/x + 3*p1*(p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/(x-1)/x/x );

  double bkg=(xf[0]-x0[0])*norm*(a+0.375*(b+c+d)+0.375*(2*b+4*c+8*d)+0.125*(3*b+9*c+27*d));
  if(bkg<0.) bkg=0.0000001;

  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf[0]-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0[0]-SIGMASS)+SIGMASS);
  int bin1=HISTCDF->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF->GetNbinsX()) bin1=HISTCDF->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF->GetNbinsX()) bin2=HISTCDF->GetNbinsX();
  double sig=xs*eff*lumi*(HISTCDF->GetBinContent(bin1)-HISTCDF->GetBinContent(bin2));

  return bkg+sig;
}

////////////////////////////////////////////////////////////////////////////////
// main function
////////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
  if(argc<=1) {
    cout << "Usage: stats signalmass [BR LFRS]" << endl;
    return 0;
  }

  SIGMASS = atof(argv[1]);
  int masspoint = int(SIGMASS);

  if(argc>2) BR = atof(argv[2]);
  if(argc>3) LFRS = argv[3];

  if( USE_DIAG_BASIS )
  {
    PAR_GUESSES[5] = PAR_DIAG[0]; PAR_GUESSES[6] = PAR_DIAG[1]; PAR_GUESSES[7] = PAR_DIAG[2]; PAR_GUESSES[8] = PAR_DIAG[3];
    PAR_ERR[5] = PAR_ERR_DIAG[0]; PAR_ERR[6] = PAR_ERR_DIAG[1]; PAR_ERR[7] = PAR_ERR_DIAG[2]; PAR_ERR[8] = PAR_ERR_DIAG[3];
  }

  // set 1-tag efficiency and efficiency errors
  PAR_GUESSES[4] = 1 - (g_eff0_h->Eval(SIGMASS)*BR + g_eff0_l->Eval(SIGMASS)*(1-BR)) - (g_eff2_h->Eval(SIGMASS)*BR + g_eff2_l->Eval(SIGMASS)*(1-BR));
  PAR_ERR[4] = sqrt( pow(g_eff0_err_h->Eval(SIGMASS)*BR,2) + pow(g_eff0_err_l->Eval(SIGMASS)*(1-BR),2) + pow(g_eff2_err_h->Eval(SIGMASS)*BR,2) + pow(g_eff2_err_l->Eval(SIGMASS)*(1-BR),2) );

  // input file names
  INPUTFILES.push_back("Data_and_ResonanceShapes/Final__histograms_CSVM_1Tag_WideJets.root");

  // setup the signal histogram
  string filename1 = "Data_and_ResonanceShapes/Resonance_Shapes_WideJets_bb.root";
  string filename2 = "Data_and_ResonanceShapes/Resonance_Shapes_WideJets_" + LFRS + ".root";

  ostringstream histname1, histname2;
  histname1 << "h_bb_" << masspoint;
  histname2 << "h_" << LFRS << "_" << masspoint;

  HISTCDF=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, (1-g_eff0_h->Eval(SIGMASS)-g_eff2_h->Eval(SIGMASS)), (1-g_eff0_l->Eval(SIGMASS)-g_eff2_l->Eval(SIGMASS)));

  assert(HISTCDF && SIGMASS>0);

  // get the data
  TH1D* data=getData(INPUTFILES, "DATA__cutHisto_allPreviousCuts________DijetMass", NBINS-1, BOUNDARIES);

  // create the output file
  ostringstream outputfile;
  outputfile << OUTPUTFILE.substr(0,OUTPUTFILE.find(".root")) << "_" << masspoint << "_" << BR << "_" << LFRS << ".root";
  TFile* rootfile=new TFile(outputfile.str().c_str(), "RECREATE");  rootfile->cd();

  // setup an initial fitter to perform a background-only fit
  Fitter initfit(data, INTEGRAL);
  for(int i=0; i<NPARS; i++) initfit.defineParameter(i, PAR_NAMES[i], PAR_GUESSES[i], PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // do an initial background-only fit, first
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]==1 || PAR_MIN[i]==PAR_MAX[i]) initfit.fixParameter(i);
  initfit.setParameter(POIINDEX, 0.0); // set the POI value to 0
  initfit.doFit();
  initfit.calcPull("pull_bkg_init")->Write();
  initfit.calcDiff("diff_bkg_init")->Write();
  initfit.write("fit_bkg_init");

  // setup the limit values
  double observedLowerBound, observedUpperBound;
  vector<double> expectedLowerBounds;
  vector<double> expectedUpperBounds;

  cout << "*********** pe=0 (data) ***********" << endl;

  // setup the fitter with the input from the background-only fit
  Fitter fit_data(data, INTEGRAL);
  fit_data.setPOIIndex(POIINDEX);
  //fit_data.setPrintLevel(0);
  for(int i=0; i<NPARS; i++) fit_data.defineParameter(i, PAR_NAMES[i], initfit.getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // perform a background-only fit
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]==1 || PAR_MIN[i]==PAR_MAX[i]) fit_data.fixParameter(i);
  fit_data.setParameter(POIINDEX, 0.0); // set the POI value to 0
  fit_data.doFit();
  fit_data.setPrintLevel(0);
  fit_data.calcPull("pull_bkg_0")->Write();
  fit_data.calcDiff("diff_bkg_0")->Write();
  fit_data.write("fit_bkg_0");

  // fix the ranges for the background parameters before calculating the posterior
  for(int i=0; i<NPARS; i++) {
    if(PAR_TYPE[i]==0 && PAR_NUIS[i]==1) {
      double val, err;
      fit_data.getParameter(i, val, err);
      if(USE_DIAG_BASIS) err = PAR_ERR[i];
      fit_data.setParLimits(i, val-err, val+err);
    }
  }

  TGraph* post_data=fit_data.calculatePosterior(NSAMPLES);
  post_data->Write("post_0");

  // put the ranges back in place
  for(int i=0; i<NPARS; i++) {
    if(PAR_TYPE[i]==0 && PAR_NUIS[i]==1) {
      fit_data.setParLimits(i, PAR_MIN[i], PAR_MAX[i]);
    }
  }

  // evaluate the limit
  pair<double, double> bounds_data=evaluateInterval(post_data, ALPHA, LEFTSIDETAIL);
  observedLowerBound=bounds_data.first;
  observedUpperBound=bounds_data.second;

  // perform the PEs (0 = data)
  for(int pe=1; pe<=NPES; ++pe) {

    cout << "*********** pe=" << pe << " ***********" << endl;
    ostringstream pestr;
    pestr << "_" << pe;

    // setup the fitter with the input from the background-only fit
    TH1D* hist = fit_data.makePseudoData((string("data")+pestr.str()).c_str());
    Fitter fit(hist, INTEGRAL);
    fit.setPOIIndex(POIINDEX);
    fit.setPrintLevel(0);
    for(int i=0; i<NPARS; i++) fit.defineParameter(i, PAR_NAMES[i], fit_data.getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

    // perform a background-only fit
    for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]==1 || PAR_MIN[i]==PAR_MAX[i]) fit.fixParameter(i);
    fit.setParameter(POIINDEX, 0.0); // set the POI value to 0
    fit.doFit();
    fit.calcPull((string("pull_bkg")+pestr.str()).c_str())->Write();
    fit.calcDiff((string("diff_bkg")+pestr.str()).c_str())->Write();
    fit.write((string("fit_bkg")+pestr.str()).c_str());

    // fix the ranges for the background parameters before calculating the posterior
    for(int i=0; i<NPARS; i++) {
      if(PAR_TYPE[i]==0 && PAR_NUIS[i]==1) {
	double val, err;
	fit.getParameter(i, val, err);
        if(USE_DIAG_BASIS) err = PAR_ERR[i];
	fit.setParLimits(i, val-err, val+err);
      }
    }

    TGraph* post=fit.calculatePosterior(NSAMPLES);
    post->Write((string("post")+pestr.str()).c_str());
    if(fit.callLimitReached()) {
      cout << "************************************************************" << endl
           << "*** Call limit reached. Skipping this pseudo-experiment. ***" << endl
           << "************************************************************" << endl;
      continue;
    }

    // put the ranges back in place
    for(int i=0; i<NPARS; i++) {
      if(PAR_TYPE[i]==0 && PAR_NUIS[i]==1) {
	fit.setParLimits(i, PAR_MIN[i], PAR_MAX[i]);
      }
    }

    // evaluate the limit
    pair<double, double> bounds=evaluateInterval(post, ALPHA, LEFTSIDETAIL);
    if(bounds.first==0. && bounds.second>0.)
    {
      expectedLowerBounds.push_back(bounds.first);
      expectedUpperBounds.push_back(bounds.second);
    }
  }

  ////////////////////////////////////////////////////////////////////////////////
  // print the results
  ////////////////////////////////////////////////////////////////////////////////

  cout << "**********************************************************************" << endl;
  for(unsigned int i=0; i<expectedLowerBounds.size(); i++)
    cout << "expected bound(" << (i+1) << ") = [ " << expectedLowerBounds[i] << " , " << expectedUpperBounds[i] << " ]" << endl;

  cout << "\nobserved bound = [ " << observedLowerBound << " , " << observedUpperBound << " ]" << endl;

  if(LEFTSIDETAIL>0.0 && NPES>0) {
    cout << "\n***** expected lower bounds *****" << endl;
    double median;
    pair<double, double> onesigma;
    pair<double, double> twosigma;
    getQuantiles(expectedLowerBounds, median, onesigma, twosigma);
    cout << "median: " << median << endl;
    cout << "+/-1 sigma band: [ " << onesigma.first << " , " << onesigma.second << " ] " << endl;
    cout << "+/-2 sigma band: [ " << twosigma.first << " , " << twosigma.second << " ] " << endl;
  }

  if(LEFTSIDETAIL<1.0 && NPES>0) {
    cout << "\n***** expected upper bounds *****" << endl;
    double median;
    pair<double, double> onesigma;
    pair<double, double> twosigma;
    getQuantiles(expectedUpperBounds, median, onesigma, twosigma);
    cout << "median: " << median << endl;
    cout << "+/-1 sigma band: [ " << onesigma.first << " , " << onesigma.second << " ] " << endl;
    cout << "+/-2 sigma band: [ " << twosigma.first << " , " << twosigma.second << " ] " << endl;
  }

  // close the output file
  rootfile->Close();

  return 0;
}
