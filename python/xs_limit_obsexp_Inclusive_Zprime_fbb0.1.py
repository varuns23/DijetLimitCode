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


BR = 0.1

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
xs_obs_limits = array('d', [0.51409400000000005, 0.31382700000000002, 0.23841899999999999, 0.14901200000000001, 0.12665999999999999, 0.134488, 0.098210800000000001, 0.070780599999999999, 0.048428800000000001, 0.040978199999999999, 0.059390800000000001, 0.055869599999999998, 0.038239099999999998, 0.0288408, 0.0275345, 0.028373900000000001, 0.022857100000000002, 0.0151246, 0.010710300000000001, 0.0074505999999999999, 0.0055879399999999996, 0.00372529, 0.0032596299999999999, 0.0032596299999999999, 0.0032596499999999998, 0.0030268000000000001, 0.0027939699999999998, 0.0026776899999999999, 0.0024031899999999999, 0.00209553, 0.0017462300000000001])
xs_exp_limits = array('d', [0.45216099999999998, 0.31296299999999999, 0.22724800000000001, 0.18626499999999999, 0.14901600000000001, 0.12994700000000001, 0.097380700000000001, 0.078623899999999997, 0.063330899999999996, 0.0540191, 0.053413200000000001, 0.046024900000000001, 0.034925200000000003, 0.029125600000000001, 0.0248723, 0.0241315, 0.0195731, 0.0142775, 0.010913300000000001, 0.0093790799999999997, 0.0079172900000000004, 0.0065192899999999996, 0.0056522999999999999, 0.0046566100000000003, 0.0041909499999999997, 0.0037389799999999998, 0.0030420899999999999, 0.0027939699999999998, 0.0025807999999999998, 0.0020954799999999998, 0.0018928599999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.40233099999999999, 0.27926499999999999, 0.193716, 0.14901200000000001, 0.119209, 0.096857899999999997, 0.081956399999999999, 0.063329899999999995, 0.052154100000000002, 0.0447035, 0.042840999999999997, 0.033527599999999998, 0.026077199999999998, 0.022351699999999999, 0.0204891, 0.017695099999999998, 0.015867200000000001, 0.011175900000000001, 0.0088476000000000006, 0.0074506099999999999, 0.0060536000000000001, 0.0046566100000000003, 0.00372529, 0.0034924600000000002, 0.0029665, 0.0025611499999999999, 0.0023283100000000001, 0.00186265, 0.00186265, 0.00162981, 0.0013969799999999999, 0.0024771699999999999, 0.0029631800000000002, 0.0035936900000000001, 0.0038469200000000002, 0.0043079399999999997, 0.0047492699999999999, 0.0056576700000000001, 0.0065637300000000003, 0.0073582400000000003, 0.0088044000000000004, 0.0097848099999999997, 0.0115332, 0.013931000000000001, 0.0179472, 0.024622499999999999, 0.031262199999999997, 0.032400600000000002, 0.035649500000000001, 0.046757800000000002, 0.059180799999999999, 0.065855300000000006, 0.064891400000000002, 0.079870099999999999, 0.100854, 0.118599, 0.15429000000000001, 0.18362700000000001, 0.22490499999999999, 0.28092099999999998, 0.36028100000000002, 0.51059900000000003])
xs_exp_limits_2sigma = array('d', [0.33018399999999998, 0.22469600000000001, 0.178814, 0.119209, 0.104308, 0.089407, 0.071074799999999994, 0.052154100000000002, 0.040978199999999999, 0.033674799999999998, 0.033674799999999998, 0.026224500000000001, 0.022351699999999999, 0.015048300000000001, 0.0149012, 0.013112199999999999, 0.0121072, 0.0083819099999999994, 0.0065560699999999998, 0.0055879399999999996, 0.0046566100000000003, 0.00372529, 0.00327802, 0.0027939699999999998, 0.0025611399999999999, 0.0020954799999999998, 0.00164821, 0.00162981, 0.0014153799999999999, 0.00128977, 0.0011733500000000001, 0.0033719800000000001, 0.0035878300000000002, 0.0044581999999999998, 0.00473377, 0.0056601000000000004, 0.0069970900000000001, 0.0080827199999999998, 0.0087213199999999994, 0.0104063, 0.010922899999999999, 0.0126634, 0.015954400000000001, 0.017247999999999999, 0.022919200000000001, 0.030215700000000002, 0.039033100000000001, 0.041852399999999998, 0.046117999999999999, 0.058806900000000002, 0.068645800000000007, 0.081475500000000006, 0.081505800000000003, 0.101308, 0.13150999999999999, 0.144647, 0.17452300000000001, 0.22225400000000001, 0.27125500000000002, 0.32178200000000001, 0.40909000000000001, 0.60468500000000003])

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
c.SaveAs('Inclusive_limit_obsexp_WideJets_Zprime_fbb0.1.eps')

