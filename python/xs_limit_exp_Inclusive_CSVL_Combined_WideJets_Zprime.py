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
xs_comb_0p1 = array('d', [0.44634600000000002, 0.31292399999999998, 0.23841899999999999, 0.18626499999999999, 0.15978100000000001, 0.133435, 0.097038700000000006, 0.074506000000000003, 0.059604999999999998, 0.052155199999999999, 0.0539877, 0.0547459, 0.036292400000000002, 0.0268147, 0.026243699999999998, 0.027914100000000001, 0.0199942, 0.013547099999999999, 0.010710300000000001, 0.0083822500000000008, 0.0074987300000000003, 0.0065193999999999998, 0.0055880399999999998, 0.00488945, 0.0042343499999999996, 0.00361065, 0.0032667099999999999, 0.0030792300000000001, 0.0026073699999999999, 0.0022119000000000002, 0.0018626599999999999])
xs_comb_1p0 = array('d', [0.211867, 0.17444499999999999, 0.13428799999999999, 0.11565599999999999, 0.099118700000000004, 0.076368500000000006, 0.0684757, 0.068145899999999995, 0.056385299999999999, 0.050083500000000003, 0.042538300000000001, 0.038610800000000001, 0.032862000000000002, 0.027311200000000001, 0.027270599999999999, 0.026530999999999999, 0.023123999999999999, 0.0154284, 0.0134725, 0.0102446, 0.0088475800000000007, 0.0074508999999999999, 0.0069642200000000001, 0.0060536799999999997, 0.0054501000000000003, 0.0049948299999999996, 0.0041914600000000002, 0.0038072399999999999, 0.0034146300000000001, 0.00302681, 0.0025611399999999999])
xs_incl_0p1 = array('d', [0.45216099999999998, 0.31296299999999999, 0.22724800000000001, 0.18626499999999999, 0.14901600000000001, 0.12994700000000001, 0.097380700000000001, 0.078623899999999997, 0.063330899999999996, 0.0540191, 0.053413200000000001, 0.046024900000000001, 0.034925200000000003, 0.029125600000000001, 0.0248723, 0.0241315, 0.0195731, 0.0142775, 0.010913300000000001, 0.0093790799999999997, 0.0079172900000000004, 0.0065192899999999996, 0.0056522999999999999, 0.0046566100000000003, 0.0041909499999999997, 0.0037389799999999998, 0.0030420899999999999, 0.0027939699999999998, 0.0025807999999999998, 0.0020954799999999998, 0.0018928599999999999])
xs_incl_1p0 = array('d', [0.57566700000000004, 0.40233099999999999, 0.30438199999999999, 0.23469400000000001, 0.18626499999999999, 0.15815899999999999, 0.119268, 0.0968691, 0.081959299999999999, 0.068686399999999995, 0.057952200000000002, 0.052431899999999997, 0.047501500000000002, 0.037827600000000003, 0.031664600000000001, 0.0308247, 0.0263275, 0.020127200000000001, 0.0155575, 0.012587599999999999, 0.011059299999999999, 0.0092695599999999996, 0.0078386600000000008, 0.0065193899999999999, 0.0055879900000000001, 0.0049103200000000001, 0.0043328000000000004, 0.0037252299999999999, 0.0032596399999999998, 0.0028013999999999999, 0.0025611399999999999])

g_comb_0p1 = TGraph(len(masses),masses,xs_comb_0p1)
g_comb_0p1.SetMarkerStyle(24)
g_comb_0p1.SetMarkerColor(kRed)
g_comb_0p1.SetLineWidth(2)
g_comb_0p1.SetLineStyle(1)
g_comb_0p1.SetLineColor(kRed)
g_comb_0p1.GetXaxis().SetTitle("Resonance Mass [GeV]")
g_comb_0p1.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
g_comb_0p1.GetYaxis().SetRangeUser(1e-03,10)
g_comb_0p1.GetXaxis().SetNdivisions(1005)

g_comb_1p0 = TGraph(len(masses),masses,xs_comb_1p0)
g_comb_1p0.SetMarkerStyle(25)
g_comb_1p0.SetMarkerColor(kRed)
g_comb_1p0.SetLineWidth(2)
g_comb_1p0.SetLineStyle(2)
g_comb_1p0.SetLineColor(kRed)

g_incl_0p1 = TGraph(len(masses),masses,xs_incl_0p1)
g_incl_0p1.SetMarkerStyle(26)
g_incl_0p1.SetMarkerColor(kGreen+2)
g_incl_0p1.SetLineWidth(2)
g_incl_0p1.SetLineStyle(1)
g_incl_0p1.SetLineColor(kGreen+2)

g_incl_1p0 = TGraph(len(masses),masses,xs_incl_1p0)
g_incl_1p0.SetMarkerStyle(27)
g_incl_1p0.SetMarkerColor(kGreen+2)
g_incl_1p0.SetLineWidth(2)
g_incl_1p0.SetLineStyle(2)
g_incl_1p0.SetLineColor(kGreen+2)

c = TCanvas("c", "",800,800)
c.cd()

g_comb_0p1.Draw("ALP")
g_comb_1p0.Draw("LP")
g_incl_0p1.Draw("LP")
g_incl_1p0.Draw("LP")

legend = TLegend(.45,.60,.85,.80)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader("Exp. 95% CL Upper Limits (stat. only)")
legend.AddEntry(g_comb_0p1, "Combined b-tagged (f_{b#bar{b}} = 0.1)","lp")
legend.AddEntry(g_comb_1p0, "Combined b-tagged (f_{b#bar{b}} = 1.0)","lp")
legend.AddEntry(g_incl_0p1, "Inclusive untagged (f_{b#bar{b}} = 0.1)","lp")
legend.AddEntry(g_incl_1p0, "Inclusive untagged (f_{b#bar{b}} = 1.0)","lp")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.89, "Z'-like")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")

c.SetLogy()
c.SaveAs('Inclusive_CSVL_Combined_limit_exp_WideJets_Zprime.eps')

