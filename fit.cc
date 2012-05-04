#include <cassert>
#include <sstream>
#include <cmath>
#include <limits>

#include <TF1.h>
#include <TMath.h>
#include <TH1D.h>
#include <TRandom3.h>
#include <TGraph.h>

#include "fit.hh"
#include "binneddata.hh"
#include "statistics.hh"

Fitter* Fitter::theFitter_;
TRandom3* Fitter::rand_;

Fitter::Fitter()
{
  data_=0;
  functionIntegral_=0;
  printlevel_=3;
  strategy_=2;
  minuit_.SetErrorDef(0.5); // likelihood
  if(!rand_) rand_=new TRandom3(31415);
  parameters_=0;
  poiIndex_=-1;
  callLimitReached_=false;
}

Fitter::Fitter(TH1D* data, integral_ptr_t functionIntegral)
{
  data_=data;
  functionIntegral_=functionIntegral;
  printlevel_=3;
  strategy_=2;
  minuit_.SetErrorDef(0.5); // likelihood
  if(!rand_) rand_=new TRandom3(31415);
  parameters_=0;
  poiIndex_=-1;
  callLimitReached_=false;
}

Fitter::~Fitter()
{
  if(parameters_) delete[] parameters_;
}


void Fitter::doFit(void)
{
  // setup the fitter so the information can be retrieved by nll
  Fitter::theFitter_=this;

  // setup TMinuit
  minuit_.SetPrintLevel(printlevel_);

  // set the strategy
  std::ostringstream command;
  command << "SET STR " << strategy_;
  minuit_.Command(command.str().c_str());

  // do the fit
  minuit_.SetFCN(nll);
  Double_t arglist[1] = {10000.0};
  Int_t err = 0;
  minuit_.mnexcm("MIGRAD",arglist,1,err);

  return;
}

TH1D* Fitter::calcPull(const char* name)
{
  TH1D* hPull=dynamic_cast<TH1D*>(data_->Clone(name));
  hPull->SetTitle("Pull Distribution");

  hPull->SetBinContent(0, 0.);
  hPull->SetBinContent(hPull->GetNbinsX()+1, 0.);
  hPull->SetBinError(0, 0.);
  hPull->SetBinError(hPull->GetNbinsX()+1, 0.);
  for(int bin=1; bin<=data_->GetNbinsX(); bin++) {
    double binwidth=data_->GetBinWidth(bin);
    double N=data_->GetBinContent(bin)*binwidth;
    double err=Fitter::histError(N);

    double x0=data_->GetBinLowEdge(bin);
    double xf=data_->GetBinLowEdge(bin+1);
    double mu=functionIntegral_(&x0, &xf, getParameters());

    double pull=(N-mu)/err;
    hPull->SetBinContent(bin, pull);
    hPull->SetBinError(bin, 1.0);
  }
  return hPull;
}

TH1D* Fitter::calcDiff(const char* name)
{
  TH1D* hDiff=dynamic_cast<TH1D*>(data_->Clone(name));
  hDiff->SetTitle("Difference Distribution");

  hDiff->SetBinContent(0, 0.);
  hDiff->SetBinContent(hDiff->GetNbinsX()+1, 0.);
  hDiff->SetBinError(0, 0.);
  hDiff->SetBinError(hDiff->GetNbinsX()+1, 0.);
  for(int bin=1; bin<=data_->GetNbinsX(); bin++) {
    double binwidth=data_->GetBinWidth(bin);
    double N=data_->GetBinContent(bin)*binwidth;
    double err=Fitter::histError(N);

    double x0=data_->GetBinLowEdge(bin);
    double xf=data_->GetBinLowEdge(bin+1);
    double mu=functionIntegral_(&x0, &xf, getParameters());

    double diff=(N-mu)/mu;
    hDiff->SetBinContent(bin, diff);
    hDiff->SetBinError(bin, err/mu);
  }
  return hDiff;
}

int Fitter::setParameter(int parno, double value)
{
  int err;
  double tmp[2];
  tmp[0]=parno+1;
  tmp[1]=value;

  minuit_.mnexcm("SET PAR", tmp, 2, err);
  return err;
}

int Fitter::setParLimits(int parno, double loLimit, double hiLimit)
{
  int err;
  double tmp[3];
  tmp[0]=parno+1;
  tmp[1]=loLimit;
  tmp[2]=hiLimit;

  minuit_.mnexcm("SET LIM", tmp, 3, err);
  return err;
}

