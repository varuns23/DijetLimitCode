#!/usr/bin/env python

import string, re
from ROOT import *
from array import array
import CMS_lumi

CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "1 fb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

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


xs_stat = [20.9545, 2.45626, 0.416225, 1.01931, 2.82771, 2.19572, 1.16475, 0.465517, 0.312011, 0.257445, 0.232343, 0.186241, 0.14177, 0.161448, 0.223433, 0.235894, 0.22298, 0.192951, 0.164016, 0.141445, 0.132672, 0.144567, 0.154099, 0.139979, 0.109849, 0.0806352, 0.0624284, 0.0528164, 0.0509088, 0.0567577, 0.0680257, 0.0716774, 0.0677652, 0.0582306, 0.0484861, 0.0427263, 0.0406525, 0.0400296, 0.0383613, 0.0356998, 0.0308406, 0.0253015, 0.0198666, 0.0152415, 0.0123197, 0.0110247, 0.00929554, 0.00821889, 0.00775016, 0.00722283, 0.00679991, 0.00656296, 0.00640062, 0.00628973, 0.0062155, 0.00616987, 0.00614263, 0.00613129, 0.00613597]
xs_stat_exp = [2.63206, 2.14471, 1.63841, 1.48217, 1.05316, 0.81135, 0.67681, 0.62097, 0.513012, 0.431082, 0.38607, 0.341819, 0.298624, 0.270375, 0.245451, 0.199897, 0.178578, 0.172584, 0.150738, 0.130131, 0.118085, 0.100697, 0.0934993, 0.0868947, 0.0863419, 0.0747488, 0.0630101, 0.0636891, 0.051635, 0.0489897, 0.0445535, 0.0413454, 0.0356299, 0.0323483, 0.0317702, 0.028163, 0.0258878, 0.0248127, 0.0219089, 0.0212312, 0.0193777, 0.0184784, 0.0187839, 0.0172933, 0.0165523, 0.0149275, 0.0144313, 0.0136047, 0.013115, 0.0127536, 0.0121895, 0.0116958, 0.0112944, 0.010989, 0.010528, 0.0103265, 0.00995773, 0.00966355, 0.00945783]

xs_sys_all = [35.7264, 5.97138, 1.07455, 2.46052, 3.95921, 3.08949, 1.86666, 0.870688, 0.550472, 0.432721, 0.372332, 0.302224, 0.243555, 0.266118, 0.322454, 0.327492, 0.311861, 0.271667, 0.233994, 0.201787, 0.190201, 0.192072, 0.190403, 0.167939, 0.139344, 0.105079, 0.0832827, 0.0691544, 0.0645502, 0.0680858, 0.074493, 0.0761205, 0.0725783, 0.0632614, 0.054249, 0.0477713, 0.0445409, 0.042211, 0.0399109, 0.0363099, 0.031959, 0.0265896, 0.021285, 0.0166404, 0.0129277, 0.011293, 0.00950463, 0.00844172, 0.00751178, 0.00699131, 0.00659847, 0.00652256, 0.00620023, 0.00613404, 0.00608264, 0.00598963, 0.00589662, 0.00596361, 0.00591097]
xs_sys_all_exp = [7.089085, 5.242335, 3.21493, 2.72778, 2.34251, 1.63937, 1.28518, 0.987911, 0.7813015, 0.65491, 0.5756145, 0.5110295, 0.4461375, 0.3843525, 0.356416, 0.309132, 0.278282, 0.2505985, 0.2180305, 0.187398, 0.170246, 0.14912, 0.1350605, 0.1142885, 0.105468, 0.0924162, 0.07800015, 0.07171155, 0.0638171, 0.05862455, 0.05148225, 0.0468188, 0.04034695, 0.0380869, 0.0330677, 0.031396, 0.02826355, 0.02571415, 0.0239881, 0.0217299, 0.02049585, 0.0190612, 0.0193599, 0.01804035, 0.0172123, 0.01540465, 0.01439935, 0.01377615, 0.01311775, 0.0125172, 0.01203865, 0.0116187, 0.0109783, 0.0107402, 0.0103624, 0.01000241, 0.00984678, 0.009574005, 0.00936249]

masses = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])

r_all_exp = array('d')
r_all = array('d')

for i in range(0,len(xs_stat)):
  r_all_exp.append( xs_sys_all_exp[i] / xs_stat_exp[i] )
  r_all.append( xs_sys_all[i] / xs_stat[i] )

g_all_exp = TGraph(len(masses),masses,r_all_exp)
g_all_exp.SetMarkerStyle(24)
g_all_exp.SetMarkerColor(kGreen+2)
g_all_exp.SetLineWidth(2)
g_all_exp.SetLineStyle(2)
g_all_exp.SetLineColor(kGreen+2)
g_all_exp.GetXaxis().SetTitle("qg resonance mass [GeV]")
g_all_exp.GetYaxis().SetTitle("Limit ratio (Syst./Stat. only)")
g_all_exp.GetYaxis().SetRangeUser(0.5,3.5)
#g_all_exp.GetXaxis().SetNdivisions(1005)

g_all = TGraph(len(masses),masses,r_all)
g_all.SetMarkerStyle(20)
g_all.SetMarkerColor(kBlack)
g_all.SetLineWidth(2)
g_all.SetLineStyle(1)
g_all.SetLineColor(kBlack)

c = TCanvas("c", "",800,800)
c.cd()

g_all_exp.Draw("ALP")
g_all.Draw("LP")

legend = TLegend(.40,.65,.60,.75)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.AddEntry(g_all_exp, "All / Stat. only (expected)","lp")
legend.AddEntry(g_all, "All / Stat. only","lp")

legend.Draw()

#l1 = TLatex()
#l1.SetTextAlign(12)
#l1.SetTextFont(42)
#l1.SetNDC()
#l1.SetTextSize(0.04)
#l1.DrawLatex(0.18,0.43, "CMS Preliminary")
#l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
#l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
#l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
#l1.DrawLatex(0.18,0.20, "Wide Jets")

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SaveAs('xs_limit_ratio_qg_Run2_13TeV.pdf')
