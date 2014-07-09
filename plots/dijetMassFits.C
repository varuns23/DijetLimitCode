#include <iostream>
#include "TROOT.h"
#include "TStyle.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TH1D.h"
#include "TF1.h"
#include "TString.h"
#include "TMinuit.h"
#include "TVirtualFitter.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TFitResult.h"

using namespace std;


Double_t fitQCD4Par(Double_t *m, Double_t *p)
{
    double x=m[0]/8000.;
    return p[0]*pow(1.-x,p[1])/pow(x,p[2]+p[3]*log(x));
}

Double_t fitQCD6Par(Double_t *m, Double_t *p)
{
    double x=m[0]/8000.;
    return p[0]*pow(1.-x,p[1])/pow(x,p[2]+p[3]*log(x)+p[4]*pow(log(x),2)+p[5]*pow(log(x),3));
}

void performFit(const string& fInputFile, const string& fPlot, const Int_t fNbins, const Double_t *fBins,
                const Double_t fLumi, const Double_t fFitXmin, const Double_t fFitXmax, const string& fLabel,
                const string& fOutputFile, const bool use6ParFit, const Double_t fP0=1e-04, const Double_t fP1=1e+01,
                const Double_t fP2=4e+00, const Double_t fP3=-0.1e-01, const Double_t fP4=0, const Double_t fP5=0)
{
  gROOT->SetBatch(kTRUE);
  gStyle->SetOptStat(kFALSE);
  gStyle->SetOptTitle(kFALSE);
  gStyle->SetPadLeftMargin(0.13);
  gStyle->SetPadRightMargin(0.07);

//   cout << "Default number of iterations: " << TVirtualFitter::GetMaxIterations() << endl;
  TVirtualFitter::SetMaxIterations(30000);

  TFile *file = new TFile(fInputFile.c_str());

  TH1D *h1_plot = (TH1D*)file->Get(fPlot.c_str());

  TH1D *h1_plot_r = (TH1D*)h1_plot->Rebin(fNbins,"h1_plot_r",fBins);

  TH1D *h1_plot_diff = (TH1D*)h1_plot_r->Clone();
  h1_plot_diff->Reset();

  for(Int_t i=1; i<=h1_plot_r->GetNbinsX(); ++i)
  {
    Double_t n   = h1_plot_r->GetBinContent(i);
    Double_t err = h1_plot_r->GetBinError(i);
    Double_t dm  = h1_plot_r->GetBinWidth(i);
   
    h1_plot_diff->SetBinContent(i, n/(dm*fLumi));
    h1_plot_diff->SetBinError(i, err/(dm*fLumi));
  }

  h1_plot_diff->GetXaxis()->SetTitle("Dijet Mass [GeV]");
  h1_plot_diff->GetYaxis()->SetTitle("d#sigma/dm [pb/GeV]");
  h1_plot_diff->GetYaxis()->SetRangeUser(1e-7,1e3);
  h1_plot_diff->SetMarkerStyle(20);
  h1_plot_diff->SetMarkerSize(0.8);
  h1_plot_diff->SetTitleOffset(1.4,"Y");

  // Fit to data
  TF1 *fit = new TF1("fit",fitQCD4Par,fFitXmin,fFitXmax,4);           // 4 Param. Fit
  if(use6ParFit) fit = new TF1("fit",fitQCD6Par,fFitXmin,fFitXmax,6); // 6 Param. Fit
//   gStyle->SetOptFit(1111);
  fit->SetParameter(0,fP0);
  fit->SetParameter(1,fP1);
  fit->SetParameter(2,fP2);
  fit->SetParameter(3,fP3);
  if(use6ParFit)
  {
    fit->SetParameter(4,fP4);
    fit->SetParameter(5,fP5);
  }
//   fit->SetParLimits(0, 0., 1.);
//   fit->SetParLimits(1, 0., 100.);
//   fit->SetParLimits(2, 0., 100.);
//   fit->SetParLimits(3,-5., 5.);
//   fit->FixParameter(3,fP3);

  fit->SetLineWidth(2);
  fit->SetLineColor(kBlue);
  cout << "*********************************************************"<<endl;
  TFitResultPtr s = h1_plot_diff->Fit("fit","SR");
  TString status_default = gMinuit->fCstatu.Data();
  // Results of the fit
  cout << "*********************************************************"<<endl;
  Double_t chi_fit = fit->GetChisquare();
  Double_t ndf_fit = fit->GetNDF();
  cout << "Chi2/ndf: " << chi_fit << "/" << ndf_fit << " = " << chi_fit/ndf_fit << endl;
  cout << "Status: "<<status_default<<endl;
  cout << "*********************************************************"<<endl;

  // Print fit results
  s->Print("V");
  
  TCanvas *c = new TCanvas("c", "",800,800);
  c->cd();

  h1_plot_diff->Draw();

  TLegend *legend = new TLegend(.7,.4,.85,.5);
  legend->SetBorderSize(0);
  legend->SetFillColor(0);
  legend->SetFillStyle(0);
  legend->AddEntry(h1_plot_diff, "Data","lp");
  legend->AddEntry(fit, "Fit","l");
  legend->Draw();
  
  TLatex l1;
  l1.SetTextAlign(12);
//   l1.SetTextFont(42);
  l1.SetNDC();
  l1.SetTextSize(0.03);
  l1.DrawLatex(0.17,0.33, "CMS Preliminary");
  l1.DrawLatex(0.17,0.27, "#intLdt = 19 fb^{-1}");
  l1.DrawLatex(0.17,0.23, "#sqrt{s} = 8 TeV");
  l1.DrawLatex(0.17,0.15, fLabel.c_str());
  
  c->SetLogy();
  c->SaveAs(fOutputFile.c_str());

  delete c;
  delete file;
}