double Fitter::getParameter(int parno) const
{
  double val, err;
  getParameter(parno, val, err);
  return val;
}

double Fitter::getParError(int parno) const
{
  double val, err;
  getParameter(parno, val, err);
  return err;
}

void Fitter::getParLimits(int parno, double &loLimit, double &hiLimit) const
{
  TString _name;
  double _val, _err;
  int _iuint;
  minuit_.mnpout(parno, _name, _val, _err, loLimit, hiLimit, _iuint);
  return;
}

double* Fitter::getParameters(void)
{
  // remove what is there
  if(parameters_) delete[] parameters_;

  int nPars=minuit_.GetNumPars();
  parameters_ = new double[nPars];
  for(int i=0; i<nPars; i++) {
    double value, err;
    getParameter(i, value, err);
    parameters_[i]=value;
  }

  return parameters_;
}

int Fitter::defineParameter(int parno, const char *name, double value, double error, double lo, double hi, bool isNuisance)
{
  parameterIsNuisance_[parno]=isNuisance;
  return minuit_.DefineParameter(parno, name, value, error, lo, hi);
}

TGraph* Fitter::calculatePosterior(int nSamples)
{
  // we need a parameter of index defined
  assert(poiIndex_>=0);

  // set the number of samples for subsequent functions
  nSamples_=nSamples;
  nCalls_=0;

  // fit for the best value of the POI
  int nPars=getNumPars();
  double loLimit, hiLimit;
  getParLimits(poiIndex_, loLimit, hiLimit);
  for(int i=0; i<nPars; i++) if(i==poiIndex_) floatParameter(i); else fixParameter(i);
  setParameter(poiIndex_, 0.1*(loLimit+hiLimit));
  doFit();
  fixParameter(poiIndex_);
  double poiBestFit=getParameter(poiIndex_);

  // setup Fitter
  Fitter::theFitter_=this;

  // now float all parameters
  for(int i=0; i<nPars; i++) if(i!=poiIndex_) floatParameter(i);

  // evalulate NLL at the POI fit value for future normalizations
  double nllNormalization=evalNLL();

  // recursively evaluate the posterior
  std::map<double, double> fcnEvaluations;
  evaluateForPosterior(loLimit, poiBestFit, hiLimit, nllNormalization, fcnEvaluations);

  // dump the info into a graph
  int cntr=0;
  double maximumVal=-9999.;
  TGraph* graph=new TGraph(fcnEvaluations.size());
  for(std::map<double, double>::const_iterator it=fcnEvaluations.begin(); it!=fcnEvaluations.end(); ++it) {
    graph->SetPoint(cntr++, it->first, it->second);
    if(it->second>maximumVal) maximumVal=it->second;
  }

  // identify trivially small points on the left
  std::vector<int> pointsToRemove;
  for(int i=0; i<graph->GetN()-1; i++) {
    double x, y, nextx, nexty;
    graph->GetPoint(i, x, y);
    graph->GetPoint(i+1, nextx, nexty);

    if(y/maximumVal<1.E-3 && nexty/maximumVal<1.E-3) pointsToRemove.push_back(i);
    else break;
  }

  // identify trivially small points on the right
  for(int i=graph->GetN()-1; i>=1; i--) {
    double x, y, nextx, nexty;
    graph->GetPoint(i, x, y);
    graph->GetPoint(i-1, nextx, nexty);

    if(y/maximumVal<1.E-3 && nexty/maximumVal<1.E-3) pointsToRemove.push_back(i);
    else break;
  }

  // sort the points to remove from first to last
  std::sort(pointsToRemove.begin(), pointsToRemove.end());

  // remove the points
  for(int i=pointsToRemove.size()-1; i>=0; i--)
    graph->RemovePoint(pointsToRemove[i]);

  return graph;
}

double Fitter::evalNLL(void)
{
  Fitter::theFitter_=this;
  int a;
  double f;
  nll(a, 0, f, getParameters(), 0);
  return f;
}

double Fitter::histError(double val)
{
  if(val<25.) return (TMath::ChisquareQuantile(0.95,2*(val+1)-TMath::ChisquareQuantile(0.05,2*val)))/4.0;
  else return sqrt(val);
}

