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

// parameters
double SIGMASS=0;
const int NPARS=18;
const int POIINDEX=0; // which parameter is "of interest"
const char* PAR_NAMES[18]    = { "xs", "lumi", "jes", "jer", "eff 0", "eff 2", "norm 0",  "p1 0",  "p2 0",  "p3 0", "norm 1",  "p1 1",  "p2 1",  "p3 1", "norm 2",  "p1 2",  "p2 2",  "p3 2" };
      double PAR_GUESSES[18] = {  0.1,  4976.,   1.0,   1.0,     0.5,     0.1,      1.0,    10.0,     5.0,     0.1,      0.1,    10.0,     5.0,     0.1,      0.1,    10.0,     5.0,     0.0 };
const double PAR_MIN[18]     = {  0.0,    0.0,   0.0,   0.0,     0.0,     0.0,      0.0,     0.0,     0.0,    -5.0,      0.0,     0.0,     0.0,    -5.0,      0.0,     0.0,     0.0,     0.0 };
const double PAR_MAX[18]     = { 1.E6,  6000.,   2.0,   2.0,     1.0,     1.0,     10.0,   100.0,   100.0,     5.0,    100.0,   100.0,   100.0,     5.0,    100.0,   100.0,   100.0,     0.0 };
const double PAR_ERR[18]     = { 0.01,   110.,  0.04,  0.10,    0.05,    0.01,    1e-01,   1e-01,   1e-02,   1e-02,    1e-01,   1e-01,   1e-01,   1e-01,    1e-01,   1e-01,   1e-01,   1e-01 };
const int PAR_TYPE[18]       = {    1,      1,     1,     1,       1,       1,        0,       0,       0,       0,        0,       0,       0,       0,        0,       0,       0,       0 }; // 1 = signal, 0 = background
const int PAR_NUIS[18]       = {    0,      0,     0,     0,       0,       0,        0,       0,       0,       0,        0,       0,       0,       0,        0,       0,       0,       0 }; // 1 = nuisance parameter, 0 = not varied (the POI is not a nuisance parameter)

// histogram binning
const int NBINS=117;
double BOUNDARIES[NBINS] = {   890,   944,  1000,  1058,  1118,  1181,  1246,  1313,  1383,  1455,  1530,  1607,  1687,
                              1770,  1856,  1945,  2037,  2132,  2231,  2332,  2438,  2546,  2659,  2775,  2895,  3019,
                              3147,  3279,  3416,  3558,  3704,  3854,  4010,  4171,  4337,  4509,  4686,  4869,  5058,

                              5890,  5944,  6000,  6058,  6118,  6181,  6246,  6313,  6383,  6455,  6530,  6607,  6687,
                              6770,  6856,  6945,  7037,  7132,  7231,  7332,  7438,  7546,  7659,  7775,  7895,  8019,
                              8147,  8279,  8416,  8558,  8704,  8854,  9010,  9171,  9337,  9509,  9686,  9869, 10058,

                             10890, 10944, 11000, 11058, 11118, 11181, 11246, 11313, 11383, 11455, 11530, 11607, 11687,
                             11770, 11856, 11945, 12037, 12132, 12231, 12332, 12438, 12546, 12659, 12775, 12895, 13019,
                             13147, 13279, 13416, 13558, 13704, 13854, 14010, 14171, 14337, 14509, 14686, 14869, 15058  };

// branching ratio for bbbar final state (calculated wrt to the branching ratio for jet-jet final state)
double BR = 1.0;

// CSVM 0- and 2-tag efficienies for bbbar, qqbar (q=u,d,s), and gg final states
double masses_eff[5] = {500.0, 700.0, 1200.0, 2000.0, 3500.0};
double eff0_bb[5] = {0.17160524155130483, 0.2178887596466533, 0.40205782158559161, 0.61369094197061025, 0.71608024920020164};
double eff2_bb[5] = {0.3355981305058609, 0.27704702893132249, 0.1331710326045685, 0.046441061587059379, 0.0236514958339091};
double eff0_qq[5] = {0.95043297410694205, 0.94047460263594074, 0.92487303265003906, 0.89754860967725336, 0.84742213510088205};
double eff2_qq[5] = {0.00053069621694909008, 0.00096965811227809045, 0.0013877181542715775, 0.0042967981011906532, 0.0054955884091400092};
double eff0_gg[5] = {0.94354528372218649, 0.931068052184721, 0.91335579728577543, 0.88441354182490028, 0.80885328292438829};
double eff2_gg[5] = {0.00066170724783880448, 0.001231980726748819, 0.0022673176685648563, 0.003742365437550646, 0.011279657100275627};

TGraph *g_eff0_bb = new TGraph(5, masses_eff,eff0_bb);
TGraph *g_eff2_bb = new TGraph(5, masses_eff,eff2_bb);
TGraph *g_eff0_qq = new TGraph(5, masses_eff,eff0_qq);
TGraph *g_eff2_qq = new TGraph(5, masses_eff,eff2_qq);
TGraph *g_eff0_gg = new TGraph(5, masses_eff,eff0_gg);
TGraph *g_eff2_gg = new TGraph(5, masses_eff,eff2_gg);

