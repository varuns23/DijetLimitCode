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

  #log_file = open("stats_" + str(mass) + "_" + str(BR) + ".log",'w')
  #log_file.write(output)
  #log_file.close()

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
xs_obs_limits = array('d', [0.34432299999999999, 0.33285799999999999, 0.22642699999999999, 0.171041, 0.096451800000000004, 0.089102100000000004, 0.096823800000000002, 0.081872500000000001, 0.059566099999999997, 0.048397900000000001, 0.052694499999999998, 0.059685500000000002, 0.048711200000000003, 0.037858500000000003, 0.033657600000000003, 0.034106400000000002, 0.032575899999999998, 0.024076500000000001, 0.0171568, 0.012107, 0.0093132100000000006, 0.0065190999999999999, 0.0051221900000000004, 0.0041908600000000002, 0.0046566100000000003, 0.0045041400000000002, 0.0040631, 0.0037000900000000001, 0.0034158700000000001, 0.0029178300000000002, 0.0025611399999999999])
xs_exp_limits = array('d', [0.30534099999999997, 0.25569700000000001, 0.21276100000000001, 0.17092499999999999, 0.137211, 0.115424, 0.096840499999999996, 0.081889000000000003, 0.070741200000000004, 0.059714700000000002, 0.055680300000000002, 0.054171200000000003, 0.044833400000000002, 0.036048400000000001, 0.031813300000000003, 0.0291381, 0.0262948, 0.021102599999999999, 0.0149149, 0.012107100000000001, 0.0107101, 0.0088474299999999999, 0.0074505600000000002, 0.0065192100000000001, 0.0055878899999999999, 0.0051223199999999997, 0.0044237699999999996, 0.00372529, 0.0032596999999999999, 0.0028665499999999998, 0.0023434100000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.27992499999999998, 0.217858, 0.19270599999999999, 0.14086599999999999, 0.111397, 0.096609799999999996, 0.081736100000000006, 0.067007300000000006, 0.059533500000000003, 0.048390900000000001, 0.044673200000000003, 0.040968699999999997, 0.037250999999999999, 0.027933900000000001, 0.024212000000000001, 0.022350700000000001, 0.018625300000000001, 0.016763400000000001, 0.0121066, 0.00985486, 0.0074505700000000001, 0.0065192999999999996, 0.0060535299999999997, 0.0051222000000000004, 0.0043634600000000004, 0.0037252499999999998, 0.00325961, 0.0030267800000000002, 0.00256113, 0.0022309700000000001,
0.0018626300000000001, 0.0034480299999999999, 0.0041012499999999999, 0.0044580899999999996, 0.00516696, 0.00589721, 0.0067585500000000003, 0.0076547899999999999, 0.0083384199999999992, 0.0095065299999999991, 0.011848900000000001, 0.013489599999999999, 0.015916300000000001, 0.0198014, 0.027254, 0.033477, 0.0363869, 0.040073999999999999, 0.0464327, 0.057053100000000002, 0.065397700000000003, 0.069953399999999999, 0.077481700000000001, 0.091381199999999996, 0.101227, 0.123309, 0.13770199999999999, 0.16896, 0.196937, 0.246665, 0.30419200000000002, 0.33503300000000003])
xs_exp_limits_2sigma = array('d', [0.24968499999999999, 0.19192300000000001, 0.16158400000000001, 0.117787, 0.10373300000000001, 0.088911400000000002, 0.066902199999999995, 0.052227799999999998, 0.044880299999999998, 0.044639699999999997, 0.037207799999999999, 0.029775099999999999, 0.026065999999999999, 0.022339500000000002, 0.018772899999999999, 0.018623299999999999, 0.0149535, 0.013037999999999999, 0.0093126500000000004, 0.0074502500000000003, 0.0065189899999999997, 0.0046932500000000004, 0.0042277199999999999, 0.0041908400000000004, 0.0035108299999999999, 0.0027939100000000001, 0.0027939200000000001, 0.0023282899999999998,
0.0018761299999999999, 0.0016298, 0.0016298, 0.0047465399999999996, 0.0055461299999999998, 0.0065250400000000002, 0.0068727099999999998, 0.0074111300000000001, 0.0090008799999999993, 0.0093747899999999992, 0.0103962, 0.0125101, 0.0140228, 0.017106699999999999, 0.019851299999999999, 0.0229865, 0.033494200000000002, 0.041863499999999998, 0.044212000000000001, 0.048967299999999998, 0.059307899999999997, 0.076283900000000002, 0.0770034, 0.080243599999999998, 0.092179899999999995, 0.11865100000000001, 0.136462, 0.150586, 0.16194700000000001, 0.19909399999999999, 0.24324000000000001, 0.29803099999999999, 0.33995799999999998, 0.36236600000000002])

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
l1.DrawLatex(0.19,0.20, "Wide Jets")
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.50, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.05)
l1.DrawLatex(0.52,0.20, "0, 1 and 2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVM_Combined_limit_obsexp_WideJets_RSG.png')

