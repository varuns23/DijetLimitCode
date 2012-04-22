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
xs_obs_limits = array('d', [1.5713699999999999, 0.94413599999999998, 0.634517, 0.44179099999999999, 0.34794900000000001, 0.36444700000000002, 0.26321600000000001, 0.178762, 0.11112900000000001, 0.089031299999999994, 0.096804500000000002, 0.123378, 0.101295, 0.073712700000000006, 0.057849999999999999, 0.055133099999999997, 0.050291799999999998, 0.040390200000000001, 0.0287865, 0.021419799999999999, 0.014900399999999999, 0.0093119599999999993, 0.0065186300000000001, 0.0055874499999999999, 0.0055876700000000003, 0.00558773, 0.0055878400000000002, 0.0055878899999999999, 0.0058918099999999999, 0.0054355699999999998, 0.0049728000000000003])
xs_exp_limits = array('d', [1.27193, 0.86320200000000002, 0.66188999999999998, 0.50315399999999999, 0.38530399999999998, 0.33626, 0.25223299999999998, 0.185893, 0.15481300000000001, 0.12373199999999999, 0.096778000000000003, 0.098647399999999996, 0.085858299999999999, 0.066045400000000004, 0.054740499999999997, 0.047403000000000001, 0.042947300000000001, 0.037007600000000002, 0.026564500000000001, 0.0214536, 0.018004699999999998, 0.0149009, 0.0127633, 0.011920200000000001, 0.0098489500000000004, 0.0085966199999999993, 0.0073284500000000002, 0.0061932300000000001, 0.0057194899999999998, 0.0058548999999999997, 0.0050291900000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [1.07663, 0.71887999999999996, 0.52961999999999998, 0.39530799999999999, 0.333538, 0.275895, 0.20662, 0.16311600000000001, 0.118689, 0.096496999999999999, 0.073274599999999995, 0.078196000000000002, 0.066042199999999995, 0.051165000000000002, 0.042826500000000003, 0.037242299999999999, 0.035391899999999997, 0.0279376, 0.022348799999999999, 0.016279700000000001, 0.0130375, 0.012106199999999999, 0.0102446, 0.0088474000000000001, 0.0074503099999999999, 0.0065191199999999998, 0.00558773, 0.0046565299999999999, 0.0041909299999999998, 0.0042126200000000003, 0.0037252499999999998, 0.0069070499999999996,
0.00766236, 0.0080280200000000003, 0.0084658200000000006, 0.0098900399999999992, 0.011167, 0.0130093, 0.0146035, 0.0174074, 0.0193142, 0.023256599999999999, 0.026587800000000002, 0.035370600000000002, 0.044689100000000002, 0.053273800000000003, 0.061782200000000002, 0.0689086, 0.085877599999999998, 0.109095, 0.13070799999999999, 0.124169, 0.15435699999999999, 0.20818600000000001, 0.25325599999999998, 0.300062, 0.39444699999999999, 0.45751399999999998, 0.58854200000000001, 0.76000199999999996, 1.0277799999999999, 1.44611])
xs_exp_limits_2sigma = array('d', [0.88140399999999997, 0.65370799999999996, 0.43376100000000001, 0.35626999999999998, 0.25702599999999998, 0.191909, 0.163188, 0.117605, 0.10359500000000001, 0.081431799999999999, 0.059324700000000001, 0.059828699999999999, 0.052416699999999997, 0.044651900000000001, 0.0336517, 0.029935199999999999, 0.026222200000000001, 0.022492100000000001, 0.018621499999999999, 0.0130367, 0.011173199999999999, 0.010243499999999999, 0.0093124599999999998, 0.0070213999999999997, 0.0055875999999999999, 0.0051589799999999996, 0.0046564299999999996, 0.0037619400000000001, 0.00372515, 0.0032595900000000001,
0.0027938899999999998, 0.0089989400000000004, 0.0091042299999999996, 0.010139, 0.010313299999999999, 0.012408199999999999, 0.0149628, 0.0179402, 0.018789299999999998, 0.020971900000000002, 0.026674099999999999, 0.032216300000000003, 0.038165999999999999, 0.041966000000000003, 0.055756100000000003, 0.062424, 0.071633799999999997, 0.078534099999999996, 0.101711, 0.132102, 0.15668199999999999, 0.15978600000000001, 0.182391, 0.24004300000000001, 0.308342, 0.36197499999999999, 0.480875, 0.53393599999999997, 0.69404900000000003, 0.84719100000000003, 1.1601600000000001, 1.58094])

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

