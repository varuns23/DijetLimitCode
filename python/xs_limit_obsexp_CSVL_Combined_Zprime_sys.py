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

  #log_file = open("stats_" + str(mass) + "_" + str(BR) + "_qq.log",'r')
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
xs_obs_limits = array('d', [0.43425900000000001, 0.35674800000000001, 0.23109099999999999, 0.14901200000000001, 0.104308, 0.096857499999999999, 0.093137700000000004, 0.082283899999999993, 0.063329899999999995, 0.057742000000000002, 0.059702199999999997, 0.057138099999999997, 0.048718999999999998, 0.036229200000000003, 0.031712499999999998, 0.0307668, 0.028506099999999999, 0.0246584, 0.018626500000000001, 0.011175900000000001, 0.00745058, 0.0055879399999999996, 0.0041909499999999997, 0.00372529, 0.00372529, 0.0034924600000000002, 0.0032596299999999999, 0.0030268000000000001, 0.0027939699999999998, 0.0023283100000000001, 0.0020954799999999998])
xs_exp_limits = array('d', [0.36749199999999999, 0.28781899999999999, 0.208616, 0.17136299999999999, 0.13954, 0.111761, 0.096857700000000005, 0.081957000000000002, 0.063329999999999997, 0.052185299999999997, 0.059220799999999997, 0.050886300000000002, 0.039568300000000001, 0.031664999999999999, 0.031030599999999998, 0.029640900000000001, 0.0251842, 0.017297199999999999, 0.0125729, 0.010483599999999999, 0.0093151499999999995, 0.0079163900000000006, 0.0069849600000000001, 0.0060536000000000001, 0.00512503, 0.00444196, 0.0037805600000000001, 0.00335308, 0.00304945, 0.0027358199999999999, 0.0023283100000000001])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.26822099999999999, 0.208617, 0.154943, 0.119209, 0.104308, 0.081956399999999999, 0.067055199999999995, 0.059604600000000001, 0.048428800000000001, 0.040978199999999999, 0.044135399999999998, 0.037252899999999999, 0.0298023, 0.024214400000000001, 0.023104300000000001, 0.021630099999999999, 0.0187254, 0.0130385, 0.0093132400000000004, 0.0083818999999999994, 0.0065192699999999998, 0.0055879500000000004, 0.0046566200000000002, 0.0041909499999999997, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.0023283100000000001, 0.0019075800000000001, 0.00186265, 0.0016522900000000001, 0.0032637, 0.0035406399999999998, 0.00409583, 0.0046639100000000003, 0.0055588, 0.0062348400000000002, 0.0069918699999999999, 0.0081657699999999993, 0.0092332300000000003, 0.011207099999999999, 0.013322799999999999, 0.015317900000000001, 0.017556200000000001, 0.024411800000000001, 0.032485600000000003, 0.035822600000000003, 0.038542199999999999, 0.040666800000000003, 0.056011199999999997, 0.069741899999999996, 0.077308199999999994, 0.076788300000000004, 0.091483900000000007, 0.106695, 0.13001199999999999, 0.152558, 0.194856, 0.242006, 0.30641800000000002, 0.39033800000000002, 0.499751])
xs_exp_limits_2sigma = array('d', [0.208616, 0.178814, 0.104308, 0.089407, 0.074505799999999997, 0.067055199999999995, 0.052154100000000002, 0.0447035, 0.040978199999999999, 0.033527599999999998, 0.033909500000000002, 0.029548999999999999, 0.0201724, 0.019203899999999999, 0.017695200000000001, 0.0149012, 0.0149012, 0.010513700000000001, 0.00745058, 0.0065192599999999998, 0.0055879399999999996, 0.0046566100000000003, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.0024542700000000001, 0.00186265, 0.00186265, 0.00162981, 0.00162981, 0.0013969799999999999, 0.0038684000000000001, 0.0042560799999999998, 0.00503098, 0.0056481999999999999, 0.0074469200000000001, 0.0080233100000000005, 0.0088689200000000006, 0.010558100000000001, 0.0119579, 0.0142008, 0.015791900000000001, 0.018455099999999999, 0.021842500000000001, 0.0301172, 0.037928000000000003, 0.0422926, 0.045876599999999997, 0.0500834, 0.071086099999999999, 0.077874600000000002, 0.10172299999999999, 0.098929400000000001, 0.11117299999999999, 0.15623000000000001, 0.17224100000000001, 0.191464, 0.24793899999999999, 0.30102800000000002, 0.350188, 0.481993, 0.59644200000000003])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,10)
graph_exp_2sigma.GetXaxis().SetNdivisions(1005)

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

legend = TLegend(.50,.63,.80,.76)
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
l1.DrawLatex(0.18,0.89, "Z'-like, f_{b#bar{b}}=" + str(BR))
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.055)
l1.DrawLatex(0.50,0.80, "0, 1 and 2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obsexp_sys_WideJets_Zprime.eps')

