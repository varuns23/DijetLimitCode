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
#include <BAT/BCLog.h>

#include "binneddata.hh"
#include "fit.hh"
#include "statistics.hh"

using namespace std;

////////////////////////////////////////////////////////////////////////////////
// magic numbers
////////////////////////////////////////////////////////////////////////////////

// number of pseudoexperiments
const int NPES=0; // 200

// number of samples of nuisance parameters for Bayesian MC integration
const int NSAMPLES=5000; // 5000

// use Markov chain Monte Carlo (MCMC) to marginalize nuisance parameters
const int useMCMC = 1;

// set offset value for different event categories
double OFFSET = 10000.;

// set the factor that defines the upper bound for the signal xs used by the MCMC as xsUpperBoundFactor*stat-only_limit
double xsUpperBoundFactor=3.0;

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
const int NPARS=30;
const int NBKGPARS=4;
const int POIINDEX=0; // which parameter is "of interest"
const char* PAR_NAMES[NPARS]    = { "xs",  "lumi", "jes", "jer", "eff 0", "eff 2",    "norm_0",      "p1_0",      "p2_0",       "p3_0",    "norm_1",      "p1_1",      "p2_1",       "p3_1",    "norm_2",      "p1_2",      "p2_2",       "p3_2", "n0_0", "n1_0", "n2_0", "n3_0", "n0_1", "n1_1", "n2_1", "n3_1", "n0_2", "n1_2", "n2_2", "n3_2" };
      double PAR_GUESSES[NPARS] = { 1E-6,  19710.,   1.0,   1.0,     0.5,     0.1, 2.88018e-01, 7.76186e+00, 5.87827e+00,  1.30733e-01, 1.62862e-01, 7.42498e+00, 5.39455e+00,  1.95727e-02, 2.19016e-03, 4.30730e+00, 6.38687e+00,  1.43647e-01,     0,       0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0 };
      double PAR_MIN[NPARS]     = {    0,     0.0,   0.0,   0.0,     0.0,     0.0,       -9999,       -9999,       -9999,        -9999,       -9999,       -9999,       -9999,        -9999,       -9999,       -9999,       -9999,        -9999,  -100,    -100,   -100,   -100,   -100,   -100,   -100,   -100,   -100,   -100,   -100,   -100 };
const double PAR_MAX[NPARS]     = {  1E2,     3E4,   2.0,   2.0,     1.0,     1.0,        9999,        9999,        9999,         9999,        9999,        9999,        9999,         9999,        9999,        9999,        9999,         9999,   100,     100,    100,    100,    100,    100,    100,    100,    100,    100,    100,    100 };
      double PAR_ERR[NPARS]     = { 1E-6, 512.46,  0.01,  0.10,    0.05,    0.01,       1e-02,       1e-01,       1e-01,        1e-02,      1e-02,        1e-01,       1e-01,        1e-02,      1e-03,        1e-01,       1e-01,        1e-02,     1,       1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1 };
const int PAR_TYPE[NPARS]       = {    1,       2,     2,     2,       2,       2,           0,           0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     3,       3,      3,      3,      3,      3,      3,      3,      3,      3,      3,      3 }; // 1,2 = signal (2 not used in the fit); 0,3 = background (3 not used in the fit)
const int PAR_NUIS[NPARS]       = {    0,       1,     1,     1,       1,       1,           0,           0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     4,       4,      4,      4,      4,      4,      4,      4,      4,      4,      4,      4 }; // 0 = not varied, >=1 = nuisance parameters with different priors (1 = Lognormal, 2 = Gaussian, 3 = Gamma, >=4 = Uniform)

//const int PAR_NUIS[NPARS]       = {    0,       1,     1,     1,       1,       1,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     4,       4,      4,      4,      4,      4,      4,      4,      4,      4,      4,      4 }; // for all
//const int PAR_NUIS[NPARS]       = {    0,       1,     0,     0,       0,       0,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     0,       0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0 }; // for lumi only
//const int PAR_NUIS[NPARS]       = {    0,       0,     1,     0,       0,       0,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     0,       0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0 }; // for jes only
//const int PAR_NUIS[NPARS]       = {    0,       0,     0,     1,       0,       0,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     0,       0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0 }; // for jer only
//const int PAR_NUIS[NPARS]       = {    0,       0,     0,     0,       1,       1,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     0,       0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0 }; // for b-tag eff only
//const int PAR_NUIS[NPARS]       = {    0,       1,     1,     1,       1,       1,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     0,       0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0 }; // for all except background
//const int PAR_NUIS[NPARS]       = {    0,       0,     0,     0,       0,       0,          0,            0,           0,            0,          0,            0,           0,            0,          0,            0,           0,            0,     4,       4,      4,      4,      4,      4,      4,      4,      4,      4,      4,      4 }; // for background only


