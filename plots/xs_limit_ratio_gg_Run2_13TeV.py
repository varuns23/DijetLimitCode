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


xs_stat = [30.303, 7.06149, 0.551883, 0.826844, 3.9482, 3.31129, 2.0955, 0.713729, 0.443153, 0.357982, 0.330766, 0.258931, 0.186376, 0.197092, 0.291734, 0.323995, 0.303538, 0.277921, 0.237822, 0.2052, 0.181507, 0.196302, 0.222027, 0.211771, 0.173583, 0.125038, 0.0978138, 0.0787462, 0.0722822, 0.076304, 0.0949005, 0.103527, 0.102056, 0.0883539, 0.0710818, 0.0608987, 0.0568118, 0.0562941, 0.0541762, 0.0505432, 0.044734, 0.0373533, 0.0287415, 0.0237149, 0.0179518, 0.014523, 0.0142933, 0.0124812, 0.0112436, 0.0106327, 0.0101725, 0.00996536, 0.00986499, 0.00985501, 0.00992039, 0.0100315, 0.0101831, 0.0104826, 0.010764]
xs_stat_exp = [3.18953, 2.75638, 1.97588, 2.07047, 1.51395, 1.13639, 1.02512, 0.825541, 0.687576, 0.645197, 0.52206, 0.45338, 0.455349, 0.364867, 0.337383, 0.318141, 0.265012, 0.258696, 0.210641, 0.197798, 0.17854, 0.148266, 0.131337, 0.12382, 0.106044, 0.0991548, 0.0998414, 0.0819558, 0.074092, 0.0665097, 0.0616004, 0.0510265, 0.0497565, 0.0490886, 0.042432, 0.0388045, 0.0357015, 0.0345422, 0.030691, 0.0286476, 0.0273476, 0.0260991, 0.0252136, 0.0259524, 0.0235038, 0.0227757, 0.0207493, 0.0197729, 0.0187126, 0.0181336, 0.0181289, 0.017387, 0.0168164, 0.0168141, 0.0166783, 0.0163614, 0.0163255, 0.0162972, 0.0163624]

xs_sys_all = [48.9834, 15.5104, 1.48702, 2.1846, 5.88462, 4.96351, 3.43921, 1.46977, 0.883418, 0.670762, 0.589426, 0.47658, 0.352378, 0.360963, 0.457307, 0.493142, 0.474156, 0.420971, 0.35761, 0.307648, 0.277725, 0.282715, 0.288767, 0.264133, 0.225759, 0.172839, 0.132423, 0.108127, 0.0957965, 0.0948413, 0.108401, 0.112502, 0.109777, 0.0974121, 0.0797746, 0.0690627, 0.0622704, 0.0600981, 0.0564474, 0.052898, 0.0471089, 0.0400551, 0.0312469, 0.0253978, 0.0195747, 0.0157275, 0.0143459, 0.0125606, 0.011287, 0.0106264, 0.0101563, 0.00984405, 0.00977102, 0.00969628, 0.00980263, 0.00980642, 0.0100955, 0.0103283, 0.010417]
xs_sys_all_exp = [14.3099, 7.80575, 4.45056, 4.424585, 3.6377, 2.577925, 2.109985, 1.5597, 1.276695, 1.02019, 0.9100545, 0.786793, 0.7137335, 0.6000835, 0.5186635, 0.496075, 0.444928, 0.383262, 0.330726, 0.3006895, 0.262522, 0.22892, 0.2040955, 0.172871, 0.157564, 0.13855, 0.126422, 0.1122625, 0.103113, 0.0875804, 0.07824025, 0.06682445, 0.0597073, 0.052169, 0.04806775, 0.04278875, 0.0397887, 0.0375644, 0.03554385, 0.03150335, 0.02964935, 0.0292615, 0.026412, 0.024826, 0.02543485, 0.0240541, 0.0209813, 0.0195814, 0.01894845, 0.01835845, 0.0179551, 0.01763815, 0.01726835, 0.0169003, 0.0166459, 0.0164321, 0.01632505, 0.0163281, 0.01661895]

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
g_all_exp.GetXaxis().SetTitle("gg resonance mass [GeV]")
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

c.SaveAs('xs_limit_ratio_gg_Run2_13TeV.pdf')
