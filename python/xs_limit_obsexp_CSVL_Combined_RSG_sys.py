#!/usr/bin/env python

import sys, os, string, re
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


BR = 0.5

########################################################
## Uncomment this part if running the limit code

#masses = array('d')
#xs_obs_limits = array('d')
#xs_exp_limits = array('d')
#masses_exp = array('d')
#xs_exp_limits_1sigma = array('d')
#xs_exp_limits_1sigma_up = array('d')
#xs_exp_limits_2sigma = array('d')
#xs_exp_limits_2sigma_up = array('d')

#mass_start = 1000
#mass_step = 100
#steps = 30

#for i in range(0,steps+1):

  #mass = mass_start + i*mass_step

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(mass) + "_" + str(BR) + ".log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))


#for i in range(0,len(masses)):
  #masses_exp.append( masses[len(masses)-i-1] )
  #xs_exp_limits_1sigma.append( xs_exp_limits_1sigma_up[len(masses)-i-1] )
  #xs_exp_limits_2sigma.append( xs_exp_limits_2sigma_up[len(masses)-i-1] )


#print "masses:"
#print masses
#print "xs_obs_limits, BR=" + str(BR) + ":"
#print xs_obs_limits
#print "xs_exp_limits, BR=" + str(BR) + ":"
#print xs_exp_limits
#print ""
#print "masses_exp:"
#print masses_exp
#print "xs_exp_limits_1sigma, BR=" + str(BR) + ":"
#print xs_exp_limits_1sigma
#print "xs_exp_limits_2sigma, BR=" + str(BR) + ":"
#print xs_exp_limits_2sigma

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_obs_limits = array('d', [0.46658699999999997, 0.40856100000000001, 0.28187600000000002, 0.177116, 0.103135, 0.104287, 0.104063, 0.10274999999999999, 0.085851800000000006, 0.063292699999999993, 0.061415299999999999, 0.062413900000000001, 0.054793799999999997, 0.046073700000000002, 0.037667600000000002, 0.034601199999999999, 0.0331995, 0.029232899999999999, 0.0235397, 0.014885499999999999, 0.011170100000000001, 0.0074479500000000001, 0.0055871999999999996, 0.0046564400000000004, 0.0044237599999999997, 0.0039580800000000001, 0.0037252600000000002, 0.0034924399999999999, 0.0032596299999999999, 0.0030268000000000001, 0.0025611100000000001])
xs_exp_limits = array('d', [0.42156399999999999, 0.33208100000000002, 0.23203099999999999, 0.19318399999999999, 0.160552, 0.126439, 0.10785599999999999, 0.107725, 0.074402700000000002, 0.059597700000000003, 0.059600800000000002, 0.055134099999999998, 0.049190499999999998, 0.039183599999999999, 0.035520299999999998, 0.031896000000000001, 0.030481299999999999, 0.022860599999999998, 0.015834000000000001, 0.013037699999999999, 0.0112368, 0.0100894, 0.0083818199999999999, 0.0074504000000000003, 0.0064922399999999998, 0.0055877899999999996, 0.0047470000000000004, 0.0041909399999999998, 0.0037588399999999998, 0.0032596700000000001, 0.0027939900000000001])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.30360500000000001, 0.24724399999999999, 0.16339899999999999, 0.132054, 0.11117100000000001, 0.096428200000000006, 0.081459799999999999, 0.074323399999999998, 0.055760700000000003, 0.048361700000000001, 0.044545800000000003, 0.0446837, 0.033525800000000001, 0.027937099999999999, 0.026074900000000002, 0.024834999999999999, 0.022348199999999999, 0.016763500000000001, 0.011651, 0.0102437, 0.0083816199999999993, 0.0069847099999999999, 0.0060533699999999998, 0.00512226, 0.00465651, 0.0041907899999999998, 0.0034633099999999998, 0.0027939699999999998, 0.00256113, 0.0020954699999999999, 0.00186264,
0.00382563, 0.0043614200000000004, 0.0048178199999999996, 0.0058014900000000003, 0.0069176799999999998, 0.0076493400000000001, 0.0084005999999999994, 0.010034299999999999, 0.011285999999999999, 0.0139585, 0.0161957, 0.018250499999999999, 0.021538700000000001, 0.029632499999999999, 0.037203899999999998, 0.038848199999999999, 0.044799400000000003, 0.048311100000000003, 0.060039000000000002, 0.076200500000000004, 0.076092800000000002, 0.087623900000000005, 0.106599, 0.14230899999999999, 0.14569099999999999, 0.16842699999999999, 0.21723799999999999, 0.264982, 0.31956400000000001, 0.47763699999999998, 0.586171])
xs_exp_limits_2sigma = array('d', [0.21201700000000001, 0.17200199999999999, 0.115012, 0.097216300000000005, 0.0837421, 0.070888199999999998, 0.059240800000000003, 0.0591152, 0.044503099999999997, 0.039281799999999999, 0.031707699999999998, 0.0338556, 0.027928100000000001, 0.0223316, 0.0211357, 0.018577699999999999, 0.0167116, 0.013037699999999999, 0.0093122900000000008, 0.0074490399999999997, 0.00651865, 0.0055874699999999998, 0.0048985299999999999, 0.00395751, 0.0037249900000000001, 0.00325946, 0.00270659, 0.00209545, 0.0018626300000000001, 0.0017948300000000001, 0.0016298, 0.0046531999999999997, 0.0055488500000000001,
0.0060669499999999998, 0.0075694000000000004, 0.00873788, 0.0102527, 0.0112262, 0.0138012, 0.0151071, 0.016701000000000001, 0.019207800000000001, 0.023133000000000001, 0.029219700000000001, 0.038912299999999997, 0.043767899999999998, 0.046111800000000001, 0.0596895, 0.068026799999999998, 0.071904800000000005, 0.092659500000000006, 0.096853599999999998, 0.11117, 0.14842900000000001, 0.17880199999999999, 0.17796999999999999, 0.21421499999999999, 0.267818, 0.31577100000000002, 0.38822200000000001, 0.56334399999999996, 0.75281100000000001])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL Combined, RSG-like resonances")
graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,10)

graph_exp_1sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_1sigma)
graph_exp_1sigma.SetFillColor(kGreen+1)

graph_exp = TGraph(len(masses),masses,xs_exp_limits)
#graph_exp.SetMarkerStyle(24)
graph_exp.SetLineWidth(2)
graph_exp.SetLineStyle(2)
graph_exp.SetLineColor(4)

graph_obs = TGraph(len(masses),masses,xs_obs_limits)
graph_obs.SetMarkerStyle(20)
graph_obs.SetLineWidth(2)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")

legend = TLegend(.50,.67,.80,.80)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits')
legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.88, "RS-graviton-like, f_{b#bar{b}}=" + str(BR))
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.43, "CMS Preliminary")
l1.DrawLatex(0.19,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.20,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.19,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.19,0.20, "Wide Jets")
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.50, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.05)
l1.DrawLatex(0.52,0.20, "0, 1 and 2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obsexp_sys_WideJets_RSG.eps')

