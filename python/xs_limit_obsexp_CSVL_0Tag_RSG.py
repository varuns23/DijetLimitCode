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
xs_obs_limits = array('d', [1.54477, 0.90504200000000001, 0.65483000000000002, 0.395453, 0.35067700000000002, 0.36762600000000001, 0.26030599999999998, 0.17061599999999999, 0.11118699999999999, 0.089138300000000004, 0.096794900000000003, 0.121518, 0.101787, 0.071764800000000004, 0.057744799999999999, 0.055086799999999998, 0.050266400000000003, 0.040317400000000003, 0.028816600000000001, 0.021420000000000002, 0.014900800000000001, 0.0093120300000000007, 0.00651865, 0.0055874599999999998, 0.0055876800000000003, 0.0055877399999999999, 0.0055878500000000001, 0.00558787, 0.0058816399999999996, 0.0054287099999999998, 0.0049748600000000002])
xs_exp_limits = array('d', [1.1337299999999999, 0.81414799999999998, 0.62246199999999996, 0.471748, 0.35930600000000001, 0.327901, 0.24701699999999999, 0.182002, 0.15606200000000001, 0.11899899999999999, 0.096781800000000001, 0.106417, 0.086324600000000001, 0.064508999999999997, 0.0551583, 0.049264099999999998, 0.043981699999999999, 0.036297500000000003, 0.0274977, 0.021651799999999999, 0.018730500000000001, 0.015546900000000001, 0.0130384, 0.011303000000000001, 0.0099658899999999998, 0.0083839699999999993, 0.0069890100000000004, 0.0060536699999999997, 0.0059561900000000001, 0.0058436199999999999, 0.0051034899999999996])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.933778, 0.55499699999999996, 0.41975099999999999, 0.353827, 0.27771600000000002, 0.26083299999999998, 0.191271, 0.14705299999999999, 0.111112, 0.096453399999999995, 0.0732907, 0.081889900000000002, 0.063308500000000004, 0.044680600000000001, 0.042344300000000001, 0.036761799999999997, 0.034036499999999997, 0.027938999999999999, 0.022107000000000002, 0.014899000000000001, 0.013037699999999999, 0.012106199999999999, 0.010244100000000001, 0.0083814000000000007, 0.0069848200000000001, 0.0063984599999999999, 0.0055876800000000003, 0.0046564900000000001, 0.0041909099999999999, 0.0041909, 0.00349249,
0.0073784100000000002, 0.0079421600000000002, 0.0083793700000000006, 0.0082842999999999997, 0.0094047799999999997, 0.010693100000000001, 0.013037999999999999, 0.014859000000000001, 0.017791999999999999, 0.0207543, 0.023642699999999999, 0.026571299999999999, 0.0370674, 0.0488069, 0.0559242, 0.0688135, 0.070577899999999999, 0.085905899999999993, 0.114688, 0.13835500000000001, 0.124679, 0.15323600000000001, 0.19996800000000001, 0.25933400000000001, 0.29927199999999998, 0.41570499999999999, 0.441195, 0.58785600000000005, 0.73258199999999996, 0.99717500000000003, 1.36978])
xs_exp_limits_2sigma = array('d', [0.58386400000000005, 0.46543699999999999, 0.27401700000000001, 0.25574999999999998, 0.22211500000000001, 0.207565, 0.14635100000000001, 0.117289, 0.082290299999999997, 0.0674704, 0.055723000000000002, 0.059836599999999997, 0.052118999999999999, 0.037199799999999998, 0.029778800000000001, 0.029786799999999999, 0.0260716, 0.0242093, 0.016759900000000001, 0.0113212, 0.010316499999999999, 0.0075240400000000001, 0.0070213300000000001, 0.0065557599999999999, 0.0055876199999999997, 0.0051220800000000002, 0.0046564299999999996, 0.0037251799999999998, 0.0035108100000000001, 0.00325954, 0.0027938899999999998,
0.0091422199999999995, 0.0101683, 0.0107181, 0.0100117, 0.012416999999999999, 0.014968499999999999, 0.017182800000000002, 0.019038699999999999, 0.0217883, 0.0265887, 0.031972, 0.038561900000000003, 0.048067100000000001, 0.056954400000000002, 0.070829400000000001, 0.082966300000000007, 0.086961899999999995, 0.106836, 0.152758, 0.164079, 0.14669399999999999, 0.187801, 0.25740000000000002, 0.32421899999999998, 0.40193699999999999, 0.54493000000000003, 0.518953, 0.70452599999999999, 0.84706599999999999, 1.1902299999999999, 1.5374699999999999])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
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
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL 0-tag")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obsexp_WideJets_RSG.eps')

