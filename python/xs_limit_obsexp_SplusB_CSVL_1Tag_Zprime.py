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

#mass_start = 1000.
#mass_step = 100.
#steps = 30

#for i in range(0,steps+1):

  #mass = mass_start + float(i)*mass_step

  #masses.append(mass)
  #masses_exp.append(mass)

  #cmd = "./stats " + str(mass) + " " + str(BR) + " qq"
  #print "Running: " + cmd
  #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  #output = proc.communicate()[0]
  #if proc.returncode != 0:
    #print output
    #sys.exit(1)
  ##print output
  #outputlines = output.split("\n")

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
xs_obs_limits = array('d', [0.71525799999999995, 0.58307100000000001, 0.83747300000000002, 0.38535900000000001, 0.193715, 0.178814, 0.19483800000000001, 0.14205300000000001, 0.10058300000000001, 0.081956399999999999, 0.070780599999999999, 0.061495500000000002, 0.048428800000000001, 0.042840900000000001, 0.035390400000000002, 0.038317200000000003, 0.0332772, 0.025645299999999999, 0.020438899999999999, 0.017894299999999998, 0.018603100000000001, 0.0168097, 0.013531100000000001, 0.010685500000000001, 0.0089268100000000003, 0.0072954700000000001, 0.0060536000000000001, 0.0046566100000000003, 0.00372529, 0.0032596299999999999, 0.0027939699999999998])
xs_exp_limits = array('d', [0.74514599999999998, 0.57663200000000003, 0.65732500000000005, 0.35686699999999999, 0.25753999999999999, 0.20117699999999999, 0.189058, 0.138154, 0.11031100000000001, 0.091448500000000002, 0.070781999999999998, 0.063112600000000005, 0.0447047, 0.040979000000000002, 0.035390499999999998, 0.037956799999999999, 0.034573399999999997, 0.024963599999999999, 0.019978300000000001, 0.017951399999999999, 0.016450099999999999, 0.016363900000000001, 0.0135735, 0.010546399999999999, 0.0090008099999999997, 0.0070044299999999999, 0.0060536000000000001, 0.0051223600000000003, 0.00465666, 0.0044657500000000001, 0.0041909800000000004])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.68546499999999999, 0.47683799999999998, 0.402418, 0.28312199999999998, 0.193715, 0.163913, 0.13411000000000001, 0.104308, 0.081956399999999999, 0.070780499999999996, 0.055879499999999999, 0.048428800000000001, 0.037253000000000001, 0.029802700000000001, 0.0279399, 0.026077800000000002, 0.0223521, 0.018626500000000001, 0.015591300000000001, 0.013969799999999999, 0.0130385, 0.0102445, 0.0088475600000000008, 0.0074506299999999998, 0.0065192799999999997, 0.0055879399999999996, 0.0046566100000000003, 0.00372529, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.0055951100000000004, 0.0059719600000000001, 0.0065233499999999998, 0.0071715900000000003, 0.0076134899999999997, 0.010047199999999999, 0.012468999999999999, 0.0156201, 0.0191016, 0.025246000000000001, 0.027310299999999999, 0.027026600000000001, 0.032875399999999999, 0.0362484, 0.0498223, 0.0579859, 0.055315599999999999, 0.059018599999999997, 0.071974399999999994, 0.093785900000000005, 0.113639, 0.16811000000000001, 0.177485, 0.24948500000000001, 0.33255000000000001, 0.34682299999999999, 0.44855400000000001, 0.59672599999999998, 1.0158700000000001, 1.10236, 1.36755])
xs_exp_limits_2sigma = array('d', [0.59604699999999999, 0.41723300000000002, 0.32782699999999998, 0.25331999999999999, 0.16508999999999999, 0.13469900000000001, 0.104308, 0.089995599999999995, 0.067055199999999995, 0.055879400000000003, 0.041272499999999997, 0.037547200000000003, 0.0298023, 0.022645999999999999, 0.022351699999999999, 0.022351800000000002, 0.018626500000000001, 0.0149012, 0.0130385, 0.011175900000000001, 0.011175900000000001, 0.0083818999999999994, 0.0069849200000000004, 0.0056615399999999996, 0.0055879399999999996, 0.0042277399999999998, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.00257953, 0.0025611399999999999, 0.0071533400000000002, 0.0079665299999999994, 0.010048700000000001, 0.012175200000000001, 0.0140605, 0.0140921, 0.018678899999999998, 0.020771700000000001, 0.027130600000000001, 0.033177400000000003, 0.036298400000000001, 0.039887600000000002, 0.045834100000000003, 0.047429699999999998, 0.061376, 0.080289399999999997, 0.073464699999999994, 0.094441999999999998, 0.10711, 0.12396, 0.15148600000000001, 0.208645, 0.25970300000000002, 0.34600399999999998, 0.43632700000000002, 0.48017900000000002, 0.61760099999999996, 0.83598799999999995, 1.1950400000000001, 1.4154599999999999, 2.0695399999999999])

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
legend.SetHeader('95% CL Upper Limits (stat. only)')
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
l1.DrawLatex(0.50,0.80, "1 b-tag")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obsexp_SplusB_WideJets_Zprime.eps')

