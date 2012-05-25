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
xs_obs_limits = array('d', [2.3737300000000001, 0.53644199999999997, 0.40234700000000001, 0.29802499999999998, 0.28523100000000001, 0.36223, 0.163913, 0.104308, 0.081956399999999999, 0.070780499999999996, 0.12318900000000001, 0.13012199999999999, 0.085433099999999998, 0.057621100000000001, 0.053197000000000001, 0.055907499999999999, 0.0472034, 0.031425799999999997, 0.019009700000000001, 0.0130387, 0.0093132300000000005, 0.0065192599999999998, 0.0046566100000000003, 0.0046566100000000003, 0.0046566100000000003, 0.0046566100000000003, 0.0046566100000000003, 0.0049624100000000004, 0.00516696, 0.0047539699999999997, 0.0040282900000000003])
xs_exp_limits = array('d', [0.77869699999999997, 0.56628599999999996, 0.43282999999999999, 0.35498600000000002, 0.26822099999999999, 0.22206300000000001, 0.192523, 0.14557600000000001, 0.11239200000000001, 0.089407200000000006, 0.076141600000000004, 0.057742099999999998, 0.050291599999999999, 0.042840900000000001, 0.035458999999999997, 0.027939700000000001, 0.024214400000000001, 0.021422500000000001, 0.018760499999999999, 0.015885900000000001, 0.0135456, 0.011425299999999999, 0.0105664, 0.0088478099999999994, 0.0079632499999999998, 0.0065229099999999998, 0.0056098700000000003, 0.0050670200000000002, 0.0044237900000000004, 0.0039941300000000002, 0.0034764599999999998])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.71525799999999995, 0.50663899999999995, 0.37971300000000002, 0.28312199999999998, 0.22351699999999999, 0.178814, 0.14156099999999999, 0.104308, 0.081956399999999999, 0.067055199999999995, 0.055879400000000003, 0.048428800000000001, 0.037253099999999997, 0.033527599999999998, 0.027939700000000001, 0.024214400000000001, 0.0186266, 0.016764100000000001, 0.0149012, 0.0121072, 0.0102446, 0.0093132300000000005, 0.0077957199999999999, 0.0065192599999999998, 0.0060536000000000001, 0.0050016699999999997, 0.0041909499999999997, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.0027939699999999998, 0.0043831399999999998, 0.0054447999999999996, 0.0062435199999999998, 0.0067311699999999999, 0.0080976099999999999, 0.0093493399999999994, 0.011198, 0.012974899999999999, 0.016106700000000002, 0.0176364, 0.021098200000000001, 0.025659000000000001, 0.028101500000000001, 0.038442799999999999, 0.0378444, 0.0483057, 0.055354800000000003, 0.064223799999999998, 0.068407800000000005, 0.090356300000000001, 0.11387, 0.142096, 0.18747900000000001, 0.28185199999999999, 0.312865, 0.34256999999999999, 0.47635699999999997, 0.51686500000000002, 0.76832400000000001, 0.99418200000000001, 1.41672])
xs_exp_limits_2sigma = array('d', [0.65565099999999998, 0.44703500000000002, 0.26822099999999999, 0.22351799999999999, 0.16508999999999999, 0.13411000000000001, 0.112347, 0.082544999999999993, 0.067055199999999995, 0.052448399999999999, 0.044997799999999998, 0.037469000000000002, 0.033527599999999998, 0.022646199999999998, 0.024214400000000001, 0.018626500000000001, 0.016763799999999999, 0.014043399999999999, 0.0130385, 0.0093132300000000005, 0.0083819099999999994, 0.0075241700000000002, 0.0065192799999999997, 0.0051222699999999999, 0.0042277399999999998, 0.0041909499999999997, 0.0035108499999999998, 0.0028307599999999999, 0.00257953, 0.0023283100000000001, 0.0023283100000000001, 0.0057796999999999996, 0.0070840399999999998, 0.0080783000000000001, 0.0085079000000000005, 0.010618300000000001, 0.0133852, 0.016652900000000002, 0.020368600000000001, 0.021226399999999999, 0.023953800000000001, 0.031075499999999999, 0.0423235, 0.044513999999999998, 0.051647899999999997, 0.053068499999999998, 0.071760199999999996, 0.069485500000000006, 0.093553899999999995, 0.103518, 0.120057, 0.157581, 0.196043, 0.26706999999999997, 0.37077500000000002, 0.457625, 0.45892100000000002, 0.67538699999999996, 0.826434, 1.16204, 1.4570799999999999, 2.3090799999999998])

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
l1.DrawLatex(0.50,0.80, "0 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obsexp_SplusB_WideJets_Zprime.eps')

