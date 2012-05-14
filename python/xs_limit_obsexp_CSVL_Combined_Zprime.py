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
xs_obs_limits = array('d', [0.40445599999999998, 0.31949499999999997, 0.20873900000000001, 0.119209, 0.089407, 0.096857499999999999, 0.089412500000000006, 0.078558600000000006, 0.055879400000000003, 0.048428800000000001, 0.059702199999999997, 0.055275499999999998, 0.040337100000000001, 0.031572599999999999, 0.029849899999999999, 0.0307668, 0.025246500000000002, 0.017207799999999999, 0.0121073, 0.0088476100000000005, 0.0065192599999999998, 0.0046566200000000002, 0.00372529, 0.0034924600000000002, 0.00372529, 0.0034924600000000002, 0.0032596299999999999, 0.0030268000000000001, 0.0026775599999999998, 0.0023283100000000001, 0.00186265])
xs_exp_limits = array('d', [0.35325400000000001, 0.27659099999999998, 0.20116600000000001, 0.171876, 0.13966600000000001, 0.11312899999999999, 0.093613100000000005, 0.078235799999999994, 0.059604699999999997, 0.053000199999999997, 0.057729200000000001, 0.0485183, 0.0396998, 0.029456400000000001, 0.029460099999999999, 0.028333299999999999, 0.023238000000000002, 0.015791300000000001, 0.011409000000000001, 0.0097793199999999993, 0.00838239, 0.00745073, 0.0062968, 0.0055879399999999996, 0.0047730699999999999, 0.00419104, 0.0036723400000000001, 0.00342742, 0.0030036099999999999, 0.0025611399999999999, 0.0022119000000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.28312300000000001, 0.22351699999999999, 0.163913, 0.12472999999999999, 0.096857499999999999, 0.087477299999999994, 0.070780700000000002, 0.059604600000000001, 0.048428800000000001, 0.040978199999999999, 0.042840799999999998, 0.037253000000000001, 0.029319899999999999, 0.0223521, 0.022351699999999999, 0.020576400000000002, 0.0174909, 0.0121072, 0.0093132300000000005, 0.00745059, 0.0060536000000000001, 0.0051222799999999999, 0.00453601, 0.00372529, 0.0034924600000000002, 0.00302681, 0.0025611399999999999, 0.0020954799999999998, 0.00186265, 0.0017462300000000001, 0.00162981, 0.00308005, 0.0033757599999999998, 0.0037283300000000002, 0.0043663, 0.0049689299999999999, 0.0058578800000000002, 0.0067843699999999996, 0.0076463399999999997, 0.0085615099999999996, 0.010398299999999999, 0.0120815, 0.0140918, 0.017039599999999998, 0.021164800000000001, 0.0309241, 0.035432699999999998, 0.037140100000000002, 0.038429600000000001, 0.051435700000000001, 0.066105800000000006, 0.0786718, 0.071012400000000003, 0.086436899999999997, 0.104647, 0.12501599999999999, 0.15207999999999999, 0.179733, 0.226518, 0.27288899999999999, 0.34948699999999999, 0.43848100000000001])
xs_exp_limits_2sigma = array('d', [0.208616, 0.178814, 0.119209, 0.089407, 0.074505799999999997, 0.074505799999999997, 0.055879400000000003, 0.048723099999999998, 0.037252899999999999, 0.0298023, 0.0298023, 0.0299495, 0.022351699999999999, 0.016763799999999999, 0.016763900000000002, 0.015048499999999999, 0.0121809, 0.0084554799999999996, 0.0065560799999999997, 0.0055879399999999996, 0.0046934200000000002, 0.0041909499999999997, 0.0035108499999999998, 0.0032596299999999999, 0.0027939699999999998, 0.0023467000000000002, 0.0020954799999999998, 0.00164821, 0.00162981, 0.0013969799999999999, 0.0011733500000000001, 0.0039181900000000002, 0.0043297500000000003, 0.00496043, 0.0056125300000000001, 0.0069482500000000004, 0.0076624400000000004, 0.0089974100000000008, 0.0104627, 0.0128641, 0.0165808, 0.019053, 0.020983100000000001, 0.022477500000000001, 0.027057899999999999, 0.042135400000000003, 0.0489145, 0.052590400000000002, 0.048159399999999998, 0.065794000000000005, 0.082339899999999994, 0.100645, 0.099898399999999998, 0.121087, 0.15529699999999999, 0.171349, 0.196297, 0.229459, 0.29501699999999997, 0.33591799999999999, 0.46523199999999998, 0.547458])

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
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_Zprime.eps')

