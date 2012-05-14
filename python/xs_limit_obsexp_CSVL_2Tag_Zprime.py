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
xs_obs_limits = array('d', [0.49345299999999997, 0.465339, 0.28312199999999998, 0.163913, 0.11921, 0.11921, 0.13411000000000001, 0.160387, 0.14735500000000001, 0.13561400000000001, 0.117662, 0.096820400000000001, 0.081821400000000002, 0.072501399999999994, 0.075647099999999995, 0.068982399999999999, 0.057373599999999997, 0.044474699999999999, 0.033529200000000002, 0.026076999999999999, 0.0204891, 0.016763799999999999, 0.0149012, 0.016763799999999999, 0.018678500000000001, 0.0179221, 0.017206300000000001, 0.0149012, 0.0149012, 0.0149012, 0.0130385])
xs_exp_limits = array('d', [0.40233099999999999, 0.35982500000000001, 0.27567199999999997, 0.23096900000000001, 0.19372500000000001, 0.16392100000000001, 0.14502999999999999, 0.13522700000000001, 0.127577, 0.12428500000000001, 0.111813, 0.091209999999999999, 0.082043400000000002, 0.068136600000000005, 0.064075400000000005, 0.060578899999999998, 0.0532539, 0.0391156, 0.033527700000000001, 0.0298024, 0.02794, 0.026076999999999999, 0.025031999999999999, 0.023814499999999999, 0.022351699999999999, 0.020567700000000001, 0.0188118, 0.018113799999999999, 0.016763799999999999, 0.015756900000000001, 0.0149012])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.34990900000000003, 0.31292399999999998, 0.193715, 0.178814, 0.14901200000000001, 0.13411000000000001, 0.111759, 0.111759, 0.096857600000000002, 0.096857799999999994, 0.084716799999999995, 0.070780499999999996, 0.058639799999999999, 0.052154100000000002, 0.048429, 0.048428899999999997, 0.037253000000000001, 0.0298023, 0.026076999999999999, 0.022351699999999999, 0.022351699999999999, 0.020006699999999999, 0.018144, 0.016763799999999999, 0.016281400000000001, 0.0149012, 0.0149012, 0.0130385, 0.0130385, 0.0130385, 0.0130385, 0.021124299999999999, 0.0218245, 0.022453999999999998, 0.0232909, 0.0258163, 0.0272657, 0.026938199999999999, 0.028677100000000001, 0.0322625, 0.034872599999999997, 0.038636299999999998, 0.041553399999999997, 0.044480400000000003, 0.056938500000000003, 0.0644787, 0.082416299999999998, 0.087708700000000001, 0.089292800000000006, 0.103364, 0.12131500000000001, 0.14316200000000001, 0.16136500000000001, 0.161216, 0.168016, 0.17299400000000001, 0.20932700000000001, 0.2361, 0.27667700000000001, 0.33134599999999997, 0.40940300000000002, 0.460148])
xs_exp_limits_2sigma = array('d', [0.24077299999999999, 0.23841899999999999, 0.14901200000000001, 0.12038699999999999, 0.112347, 0.104308, 0.089407, 0.089407100000000003, 0.067055199999999995, 0.075094400000000006, 0.067349500000000007, 0.0561737, 0.041272499999999997, 0.0447035, 0.033527599999999998, 0.033527599999999998, 0.027939700000000001, 0.0206362, 0.0204891, 0.018626500000000001, 0.015048300000000001, 0.0149012, 0.0149012, 0.0130385, 0.011175900000000001, 0.011323, 0.011175900000000001, 0.011175900000000001, 0.011175900000000001, 0.011175900000000001, 0.011175900000000001, 0.025826999999999999, 0.026002899999999999, 0.027014900000000001, 0.028630099999999999, 0.031696299999999997, 0.033959099999999999, 0.033644199999999999, 0.035192800000000003, 0.039169000000000002, 0.0434965, 0.050135100000000002, 0.055090300000000002, 0.057843800000000001, 0.081474699999999997, 0.078794500000000003, 0.11521199999999999, 0.11119999999999999, 0.119809, 0.125279, 0.16767899999999999, 0.179123, 0.23899200000000001, 0.23022599999999999, 0.24886, 0.24684400000000001, 0.28989999999999999, 0.27877400000000002, 0.31942799999999999, 0.387907, 0.46090500000000001, 0.51962399999999997])

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
c.SaveAs('CSVL_2Tag_limit_obsexp_WideJets_Zprime.eps')

