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


xs_stat = [4.08257, 1.15721, 0.411506, 1.15263, 1.92977, 1.49016, 0.619607, 0.358359, 0.25801, 0.239432, 0.211465, 0.140706, 0.119473, 0.163481, 0.205587, 0.186243, 0.166694, 0.138751, 0.111409, 0.0986304, 0.104581, 0.11652, 0.113457, 0.0909747, 0.0661994, 0.0496412, 0.0398354, 0.03632, 0.0391764, 0.0470021, 0.0538693, 0.0533153, 0.0462661, 0.037536, 0.0318938, 0.0310645, 0.0324212, 0.0327933, 0.0311751, 0.0276193, 0.0229468, 0.0178672, 0.0133949, 0.0103379, 0.008632, 0.00751769, 0.00640263, 0.00573242, 0.00528528, 0.00497243, 0.00478172, 0.00464553, 0.00454648, 0.00447099, 0.0044117, 0.00436576, 0.00433159, 0.00430457, 0.00428106]
xs_stat_exp = [1.88695, 1.38645, 1.04097, 0.944241, 0.790821, 0.628347, 0.541367, 0.464813, 0.391869, 0.350656, 0.280238, 0.243175, 0.23424, 0.221311, 0.179991, 0.159704, 0.136738, 0.135707, 0.109479, 0.0996454, 0.0867903, 0.0767661, 0.0742238, 0.0665354, 0.061057, 0.0508328, 0.0484223, 0.0426503, 0.0407527, 0.0359847, 0.0320939, 0.0310224, 0.0271168, 0.0252927, 0.0231952, 0.0226623, 0.0203398, 0.0185865, 0.0170746, 0.0156388, 0.0147899, 0.013356, 0.0128138, 0.0132808, 0.0120217, 0.0115591, 0.0106948, 0.00998218, 0.00962778, 0.00915704, 0.00855671, 0.00809804, 0.00779993, 0.00758996, 0.00721888, 0.00714414, 0.00697149, 0.00681597, 0.00654551]

xs_sys_all = [9.40926, 2.43906, 0.910499, 2.08377, 2.5177, 1.93801, 0.966811, 0.52548, 0.372833, 0.329731, 0.281811, 0.197427, 0.17298, 0.214424, 0.249173, 0.231978, 0.207971, 0.17574, 0.145654, 0.129756, 0.130175, 0.134556, 0.127838, 0.107588, 0.0816507, 0.0613637, 0.0489548, 0.0440702, 0.0467642, 0.0528795, 0.0572189, 0.0560747, 0.0500719, 0.0423368, 0.0363495, 0.0345555, 0.0342006, 0.0336598, 0.0316734, 0.0286289, 0.024299, 0.0192873, 0.0147333, 0.011114, 0.00910687, 0.00733415, 0.00643575, 0.00567518, 0.00525264, 0.00497117, 0.00470794, 0.00461385, 0.00453011, 0.00449871, 0.00436492, 0.00437861, 0.00432459, 0.00422855, 0.00418351]
xs_sys_all_exp = [5.204195, 2.86269, 2.050125, 1.64843, 1.35405, 1.070275, 0.801828, 0.6297815, 0.544051, 0.4537925, 0.384346, 0.346753, 0.291055, 0.2584985, 0.232526, 0.214876, 0.190474, 0.1675035, 0.1394435, 0.1285075, 0.1180065, 0.1020255, 0.0864763, 0.07896825, 0.0713416, 0.06460235, 0.0542506, 0.04943465, 0.0474189, 0.0450728, 0.0376913, 0.034277, 0.02910485, 0.0279689, 0.0262188, 0.0241634, 0.0209493, 0.01944405, 0.0176617, 0.0155395, 0.01619395, 0.0152521, 0.0136574, 0.0136716, 0.01205665, 0.011283, 0.0106252, 0.010188, 0.00948734, 0.00901268, 0.0085077, 0.008262875, 0.00787107, 0.00746096, 0.007187505, 0.006853685, 0.00669998, 0.00650749, 0.006351665]

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
g_all_exp.GetXaxis().SetTitle("qq resonance mass [GeV]")
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

c.SaveAs('xs_limit_ratio_qq_Run2_13TeV.pdf')
