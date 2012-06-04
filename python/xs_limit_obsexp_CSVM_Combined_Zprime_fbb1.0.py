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


BR = 1.0

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
xs_obs_limits = array('d', [0.18573200000000001, 0.18609400000000001, 0.125028, 0.099885299999999996, 0.055879400000000003, 0.052154100000000002, 0.055879400000000003, 0.052156099999999997, 0.042840799999999998, 0.0353903, 0.041303199999999998, 0.040616300000000001, 0.034727599999999997, 0.0294781, 0.0278915, 0.029205399999999999, 0.026135499999999999, 0.019807499999999999, 0.014190299999999999, 0.0107102, 0.0074506299999999998, 0.0060536000000000001, 0.0046566200000000002, 0.0044237900000000004, 0.0045030000000000001, 0.0042498800000000002, 0.0037592400000000001, 0.0035701499999999998, 0.0031558900000000002, 0.00282256, 0.0025611399999999999])
xs_exp_limits = array('d', [0.164411, 0.139958, 0.122562, 0.099496399999999999, 0.083797300000000005, 0.070780800000000005, 0.059604699999999997, 0.052155899999999998, 0.044704399999999998, 0.045080799999999997, 0.042712600000000003, 0.0390176, 0.033817699999999999, 0.0281175, 0.0265045, 0.023905699999999998, 0.021625999999999999, 0.017090999999999999, 0.0125729, 0.0107102, 0.0088479300000000004, 0.0074508200000000004, 0.0065547599999999998, 0.0060536000000000001, 0.0052387099999999997, 0.0050058699999999999, 0.0041909499999999997, 0.0036661200000000001, 0.0032596299999999999, 0.0028115000000000002, 0.0023283100000000001])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.14901200000000001, 0.119209, 0.104308, 0.0856817, 0.067055199999999995, 0.059604600000000001, 0.048429300000000002, 0.0447035, 0.037252899999999999, 0.037252899999999999, 0.0353903, 0.029319899999999999, 0.026077099999999999, 0.022351699999999999, 0.020099800000000001, 0.0193428, 0.015832499999999999, 0.0139703, 0.0102445, 0.0083819700000000007, 0.0065192599999999998, 0.0060536000000000001, 0.0055879399999999996, 0.0046566200000000002, 0.0041909499999999997, 0.0034924600000000002, 0.0032596299999999999, 0.0027939699999999998, 0.0025611599999999998, 0.0020954799999999998, 0.00186265, 0.0034456299999999999, 0.0038072700000000002, 0.0043444499999999997, 0.0048426900000000002, 0.0056353000000000002, 0.0066029799999999996, 0.0067053900000000003, 0.0078052299999999998, 0.0088419899999999992, 0.010060100000000001, 0.011926900000000001, 0.0137328, 0.016190699999999999, 0.020381400000000001, 0.027892900000000002, 0.030673800000000001, 0.031119299999999999, 0.036484099999999998, 0.044333400000000002, 0.048880399999999997, 0.051075799999999998, 0.057732699999999998, 0.062740699999999996, 0.067017199999999999, 0.076666300000000007, 0.084860500000000005, 0.099848999999999993, 0.114796, 0.14094100000000001, 0.16691500000000001, 0.18243300000000001])
xs_exp_limits_2sigma = array('d', [0.13411000000000001, 0.10474, 0.089996199999999998, 0.071074799999999994, 0.059604600000000001, 0.052154100000000002, 0.0447035, 0.033665500000000001, 0.030096600000000001, 0.030096600000000001, 0.027939700000000001, 0.022351699999999999, 0.022351699999999999, 0.016910999999999999, 0.0149012, 0.0149552, 0.0121072, 0.011229899999999999, 0.0075046899999999996, 0.0065192599999999998, 0.00515906, 0.0042277399999999998, 0.0041909599999999997, 0.00372529, 0.00327802, 0.0027939699999999998, 0.00257953, 0.00187615, 0.0020954799999999998, 0.00163843, 0.0014055999999999999, 0.0048298400000000002, 0.0053027100000000004, 0.0062010299999999997, 0.0059574900000000002, 0.0077630199999999998, 0.0082299499999999998, 0.0086511299999999999, 0.0097071399999999995, 0.0110227, 0.012223400000000001, 0.014549299999999999, 0.0177416, 0.019083699999999999, 0.0269433, 0.033594199999999998, 0.0389783, 0.038247400000000001, 0.040219199999999997, 0.053578500000000001, 0.061155000000000001, 0.059693900000000001, 0.070113300000000003, 0.078218999999999997, 0.0954372, 0.098543400000000003, 0.105741, 0.12247, 0.126974, 0.168126, 0.186088, 0.201484])

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
l1.DrawLatex(0.50,0.80, "0, 1 and 2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVM_Combined_limit_obsexp_WideJets_Zprime_fbb1.0.eps')

