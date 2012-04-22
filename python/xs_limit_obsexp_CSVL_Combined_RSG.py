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

  #cmd = "./stats " + str(mass) + " " + " " + str(BR)
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
xs_obs_limits = array('d', [0.432533, 0.38002399999999997, 0.23693, 0.14812900000000001, 0.095907300000000001, 0.096360699999999994, 0.104253, 0.101704, 0.075647199999999998, 0.055842999999999997, 0.057180000000000002, 0.062090199999999998, 0.0492615, 0.038636999999999998, 0.034674299999999998, 0.034761300000000002, 0.031689700000000001, 0.023953599999999999, 0.016654599999999999, 0.012107100000000001, 0.0088473100000000006, 0.0065191199999999998, 0.00512226, 0.0041908700000000002, 0.0041909, 0.0041909399999999998, 0.0037252700000000001, 0.0032596499999999998, 0.0030268299999999999, 0.0027939599999999998, 0.0023283000000000002])
xs_exp_limits = array('d', [0.38608999999999999, 0.31178400000000001, 0.23152300000000001, 0.182084, 0.14857100000000001, 0.12660199999999999, 0.107683, 0.100581, 0.079569500000000001, 0.066294000000000006, 0.054121599999999999, 0.055189700000000001, 0.043257299999999999, 0.0361965, 0.0323028, 0.0298725, 0.026485499999999999, 0.020450599999999999, 0.0153977, 0.012107100000000001, 0.0107101, 0.0089616499999999998, 0.0077433399999999996, 0.00651922, 0.0055879600000000003, 0.0048904200000000004, 0.0044238000000000003, 0.00373164, 0.0032596299999999999, 0.0029651399999999998, 0.0025611499999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.34023399999999998, 0.26499200000000001, 0.199827, 0.14723900000000001, 0.12601200000000001, 0.096448900000000004, 0.089127200000000004, 0.074445499999999998, 0.063281100000000007, 0.052138200000000003, 0.044666600000000001, 0.040972300000000003, 0.033523299999999999, 0.0260758, 0.0260851, 0.023284099999999999, 0.020787099999999999, 0.016763199999999999, 0.0118653, 0.0093126400000000005, 0.0081404900000000002, 0.00698483, 0.0060534600000000001, 0.0050015800000000003, 0.0041909, 0.0037252499999999998, 0.00325961, 0.0027939599999999998, 0.0023283000000000002, 0.0020954599999999999,
0.0018626300000000001, 0.0033297600000000002, 0.0036940100000000002, 0.0042356900000000003, 0.0047584200000000002, 0.0056297500000000002, 0.0068011299999999998, 0.0076980900000000003, 0.0086043400000000003, 0.0096185300000000001, 0.0115792, 0.0137801, 0.015561699999999999, 0.018594200000000002, 0.026198900000000001, 0.031979, 0.0374011, 0.040147099999999998, 0.049163499999999999, 0.058594599999999997, 0.066726800000000003, 0.072037799999999999, 0.080177300000000007, 0.096375600000000006, 0.11559999999999999, 0.13081499999999999, 0.161581, 0.18727099999999999, 0.20874500000000001, 0.259992, 0.35752699999999998, 0.446434])
xs_exp_limits_2sigma = array('d', [0.28301100000000001, 0.234484, 0.17699500000000001, 0.13286500000000001, 0.089491600000000004, 0.088751899999999995, 0.0742337, 0.059432100000000002, 0.052071199999999998, 0.0449518, 0.037216699999999998, 0.035375799999999999, 0.026065399999999999, 0.0223409, 0.0223457, 0.018622799999999998, 0.017694100000000001, 0.013037999999999999, 0.0093121999999999996, 0.0074501699999999999, 0.0065189999999999996, 0.0055875300000000003, 0.0046564500000000003, 0.0037620000000000002, 0.00349241, 0.0027939100000000001, 0.0027939200000000001, 0.0023467000000000002, 0.0020954599999999999,
0.0018565700000000001, 0.0016298, 0.0042370400000000001, 0.0045073200000000004, 0.0052922899999999998, 0.0062512100000000001, 0.0072177400000000003, 0.0085528400000000008, 0.0089196499999999995, 0.010419899999999999, 0.0132167, 0.015862899999999999, 0.016210499999999999, 0.0188825, 0.023547599999999998, 0.033520399999999999, 0.040466599999999998, 0.045498200000000003, 0.048098500000000002, 0.062251300000000002, 0.072390599999999999, 0.083247000000000002, 0.086937, 0.094924800000000004, 0.11204, 0.13734499999999999, 0.14813399999999999, 0.194218, 0.23671, 0.24984400000000001, 0.303811, 0.39692499999999997, 0.51659900000000003])

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
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL Combined")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_RSG.eps')

