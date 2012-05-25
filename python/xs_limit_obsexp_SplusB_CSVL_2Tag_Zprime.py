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
xs_obs_limits = array('d', [1.27722, 1.39391, 0.28312199999999998, 0.163913, 0.11921, 0.11921, 0.13411500000000001, 0.219972, 0.20991199999999999, 0.18296200000000001, 0.147429, 0.11325499999999999, 0.0943277, 0.084335300000000002, 0.092457300000000006, 0.087238099999999999, 0.066012799999999996, 0.044591199999999998, 0.033529200000000002, 0.026076999999999999, 0.0204891, 0.016763799999999999, 0.0149012, 0.016763799999999999, 0.018681199999999999, 0.018048100000000001, 0.017250000000000001, 0.0149012, 0.0149012, 0.0149012, 0.0130385])
xs_exp_limits = array('d', [0.83538800000000002, 0.659188, 0.28312500000000002, 0.23644399999999999, 0.19376399999999999, 0.185253, 0.14903, 0.20502400000000001, 0.20493500000000001, 0.17777299999999999, 0.14631, 0.114636, 0.098352300000000004, 0.079840599999999998, 0.088084200000000001, 0.087249599999999997, 0.069773299999999996, 0.043037600000000002, 0.035075299999999997, 0.031312899999999998, 0.027939700000000001, 0.026076999999999999, 0.0242145, 0.024214400000000001, 0.022351800000000002, 0.020489400000000001, 0.018626500000000001, 0.017695499999999999, 0.016763799999999999, 0.0149012, 0.0149012])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.53773700000000002, 0.44129400000000002, 0.238422, 0.193715, 0.163913, 0.14156099999999999, 0.119211, 0.12915299999999999, 0.13664000000000001, 0.115026, 0.089407, 0.0745059, 0.063329999999999997, 0.051952900000000003, 0.064431799999999997, 0.054994800000000003, 0.042841200000000003, 0.032562800000000003, 0.027939700000000001, 0.026076999999999999, 0.023732, 0.022351699999999999, 0.020417600000000001, 0.018626500000000001, 0.016763799999999999, 0.0149012, 0.0149012, 0.0146599, 0.0130385, 0.0130385, 0.0130385, 0.0218421, 0.022858699999999999, 0.023506200000000001, 0.0242864, 0.025755299999999998, 0.0278734, 0.028389299999999999, 0.031072099999999998, 0.0367899, 0.040097800000000003, 0.043008299999999999, 0.047561199999999998, 0.057033100000000003, 0.065794199999999997, 0.091599, 0.122414, 0.122146, 0.126556, 0.15195800000000001, 0.174207, 0.20977999999999999, 0.26619100000000001, 0.281443, 0.27913100000000002, 0.217225, 0.29430000000000001, 0.32191199999999998, 0.45157799999999998, 0.54077600000000003, 0.93727000000000005, 1.17683])
xs_exp_limits_2sigma = array('d', [0.41723300000000002, 0.336588, 0.20916899999999999, 0.163913, 0.13411100000000001, 0.112347, 0.104308, 0.104309, 0.104115, 0.096507599999999999, 0.074505799999999997, 0.059604600000000001, 0.055879400000000003, 0.044606600000000003, 0.044763699999999997, 0.0443536, 0.033587199999999998, 0.027939700000000001, 0.0204891, 0.018773600000000001, 0.018626500000000001, 0.016910999999999999, 0.0149012, 0.0149012, 0.0130385, 0.0130385, 0.011323, 0.011175900000000001, 0.011175900000000001, 0.011175900000000001, 0.011175900000000001, 0.027691199999999999, 0.028465299999999999, 0.031180699999999999, 0.034057999999999998, 0.035233500000000001, 0.038346199999999997, 0.040480299999999997, 0.041495499999999998, 0.044687299999999999, 0.0530295, 0.062317999999999998, 0.068224499999999993, 0.074749999999999997, 0.090449500000000002, 0.119808, 0.143846, 0.14627000000000001, 0.14247099999999999, 0.18706800000000001, 0.22228500000000001, 0.26061800000000002, 0.298149, 0.33486700000000003, 0.369056, 0.29624400000000001, 0.396428, 0.49252499999999999, 0.61149900000000001, 0.78234599999999999, 0.97895600000000005, 1.25299])

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
l1.DrawLatex(0.50,0.80, "2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_2Tag_limit_obsexp_SplusB_WideJets_Zprime.eps')

