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
#include <TVectorD.h>
#include <TMatrixD.h>
#include <TMatrixDSym.h>
#include <TMatrixDSymEigen.h>

#include "binneddata.hh"
#include "fit.hh"
#include "statistics.hh"

using namespace std;

////////////////////////////////////////////////////////////////////////////////
// magic numbers
////////////////////////////////////////////////////////////////////////////////

// number of pseudoexperiments
const int NPES=200; // 100

// number of samples of nuisance parameters for Bayesian MC integration
const int NSAMPLES=2000; // 2000

// use a B-only fit for the background systematics
const bool useBonlyFit = 1;

// constrain S to be positive in the S+B fit
const bool posS = 0;

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
const int NPARS=26;  // TMinuit does not support more than 26 variable parameters!
const int NBKGPARS=4;
const int POIINDEX=0; // which parameter is "of interest"
const char* PAR_NAMES[NPARS]    = { "xs", "lumi", "jes", "jer", "eff 0", "eff 2",    "norm_0",      "p1_0",      "p2_0",       "p3_0",    "norm_1",      "p1_1",      "p2_1",       "p3_1",    "norm_2",      "p1_2",      "p2_2",       "p3_2", "n0_0", "n1_0", "n2_0", "n0_1", "n1_1", "n2_1", "n0_2", "n1_2" };
      double PAR_GUESSES[NPARS] = { 1E-5,  4976.,   1.0,   1.0,     0.5,     0.1, 2.28255e-01, 8.51130e+00, 5.42168e+00,  5.23767e-02, 1.41453e-01, 8.47691e+00, 4.97184e+00, -3.60922e-02, 4.11375e-03, 6.37762e+00, 5.58514e+00,  4.93530e-02,    10,      10,     10,     10,     10,     10,     10,     10 };
      double PAR_MIN[NPARS]     = {    0,    0.0,   0.0,   0.0,     0.0,     0.0,       -9999,       -9999,       -9999,        -9999,       -9999,       -9999,       -9999,        -9999,       -9999,       -9999,       -9999,        -9999,     9,       9,      9,      9,      9,      9,      9,      9 };
const double PAR_MAX[NPARS]     = { 1.E6,  6000.,   2.0,   2.0,     1.0,     1.0,        9999,        9999,        9999,         9999,        9999,        9999,        9999,         9999,        9999,        9999,        9999,         9999,    11,      11,     11,     11,     11,     11,     11,     11 };
      double PAR_ERR[NPARS]     = { 1E-3,   110.,  0.03,  0.10,    0.05,    0.01,      1e-02,        1e-01,       1e-01,        1e-02,      1e-02,        1e-01,       1e-01,        1e-02,      1e-03,        1e-01,       1e-01,        1e-02,     1,       1,      1,      1,      1,      1,      1,      1 };
const int PAR_TYPE[NPARS]       = {    1,      2,     2,     2,       2,       2,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     3,       3,      3,      3,      3,      3,      3,      3 }; // 1,2 = signal (2 not used in the fit); 0,3 = background (3 not used in the fit)
const int PAR_NUIS[NPARS]       = {    0,      1,     1,     1,       1,       1,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     1,       1,      1,      1,      1,      1,      1,      1 }; // 1 = nuisance parameter, 0 = not varied (the POI is not a nuisance parameter)

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

// covariance matrix
double COV_MATRIX[NPARS][NPARS];
TMatrixDSym covMatrix0 = TMatrixDSym(NBKGPARS);
TMatrixDSym covMatrix1 = TMatrixDSym(NBKGPARS);
TMatrixDSym covMatrix2 = TMatrixDSym(NBKGPARS);
TVectorD eigenValues0 = TVectorD(NBKGPARS);
TMatrixD eigenVectors0 = TMatrixD(NBKGPARS,NBKGPARS);
TVectorD eigenValues1 = TVectorD(NBKGPARS);
TMatrixD eigenVectors1 = TMatrixD(NBKGPARS,NBKGPARS);
TVectorD eigenValues2 = TVectorD(NBKGPARS);
TMatrixD eigenVectors2 = TMatrixD(NBKGPARS,NBKGPARS);

// shift in the counter used to extract the covariance matrix
int shift = 1;

// branching ratio for bbbar final state (calculated wrt to the branching ratio for jet-jet final state)
double BR = 1.;

// light flavor resonance shape
string LFRS = "gg";