void Fitter::nll(int &, double *, double &f, double *par, int)
{
  assert(Fitter::theFitter_);
  TH1D* data=Fitter::theFitter_->data_;
  integral_ptr_t functionIntegral=Fitter::theFitter_->functionIntegral_;

  f=0.0;
  for(int bin=1; bin<=data->GetNbinsX(); bin++) {
    double binwidth=data->GetBinWidth(bin);
    double N=data->GetBinContent(bin)*binwidth;

    double x0=data->GetBinLowEdge(bin);
    double xf=data->GetBinLowEdge(bin+1);
    double mu=functionIntegral(&x0, &xf, par);

    if(N==0.0) f += mu;
    else f -= (N*TMath::Log(mu) - TMath::LnGamma(N+1) - mu);
  }
  return;
}

TH1D* Fitter::makePseudoData(const char* name, double* parameters)
{
  if(!parameters) parameters=getParameters();

  // start with a copy of the original dataset
  TH1D* hData=dynamic_cast<TH1D*>(data_->Clone(name));

  for(int bin=1; bin<=hData->GetNbinsX(); ++bin) {
    double lobin=hData->GetBinLowEdge(bin);
    double hibin=hData->GetBinLowEdge(bin+1);
    double integral=functionIntegral_(&lobin, &hibin, parameters);
    double val=rand_->Poisson(integral);
    double binWidth=hData->GetBinWidth(bin);
    hData->SetBinContent(bin, val/binWidth);
    hData->SetBinError(bin, histError(val)/binWidth);
  }
  return hData;
}


void Fitter::evaluateForPosterior(double lo, double mid, double hi, double nllNormalization, std::map<double, double>& fcnEval_)
{
  if((nCalls_++)>150) {
    callLimitReached_=true;
    return;
  }
  // get the low value
  std::map<double, double>::iterator findit;
  findit = fcnEval_.find(lo);
  double loVal;
  if(findit==fcnEval_.end()) {
    loVal=computeLikelihoodWithSystematics(lo, nllNormalization);
    fcnEval_[lo]=loVal;
  } else {
    loVal=fcnEval_[lo];
  }

  // get the middle value
  findit = fcnEval_.find(mid);
  double midVal;
  if(findit==fcnEval_.end()) {
    midVal=computeLikelihoodWithSystematics(mid, nllNormalization);
    fcnEval_[mid]=midVal;
  } else {
    midVal=fcnEval_[mid];
  }

  // get the high value
  findit = fcnEval_.find(hi);
  double hiVal;
  if(findit==fcnEval_.end()) {
    hiVal=computeLikelihoodWithSystematics(hi, nllNormalization);
    fcnEval_[hi]=hiVal;
  } else {
    hiVal=fcnEval_[hi];
  }

  //  std::cout << "lo=" << lo << "; mid=" << mid << "; hi=" << hi << "; loval=" << loVal << "; midval=" << midVal << "; hival=" << hiVal << std::endl;
  double maximumVal = -999.;
  for(std::map<double, double>::const_iterator it=fcnEval_.begin(); it!=fcnEval_.end(); ++it)
    if(maximumVal<it->second)
      maximumVal=it->second;

  if(fabs(loVal-midVal)>0.04*maximumVal || fabs(hiVal-midVal)>0.04*maximumVal) {
    if(fabs(lo-mid)/mid>0.001) evaluateForPosterior(lo, 0.5*(lo+mid), mid, nllNormalization, fcnEval_);
    if(fabs(hi-mid)/hi>0.001) evaluateForPosterior(mid, 0.5*(mid+hi), hi, nllNormalization, fcnEval_);
  }

  return;
}