TH1D* HIST_bb=0; // bbbar signal histogram
TH1D* HISTCDF_bb=0; // bbbar signal CDF
TH1D* HIST_gg=0; // gg signal histogram
TH1D* HISTCDF_gg=0; // gg signal CDF

////////////////////////////////////////////////////////////////////////////////
// function integral -- 0-tag
////////////////////////////////////////////////////////////////////////////////
double INTEGRAL_0Tag(double *fx0, double *fxf, double *par)
{
  double x0=fx0[0];
  double xf=fxf[0];
  double xs=par[0];
  double lumi=par[1];
  double jes=par[2];
  double jer=par[3];
  double eff=par[4];
  double norm=par[6];
  double p1=par[7];
  double p2=par[8];
  double p3=par[9];

  // uses Simpson's 3/8th rule to compute the background integral over a short interval
  // also use a power series expansion to determine the intermediate intervals since the pow() call is expensive

  double dx=(xf-x0)/3./7000.;
  double x=x0/7000.0;
  double logx=log(x);

  double a=pow(1-x,p1)/pow(x,p2+p3*logx);
  double b=dx*a/x/(x-1)*(p2+p1*x-p2*x-2*p3*(x-1)*logx);
  double c=0.5*dx*dx*a*( (p1-1)*p1/(x-1)/(x-1) - 2*p1*(p2+2*p3*logx)/(x-1)/x + (p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/x/x );
  double d=0.166666667*dx*dx*dx*a*( (p1-2)*(p1-1)*p1/(x-1)/(x-1)/(x-1) - 3*(p1-1)*p1*(p2+2*p3*logx)/(x-1)/(x-1)/x - (1+p2+2*p3*logx)*(p2*(2+p2) - 6*p3 + 4*p3*logx*(1+p2*p3*logx))/x/x/x + 3*p1*(p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/(x-1)/x/x );

  double bkg=(xf-x0)*norm*(a+0.375*(b+c+d)+0.375*(2*b+4*c+8*d)+0.125*(3*b+9*c+27*d));
  if(bkg<0) bkg=0.0000001;
  
  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0-SIGMASS)+SIGMASS);
  int bin1=HISTCDF_gg->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF_gg->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF_gg->GetNbinsX()) bin1=HISTCDF_gg->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF_gg->GetNbinsX()) bin2=HISTCDF_gg->GetNbinsX();
  double sig=xs*eff*lumi*(HISTCDF_gg->GetBinContent(bin1)-HISTCDF_gg->GetBinContent(bin2));

  return bkg+sig;
}

////////////////////////////////////////////////////////////////////////////////
// function integral -- 1-tag
////////////////////////////////////////////////////////////////////////////////
double INTEGRAL_1Tag(double *fx0, double *fxf, double *par)
{
  double x0=fx0[0]-5000.;
  double xf=fxf[0]-5000.;
  double xs=par[0];
  double lumi=par[1];
  double jes=par[2];
  double jer=par[3];
  double eff=1-par[4]-par[5];
  double norm=par[10];
  double p1=par[11];
  double p2=par[12];
  double p3=par[13];

  // uses Simpson's 3/8th rule to compute the background integral over a short interval
  // also use a power series expansion to determine the intermediate intervals since the pow() call is expensive

  double dx=(xf-x0)/3./7000.;
  double x=x0/7000.0;
  double logx=log(x);

  double a=pow(1-x,p1)/pow(x,p2+p3*logx);
  double b=dx*a/x/(x-1)*(p2+p1*x-p2*x-2*p3*(x-1)*logx);
  double c=0.5*dx*dx*a*( (p1-1)*p1/(x-1)/(x-1) - 2*p1*(p2+2*p3*logx)/(x-1)/x + (p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/x/x );
  double d=0.166666667*dx*dx*dx*a*( (p1-2)*(p1-1)*p1/(x-1)/(x-1)/(x-1) - 3*(p1-1)*p1*(p2+2*p3*logx)/(x-1)/(x-1)/x - (1+p2+2*p3*logx)*(p2*(2+p2) - 6*p3 + 4*p3*logx*(1+p2*p3*logx))/x/x/x + 3*p1*(p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/(x-1)/x/x );

  double bkg=(xf-x0)*norm*(a+0.375*(b+c+d)+0.375*(2*b+4*c+8*d)+0.125*(3*b+9*c+27*d));
  if(bkg<0) bkg=0.0000001;
    
  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0-SIGMASS)+SIGMASS);
  int bin1=HISTCDF_gg->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF_gg->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF_gg->GetNbinsX()) bin1=HISTCDF_gg->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF_gg->GetNbinsX()) bin2=HISTCDF_gg->GetNbinsX();
  double sig=xs*eff*lumi*(HISTCDF_gg->GetBinContent(bin1)-HISTCDF_gg->GetBinContent(bin2));

  return bkg+sig;
}