void drawFit(const string& fInputFile, const string& fPlot, const Int_t fNbins, const Double_t *fBins,
             const Double_t fLumi, const Double_t fFitXmin, const Double_t fFitXmax, const string& fLabel,
             const string& fOutputFile, const bool use6ParFit, const Double_t fP0=1e-04, const Double_t fP1=1e+01,
             const Double_t fP2=4e+00, const Double_t fP3=-0.1e-01, const Double_t fP4=0, const Double_t fP5=0)
{
  gROOT->SetBatch(kTRUE);
  gStyle->SetOptStat(kFALSE);
  gStyle->SetOptTitle(kFALSE);
  gStyle->SetPadLeftMargin(0.13);
  gStyle->SetPadRightMargin(0.07);

  TFile *file = new TFile(fInputFile.c_str());

  TH1D *h1_plot = (TH1D*)file->Get(fPlot.c_str());

  TH1D *h1_plot_r = (TH1D*)h1_plot->Rebin(fNbins,"h1_plot_r",fBins);

  TH1D *h1_plot_diff = (TH1D*)h1_plot_r->Clone();
  h1_plot_diff->Reset();

  for(Int_t i=1; i<=h1_plot_r->GetNbinsX(); ++i)
  {
    Double_t n   = h1_plot_r->GetBinContent(i);
    Double_t err = h1_plot_r->GetBinError(i);
    Double_t dm  = h1_plot_r->GetBinWidth(i);

    h1_plot_diff->SetBinContent(i, n/(dm*fLumi));
    h1_plot_diff->SetBinError(i, err/(dm*fLumi));
  }

  h1_plot_diff->GetXaxis()->SetTitle("Dijet Mass [GeV]");
  h1_plot_diff->GetYaxis()->SetTitle("d#sigma/dm [pb/GeV]");
  h1_plot_diff->GetYaxis()->SetRangeUser(1e-7,1e3);
  h1_plot_diff->SetMarkerStyle(20);
  h1_plot_diff->SetMarkerSize(0.8);
  h1_plot_diff->SetTitleOffset(1.4,"Y");

  // Fit function
  TF1 *fit = new TF1("fit",fitQCD4Par,fFitXmin,fFitXmax,4);           // 4 Param. Fit
  if(use6ParFit) fit = new TF1("fit",fitQCD6Par,fFitXmin,fFitXmax,6); // 6 Param. Fit
  fit->FixParameter(0,fP0/fLumi);
  fit->FixParameter(1,fP1);
  fit->FixParameter(2,fP2);
  fit->FixParameter(3,fP3);
  if(use6ParFit)
  {
    fit->FixParameter(4,fP4);
    fit->FixParameter(5,fP5);
  }

  fit->SetLineWidth(2);
  fit->SetLineColor(kBlue);

  TCanvas *c = new TCanvas("c", "",800,800);
  c->cd();

  h1_plot_diff->Draw();
  fit->Draw("same");

  TLegend *legend = new TLegend(.7,.4,.85,.5);
  legend->SetBorderSize(0);
  legend->SetFillColor(0);
  legend->SetFillStyle(0);
  legend->AddEntry(h1_plot_diff, "Data","lp");
  legend->AddEntry(fit, "Fit","l");
  legend->Draw();

  TLatex l1;
  l1.SetTextAlign(12);
//   l1.SetTextFont(42);
  l1.SetNDC();
  l1.SetTextSize(0.03);
  l1.DrawLatex(0.17,0.33, "CMS Preliminary");
  l1.DrawLatex(0.17,0.27, "#intLdt = 19 fb^{-1}");
  l1.DrawLatex(0.17,0.23, "#sqrt{s} = 8 TeV");
  l1.DrawLatex(0.17,0.15, fLabel.c_str());

  c->SetLogy();
  c->SaveAs(fOutputFile.c_str());

  delete c;
  delete file;
}


