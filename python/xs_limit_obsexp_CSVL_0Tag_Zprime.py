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
xs_obs_limits = array('d', [0.98086799999999996, 0.53644199999999997, 0.40234599999999998, 0.29802499999999998, 0.27633600000000003, 0.271092, 0.163913, 0.104308, 0.081956399999999999, 0.070780499999999996, 0.097981399999999996, 0.096766500000000005, 0.068339700000000003, 0.052049699999999997, 0.045315300000000003, 0.043900799999999997, 0.0365305, 0.0267756, 0.018867600000000002, 0.0130387, 0.0093133000000000001, 0.0065192599999999998, 0.0046566100000000003, 0.0046566100000000003, 0.0046566100000000003, 0.0046566100000000003, 0.0046566100000000003, 0.0049346499999999996, 0.0049714099999999999, 0.00459035, 0.0040110199999999997])
xs_exp_limits = array('d', [0.80492699999999995, 0.53646899999999997, 0.41724099999999997, 0.32782600000000001, 0.26822099999999999, 0.24529799999999999, 0.17136399999999999, 0.13553499999999999, 0.108046, 0.089407700000000007, 0.089886300000000002, 0.079916000000000001, 0.061157900000000001, 0.048450100000000003, 0.040210900000000001, 0.039331400000000002, 0.031674800000000003, 0.0255762, 0.018344099999999999, 0.015981499999999999, 0.013776399999999999, 0.0116679, 0.0097812999999999997, 0.0088486699999999995, 0.0074513599999999998, 0.0063560200000000004, 0.0055879900000000001, 0.0054371100000000002, 0.0052806800000000003, 0.00442473, 0.00387025])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.715256, 0.44703500000000002, 0.32010699999999997, 0.23841899999999999, 0.208616, 0.193715, 0.12665999999999999, 0.096857499999999999, 0.074505799999999997, 0.065125500000000003, 0.063329899999999995, 0.059606699999999999, 0.048428800000000001, 0.035390600000000001, 0.031182600000000001, 0.0298024, 0.0251457, 0.018627000000000001, 0.013728600000000001, 0.011175900000000001, 0.0102446, 0.0093132300000000005, 0.00745058, 0.0065192599999999998, 0.0055879399999999996, 0.0046566100000000003, 0.0041909499999999997, 0.00372529, 0.0038978400000000001, 0.0032596299999999999, 0.0027939699999999998, 0.0061443299999999999, 0.0069320299999999996, 0.00710313, 0.0071515199999999998, 0.0075725699999999998, 0.0084274799999999993, 0.0099383000000000006, 0.011515900000000001, 0.0136136, 0.015851400000000002, 0.018441800000000001, 0.0207846, 0.023369399999999999, 0.034362299999999998, 0.043189699999999998, 0.049638500000000002, 0.056185800000000001, 0.065086699999999997, 0.081521999999999997, 0.10578, 0.12339899999999999, 0.111888, 0.140823, 0.18720899999999999, 0.222608, 0.31103199999999998, 0.33736699999999997, 0.41395399999999999, 0.53003599999999995, 0.65962100000000001, 0.94771499999999997])
xs_exp_limits_2sigma = array('d', [0.53644199999999997, 0.33017999999999997, 0.23841899999999999, 0.178814, 0.163913, 0.14215, 0.090584200000000004, 0.082544999999999993, 0.067055199999999995, 0.045292100000000002, 0.048428800000000001, 0.0447035, 0.035537399999999997, 0.027939700000000001, 0.024214400000000001, 0.022498899999999999, 0.018773600000000001, 0.0149012, 0.0102445, 0.0084554799999999996, 0.00745058, 0.0056615099999999998, 0.0055879399999999996, 0.0051222699999999999, 0.0042277399999999998, 0.0041909499999999997, 0.00327802, 0.0032596299999999999, 0.0028307599999999999, 0.0025611399999999999, 0.0023283100000000001, 0.0075654199999999998, 0.0087675199999999991, 0.0100018, 0.0095805700000000001, 0.0091295500000000002, 0.011479400000000001, 0.013711299999999999, 0.0147285, 0.0174203, 0.019364200000000002, 0.022352799999999999, 0.0290937, 0.034601199999999999, 0.044639600000000002, 0.054637499999999999, 0.0648706, 0.068953500000000001, 0.0816249, 0.109695, 0.136352, 0.157526, 0.13497400000000001, 0.18290000000000001, 0.23358200000000001, 0.289798, 0.42285800000000001, 0.40473500000000001, 0.50388599999999995, 0.60799599999999998, 0.79796, 1.12487])

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
c.SaveAs('CSVL_0Tag_limit_obsexp_WideJets_Zprime.eps')

