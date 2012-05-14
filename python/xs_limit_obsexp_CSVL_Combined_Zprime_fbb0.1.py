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
xs_obs_limits = array('d', [0.52176599999999995, 0.32836700000000002, 0.23841999999999999, 0.14901200000000001, 0.119209, 0.12904199999999999, 0.097415799999999997, 0.067055199999999995, 0.048428800000000001, 0.042840799999999998, 0.060492499999999998, 0.0564705, 0.038407799999999999, 0.028894800000000002, 0.0276315, 0.0285773, 0.0230666, 0.0152424, 0.0107105, 0.0074506099999999999, 0.0055879399999999996, 0.00372529, 0.0032596299999999999, 0.0032596299999999999, 0.0032596299999999999, 0.0030268000000000001, 0.0030268000000000001, 0.0026775499999999999, 0.0023496599999999999, 0.0020954799999999998, 0.00174625])
xs_exp_limits = array('d', [0.44634600000000002, 0.31292399999999998, 0.23841899999999999, 0.18626499999999999, 0.15978100000000001, 0.133435, 0.097038700000000006, 0.074506000000000003, 0.059604999999999998, 0.052155199999999999, 0.0539877, 0.0547459, 0.036292400000000002, 0.0268147, 0.026243699999999998, 0.027914100000000001, 0.0199942, 0.013547099999999999, 0.010710300000000001, 0.0083822500000000008, 0.0074987300000000003, 0.0065193999999999998, 0.0055880399999999998, 0.00488945, 0.0042343499999999996, 0.00361065, 0.0032667099999999999, 0.0030792300000000001, 0.0026073699999999999, 0.0022119000000000002, 0.0018626599999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.37971300000000002, 0.23841899999999999, 0.193715, 0.14156099999999999, 0.111759, 0.096857700000000005, 0.074505799999999997, 0.059604600000000001, 0.047463900000000003, 0.040978199999999999, 0.040978199999999999, 0.040735199999999999, 0.024214699999999999, 0.0204891, 0.0186266, 0.020467099999999998, 0.016195000000000001, 0.0093132400000000004, 0.00745058, 0.0068643200000000001, 0.0055879399999999996, 0.0046566100000000003, 0.00372529, 0.0034924600000000002, 0.0032596299999999999, 0.0025611499999999999, 0.0020954799999999998, 0.00186265, 0.0018324999999999999, 0.0015695100000000001, 0.0013969799999999999, 0.00268192, 0.0029386099999999999, 0.0033597000000000002, 0.00391223, 0.0044200400000000001, 0.0051199699999999997, 0.0058962700000000003, 0.0067557600000000004, 0.00757896, 0.00886552, 0.0106721, 0.0130511, 0.015714599999999999, 0.020013, 0.0280229, 0.037561600000000001, 0.034280900000000003, 0.037404699999999999, 0.048109100000000002, 0.070673700000000006, 0.074097800000000005, 0.066572999999999993, 0.0795627, 0.104465, 0.13181100000000001, 0.19073300000000001, 0.19397700000000001, 0.25835000000000002, 0.30061199999999999, 0.38706000000000002, 0.53996500000000003])
xs_exp_limits_2sigma = array('d', [0.24077299999999999, 0.178814, 0.13411100000000001, 0.104308, 0.089407, 0.081956399999999999, 0.045292100000000002, 0.041272499999999997, 0.037252899999999999, 0.028086799999999999, 0.0298024, 0.031664999999999999, 0.016763900000000002, 0.015048300000000001, 0.0149012, 0.015906400000000001, 0.011249500000000001, 0.00745058, 0.0065192699999999998, 0.0055879399999999996, 0.0046566200000000002, 0.00372529, 0.0034924600000000002, 0.0027939699999999998, 0.0025611399999999999, 0.0020954799999999998, 0.00186265, 0.00162981, 0.0013969799999999999, 0.0011733500000000001, 0.00093132299999999996, 0.00330964, 0.0036904500000000001, 0.0041934099999999998, 0.0048478100000000001, 0.0061479799999999999, 0.0066069600000000003, 0.0077128099999999996, 0.0090035199999999992, 0.0115079, 0.0141564, 0.017042000000000002, 0.0175243, 0.019532299999999999, 0.025695900000000001, 0.035665599999999999, 0.046473100000000003, 0.045098300000000001, 0.042854499999999997, 0.058628899999999998, 0.082905900000000005, 0.091737899999999997, 0.086587399999999995, 0.11679200000000001, 0.15659699999999999, 0.183915, 0.23408399999999999, 0.27060699999999999, 0.36102200000000001, 0.42707899999999999, 0.59045700000000001, 0.74752099999999999])

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
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_Zprime_fbb0.1.eps')

