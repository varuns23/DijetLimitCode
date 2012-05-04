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
xs_obs_limits = array('d', [0.38081700000000002, 0.40555200000000002, 0.328407, 0.28402500000000003, 0.16228100000000001, 0.11837, 0.11849999999999999, 0.11862499999999999, 0.12596099999999999, 0.14103199999999999, 0.18537600000000001, 0.180225, 0.15529499999999999, 0.114439, 0.088688699999999995, 0.081811099999999998, 0.074330800000000002, 0.066901600000000006, 0.066948999999999995, 0.059259600000000003, 0.059348999999999999, 0.059326400000000001, 0.061089499999999998, 0.068776799999999999, 0.073133799999999999, 0.074335200000000004, 0.074649300000000002, 0.074486300000000005, 0.078282299999999999, 0.081669699999999998, 0.081660999999999997])
xs_exp_limits = array('d', [0.37195699999999998, 0.32053599999999999, 0.28655599999999998, 0.25087599999999999, 0.20344200000000001, 0.181752, 0.17748, 0.15637400000000001, 0.15126000000000001, 0.148868, 0.174234, 0.15684500000000001, 0.14494799999999999, 0.10424799999999999, 0.096659700000000001, 0.089238899999999996, 0.079422699999999999, 0.074201699999999995, 0.070700100000000002, 0.066176899999999997, 0.059498200000000001, 0.059254500000000002, 0.059274599999999997, 0.063754599999999995, 0.066841300000000006, 0.067819199999999996, 0.069781700000000002, 0.074229299999999998, 0.073914199999999999, 0.073515800000000006, 0.073998400000000006])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.32519199999999998, 0.26684000000000002, 0.23768800000000001, 0.20579500000000001, 0.163438, 0.147068, 0.13342799999999999, 0.11798400000000001, 0.118338, 0.11858299999999999, 0.13406000000000001, 0.12895100000000001, 0.111691, 0.081942699999999993, 0.074201299999999998, 0.066840200000000002, 0.0594359, 0.059371300000000002, 0.059173000000000003, 0.051726099999999997, 0.051659400000000001, 0.044691300000000003, 0.044495899999999998, 0.051615399999999999, 0.051695199999999997, 0.051524899999999998, 0.0515918, 0.051603400000000001, 0.051742299999999998, 0.051911400000000003, 0.058432900000000003,
0.099522899999999997, 0.098047099999999998, 0.093316700000000002, 0.094305700000000006, 0.0962118, 0.097294800000000001, 0.089555300000000004, 0.090190900000000004, 0.074378799999999995, 0.075385599999999997, 0.079083799999999996, 0.082031900000000005, 0.083224300000000001, 0.096798999999999996, 0.104487, 0.10870299999999999, 0.119657, 0.135875, 0.18488099999999999, 0.18943499999999999, 0.217336, 0.193383, 0.19961799999999999, 0.21546899999999999, 0.205009, 0.22364700000000001, 0.255882, 0.31461699999999998, 0.34276099999999998, 0.38139699999999999, 0.41420400000000002])
xs_exp_limits_2sigma = array('d', [0.28620699999999999, 0.233014, 0.21852199999999999, 0.17468800000000001, 0.14557899999999999, 0.117992, 0.103176, 0.087799000000000002, 0.088044700000000004, 0.10324700000000001, 0.10341500000000001, 0.103883, 0.096238599999999994, 0.066345299999999996, 0.0589895, 0.051624400000000001, 0.0444284, 0.044321800000000001, 0.044260500000000001, 0.044099399999999997, 0.041091000000000003, 0.040903500000000002, 0.044250999999999999, 0.044244199999999997, 0.044244899999999997, 0.044242900000000002, 0.044200999999999997, 0.044192099999999998, 0.044451400000000002, 0.051401000000000002,
0.0513645, 0.124664, 0.134931, 0.12436, 0.132438, 0.11842999999999999, 0.120043, 0.11325399999999999, 0.10649, 0.100026, 0.092860399999999996, 0.095491699999999999, 0.09393, 0.10884199999999999, 0.13372999999999999, 0.123682, 0.12762399999999999, 0.13677900000000001, 0.15623400000000001, 0.20774999999999999, 0.226608, 0.26503500000000002, 0.22888500000000001, 0.245617, 0.25009799999999999, 0.252193, 0.255969, 0.29093599999999997, 0.37069000000000002, 0.41510799999999998, 0.43604700000000002, 0.46743299999999999])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVM 2-tag, RSG-like resonances")
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
l1.DrawLatex(0.19,0.20, "Wide Jets")
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.40, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.05)
l1.DrawLatex(0.75,0.20, "2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVM_2Tag_limit_obsexp_WideJets_RSG.eps')