////////////////////////////////////////////////////////////////////////////////
// function integral -- 2-tag
////////////////////////////////////////////////////////////////////////////////
double INTEGRAL_2Tag(double *fx0, double *fxf, double *par)
{
  double x0=fx0[0]-10000.;
  double xf=fxf[0]-10000.;
  double xs=par[0];
  double lumi=par[1];
  double jes=par[2];
  double jer=par[3];
  double eff=par[5];
  double norm=par[14];
  double p1=par[15];
  double p2=par[16];
  double p3=par[17];

  // uses Simpson's 3/8th rule to compute the background integral over a short interval
  // also use a power series expansion to determine the intermediate intervals since the pow() call is expensive

  double dx=(xf-x0)/3./7000.;
  double x=x0/7000.0;
  double logx=log(x);

  double a=pow(1-x,p1)/pow(x,p2+p3*logx);
  double b=dx*a/x/(x-1)*(p2+p1*x-p2*x-2*p3*(x-1)*logx);
  double c=0.5*dx*dx*a*( (p1-1)*p1/(x-1)/(x-1) - 2*p1*(p2+2*p3*logx)/(x-1)/x + (p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/x/x );
  double d=0.166666667*dx*dx*dx*a*( (p1-2)*(p1-1)*p1/(x-1)/(x-1)/(x-1) - 3*(p1-1)*p1*(p2+2*p3*logx)/(x-1)/(x-1)/x - (1+p2+2*p3*logx)*(p2*(2+p2) - 6*p3 + 4*p3*logx*(1+p2*p3*logx))/x/x/x + 3*p1*(p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/(x-1)/x/x );

  double bkg=(xf-x0)*norm*(a+0.375*(b+c+d)+0.375*(2*b+4*c+8*d)+0.125*(3*b+9*c+27*d));
  if(bkg<0) bkg=0.0000001;
  
  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0-SIGMASS)+SIGMASS);
  int bin1=HISTCDF_bb->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF_bb->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF_bb->GetNbinsX()) bin1=HISTCDF_bb->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF_bb->GetNbinsX()) bin2=HISTCDF_bb->GetNbinsX();
  double sig=xs*eff*lumi*(HISTCDF_bb->GetBinContent(bin1)-HISTCDF_bb->GetBinContent(bin2));

  return bkg+sig;
}

////////////////////////////////////////////////////////////////////////////////
// main function integral
////////////////////////////////////////////////////////////////////////////////
double INTEGRAL(double *x0, double *xf, double *par)
{
  if(xf[0]<=5890.) return INTEGRAL_0Tag(x0, xf, par);

  else if(xf[0]>5890. && xf[0]<=10890.) return INTEGRAL_1Tag(x0, xf, par);

  else return INTEGRAL_2Tag(x0, xf, par);
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
  // 2-tag efficiency
  PAR_GUESSES[5] = g_eff2_bb->Eval(SIGMASS)*BR + 0.5*(g_eff2_qq->Eval(SIGMASS) + g_eff2_gg->Eval(SIGMASS))*(1-BR);

  // input file names
  INPUTFILES.push_back("Data_and_ResonanceShapes/Final__histograms_CSVM_0Tag_WideJets.root");
  INPUTFILES.push_back("Data_and_ResonanceShapes/Final__histograms_CSVM_1Tag_WideJets.root");
  INPUTFILES.push_back("Data_and_ResonanceShapes/Final__histograms_CSVM_2Tag_WideJets.root");
  
  // setup the signal histogram
  TFile* histfile_bb=new TFile("Data_and_ResonanceShapes/Resonance_Shapes_WideJets_bb.root");
  
  ostringstream histname_bb, cdfname_bb, histname_gg, cdfname_gg, outputfile;
  histname_bb << "h_bb_" << masspoint;
  cdfname_bb << "h_bb_" << masspoint << "_cdf";
  
  HIST_bb=(TH1D*)histfile_bb->Get(histname_bb.str().c_str());
  HISTCDF_bb=(TH1D*)histfile_bb->Get(cdfname_bb.str().c_str());
  
  assert(HIST_bb && HISTCDF_bb && SIGMASS>0);

  TFile* histfile_gg=new TFile("Data_and_ResonanceShapes/Resonance_Shapes_WideJets_gg.root");

  histname_gg << "h_gg_" << masspoint;
  cdfname_gg << "h_gg_" << masspoint << "_cdf";

  HIST_gg=(TH1D*)histfile_gg->Get(histname_gg.str().c_str());
  HISTCDF_gg=(TH1D*)histfile_gg->Get(cdfname_gg.str().c_str());

  assert(HIST_gg && HISTCDF_gg && SIGMASS>0);
  
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