// CSVL 0- and 2-tag efficienies and efficieny erros for heavy and light flavor final states
double masses_eff[5] = {500.0, 700.0, 1200.0, 2000.0, 3500.0};
double eff0_h[5] = {0.075190481730750422, 0.092189096135135151, 0.17201223401970492, 0.32047805349296232, 0.44234154305258216};
double eff2_h[5] = {0.52785268605907942, 0.48045368192262933, 0.334041805776981, 0.18690492564265077, 0.11826979776906879};
double eff0_l[5] = {0.7975218492033489, 0.7907476660899039, 0.7660975206782392, 0.7202049472961713, 0.623953840878057};
double eff2_l[5] = {0.012362415206298268, 0.011480309330892644, 0.015051930138445458, 0.022660032461222446, 0.04306123992381192};

double eff0_err_h[5] = {0.010219706183534143, 0.012473030851601145, 0.019620181633986555, 0.040560602922774504, 0.039263984277089076};
double eff2_err_h[5] = {0.02697328322836535, 0.027583170855405945, 0.02628211062017828, 0.030936028907094185, 0.020878956880156428};
double eff0_err_l[5] = {0.029871577320823017, 0.03198206919409663, 0.027800156765285577, 0.0544819257912722, 0.05383311405862656};
double eff2_err_l[5] = {0.004544933683004768, 0.0023825339983753434, 0.0039576140923348845, 0.012763868646675162, 0.017833102325434967};

TGraph *g_eff0_h = new TGraph(5, masses_eff, eff0_h);
TGraph *g_eff2_h = new TGraph(5, masses_eff, eff2_h);
TGraph *g_eff0_l = new TGraph(5, masses_eff, eff0_l);
TGraph *g_eff2_l = new TGraph(5, masses_eff, eff2_l);

TGraph *g_eff0_err_h = new TGraph(5, masses_eff, eff0_err_h);
TGraph *g_eff2_err_h = new TGraph(5, masses_eff, eff2_err_h);
TGraph *g_eff0_err_l = new TGraph(5, masses_eff, eff0_err_l);
TGraph *g_eff2_err_l = new TGraph(5, masses_eff, eff2_err_l);


