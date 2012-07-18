#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()


masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_CSVL = array('d', [0.230407, 0.16552, 0.14075199999999999, 0.106697, 0.092528899999999997, 0.080888000000000002, 0.073737200000000003, 0.061639699999999999, 0.054559799999999999, 0.048937399999999999, 0.041352699999999999, 0.032641799999999999, 0.0290809, 0.024971699999999999, 0.023012999999999999, 0.018338699999999999, 0.016216100000000001, 0.013420899999999999, 0.012352200000000001, 0.010660299999999999, 0.0092406299999999997, 0.0079368200000000007, 0.0069036000000000002, 0.0060510099999999999, 0.0051682899999999999, 0.0046795099999999996, 0.0042695900000000002, 0.0036036100000000001, 0.0031934200000000002, 0.0028628299999999998, 0.0024946299999999999])
xs_CSVM = array('d', [0.18385799999999999, 0.12766, 0.116817, 0.0985983, 0.0854573, 0.074692999999999996, 0.060577600000000002, 0.0542148, 0.048579499999999998, 0.046760500000000003, 0.044961399999999999, 0.035224999999999999, 0.030095799999999999, 0.0278091, 0.022091699999999999, 0.019181699999999999, 0.015778500000000001, 0.0141841, 0.012389799999999999, 0.01076, 0.0091437099999999993, 0.0078811599999999999, 0.0070743200000000003, 0.0061536899999999999, 0.0052845799999999997, 0.0043975799999999999, 0.0039847499999999996, 0.00348979, 0.0033443399999999999, 0.00298606, 0.0025222199999999999])
xs_TCHEL = array('d', [0.46946199999999999, 0.33847100000000002, 0.26385999999999998, 0.197653, 0.16266600000000001, 0.13825599999999999, 0.117217, 0.100137, 0.076528100000000002, 0.061874499999999999, 0.0537259, 0.047278100000000003, 0.0382925, 0.030430499999999999, 0.026577199999999999, 0.024372899999999999, 0.020081600000000002, 0.017305899999999999, 0.0140844, 0.012087799999999999, 0.0099779499999999993, 0.0086453199999999997, 0.0070874900000000001, 0.0062656600000000002, 0.0054286200000000003, 0.0047464899999999999, 0.0040479499999999998, 0.00362028, 0.00322201, 0.0028852999999999999, 0.0025588500000000001])

g_CSVL = TGraph(len(masses),masses,xs_CSVL)
g_CSVL.SetMarkerStyle(24)
g_CSVL.SetMarkerColor(kGreen+2)
g_CSVL.SetLineWidth(2)
g_CSVL.SetLineStyle(1)
g_CSVL.SetLineColor(kGreen+2)
g_CSVL.GetXaxis().SetTitle("Resonance Mass [GeV]")
g_CSVL.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
g_CSVL.GetYaxis().SetRangeUser(1e-03,10)
g_CSVL.GetXaxis().SetNdivisions(1005)

g_CSVM = TGraph(len(masses),masses,xs_CSVM)
g_CSVM.SetMarkerStyle(25)
g_CSVM.SetMarkerColor(kRed)
g_CSVM.SetLineWidth(2)
g_CSVM.SetLineStyle(2)
g_CSVM.SetLineColor(kRed)

g_TCHEL = TGraph(len(masses),masses,xs_TCHEL)
g_TCHEL.SetMarkerStyle(26)
g_TCHEL.SetMarkerColor(kBlue)
g_TCHEL.SetLineWidth(2)
g_TCHEL.SetLineStyle(3)
g_TCHEL.SetLineColor(kBlue)


c = TCanvas("c", "",800,800)
c.cd()

g_CSVL.Draw("AL")
g_CSVM.Draw("L")
g_TCHEL.Draw("L")

legend = TLegend(.45,.60,.85,.80)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader("Exp. 95% CL Upper Limits (stat. only)")
legend.AddEntry(g_TCHEL, "TCHEL","l")
legend.AddEntry(g_CSVL, "CSVL","l")
legend.AddEntry(g_CSVM, "CSVM","l")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.89, "qq/bb, f_{b#bar{b}}=1.0")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.055)
l1.DrawLatex(0.535,0.84, "0, 1 and 2 b-tags")

c.SetLogy()
c.SaveAs('CSVL_CSVM_TCHEL_Combined_limit_exp_SplusB_WideJets_Zprime_fbb1.0.eps')
