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
xs_obs_limits = array('d', [0.71525799999999995, 0.54888099999999995, 0.47423999999999999, 0.34092699999999998, 0.193715, 0.178814, 0.18093100000000001, 0.13927999999999999, 0.10058300000000001, 0.081956399999999999, 0.070780499999999996, 0.060666499999999998, 0.048428800000000001, 0.042840900000000001, 0.037253099999999997, 0.035349400000000003, 0.0302072, 0.024635199999999999, 0.020204400000000001, 0.017368499999999999, 0.016094899999999999, 0.014931699999999999, 0.012670300000000001, 0.010504599999999999, 0.0088163300000000007, 0.0072706699999999999, 0.0060536000000000001, 0.0046566100000000003, 0.00372529, 0.0032596299999999999, 0.0027939699999999998])
xs_exp_limits = array('d', [0.74512, 0.53644199999999997, 0.423985, 0.32089899999999999, 0.23841899999999999, 0.193716, 0.16794000000000001, 0.12826299999999999, 0.10058300000000001, 0.085681800000000002, 0.070780599999999999, 0.055879400000000003, 0.0465666, 0.043313600000000001, 0.0353903, 0.033949199999999999, 0.029020199999999999, 0.023946499999999999, 0.018627700000000001, 0.016269599999999999, 0.015525499999999999, 0.013855599999999999, 0.011652300000000001, 0.0098685200000000004, 0.0087963599999999996, 0.0065192799999999997, 0.0058873199999999997, 0.0051223600000000003, 0.0046566999999999997, 0.0044348399999999998, 0.0041909800000000004])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.59604699999999999, 0.44703700000000002, 0.357628, 0.25331999999999999, 0.193715, 0.14901200000000001, 0.12472999999999999, 0.104308, 0.074506699999999995, 0.059605100000000001, 0.052154100000000002, 0.048428800000000001, 0.037253000000000001, 0.0298023, 0.0274573, 0.026076999999999999, 0.022351800000000002, 0.017695099999999998, 0.014659999999999999, 0.0121072, 0.0121072, 0.011175900000000001, 0.0088475600000000008, 0.0073299999999999997, 0.0065192599999999998, 0.0055879399999999996, 0.00453601, 0.00372529, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.0054727600000000001, 0.0058552999999999999, 0.0062888700000000002, 0.0067905400000000003, 0.0074453399999999999, 0.0089593799999999994, 0.0116174, 0.012961200000000001, 0.0151021, 0.017926899999999999, 0.020499799999999999, 0.021534999999999999, 0.025694600000000001, 0.030511, 0.038277800000000001, 0.045149599999999998, 0.046906200000000002, 0.055165499999999999, 0.062667200000000006, 0.075429700000000002, 0.092911300000000002, 0.11321299999999999, 0.12751299999999999, 0.16200500000000001, 0.20658000000000001, 0.24756600000000001, 0.310894, 0.41014299999999998, 0.493757, 0.59870699999999999, 0.83298700000000003])
xs_exp_limits_2sigma = array('d', [0.47683700000000001, 0.357628, 0.229403, 0.208616, 0.14901200000000001, 0.119209, 0.090584999999999999, 0.0825457, 0.067055199999999995, 0.045292100000000002, 0.040978199999999999, 0.037547200000000003, 0.028086900000000001, 0.022351699999999999, 0.018773600000000001, 0.0206362, 0.016763799999999999, 0.014043399999999999, 0.011175900000000001, 0.0093868000000000007, 0.0102445, 0.0083819099999999994, 0.0069849200000000004, 0.0055879399999999996, 0.0051222699999999999, 0.0041909499999999997, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.00257953, 0.0025611399999999999, 0.0064840200000000001, 0.0073003699999999996, 0.0090584399999999992, 0.010518100000000001, 0.0115695, 0.0114117, 0.014115300000000001, 0.0157156, 0.0195532, 0.024722299999999999, 0.028270799999999999, 0.0278009, 0.031013099999999998, 0.0387879, 0.0464322, 0.058037999999999999, 0.056834099999999999, 0.072726600000000002, 0.084208099999999994, 0.10076599999999999, 0.110527, 0.139015, 0.15359500000000001, 0.20587800000000001, 0.241201, 0.288854, 0.36458200000000002, 0.47001199999999999, 0.59150999999999998, 0.70199400000000001, 0.94653100000000001])

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
c.SaveAs('CSVL_1Tag_limit_obsexp_WideJets_Zprime.eps')