TH1D* HISTCDF_0Tag=0; // 0-tag signal CDF
TH1D* HISTCDF_1Tag=0; // 1-tag signal CDF
TH1D* HISTCDF_2Tag=0; // 2-tag signal CDF

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
  double n[NBKGPARS] = {0.};
  n[0]=par[18]-10.;
  n[1]=par[19]-10.;
  n[2]=par[20]-10.;
  n[3]=0.;

  if( COV_MATRIX[0+shift][0+shift]>0. && (n[0]!=0. || n[1]!=0. || n[2]!=0. || n[3]!=0.) )
  {
    double g[NBKGPARS] = {0.};
    for(int v=0; v<(NBKGPARS-1); ++v)
    {
      for(int k=0; k<NBKGPARS; ++k) g[k]=n[v]*eigenValues0(v)*eigenVectors0[k][v];
      norm += g[0];
      p1   += g[1];
      p2   += g[2];
      p3   += g[3];
    }
  }

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
  if(bkg<0.) bkg=0.0000001;

  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0-SIGMASS)+SIGMASS);
  int bin1=HISTCDF_0Tag->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF_0Tag->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF_0Tag->GetNbinsX()) bin1=HISTCDF_0Tag->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF_0Tag->GetNbinsX()) bin2=HISTCDF_0Tag->GetNbinsX();
  double sig=xs*eff*lumi*(HISTCDF_0Tag->GetBinContent(bin1)-HISTCDF_0Tag->GetBinContent(bin2));

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
  double eff=((1-par[4]-par[5])>=0. ? (1-par[4]-par[5]) : 0.);
  double norm=par[10];
  double p1=par[11];
  double p2=par[12];
  double p3=par[13];
  double n[NBKGPARS] = {0.};
  n[0]=par[21]-10.;
  n[1]=par[22]-10.;
  n[2]=par[23]-10.;
  n[3]=0.;

  if( COV_MATRIX[4+shift][4+shift]>0. && (n[0]!=0. || n[1]!=0. || n[2]!=0. || n[3]!=0.) )
  {
    double g[NBKGPARS] = {0.};
    for(int v=0; v<(NBKGPARS-1); ++v)
    {
      for(int k=0; k<NBKGPARS; ++k) g[k]=n[v]*eigenValues1(v)*eigenVectors1[k][v];
      norm += g[0];
      p1   += g[1];
      p2   += g[2];
      p3   += g[3];
    }
  }

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
  if(bkg<0.) bkg=0.0000001;

  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0-SIGMASS)+SIGMASS);
  int bin1=HISTCDF_1Tag->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF_1Tag->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF_1Tag->GetNbinsX()) bin1=HISTCDF_1Tag->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF_1Tag->GetNbinsX()) bin2=HISTCDF_1Tag->GetNbinsX();
  double sig=xs*eff*lumi*(HISTCDF_1Tag->GetBinContent(bin1)-HISTCDF_1Tag->GetBinContent(bin2));

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
  double n[NBKGPARS] = {0.};
  n[0]=par[24]-10.;
  n[1]=par[25]-10.;
  n[2]=0.;
  n[3]=0.;

  if( COV_MATRIX[8+shift][8+shift]>0. && (n[0]!=0. || n[1]!=0. || n[2]!=0. || n[3]!=0.) )
  {
    double g[NBKGPARS] = {0.};
    for(int v=0; v<(NBKGPARS-2); ++v)
    {
      for(int k=0; k<NBKGPARS; ++k) g[k]=n[v]*eigenValues2(v)*eigenVectors2[k][v];
      norm += g[0];
      p1   += g[1];
      p2   += g[2];
      p3   += g[3];
    }
  }

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
  if(bkg<0.) bkg=0.0000001;

  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0-SIGMASS)+SIGMASS);
  int bin1=HISTCDF_2Tag->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF_2Tag->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF_2Tag->GetNbinsX()) bin1=HISTCDF_2Tag->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF_2Tag->GetNbinsX()) bin2=HISTCDF_2Tag->GetNbinsX();
  double sig=xs*eff*lumi*(HISTCDF_2Tag->GetBinContent(bin1)-HISTCDF_2Tag->GetBinContent(bin2));

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
    cout << "Usage: stats signalmass [BR LFRS]" << endl;
    return 0;
  }

  SIGMASS = atof(argv[1]);
  int masspoint = int(SIGMASS);

  if(argc>2) BR = atof(argv[2]);
  if(argc>3) LFRS = argv[3];

  if(useBonlyFit) shift = 0;

  if(!posS) PAR_MIN[POIINDEX] = -PAR_MAX[POIINDEX];

  // initialize the covariance matrix
  for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }

  // set 0-tag efficiency and efficiency errors
  PAR_GUESSES[4] = g_eff0_h->Eval(SIGMASS)*BR + g_eff0_l->Eval(SIGMASS)*(1-BR);
  PAR_ERR[4] = sqrt( pow(g_eff0_err_h->Eval(SIGMASS)*BR,2) + pow(g_eff0_err_l->Eval(SIGMASS)*(1-BR),2) );
  // set 2-tag efficiency and efficiency errors
  PAR_GUESSES[5] = g_eff2_h->Eval(SIGMASS)*BR + g_eff2_l->Eval(SIGMASS)*(1-BR);
  PAR_ERR[5] = sqrt( pow(g_eff2_err_h->Eval(SIGMASS)*BR,2) + pow(g_eff2_err_l->Eval(SIGMASS)*(1-BR),2) );

  // input file names
  INPUTFILES.push_back("/uscms/home/ferencek/MyAnalysis/MyAnalyzer/test/LimitCode/Data_and_ResonanceShapes/Final__histograms_CSVL_0Tag_WideJets.root");
  INPUTFILES.push_back("/uscms/home/ferencek/MyAnalysis/MyAnalyzer/test/LimitCode/Data_and_ResonanceShapes/Final__histograms_CSVL_1Tag_WideJets.root");
  INPUTFILES.push_back("/uscms/home/ferencek/MyAnalysis/MyAnalyzer/test/LimitCode/Data_and_ResonanceShapes/Final__histograms_CSVL_2Tag_WideJets.root");

  // setup the signal histogram
  string filename1 = "/uscms/home/ferencek/MyAnalysis/MyAnalyzer/test/LimitCode/Data_and_ResonanceShapes/Resonance_Shapes_WideJets_bb.root";
  string filename2 = "/uscms/home/ferencek/MyAnalysis/MyAnalyzer/test/LimitCode/Data_and_ResonanceShapes/Resonance_Shapes_WideJets_" + LFRS + ".root";

  ostringstream histname1, histname2;
  histname1 << "h_bb_" << masspoint;
  histname2 << "h_" << LFRS << "_" << masspoint;

  // commented out since the limit code currenlty does not work with combined shapes
  HISTCDF_0Tag=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, g_eff0_h->Eval(SIGMASS), g_eff0_l->Eval(SIGMASS), "_0Tag");
  HISTCDF_1Tag=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, (1-g_eff0_h->Eval(SIGMASS)-g_eff2_h->Eval(SIGMASS)), (1-g_eff0_l->Eval(SIGMASS)-g_eff2_l->Eval(SIGMASS)), "_1Tag");
  HISTCDF_2Tag=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, g_eff2_h->Eval(SIGMASS), g_eff2_l->Eval(SIGMASS), "_2Tag");

  assert(HISTCDF_0Tag && HISTCDF_1Tag && HISTCDF_2Tag && SIGMASS>0);

  // get the data
  TH1D* data=getData(INPUTFILES, "DATA__cutHisto_allPreviousCuts________DijetMass", NBINS-1, BOUNDARIES);

  // create the output file
  ostringstream outputfile;
  outputfile << OUTPUTFILE.substr(0,OUTPUTFILE.find(".root")) << "_" << masspoint << "_" << BR << "_" << LFRS << ".root";
  TFile* rootfile=new TFile(outputfile.str().c_str(), "RECREATE");  rootfile->cd();

  // POI value
  double POIval;

  // setup an initial fitter to perform a signal+background fit
  Fitter initfit(data, INTEGRAL);
  for(int i=0; i<NPARS; i++) initfit.defineParameter(i, PAR_NAMES[i], PAR_GUESSES[i], PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // do an initial signal+background fit first
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) initfit.fixParameter(i);
  initfit.doFit();
  POIval = initfit.getParameter(POIINDEX); // get the POI value for later use
  initfit.fixParameter(POIINDEX); // a parameter needs to be fixed before its value can be changed
  initfit.setParameter(POIINDEX, 0.0); // set the POI value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
  initfit.setPrintLevel(0);
  initfit.calcPull("pull_bkg_init")->Write();
  initfit.calcDiff("diff_bkg_init")->Write();
  initfit.write("fit_bkg_init");
  initfit.setParameter(POIINDEX, POIval);

  // setup the limit values
  double observedLowerBound, observedUpperBound;
  vector<double> expectedLowerBounds;
  vector<double> expectedUpperBounds;

  cout << "*********** pe=0 (data) ***********" << endl;

  // setup the fitter with the input from the signal+background fit
  Fitter fit_data(data, INTEGRAL);
  fit_data.setPOIIndex(POIINDEX);
  //fit_data.setPrintLevel(0);
  for(int i=0; i<NPARS; i++) fit_data.defineParameter(i, PAR_NAMES[i], initfit.getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // perform a signal+background fit or a background-only fit with a fixed non-zero signal
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) fit_data.fixParameter(i);
  if(useBonlyFit) { fit_data.doFit(); fit_data.fixParameter(POIINDEX); }
  fit_data.doFit(&COV_MATRIX[0][0], NPARS);
  cout << "Data fit status: " << fit_data.getFitStatus() << endl;
  POIval = fit_data.getParameter(POIINDEX); // get the POI value for later use
  fit_data.fixParameter(POIINDEX); // a parameter needs to be fixed before its value can be changed
  fit_data.setParameter(POIINDEX, 0.0); // set the POI value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
  fit_data.setPrintLevel(0);
  fit_data.calcPull("pull_bkg_0")->Write();
  fit_data.calcDiff("diff_bkg_0")->Write();
  fit_data.write("fit_bkg_0");

  // calculate eigenvalues and eigenvectors
  for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix0(i,j)=COV_MATRIX[i+shift][j+shift]; } }
  const TMatrixDSymEigen eigen_data0(covMatrix0);
  eigenValues0 = eigen_data0.GetEigenValues();
  eigenValues0.Sqrt();
  eigenVectors0 = eigen_data0.GetEigenVectors();
  for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix1(i,j)=COV_MATRIX[i+4+shift][j+4+shift]; } }
  const TMatrixDSymEigen eigen_data1(covMatrix1);
  eigenValues1 = eigen_data1.GetEigenValues();
  eigenValues1.Sqrt();
  eigenVectors1 = eigen_data1.GetEigenVectors();
  for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix2(i,j)=COV_MATRIX[i+8+shift][j+8+shift]; } }
  const TMatrixDSymEigen eigen_data2(covMatrix2);
  eigenValues2 = eigen_data2.GetEigenValues();
  eigenValues2.Sqrt();
  eigenVectors2 = eigen_data2.GetEigenVectors();

  fit_data.setParLimits(POIINDEX, 0.0, PAR_MAX[POIINDEX]); // for posterior calculation, signal has to be positive
  TGraph* post_data=fit_data.calculatePosterior(NSAMPLES);
  post_data->Write("post_0");

  // evaluate the limit
  pair<double, double> bounds_data=evaluateInterval(post_data, ALPHA, LEFTSIDETAIL);
  observedLowerBound=bounds_data.first;
  observedUpperBound=bounds_data.second;

  // reset the covariance matrix
  for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }

  // perform the PEs
  for(int pe=1; pe<=NPES; ++pe) {

    cout << "*********** pe=" << pe << " ***********" << endl;
    ostringstream pestr;
    pestr << "_" << pe;

    // setup the fitter with the input from the signal+background fit
    fit_data.setParameter(POIINDEX, 0.0); // set the POI value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
    TH1D* hist = fit_data.makePseudoData((string("data")+pestr.str()).c_str());
    fit_data.setParameter(POIINDEX, POIval);

    Fitter fit(hist, INTEGRAL);
    fit.setPOIIndex(POIINDEX);
    fit.setPrintLevel(0);
    for(int i=0; i<NPARS; i++) fit.defineParameter(i, PAR_NAMES[i], fit_data.getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

    // perform a signal+background fit or a background-only fit with a fixed non-zero signal
    for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) fit.fixParameter(i);
    if(useBonlyFit) { fit.doFit(); fit.fixParameter(POIINDEX); }
    fit.doFit(&COV_MATRIX[0][0], NPARS);
    string fitStatus = fit.getFitStatus();
    if(fitStatus=="FAILED    ") continue; // skip this PE if the fit failed
    fit.fixParameter(POIINDEX); // a parameter needs to be fixed before its value can be changed
    fit.setParameter(POIINDEX, 0.0); // set the POI value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
    fit.calcPull((string("pull_bkg")+pestr.str()).c_str())->Write();
    fit.calcDiff((string("diff_bkg")+pestr.str()).c_str())->Write();
    fit.write((string("fit_bkg")+pestr.str()).c_str());

    // calculate eigenvalues and eigenvectors
    for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix0(i,j)=COV_MATRIX[i+shift][j+shift]; } }
    const TMatrixDSymEigen eigen0(covMatrix0);
    eigenValues0 = eigen0.GetEigenValues();
    bool hasNegativeElement = false;
    for(int i = 0; i<NBKGPARS; ++i) { if(eigenValues0(i)<0.) hasNegativeElement = true; }
    if(hasNegativeElement) continue;
    eigenValues0.Sqrt();
    eigenVectors0 = eigen0.GetEigenVectors();
    for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix1(i,j)=COV_MATRIX[i+4+shift][j+4+shift]; } }
    const TMatrixDSymEigen eigen1(covMatrix1);
    eigenValues1 = eigen1.GetEigenValues();
    hasNegativeElement = false;
    for(int i = 0; i<NBKGPARS; ++i) { if(eigenValues1(i)<0.) hasNegativeElement = true; }
    if(hasNegativeElement) continue;
    eigenValues1.Sqrt();
    eigenVectors1 = eigen1.GetEigenVectors();
    for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix2(i,j)=COV_MATRIX[i+8+shift][j+8+shift]; } }
    const TMatrixDSymEigen eigen2(covMatrix2);
    eigenValues2 = eigen2.GetEigenValues();
    hasNegativeElement = false;
    for(int i = 0; i<NBKGPARS; ++i) { if(eigenValues2(i)<0.) hasNegativeElement = true; }
    if(hasNegativeElement) continue;
    eigenValues2.Sqrt();
    eigenVectors2 = eigen2.GetEigenVectors();

    fit.setParLimits(POIINDEX, 0.0, PAR_MAX[POIINDEX]); // for posterior calculation, signal has to be positive
    TGraph* post=fit.calculatePosterior(NSAMPLES);
    post->Write((string("post")+pestr.str()).c_str());
    if(fit.callLimitReached()) {
      cout << "************************************************************" << endl
           << "*** Call limit reached. Skipping this pseudo-experiment. ***" << endl
           << "************************************************************" << endl;
      continue;
    }

    // evaluate the limit
    pair<double, double> bounds=evaluateInterval(post, ALPHA, LEFTSIDETAIL);
    if(bounds.first==0. && bounds.second>0.)
    {
      expectedLowerBounds.push_back(bounds.first);
      expectedUpperBounds.push_back(bounds.second);
    }

    // reset the covariance matrix
    for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }
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
