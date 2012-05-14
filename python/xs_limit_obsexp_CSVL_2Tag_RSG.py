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
xs_obs_limits = array('d', [0.50567200000000001, 0.48394500000000001, 0.28312199999999998, 0.178814, 0.13411200000000001, 0.119211, 0.13411000000000001, 0.165992, 0.15706500000000001, 0.14152300000000001, 0.124318, 0.10662199999999999, 0.090940300000000002, 0.081103900000000007, 0.079797099999999996, 0.074583700000000003, 0.0618661, 0.050253100000000002, 0.0391156, 0.0298023, 0.022351699999999999, 0.018626500000000001, 0.018626500000000001, 0.018626500000000001, 0.0204891, 0.0213805, 0.019093300000000001, 0.018626500000000001, 0.018626500000000001, 0.016763799999999999, 0.016763799999999999])
xs_exp_limits = array('d', [0.41723300000000002, 0.37268499999999999, 0.28312300000000001, 0.23469400000000001, 0.20116600000000001, 0.17136599999999999, 0.14901700000000001, 0.138848, 0.13459499999999999, 0.122625, 0.11525000000000001, 0.099656900000000007, 0.092661499999999994, 0.074580400000000005, 0.072688000000000003, 0.065179799999999996, 0.057570000000000003, 0.045078, 0.037335699999999999, 0.033527599999999998, 0.031664999999999999, 0.0298024, 0.027939700000000001, 0.026077199999999998, 0.0247677, 0.0242314, 0.022352299999999999, 0.021541000000000001, 0.0217562, 0.0204891, 0.0204891])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.357628, 0.31292399999999998, 0.208616, 0.189856, 0.14901200000000001, 0.13963200000000001, 0.119209, 0.111761, 0.096858899999999998, 0.096861299999999997, 0.089407200000000006, 0.0745059, 0.063329899999999995, 0.055879400000000003, 0.052154100000000002, 0.050291599999999999, 0.042358399999999997, 0.0353903, 0.0298023, 0.026076999999999999, 0.023732, 0.022351699999999999, 0.0204891, 0.0204891, 0.018626500000000001, 0.018144, 0.016281400000000001, 0.0149012, 0.0149012, 0.0149012, 0.0149012, 0.026564299999999999, 0.026676700000000001, 0.0270659, 0.026894600000000001, 0.0278347, 0.030060699999999999, 0.031259500000000003, 0.033237000000000003, 0.036377300000000001, 0.0393798, 0.043318500000000003, 0.047099500000000002, 0.049438299999999998, 0.064331700000000006, 0.069620899999999999, 0.089028300000000005, 0.091689199999999998, 0.093402799999999994, 0.114452, 0.125641, 0.151808, 0.170456, 0.17213000000000001, 0.17374400000000001, 0.18219299999999999, 0.21667500000000001, 0.24101, 0.28328500000000001, 0.33697700000000003, 0.418904, 0.46674100000000002])
xs_exp_limits_2sigma = array('d', [0.24077399999999999, 0.23841899999999999, 0.163913, 0.13411100000000001, 0.119209, 0.104308, 0.089407200000000006, 0.089995599999999995, 0.075683299999999995, 0.082544999999999993, 0.071074899999999996, 0.059604600000000001, 0.0447035, 0.0447035, 0.040978199999999999, 0.040978199999999999, 0.030096600000000001, 0.022351699999999999, 0.022351699999999999, 0.0206362, 0.018626500000000001, 0.015048300000000001, 0.0149012, 0.0149012, 0.0131857, 0.0149012, 0.0130385, 0.0130385, 0.0130385, 0.0130385, 0.0130385, 0.031683000000000003, 0.030560299999999999, 0.031230299999999999, 0.033583799999999997, 0.036072399999999998, 0.038961700000000002, 0.037785100000000002, 0.039166100000000002, 0.0462843, 0.0497755, 0.054156799999999998, 0.0585824, 0.0659164, 0.086263500000000007, 0.096254300000000001, 0.11104600000000001, 0.120417, 0.139241, 0.13466500000000001, 0.15917400000000001, 0.200352, 0.25527699999999998, 0.236844, 0.22450999999999999, 0.25479800000000002, 0.30324000000000001, 0.28962700000000002, 0.32381599999999999, 0.39599899999999999, 0.48366199999999998, 0.502077])

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
l1.DrawLatex(0.50,0.80, "2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_2Tag_limit_obsexp_WideJets_RSG.eps')

