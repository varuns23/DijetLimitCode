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
xs_obs_limits = array('d', [0.254299, 0.24431800000000001, 0.14901200000000001, 0.089407100000000003, 0.067055500000000004, 0.067055400000000001, 0.070780700000000002, 0.088384699999999997, 0.0834178, 0.076102699999999995, 0.066885100000000003, 0.056083300000000003, 0.049866599999999997, 0.044962500000000002, 0.045391599999999997, 0.042793100000000001, 0.0358483, 0.0282963, 0.022351800000000002, 0.017695099999999998, 0.0130385, 0.011175900000000001, 0.011175900000000001, 0.011175900000000001, 0.0121072, 0.012644900000000001, 0.0123561, 0.0121073, 0.011175900000000001, 0.011175900000000001, 0.011175900000000001])
xs_exp_limits = array('d', [0.208616, 0.19312599999999999, 0.14901200000000001, 0.119215, 0.104314, 0.0894094, 0.078234300000000007, 0.074772900000000003, 0.068765900000000005, 0.065226999999999993, 0.062028800000000002, 0.051896499999999998, 0.050171800000000003, 0.041457300000000002, 0.038734600000000001, 0.038123299999999999, 0.032692199999999998, 0.024803599999999999, 0.0222995, 0.018626799999999999, 0.018626500000000001, 0.017741699999999999, 0.016763900000000002, 0.015944799999999999, 0.0149018, 0.0149179, 0.014045200000000001, 0.0135073, 0.0132882, 0.0130385, 0.0130385])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.178818, 0.16198299999999999, 0.104309, 0.096857600000000002, 0.080026799999999995, 0.070780599999999999, 0.059604799999999999, 0.059604699999999997, 0.052154100000000002, 0.052154100000000002, 0.048429199999999999, 0.040978599999999997, 0.0353903, 0.031183300000000001, 0.029802499999999999, 0.0298024, 0.024214400000000001, 0.0204891, 0.016763799999999999, 0.0149012, 0.0146599, 0.0137121, 0.0130385, 0.012797299999999999, 0.011175900000000001, 0.011175900000000001, 0.0109347, 0.0102445, 0.0102445, 0.0102445, 0.0102445, 0.017097600000000001, 0.017089400000000001, 0.017057599999999999, 0.017130699999999999, 0.018378700000000001, 0.0191016, 0.019209199999999999, 0.020418499999999999, 0.0225396, 0.023423099999999999, 0.025992299999999999, 0.027847400000000001, 0.028724300000000001, 0.035909499999999997, 0.039731500000000003, 0.051118200000000003, 0.050093199999999997, 0.051234700000000001, 0.062568499999999999, 0.068107699999999993, 0.081642800000000001, 0.090075199999999994, 0.088511000000000006, 0.097195000000000004, 0.095908099999999996, 0.112514, 0.12537899999999999, 0.147009, 0.17316799999999999, 0.21390400000000001, 0.240867])
xs_exp_limits_2sigma = array('d', [0.13411100000000001, 0.13411200000000001, 0.081956399999999999, 0.067643900000000007, 0.060193200000000002, 0.052448399999999999, 0.0447035, 0.048428800000000001, 0.037547200000000003, 0.041272499999999997, 0.037547200000000003, 0.0300968, 0.022646199999999998, 0.022498899999999999, 0.022498899999999999, 0.022498899999999999, 0.0204891, 0.0130385, 0.0130385, 0.0130385, 0.011175900000000001, 0.0102445, 0.0093132300000000005, 0.0084554799999999996, 0.00745058, 0.0083818999999999994, 0.0075241600000000002, 0.00745058, 0.00745058, 0.00745058, 0.00745058, 0.020914700000000001, 0.020610699999999999, 0.020556999999999999, 0.021372700000000001, 0.023158000000000002, 0.024954799999999999, 0.0235883, 0.024137800000000001, 0.027343900000000001, 0.029547500000000001, 0.032915899999999998, 0.035503699999999999, 0.037815700000000001, 0.050273499999999999, 0.055832699999999999, 0.064166100000000004, 0.065972299999999998, 0.078011999999999998, 0.079456899999999997, 0.090987700000000005, 0.108429, 0.13830100000000001, 0.12767000000000001, 0.129109, 0.13428000000000001, 0.155005, 0.15113099999999999, 0.169818, 0.204711, 0.24201600000000001, 0.26599099999999998])

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
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_Zprime_fbb1.0.eps')

