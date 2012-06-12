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
xs_obs_limits = array('d', [1.1756500000000001, 0.86084899999999998, 0.263907, 0.155894, 0.10377500000000001, 0.099532300000000004, 0.095978599999999997, 0.086569999999999994, 0.067128099999999996, 0.058552699999999999, 0.076283799999999999, 0.076775300000000005, 0.059325799999999998, 0.042446299999999999, 0.038846899999999997, 0.041987999999999998, 0.038195699999999999, 0.032306700000000001, 0.018825100000000001, 0.0128694, 0.0085677400000000008, 0.0061665399999999999, 0.0045899699999999996, 0.0039427000000000004, 0.0037603900000000002, 0.0035897799999999999, 0.0033545900000000002, 0.0032012899999999999, 0.0028911200000000001, 0.0025480199999999998, 0.0022226799999999999])
xs_exp_limits = array('d', [0.39151999999999998, 0.30326999999999998, 0.23120099999999999, 0.191969, 0.15026900000000001, 0.12573400000000001, 0.106708, 0.088930200000000001, 0.075606000000000007, 0.062084100000000003, 0.053101700000000002, 0.042151599999999997, 0.034970000000000001, 0.031502700000000002, 0.026382300000000001, 0.021570300000000001, 0.018985399999999999, 0.015077699999999999, 0.0131942, 0.0119113, 0.010478599999999999, 0.0089991299999999993, 0.0075281799999999998, 0.0067094600000000004, 0.0056430999999999999, 0.0047356100000000003, 0.0042589699999999999, 0.0036872900000000002, 0.0032122700000000001, 0.0027954199999999998, 0.0023793299999999998])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.37743900000000002, 0.259432, 0.206067, 0.15629599999999999, 0.127108, 0.10401100000000001, 0.090700500000000003, 0.070299100000000003, 0.059106699999999998, 0.050224999999999999, 0.042338099999999997, 0.033384799999999999, 0.027458099999999999, 0.0252403, 0.020413799999999999, 0.0174383, 0.0141823, 0.012154, 0.0109275, 0.0090982800000000003, 0.0082999900000000001, 0.0070864300000000003, 0.0060666699999999997, 0.0049714800000000003, 0.0043382100000000003, 0.0036070199999999998, 0.0032238800000000001, 0.0027659099999999999, 0.00232979, 0.00202214, 0.00181843, 0.0033388900000000002, 0.0036516999999999999, 0.0041699199999999997, 0.0049027200000000002, 0.0058812400000000003, 0.00691283, 0.0082862300000000003, 0.0088801599999999998, 0.010774000000000001, 0.012534200000000001, 0.014095699999999999, 0.015656300000000001, 0.018156499999999999, 0.021229100000000001, 0.026627999999999999, 0.028591499999999999, 0.035426699999999998, 0.044062900000000002, 0.052093, 0.056725900000000003, 0.081067399999999998, 0.082919400000000004, 0.11351700000000001, 0.13253999999999999, 0.158557, 0.190971, 0.23962700000000001, 0.283331, 0.35977700000000001, 0.54832199999999998, 0.66052])
xs_exp_limits_2sigma = array('d', [0.35229100000000002, 0.238597, 0.19611000000000001, 0.13624800000000001, 0.104005, 0.089121300000000001, 0.071814299999999998, 0.058660200000000003, 0.0513331, 0.041055300000000003, 0.032969199999999997, 0.027876399999999999, 0.023303299999999999, 0.021287899999999998, 0.0161473, 0.014857, 0.01242, 0.010025299999999999, 0.0094231999999999996, 0.0073391200000000002, 0.0065163299999999999, 0.0052061800000000004, 0.0045589300000000001, 0.0039854199999999999, 0.0035635300000000001, 0.0028702699999999999, 0.0023185100000000002, 0.0019648399999999998, 0.00180152, 0.00176373, 0.0015090500000000001, 0.0046380099999999997, 0.0051213500000000002, 0.0056208400000000002, 0.0066840299999999997, 0.0075826599999999997, 0.0083711199999999993, 0.0104308, 0.012133, 0.0139831, 0.0154164, 0.0176036, 0.020348399999999999, 0.024518999999999999, 0.0289657, 0.034263799999999997, 0.041124800000000003, 0.048088899999999997, 0.054673399999999997, 0.070569800000000002, 0.075717400000000004, 0.109079, 0.113202, 0.14751400000000001, 0.177732, 0.20059299999999999, 0.25151499999999999, 0.32425199999999998, 0.396758, 0.52501600000000004, 0.75024000000000002, 1.1584700000000001])

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
l1.DrawLatex(0.18,0.89, "qq/bb, f_{b#bar{b}}=" + str(BR))
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
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_sys_WideJets_Zprime.eps')