double Fitter::computeLikelihoodWithSystematics(double poiVal, double nllNormalization)
{
  // setup parameters
  int a;
  double f;
  double *pars=getParameters();
  pars[poiIndex_]=poiVal;

  // no systematics
  if(nSamples_==0) {
    nll(a, 0, f, pars, 0);
    return TMath::Exp(-f+nllNormalization);
  }

  // setup lognormals
  std::map<int, RandomLognormal*> lognorms;
  for(std::map<int, bool>::const_iterator it=parameterIsNuisance_.begin(); it!=parameterIsNuisance_.end(); ++it) {
    if(it->second) {
      assert(it->first!=poiIndex_);
      double parval, parerr;
      double lolim, uplim;
      getParameter(it->first, parval, parerr);
      getParLimits(it->first, lolim, uplim);
      if(lolim<parval-5*parerr) lolim=parval-5*parerr;
      if(uplim>parval+5*parerr) uplim=parval+5*parerr;
      lognorms[it->first]=new RandomLognormal(parval, parerr, lolim, uplim);
    }
  }

  // calculate average likelihood value over nuisance parameters
  double total=0.0;
  for(int sample=0; sample<=nSamples_; sample++) {
    for(std::map<int, RandomLognormal*>::const_iterator it=lognorms.begin(); it!=lognorms.end(); ++it)
      pars[it->first]=it->second->getRandom();
    nll(a,0,f,pars,0);
    double like=TMath::Exp(-f+nllNormalization);

    //if(like>10) {
    //  int nPars=minuit_.GetNumPars();
    //  std::cout << "sample=" << sample << std::endl;
    //  for(int i=0; i<nPars; i++) {
    //    std::cout << "pars[" << i << "]=" << pars[i] << std::endl;
    //  }
    //  std::cout << "like=" << like << "; f=" << f << "; norm=" << nllNormalization << std::endl;
    //  assert(0);
    //}

    total+=like;
  }

  // remove lognormals
  for(std::map<int, RandomLognormal*>::const_iterator it=lognorms.begin(); it!=lognorms.end(); ++it) delete it->second;

  return total/nSamples_;
}

double Fitter::calculateUpperBoundWithCLs(int nSamples, double alpha)
{
  // we need a parameter of index defined
  assert(poiIndex_>=0);

  // set the number of samples for subsequent functions
  nSamples_=nSamples;

  // fit for the best value of the POI
  int nPars=getNumPars();
  double loLimit, hiLimit;
  getParLimits(poiIndex_, loLimit, hiLimit);
  for(int i=0; i<nPars; i++) if(i==poiIndex_) floatParameter(i); else fixParameter(i);
  setParameter(poiIndex_, 0.1*(loLimit+hiLimit));
  doFit();
  double poiBestFit=getParameter(poiIndex_);
  double poiBestFitErr=getParError(poiIndex_);
  fixParameter(poiIndex_);

  // now float all parameters
  for(int i=0; i<nPars; i++) if(i!=poiIndex_) floatParameter(i);

  // scan the CLs in steps of error, first
  double poiVal;
  double prevPoiVal=0.0;
  double prevCLsVal=nSamples;
  double CLsVal=0.0;
  for(poiVal=poiBestFit; poiVal<hiLimit; poiVal+=poiBestFitErr) {

    // calculate CLs
    std::vector<double> CLb, CLsb;
    std::pair<int, int> numden=calculateCLs_(poiVal, CLb, CLsb);
    double A=static_cast<double>(numden.first)/nSamples;
    double B=static_cast<double>(numden.second)/nSamples;
    double Aerr=sqrt(A*(1-A)/nSamples);
    double Berr=sqrt(B*(1-B)/nSamples);
    CLsVal = B==0 ? nSamples*2 : A/B;
    double CLsErr = Aerr==0 || Berr==0 ? 0. : CLsVal*sqrt(Aerr*Aerr/A/A+Berr*Berr/B/B);
    double diff=fabs(CLsVal-alpha);

    std::cout << "Scan: CLsVal=" << CLsVal << "; poiVal=" << poiVal << std::endl;

    if(diff<CLsErr) return poiVal;

    if((prevCLsVal>=alpha && CLsVal<=alpha) || (prevCLsVal<=alpha && CLsVal>=alpha)) break;

    prevPoiVal=poiVal;
    prevCLsVal=CLsVal;
  }
  if(poiVal>=hiLimit) return -999.;

  // now, try to converge on best CLs point
  double poiValLo=prevPoiVal;
  double poiValHi=poiVal;
  double CLsValLo=prevCLsVal;
  double CLsValHi=CLsVal;
  int cntr=0;
  do {
    poiVal=(alpha-CLsValLo)*(poiValHi-poiValLo)/(CLsValHi-CLsValLo)+poiValLo;
    std::vector<double> CLb, CLsb;
    std::pair<int, int> numden=calculateCLs_(poiVal, CLb, CLsb);
    double A=static_cast<double>(numden.first)/nSamples;
    double B=static_cast<double>(numden.second)/nSamples;
    double Aerr=sqrt(A*(1-A)/nSamples);
    double Berr=sqrt(B*(1-B)/nSamples);
    double CLsVal = B==0 ? nSamples*2 : A/B;
    double CLsErr = Aerr==0 || Berr==0 ? 0. : CLsVal*sqrt(Aerr*Aerr/A/A+Berr*Berr/B/B);
    double diff=fabs(CLsVal-alpha);

    std::cout << "poiVal=" << poiVal << "; poiValLo=" << poiValLo << "; poiValHi=" << poiValHi
	      << "; CLsVal=" << CLsVal << "; CLsErr=" << CLsErr << "; CLSValLo=" << CLsValLo << "; CLsValHi=" << CLsValHi << std::endl;
    std::cout << "A=" << A << "; Aerr=" << Aerr
	      <<"; B=" << B << "; Berr=" << Berr << std::endl;

    if(diff>CLsErr) {
      if(alpha>CLsVal) {
	poiValHi=poiVal;
	CLsValHi=CLsVal;
      } else {
	poiValLo=poiVal;
	CLsValLo=CLsVal;
      }
    } else {
      break;
    }

  }while(cntr<100);

  return poiVal;
}

