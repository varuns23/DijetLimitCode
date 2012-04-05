#include "binneddata.hh"
#include "fit.hh"

#include <cassert>
#include <iostream>
#include <fstream>

#include <TFile.h>
#include <TH1D.h>

TH1D* getData(const std::vector<std::string>& filenames, const char* histname, int nbins, double* bins)
{
  TH1D* hist=new TH1D("normalized_data", "normalized data", nbins, bins);

  unsigned nFiles = filenames.size();
  
  TFile *files[nFiles];
  TH1D *hists[nFiles];

  // open input files and get input histograms
  for(unsigned i=0; i<nFiles; ++i)
  {
    files[i] = new TFile(filenames[i].c_str());
    hists[i] = (TH1D*)files[i]->Get(histname);
  }

  // normalize the data in the histogram
  for(int i=1; i<=hist->GetNbinsX(); ++i) {
   
    if(hist->GetXaxis()->GetBinUpEdge(i)<=5890.)
    {
      double offset = 0.;
      int bin_min = hists[0]->GetXaxis()->FindBin(hist->GetXaxis()->GetBinLowEdge(i)-offset+0.5);
      int bin_max = hists[0]->GetXaxis()->FindBin(hist->GetXaxis()->GetBinUpEdge(i)-offset-0.5);
      double val=hists[0]->Integral(bin_min,bin_max);
      double err=Fitter::histError(val);
      double width=hist->GetBinWidth(i);
      hist->SetBinContent(i, val/width);
      hist->SetBinError(i, err/width);
    }
    else if(hist->GetXaxis()->GetBinUpEdge(i)>5890. && hist->GetXaxis()->GetBinUpEdge(i)<=10890. && nFiles>1)
    {
      double offset = 5000.;
      int bin_min = hists[1]->GetXaxis()->FindBin(hist->GetXaxis()->GetBinLowEdge(i)-offset+0.5);
      int bin_max = hists[1]->GetXaxis()->FindBin(hist->GetXaxis()->GetBinUpEdge(i)-offset-0.5);
      double val=hists[1]->Integral(bin_min,bin_max);
      double err=Fitter::histError(val);
      double width=hist->GetBinWidth(i);
      hist->SetBinContent(i, val/width);
      hist->SetBinError(i, err/width);
    }
    else if(hist->GetXaxis()->GetBinUpEdge(i)>10890. && nFiles>2)
    {
      double offset = 10000.;
      int bin_min = hists[2]->GetXaxis()->FindBin(hist->GetXaxis()->GetBinLowEdge(i)-offset+0.5);
      int bin_max = hists[2]->GetXaxis()->FindBin(hist->GetXaxis()->GetBinUpEdge(i)-offset-0.5);
      double val=hists[2]->Integral(bin_min,bin_max);
      double err=Fitter::histError(val);
      double width=hist->GetBinWidth(i);
      hist->SetBinContent(i, val/width);
      hist->SetBinError(i, err/width);
    }
  }

  // do some checks
  if(hist->GetBinContent(0)>0.0 || hist->GetBinContent(hist->GetNbinsX()+1)>0.0) {
    std::cerr << "There is an underflow/overflow.  This should be fixed.  Please rebin!" << std::endl;
    assert(0);
  }
  if(hist->GetBinContent(1)<=0.0) {
    std::cerr << "The first data bin is empty. This will give incorrect results.  Please rebin!" << std::endl;
    assert(0);
  }

  return hist;
}