// histogram binning
const int NBINS=137;
double BOUNDARIES[NBINS+1] = {   890,   944,  1000,  1058,  1118,  1181,  1246,  1313,  1383,  1455,  1530,  1607,  1687,
                                1770,  1856,  1945,  2037,  2132,  2231,  2332,  2438,  2546,  2659,  2775,  2895,  3019,
                                3147,  3279,  3416,  3558,  3704,  3854,  4010,  4171,  4337,  4509,  4686,  4869,  5058, 
                                5253,  5455,  5663,  5877,  6099,  6328,  6564,

                               10890, 10944, 11000, 11058, 11118, 11181, 11246, 11313, 11383, 11455, 11530, 11607, 11687,
                               11770, 11856, 11945, 12037, 12132, 12231, 12332, 12438, 12546, 12659, 12775, 12895, 13019,
                               13147, 13279, 13416, 13558, 13704, 13854, 14010, 14171, 14337, 14509, 14686, 14869, 15058, 
                               15253, 15455, 15663, 15877, 16099, 16328, 16564,

                               20890, 20944, 21000, 21058, 21118, 21181, 21246, 21313, 21383, 21455, 21530, 21607, 21687,
                               21770, 21856, 21945, 22037, 22132, 22231, 22332, 22438, 22546, 22659, 22775, 22895, 23019,
                               23147, 23279, 23416, 23558, 23704, 23854, 24010, 24171, 24337, 24509, 24686, 24869, 25058, 
                               25253, 25455, 25663, 25877, 26099, 26328, 26564   };

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

// CSVL 0- and 2-tag efficiencies and efficiency errors for heavy and light flavor final states
double masses_eff[5] = {1000.0, 2000.0, 3000.0, 4000.0, 5500.0};
double eff0_h[5] = {0.14375,0.347866, 0.474486, 0.515598, 0.406457};
double eff2_h[5] = {0.362346,0.153207,0.0892634, 0.0764071, 0.141174};
double eff0_l[5] = {0.823713, 0.779573, 0.742028, 0.716053, 0.753072};
double eff2_l[5] = {0.0168151, 0.0245664, 0.0301618, 0.0364609, 0.0292424};