std::pair<int, int> Fitter::calculateCLs_(double poiVal, std::vector<double>& CLb, std::vector<double>& CLsb)
{
  // setup parameters
  int a;
  double f;
  double *pars=getParameters();

  // setup lognormals
  std::map<int, RandomLognormal*> lognorms;
  for(std::map<int, bool>::const_iterator it=parameterIsNuisance_.begin(); it!=parameterIsNuisance_.end(); ++it) {
    if(it->second) {
      assert(it->first!=poiIndex_);
      double parval, parerr;
      double lolim, uplim;
      getParameter(it->first, parval, parerr);
      getParLimits(it->first, lolim, uplim);
      if(lolim<parval-5*parerr) lolim=parval-5*parerr;
      if(uplim>parval+5*parerr) uplim=parval+5*parerr;
      lognorms[it->first]=new RandomLognormal(parval, parerr, lolim, uplim);
    }
  }

  TH1D* theData=data_;

  for(int i=0; i<nSamples_; i++) {

    // create the pseudodata
    TH1D* CLSB_pdata;
    TH1D* CLB_pdata;
    if(i>0) {
      for(std::map<int, RandomLognormal*>::const_iterator it=lognorms.begin(); it!=lognorms.end(); ++it)
	pars[it->first]=it->second->getRandom();

      pars[poiIndex_]=poiVal;
      data_=theData;
      CLSB_pdata=makePseudoData("CLSB_pdata", pars);
      pars[poiIndex_]=0.0;
      CLB_pdata=makePseudoData("CLB_pdata", pars);
    } else {
      CLSB_pdata=theData;
      CLB_pdata=theData;
    }

    // CL_{s+b}
    data_=CLSB_pdata;
    pars[poiIndex_]=poiVal;
    nll(a, 0, f, pars, 0);
    double llnum=f;
    pars[poiIndex_]=0.0;
    nll(a, 0, f, pars, 0);
    double llden=f;
    CLsb.push_back(2*llnum-2*llden);

    // CL_{b}
    data_=CLB_pdata;
    pars[poiIndex_]=poiVal;
    nll(a, 0, f, pars, 0);
    llnum=f;
    pars[poiIndex_]=0.0;
    nll(a, 0, f, pars, 0);
    llden=f;
    CLb.push_back(2*llnum-2*llden);

    // remove the pseudodata
    if(i>0) {
      delete CLSB_pdata;
      delete CLB_pdata;
    }
  }

  // remove lognormals
  for(std::map<int, RandomLognormal*>::const_iterator it=lognorms.begin(); it!=lognorms.end(); ++it) delete it->second;

  // set the data back
  data_=theData;

  // calculate the CLs
  int nNum=0, nDen=0;
  for(unsigned int i=1; i<CLb.size(); i++) {

    bool numPass=(CLsb[i]>=CLsb[0]);
    bool denPass=(CLb[i]>CLb[0]);

    nNum+=numPass;
    nDen+=denPass;
  }
  return std::pair<int, int>(nNum, nDen);
}
