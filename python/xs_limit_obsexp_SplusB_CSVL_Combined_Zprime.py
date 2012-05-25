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
xs_obs_limits = array('d', [1.0873299999999999, 0.78126899999999999, 0.22914699999999999, 0.119209, 0.089407, 0.096857499999999999, 0.089408600000000005, 0.080405000000000004, 0.055879499999999999, 0.048428800000000001, 0.075565999999999994, 0.072859099999999996, 0.048330499999999998, 0.035445600000000001, 0.035274399999999997, 0.041706300000000002, 0.033661299999999998, 0.019999099999999999, 0.0121072, 0.0088476100000000005, 0.0065192599999999998, 0.0046566200000000002, 0.00372529, 0.0034924600000000002, 0.00372529, 0.0034924600000000002, 0.0032596299999999999, 0.0030268000000000001, 0.0026775599999999998, 0.0023283100000000001, 0.00186265])
xs_exp_limits = array('d', [0.63905199999999995, 0.61605299999999996, 0.210283, 0.163913, 0.12665999999999999, 0.110234, 0.105529, 0.087496099999999993, 0.065312700000000001, 0.052154600000000002, 0.082772700000000005, 0.069321199999999999, 0.051222400000000001, 0.036921700000000002, 0.0332777, 0.040375399999999999, 0.032074999999999999, 0.019127999999999999, 0.0121072, 0.010245600000000001, 0.0088459300000000001, 0.0074087399999999996, 0.0062865400000000002, 0.0053551099999999997, 0.0045402000000000003, 0.0039601899999999997, 0.0035590499999999998, 0.0030268000000000001, 0.0027939699999999998, 0.0023283100000000001, 0.0020954799999999998])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.40090999999999999, 0.407306, 0.178814, 0.12665999999999999, 0.104308, 0.089407, 0.081956500000000002, 0.067055199999999995, 0.048428800000000001, 0.040978199999999999, 0.0504929, 0.046857599999999999, 0.032498800000000001, 0.0242145, 0.0248361, 0.029091100000000002, 0.0248647, 0.0121076, 0.0088476100000000005, 0.00745058, 0.0065192599999999998, 0.0055879399999999996, 0.0046566100000000003, 0.00372529, 0.0034924600000000002, 0.0031993299999999998, 0.0027336700000000001, 0.0022680000000000001, 0.00186265, 0.0017462300000000001, 0.0013969900000000001, 0.0029149599999999999, 0.0032892500000000001, 0.0037179299999999999, 0.00424683, 0.0048579599999999997, 0.0057220400000000003, 0.0070895000000000003, 0.0082046500000000008, 0.0093673899999999997, 0.0107679, 0.0127241, 0.0147663, 0.0176334, 0.029265800000000002, 0.042508999999999998, 0.050431200000000002, 0.047683999999999997, 0.055212799999999999, 0.074240700000000007, 0.092579300000000003, 0.108886, 0.077115000000000003, 0.106182, 0.137131, 0.15532199999999999, 0.18157699999999999, 0.21912499999999999, 0.25412200000000001, 0.36805900000000003, 0.70217799999999997, 0.90498800000000001])
xs_exp_limits_2sigma = array('d', [0.31065999999999999, 0.25331999999999999, 0.16403200000000001, 0.105172, 0.083133600000000002, 0.075094400000000006, 0.059604699999999997, 0.052154100000000002, 0.0447035, 0.033674799999999998, 0.037390699999999999, 0.027999300000000001, 0.024430500000000001, 0.018773600000000001, 0.017768900000000001, 0.019832200000000001, 0.015832499999999999, 0.011175900000000001, 0.00745058, 0.0065192599999999998, 0.00515906, 0.0042277399999999998, 0.0037620800000000001, 0.00327802, 0.0027939699999999998, 0.0025611399999999999, 0.0021138699999999999, 0.00186265, 0.00162981, 0.0013969799999999999, 0.00128057, 0.0039841099999999999, 0.00410882, 0.0046013399999999998, 0.0055724700000000004, 0.0069215800000000001, 0.0080092099999999992, 0.0097663899999999998, 0.0101218, 0.0133271, 0.0177574, 0.0190257, 0.0183526, 0.024821800000000002, 0.035458999999999997, 0.04929, 0.056616, 0.055492800000000002, 0.068554900000000002, 0.092940400000000006, 0.107657, 0.12879599999999999, 0.121277, 0.141177, 0.16975799999999999, 0.180427, 0.24653800000000001, 0.35147600000000001, 0.35938999999999999, 0.59082800000000002, 0.762741, 0.98211499999999996])


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
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_WideJets_Zprime.eps')