double eff0_err_h[5] = {0.00227473 ,0.0121575 ,0.0237492 ,0.0258029 ,0.0257271};
double eff2_err_h[5] = {0.0318082 ,0.0278846 ,0.0220702 ,0.0198965 ,0.0298934};
double eff0_err_l[5] = {0.0608508 ,0.0453744 ,0.0497222 ,0.0481305 ,0.0520862};
double eff2_err_l[5] = {0.00682908 ,0.00930803 ,0.0120509 ,0.015401 ,0.0144653};

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
  n[0]=par[18];
  n[1]=par[19];
  n[2]=par[20];
  n[3]=par[21];

  if( COV_MATRIX[0+shift][0+shift]>0. && (n[0]!=0. || n[1]!=0. || n[2]!=0. || n[3]!=0.) )
  {
    double g[NBKGPARS] = {0.};
    for(int v=0; v<NBKGPARS; ++v)
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

  double dx=(xf-x0)/3./8000.;
  double x=x0/8000.0;
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
  double x0=fx0[0]-OFFSET;
  double xf=fxf[0]-OFFSET;
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
  n[0]=par[22];
  n[1]=par[23];
  n[2]=par[24];
  n[3]=par[25];

  if( COV_MATRIX[4+shift][4+shift]>0. && (n[0]!=0. || n[1]!=0. || n[2]!=0. || n[3]!=0.) )
  {
    double g[NBKGPARS] = {0.};
    for(int v=0; v<NBKGPARS; ++v)
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

  double dx=(xf-x0)/3./8000.;
  double x=x0/8000.0;
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
  double x0=fx0[0]-2*OFFSET;
  double xf=fxf[0]-2*OFFSET;
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
  n[0]=par[26];
  n[1]=par[27];
  n[2]=par[28];
  n[3]=par[29];

  if( COV_MATRIX[8+shift][8+shift]>0. && (n[0]!=0. || n[1]!=0. || n[2]!=0. || n[3]!=0.) )
  {
    double g[NBKGPARS] = {0.};
    for(int v=0; v<NBKGPARS; ++v)
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

  double dx=(xf-x0)/3./8000.;
  double x=x0/8000.0;
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
  if(xf[0]<=(BOUNDARIES[0]+OFFSET)) return INTEGRAL_0Tag(x0, xf, par);

  else if(xf[0]>(BOUNDARIES[0]+OFFSET) && xf[0]<=(BOUNDARIES[0]+2*OFFSET)) return INTEGRAL_1Tag(x0, xf, par);

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

  if(!posS) PAR_MIN[0] = -PAR_MAX[0];

  // initialize the covariance matrix
  for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }

  // enable more detailed printout from the BAT MCMC
  BCLog::SetLogLevel(BCLog::detail); 

  // set 0-tag efficiency and efficiency errors
  PAR_GUESSES[4] = g_eff0_h->Eval(SIGMASS)*BR + g_eff0_l->Eval(SIGMASS)*(1-BR);
  PAR_ERR[4] = sqrt( pow(g_eff0_err_h->Eval(SIGMASS)*BR,2) + pow(g_eff0_err_l->Eval(SIGMASS)*(1-BR),2) );
  // set 2-tag efficiency and efficiency errors
  PAR_GUESSES[5] = g_eff2_h->Eval(SIGMASS)*BR + g_eff2_l->Eval(SIGMASS)*(1-BR);
  PAR_ERR[5] = sqrt( pow(g_eff2_err_h->Eval(SIGMASS)*BR,2) + pow(g_eff2_err_l->Eval(SIGMASS)*(1-BR),2) );

  // input file names
  INPUTFILES.push_back("Data_and_ResonanceShapes/Histos_data_0tag.root");
  INPUTFILES.push_back("Data_and_ResonanceShapes/Histos_data_1tag.root");
  INPUTFILES.push_back("Data_and_ResonanceShapes/Histos_data_2tag.root");

 // setup the signal histogram
  string filename1 = "Data_and_ResonanceShapes/Resonance_Shapes_bb_Pythia8.root";
  string filename2 = "Data_and_ResonanceShapes/Resonance_Shapes_" + LFRS + "_Pythia8.root";

  ostringstream histname1, histname2;
  histname1 << "h_bb_" << masspoint;
  histname2 << "h_" << LFRS << "_" << masspoint;

  // commented out since the limit code currenlty does not work with combined shapes
  HISTCDF_0Tag=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, g_eff0_h->Eval(SIGMASS), g_eff0_l->Eval(SIGMASS), "_0Tag");
  HISTCDF_1Tag=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, (1-g_eff0_h->Eval(SIGMASS)-g_eff2_h->Eval(SIGMASS)), (1-g_eff0_l->Eval(SIGMASS)-g_eff2_l->Eval(SIGMASS)), "_1Tag");
  HISTCDF_2Tag=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, g_eff2_h->Eval(SIGMASS), g_eff2_l->Eval(SIGMASS), "_2Tag");

  assert(HISTCDF_0Tag && HISTCDF_1Tag && HISTCDF_2Tag && SIGMASS>0);

  // get the data
  TH1D* data=getData(INPUTFILES, "hDijetMass_data_fine", NBINS, BOUNDARIES, OFFSET);

  // create the output file
  ostringstream outputfile;
  outputfile << OUTPUTFILE.substr(0,OUTPUTFILE.find(".root")) << "_" << masspoint << "_" << BR << "_" << LFRS << ".root";
  TFile* rootfile=new TFile(outputfile.str().c_str(), "RECREATE");  rootfile->cd();

  // xs value
  double XSval;

  // setup an initial fitter to perform a signal+background fit
  Fitter* initfit = new Fitter(data, INTEGRAL, NPARS);
  for(int i=0; i<NPARS; i++) initfit->defineParameter(i, PAR_NAMES[i], PAR_GUESSES[i], PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // do an initial signal+background fit first
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) initfit->fixParameter(i);
  initfit->doFit();
  XSval = initfit->getParameter(0); // get the xs value for later use
  initfit->fixParameter(0); // a parameter needs to be fixed before its value can be changed
  initfit->setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
  initfit->setPrintLevel(0);
  initfit->calcPull("pull_bkg_init")->Write();
  initfit->calcDiff("diff_bkg_init")->Write();
  initfit->write("fit_bkg_init");
  initfit->setParameter(0, XSval);

  // setup the limit values
  double observedLowerBound, observedUpperBound;
  vector<double> expectedLowerBounds;
  vector<double> expectedUpperBounds;

  cout << "********************** pe=0 (data) **********************" << endl;

  // setup the fitter with the input from the signal+background fit
  Fitter* fit_data = new Fitter(data, INTEGRAL, NPARS);
  fit_data->setPOIIndex(POIINDEX);
  //fit_data->setPrintLevel(0);
  for(int i=0; i<NPARS; i++) fit_data->defineParameter(i, PAR_NAMES[i], initfit->getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // perform a signal+background fit or a background-only fit with a fixed non-zero signal
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) fit_data->fixParameter(i);
  if(useBonlyFit) { fit_data->doFit(); fit_data->fixParameter(0); }
  fit_data->doFit(&COV_MATRIX[0][0], NPARS);
  cout << "Data fit status: " << fit_data->getFitStatus() << endl;
  fit_data->fixParameter(0); // a parameter needs to be fixed before its value can be changed
  fit_data->setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
  fit_data->setPrintLevel(0);
  fit_data->calcPull("pull_bkg_0")->Write();
  fit_data->calcDiff("diff_bkg_0")->Write();
  fit_data->write("fit_bkg_0");

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

  fit_data->setParLimits(0, 0.0, PAR_MAX[0]); // for posterior calculation, signal has to be positive
  TGraph* post_data = 0;
  if(useMCMC==0)
  {
    post_data=fit_data->calculatePosterior(NSAMPLES);
    post_data->Write("post_0");
    cout << "Call limit reached: " << (fit_data->callLimitReached() ? "True" : "False") << endl;
  }
  else
  {
    post_data=fit_data->calculatePosterior(0);
    pair<double, double> statonly_bounds=evaluateInterval(post_data, ALPHA, LEFTSIDETAIL);
    fit_data->setParLimits(0, 0.0, xsUpperBoundFactor*(statonly_bounds.second));
    post_data=fit_data->calculatePosterior(NSAMPLES, useMCMC);
    //fit_data->PrintAllMarginalized("plots.ps");
    //fit_data->PrintResults("results.txt");
    post_data->Write("post_0");
  }

  // evaluate the limit
  pair<double, double> bounds_data=evaluateInterval(post_data, ALPHA, LEFTSIDETAIL);
  observedLowerBound=bounds_data.first;
  observedUpperBound=bounds_data.second;

  // reset the covariance matrix
  for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }

  // perform the PEs
  for(int pe=1; pe<=NPES; ++pe) {

    cout << "********************** pe=" << pe << " **********************" << endl;
    ostringstream pestr;
    pestr << "_" << pe;

    // setup the fitter with the input from the signal+background fit
    fit_data->setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
    TH1D* hist = fit_data->makePseudoData((string("data")+pestr.str()).c_str());
    fit_data->setParameter(0, PAR_GUESSES[0]);

    Fitter* fit = new Fitter(hist, INTEGRAL, NPARS);
    fit->setPOIIndex(POIINDEX);
    fit->setPrintLevel(0);
    for(int i=0; i<NPARS; i++) fit->defineParameter(i, PAR_NAMES[i], fit_data->getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

    // perform a signal+background fit or a background-only fit with a fixed non-zero signal
    for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) fit->fixParameter(i);
    if(useBonlyFit) { fit->doFit(); fit->fixParameter(0); }
    fit->doFit(&COV_MATRIX[0][0], NPARS);
    if(fit->getFitStatus().find("CONVERGED")==string::npos) continue; // skip this PE if the fit failed
    fit->fixParameter(0); // a parameter needs to be fixed before its value can be changed
    fit->setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
    fit->calcPull((string("pull_bkg")+pestr.str()).c_str())->Write();
    fit->calcDiff((string("diff_bkg")+pestr.str()).c_str())->Write();
    fit->write((string("fit_bkg")+pestr.str()).c_str());

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

    fit->setParLimits(0, 0.0, PAR_MAX[0]); // for posterior calculation, signal has to be positive
    TGraph* post = 0;
    if(useMCMC==0)
    {
      post=fit->calculatePosterior(NSAMPLES);
      post->Write((string("post")+pestr.str()).c_str());
      cout << "Call limit reached in pe=" << pe << ": " << (fit->callLimitReached() ? "True" : "False") << endl;
    }
    else
    {
      post=fit->calculatePosterior(0);
      pair<double, double> statonly_bounds=evaluateInterval(post, ALPHA, LEFTSIDETAIL);
      fit->setParLimits(0, 0.0, xsUpperBoundFactor*(statonly_bounds.second));
      post=fit->calculatePosterior(NSAMPLES, useMCMC);
      post->Write((string("post")+pestr.str()).c_str());
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

    delete fit;
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
