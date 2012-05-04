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
xs_obs_limits = array('d', [0.48680699999999999, 0.46468399999999999, 0.28148099999999998, 0.17741499999999999, 0.133739, 0.1181, 0.13380500000000001, 0.15837200000000001, 0.15114, 0.136603, 0.118712, 0.101815, 0.086243899999999998, 0.076554700000000003, 0.075268100000000004, 0.071285200000000007, 0.058854400000000001, 0.046178400000000001, 0.035378300000000001, 0.026064, 0.020473700000000001, 0.016751599999999998, 0.016759799999999998, 0.0167577, 0.0186255, 0.018454999999999999, 0.0171135, 0.014896899999999999, 0.014897199999999999, 0.014899300000000001, 0.0139664])
xs_exp_limits = array('d', [0.40685199999999999, 0.36591200000000002, 0.28091899999999997, 0.23013800000000001, 0.193352, 0.16369600000000001, 0.14499100000000001, 0.13628000000000001, 0.125916, 0.117206, 0.110141, 0.091465199999999997, 0.085401199999999997, 0.069506499999999999, 0.065265900000000002, 0.063668600000000006, 0.054166499999999999, 0.042029799999999999, 0.034592299999999999, 0.029800900000000002, 0.027938299999999999, 0.0260746, 0.024639399999999999, 0.024208199999999999, 0.022345299999999998, 0.021510600000000001, 0.019092100000000001, 0.018619199999999999, 0.017758699999999999, 0.016756900000000002, 0.0152032])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.34038800000000002, 0.304012, 0.20030100000000001, 0.178809, 0.147033, 0.13323699999999999, 0.111206, 0.111342, 0.096567500000000001, 0.096738900000000003, 0.089187299999999997, 0.070771700000000007, 0.0595445, 0.054863799999999997, 0.048422800000000002, 0.0513727, 0.040946999999999997, 0.0325499, 0.0260734, 0.023718400000000001, 0.0223374, 0.0211755, 0.018620000000000001, 0.0167601, 0.016754999999999999, 0.0148968, 0.0148915, 0.013032800000000001, 0.0130323, 0.013029199999999999, 0.013029000000000001, 0.0212152, 0.022072899999999999, 0.0226307, 0.023536100000000001,
0.025548100000000001, 0.0271075, 0.027506200000000001, 0.0298251, 0.033247699999999998, 0.035426699999999998, 0.040064500000000003, 0.042540000000000001, 0.045211899999999999, 0.0578018, 0.064932000000000004, 0.084402699999999997, 0.085548799999999994, 0.091238299999999994, 0.107543, 0.121472, 0.144314, 0.161499, 0.160354, 0.18057300000000001, 0.177787, 0.21252399999999999, 0.24005000000000001, 0.27925499999999998, 0.335951, 0.40742200000000001, 0.46204600000000001])
xs_exp_limits_2sigma = array('d', [0.23213800000000001, 0.23081299999999999, 0.15870500000000001, 0.13064799999999999, 0.117441, 0.10356600000000001, 0.088558799999999993, 0.088395500000000002, 0.067414100000000005, 0.074277399999999993, 0.067210800000000001, 0.055821099999999998, 0.041157800000000001, 0.040926999999999998, 0.040933999999999998, 0.0355105, 0.0300646, 0.022326800000000001, 0.0204703, 0.018766100000000001, 0.015037, 0.0148933, 0.0148874, 0.0130294, 0.0113166, 0.0130321, 0.0113192, 0.011169, 0.011169200000000001, 0.0111687, 0.0111682, 0.0261383, 0.025981899999999999, 0.026982300000000001,
0.028894099999999999, 0.031811899999999997, 0.034854999999999997, 0.033975699999999998, 0.0350882, 0.040867399999999998, 0.044442000000000002, 0.0504048, 0.0548692, 0.061441500000000003, 0.081232299999999993, 0.090263200000000002, 0.105591, 0.110276, 0.13231699999999999, 0.136713, 0.158827, 0.19179199999999999, 0.245641, 0.23117099999999999, 0.23638799999999999, 0.248251, 0.29239700000000002, 0.28828300000000001, 0.318718, 0.38752300000000001, 0.46166800000000002, 0.51652600000000004])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL 2-tag, RSG-like resonances")
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
legend.SetHeader('95% CL Upper Limits (stat. only)')
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
l1.DrawLatex(0.75,0.20, "2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_2Tag_limit_obsexp_WideJets_RSG.eps')

