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

  #cmd = "./stats " + str(mass) + " " + str(BR) + " gg"
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
xs_obs_limits = array('d', [1.71994, 1.01414, 0.774891, 0.50664399999999998, 0.402333, 0.40880100000000003, 0.28795100000000001, 0.193715, 0.13411000000000001, 0.104308, 0.120215, 0.140455, 0.115603, 0.083893400000000007, 0.067978700000000003, 0.063585500000000003, 0.055571500000000003, 0.042447600000000002, 0.031569199999999999, 0.022351800000000002, 0.0149012, 0.011175900000000001, 0.00745058, 0.0065192599999999998, 0.0069849200000000004, 0.0069849200000000004, 0.0065192599999999998, 0.00714798, 0.0067152699999999997, 0.00665052, 0.0061487099999999999])
xs_exp_limits = array('d', [1.49013, 0.95368299999999995, 0.71526999999999996, 0.56625800000000004, 0.41723300000000002, 0.371618, 0.27065099999999997, 0.208616, 0.18024100000000001, 0.14156099999999999, 0.111759, 0.110586, 0.098202999999999999, 0.076587199999999994, 0.064117900000000005, 0.057197600000000001, 0.050773400000000003, 0.037861499999999999, 0.0297831, 0.0242163, 0.0219413, 0.0177749, 0.0149014, 0.013009400000000001, 0.011265600000000001, 0.0097796500000000008, 0.0084128399999999996, 0.0074150800000000001, 0.0073746599999999999, 0.0065868100000000002, 0.0065193899999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [1.3112999999999999, 0.77485999999999999, 0.53644199999999997, 0.41723300000000002, 0.32782699999999998, 0.29416599999999998, 0.208618, 0.163913, 0.13025100000000001, 0.104308, 0.089407200000000006, 0.092167700000000005, 0.074505799999999997, 0.055879400000000003, 0.048428800000000001, 0.040978199999999999, 0.038633099999999997, 0.0298024, 0.024214400000000001, 0.018385200000000001, 0.0149012, 0.013969799999999999, 0.0121072, 0.0102445, 0.0083818999999999994, 0.0069849200000000004, 0.0065192599999999998, 0.0055879399999999996, 0.0051222699999999999, 0.0055422600000000002, 0.0041909499999999997, 0.0088176999999999995, 0.0087935800000000005, 0.0097908800000000001, 0.010156999999999999, 0.011257400000000001, 0.0125217, 0.015055499999999999, 0.016829199999999999, 0.020385899999999998, 0.023624300000000001, 0.0267744, 0.030246100000000001, 0.037314800000000002, 0.050124099999999998, 0.062839000000000006, 0.072008299999999997, 0.079927700000000004, 0.10152, 0.12903999999999999, 0.149724, 0.15656900000000001, 0.17771600000000001, 0.23267399999999999, 0.28809800000000002, 0.32682699999999998, 0.46152799999999999, 0.50795500000000005, 0.66753899999999999, 0.84659799999999996, 1.1124700000000001, 1.6406000000000001])
xs_exp_limits_2sigma = array('d', [0.95367400000000002, 0.59604599999999996, 0.41723300000000002, 0.29802299999999998, 0.24077399999999999, 0.23841899999999999, 0.163913, 0.12038699999999999, 0.090584499999999998, 0.082545400000000005, 0.067055400000000001, 0.060781799999999997, 0.052154100000000002, 0.048428800000000001, 0.040978199999999999, 0.030096600000000001, 0.031664999999999999, 0.024361500000000001, 0.018626500000000001, 0.0149012, 0.011323, 0.00860263, 0.0084554799999999996, 0.0083818999999999994, 0.0065560499999999999, 0.0056615099999999998, 0.0055879399999999996, 0.0041909499999999997, 0.0041909499999999997, 0.0037620800000000001, 0.00329642, 0.0118067, 0.0125199, 0.0127432, 0.012379899999999999, 0.014271499999999999, 0.0168139, 0.019732, 0.0214145, 0.0250668, 0.030010700000000001, 0.035181299999999999, 0.043318000000000002, 0.0474037, 0.0600604, 0.083859600000000006, 0.086202799999999996, 0.094542200000000007, 0.124768, 0.16927900000000001, 0.19112000000000001, 0.19189100000000001, 0.21273900000000001, 0.297734, 0.351798, 0.43595800000000001, 0.62752699999999995, 0.57497200000000004, 0.79187200000000002, 0.93597600000000003, 1.27433, 1.7465900000000001])

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
l1.DrawLatex(0.18,0.89, "RS-graviton-like, f_{b#bar{b}}=" + str(BR))
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.055)
l1.DrawLatex(0.50,0.80, "0 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obsexp_WideJets_RSG.eps')