void makePlots()
{

  Double_t xbins[] = {  325,  354,  386,  419,  453,  489,  526,  565,  606,  649,  693,  740,  788,  838,
                        890,  944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770,
                       1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279,
                       3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058 };

// ##################
// ## Dijet scouting
// ##################

  performFit("Data_and_ResonanceShapes/DataScouting_Bora040214_Run2012BCD_runrange_193834-208686_dijet.root",
             "scoutingDiJetVariables/h1_MjjWide_finalSel", 52, xbins,
             19000, 325, 5058, "M_{jj}>325 GeV", "DijetMass_4ParFit_DijetScouting_Run1_8TeV.eps", 0, 1.89589e-06, 5.26434e+00, 7.25675e+00, 3.77102e-01);

  performFit("Data_and_ResonanceShapes/DataScouting_Bora040214_Run2012BCD_runrange_193834-208686_dijet.root",
             "scoutingDiJetVariables/h1_MjjWide_finalSel", 52, xbins,
             19000, 325, 5058, "M_{jj}>325 GeV", "DijetMass_6ParFit_DijetScouting_Run1_8TeV.eps", 1, 5.80192e-05, 8.84523e+00, 4.74445e+00, -2.30726e-01, -2.65443e-02, 5.61031e-03);

  drawFit("Data_and_ResonanceShapes/DataScouting_Bora040214_Run2012BCD_runrange_193834-208686_dijet.root",
          "scoutingDiJetVariables/h1_MjjWide_finalSel", 52, xbins,
          19000, 325, 5058, "M_{jj}>325 GeV", "DijetMass_Draw4ParFit_DijetScouting_Run1_8TeV.eps", 0, 3.63970e-02, 5.28137e+00, 7.24871e+0, 3.76469e-01);

  drawFit("Data_and_ResonanceShapes/DataScouting_Bora040214_Run2012BCD_runrange_193834-208686_dijet.root",
          "scoutingDiJetVariables/h1_MjjWide_finalSel", 52, xbins,
          19000, 325, 5058, "M_{jj}>325 GeV", "DijetMass_Draw6ParFit_DijetScouting_Run1_8TeV.eps", 1, 6.38418e-02, 6.51937e+00, 7.43862e+00, 8.27179e-01, 1.70526e-01, 1.99467e-02);
}

