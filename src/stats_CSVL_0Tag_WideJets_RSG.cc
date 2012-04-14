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
const char* PAR_NAMES[9]    = { "xs", "lumi", "jes", "jer", "eff",  "bkg norm",        "p1",        "p2",        "p3" };
      double PAR_GUESSES[9] = {  0.1,  4976.,   1.0,   1.0,   0.5, 2.28123e-01, 8.50964e+00, 5.42146e+00,  5.21746e-02 };
const double PAR_MIN[9]     = {  0.0,    0.0,   0.0,   0.0,   0.0,      -9999.,      -9999.,      -9999.,       -9999. };
const double PAR_MAX[9]     = { 1.E6,  6000.,   2.0,   2.0,   1.0,       9999.,       9999.,       9999.,        9999. };
const double PAR_ERR[9]     = { 0.01,   110.,  0.04,  0.10,  0.01,      1e-02,        1e-01,       1e-01,        1e-02 };
const int PAR_TYPE[9]       = {    1,      1,     1,     1,     1,          0,            0,           0,            0 }; // 1 = signal, 0 = background
const int PAR_NUIS[9]       = {    0,      0,     0,     0,     0,          0,            0,           0,            0 }; // 1 = nuisance parameter, 0 = not varied (the POI is not a nuisance parameter)

// branching ratio for bbbar final state (calculated wrt to the branching ratio for jet-jet final state)
double BR = 0.5;

// CSVL 0- and 2-tag efficienies for bbbar, qqbar (q=u,d,s), and gg final states
double masses_eff[5] = {500.0, 700.0, 1200.0, 2000.0, 3500.0};
double eff0_bb[5] = {0.07566560750023392, 0.093798093658347556, 0.17686842960103721, 0.32036809763587371, 0.43667447888414251};
double eff2_bb[5] = {0.52048508104426927, 0.47659587963276495, 0.32554327768229174, 0.18630154927758516, 0.1179460173756543};
double eff0_qq[5] = {0.78212481758405927, 0.77461177040139884, 0.75412365824006677, 0.70035464726177254, 0.61340398303170407};
double eff2_qq[5] = {0.014641303616731121, 0.013266703827432736, 0.01697287708152773, 0.02904675986456649, 0.04811499917189839};
double eff0_gg[5] = {0.81287049953731338, 0.80087221942094577, 0.78140021589889264, 0.72823533245435979, 0.60131755978964641};
double eff2_gg[5] = {0.0099198174690723652, 0.011567194364297834, 0.013782307728850961, 0.022187987310310575, 0.052889196215636237};

TGraph *g_eff0_bb = new TGraph(5, masses_eff,eff0_bb);
TGraph *g_eff2_bb = new TGraph(5, masses_eff,eff2_bb);
TGraph *g_eff0_qq = new TGraph(5, masses_eff,eff0_qq);
TGraph *g_eff2_qq = new TGraph(5, masses_eff,eff2_qq);
TGraph *g_eff0_gg = new TGraph(5, masses_eff,eff0_gg);
TGraph *g_eff2_gg = new TGraph(5, masses_eff,eff2_gg);

TH1D* HIST=0; // signal histogram
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
    cout << "Usage: stats signalmass [bbbar_BR]" << endl;
    return 0;
  }

  SIGMASS = atof(argv[1]);
  int masspoint = int(SIGMASS);

  if(argc>2) BR = atof(argv[2]);
  
  // 0-tag efficiency
  PAR_GUESSES[4] = g_eff0_bb->Eval(SIGMASS)*BR + 0.5*(g_eff0_qq->Eval(SIGMASS) + g_eff0_gg->Eval(SIGMASS))*(1-BR);

  // input file names
  INPUTFILES.push_back("Data_and_ResonanceShapes/Final__histograms_CSVL_0Tag_WideJets.root");
  
  // setup the signal histogram
  TFile* histfile=new TFile("Data_and_ResonanceShapes/Resonance_Shapes_WideJets_gg.root");
  
  ostringstream histname, cdfname, outputfile;
  histname << "h_gg_" << masspoint;
  cdfname << "h_gg_" << masspoint << "_cdf";
  
  HIST=(TH1D*)histfile->Get(histname.str().c_str());
  HISTCDF=(TH1D*)histfile->Get(cdfname.str().c_str());
  
  assert(HIST && HISTCDF && SIGMASS>0);
  
  // get the data
  TH1D* data=getData(INPUTFILES, "DATA__cutHisto_allPreviousCuts________DijetMass", NBINS-1, BOUNDARIES);
  
  // create the output file
  outputfile << OUTPUTFILE.substr(0,OUTPUTFILE.find(".root")) << "_" << masspoint << "_" << BR << ".root";
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
  fit_data.setPrintLevel(0);
  for(int i=0; i<NPARS; i++) fit_data.defineParameter(i, PAR_NAMES[i], initfit.getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // perform a background-only fit
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]==1 || PAR_MIN[i]==PAR_MAX[i]) fit_data.fixParameter(i);
  fit_data.setParameter(POIINDEX, 0.0); // set the POI value to 0
  fit_data.doFit();
  fit_data.calcPull("pull_bkg_0")->Write();
  fit_data.calcDiff("diff_bkg_0")->Write();
  fit_data.write("fit_bkg_0");

  // fix the ranges for the background parameters before calculating the posterior
  for(int i=0; i<NPARS; i++) {
    if(PAR_TYPE[i]==0 && PAR_NUIS[i]==1) {
      double val, err;
      fit_data.getParameter(i, val, err);
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
	fit.setParLimits(i, val-err, val+err);
      }
    }

    TGraph* post=fit.calculatePosterior(NSAMPLES);
    post->Write((string("post")+pestr.str()).c_str());

    // put the ranges back in place
    for(int i=0; i<NPARS; i++) {
      if(PAR_TYPE[i]==0 && PAR_NUIS[i]==1) {
	fit.setParLimits(i, PAR_MIN[i], PAR_MAX[i]);
      }
    }

    // evaluate the limit
    pair<double, double> bounds=evaluateInterval(post, ALPHA, LEFTSIDETAIL);
    if(bounds.second!=0.)
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
