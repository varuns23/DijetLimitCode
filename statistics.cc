#include "statistics.hh"

#include <sstream>
#include <cassert>

#include <TGraph.h>
#include <TMath.h>
#include <TH1D.h>
#include <TF1.h>

int RandomLognormal::counter_=0;

std::pair<double, double> evaluateInterval(TGraph* posterior, double alpha, double leftsidetail)
{
  double lowerCutOff = leftsidetail * alpha;
  double upperCutOff = 1. - (1.- leftsidetail) * alpha;

  double upper = 0, lower = 0;

  // normalize the interval, first
  double normalization=0.0;
  for(int i=0; i<posterior->GetN()-1; i++) {
    double firstx, firsty;
    double nextx, nexty;
    posterior->GetPoint(i, firstx, firsty);
    posterior->GetPoint(i+1, nextx, nexty);

    double intervalIntegral=(nextx-firstx)*0.5*(firsty+nexty);
    normalization+=intervalIntegral;
  }

  // now compute the intervals
  double integral=0.0;
  for(int i=0; i<posterior->GetN()-1; i++) {
    double firstx, firsty;
    double nextx, nexty;
    posterior->GetPoint(i, firstx, firsty);
    posterior->GetPoint(i+1, nextx, nexty);

    double intervalIntegral=(nextx-firstx)*0.5*(firsty+nexty)/normalization;

    // interpolate lower
    if(integral<=lowerCutOff && (integral+intervalIntegral)>=lowerCutOff) {
      lower=firstx;
    }
    if(integral<=upperCutOff && (integral+intervalIntegral)>=upperCutOff) {
      upper=firstx;
    }
    integral+=intervalIntegral;
  }

  std::pair<double, double> p(lower, upper);
  return p;
}

void getQuantiles(std::vector<double>& limits, double &median_, std::pair<double, double>& onesigma_, std::pair<double, double>& twosigma_) {
  unsigned int nit=limits.size();
  if(nit==0) return;

  // sort the vector with limits
  std::sort(limits.begin(), limits.end());

  // median for the expected limit
  median_ = TMath::Median(nit, &limits[0]);

  // quantiles for the expected limit bands
  double prob[4]; // array with quantile boundaries
  prob[0] = 0.021;
  prob[1] = 0.159;
  prob[2] = 0.841;
  prob[3] = 0.979;

  // array for the results
  double quantiles[4];
  TMath::Quantiles(nit, 4, &limits[0], quantiles, prob); // evaluate quantiles
  onesigma_.first=quantiles[1];
  onesigma_.second=quantiles[2];
  twosigma_.first=quantiles[0];
  twosigma_.second=quantiles[3];

  return;
}

double lognormal(double *x, double *par)
{
  if(par[0]<0.0) {
    std::cout << "par[0] = " << par[0] << std::endl;
    assert(0);
  }
  if(par[1]<0.0) {
    std::cout << "par[1] = " << par[1] << std::endl;
    assert(0);
  }

  double m0=par[0];
  double k=par[1]/par[0]+1.;
  double s=TMath::Log(k);
  return TMath::LogNormal(x[0], s, 0.0, m0);
  }

RandomLognormal::RandomLognormal(double median, double variance)
{
  double min = std::max(0.0, median-5.0*variance);
  double max = (median+5.0*variance);

  // create function
  std::ostringstream oss;
  oss << "_Random_Lognormal__lognormfcn_" << (counter_++);
  lognormfcn_ = new TF1(oss.str().c_str(), lognormal, min, max, 2);
  lognormfcn_->SetParameter(0, median);
  lognormfcn_->SetParameter(1, variance);
}

RandomLognormal::RandomLognormal(double median, double variance, double min, double max)
{
  // create function
  std::ostringstream oss;
  oss << "_Random_Lognormal__lognormfcn_" << (counter_++);
  lognormfcn_ = new TF1(oss.str().c_str(), lognormal, min, max, 2);
  lognormfcn_->SetParameter(0, median);
  lognormfcn_->SetParameter(1, variance);
}

RandomLognormal::~RandomLognormal()
{
  delete lognormfcn_;
}

double RandomLognormal::getRandom(void) const
{
  return lognormfcn_->GetRandom();
}
