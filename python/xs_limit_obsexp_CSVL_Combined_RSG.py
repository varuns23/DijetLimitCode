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
xs_obs_limits = array('d', [0.43779699999999999, 0.38328499999999999, 0.24687100000000001, 0.14901200000000001, 0.096857499999999999, 0.096857499999999999, 0.104308, 0.104522, 0.081644700000000001, 0.063330300000000006, 0.065327399999999994, 0.065512200000000007, 0.053470700000000003, 0.042758999999999998, 0.038424899999999998, 0.038156099999999998, 0.033347300000000003, 0.0249803, 0.017419, 0.0121072, 0.0093132400000000004, 0.00745058, 0.0055879399999999996, 0.0051222699999999999, 0.0051222699999999999, 0.0046566100000000003, 0.0041909499999999997, 0.0041909499999999997, 0.0037253, 0.0032596299999999999, 0.0027939699999999998])
xs_exp_limits = array('d', [0.387932, 0.32645200000000002, 0.223526, 0.19561200000000001, 0.16650300000000001, 0.132157, 0.115193, 0.103962, 0.082050799999999993, 0.067266900000000004, 0.061823799999999998, 0.057415899999999999, 0.049415500000000001, 0.042342200000000003, 0.034446699999999997, 0.0336855, 0.033328499999999997, 0.0220974, 0.016329099999999999, 0.013038599999999999, 0.011642, 0.0097789000000000001, 0.0088477599999999997, 0.0074505999999999999, 0.0065193300000000003, 0.0060357400000000004, 0.00517791, 0.0047223600000000001, 0.0042982599999999999, 0.0036637900000000001, 0.0033130600000000001])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.33886899999999998, 0.25332399999999999, 0.189856, 0.14708299999999999, 0.11728, 0.104308, 0.089407, 0.080027100000000004, 0.059604600000000001, 0.052154100000000002, 0.048428800000000001, 0.044703899999999998, 0.0391156, 0.0298024, 0.026076999999999999, 0.025905600000000001, 0.023770800000000002, 0.017695200000000001, 0.0121072, 0.0102446, 0.0083818999999999994, 0.0073299699999999999, 0.0065192599999999998, 0.0055879399999999996, 0.0046566100000000003, 0.0041909499999999997, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.0025611399999999999, 0.0023283100000000001, 0.0044271099999999997, 0.0049036399999999999, 0.00546504, 0.0062473199999999998, 0.0072389899999999998, 0.0081127400000000002, 0.0094658099999999998, 0.010490599999999999, 0.0120658, 0.0143035, 0.0162536, 0.019594799999999999, 0.022883299999999999, 0.0290955, 0.040820500000000003, 0.046243899999999998, 0.048538400000000002, 0.052280899999999998, 0.070364399999999994, 0.081416699999999995, 0.084204100000000004, 0.091209999999999999, 0.107846, 0.13293199999999999, 0.14847399999999999, 0.17693200000000001, 0.21207699999999999, 0.252604, 0.304087, 0.41606900000000002, 0.46282200000000001])
xs_exp_limits_2sigma = array('d', [0.22351699999999999, 0.208616, 0.12038699999999999, 0.104897, 0.089407, 0.081956500000000002, 0.067055199999999995, 0.059604699999999997, 0.0447035, 0.037547200000000003, 0.037547200000000003, 0.037253000000000001, 0.028086799999999999, 0.0206362, 0.0204891, 0.0170581, 0.018626500000000001, 0.0121808, 0.0093132300000000005, 0.00745058, 0.00659283, 0.0055879399999999996, 0.0051222699999999999, 0.0042277399999999998, 0.0037620800000000001, 0.0034924600000000002, 0.0032596299999999999, 0.0027939699999999998, 0.0021138699999999999, 0.00186265, 0.00186265, 0.0056152800000000003, 0.0063067399999999999, 0.0073987699999999998, 0.0087597300000000003, 0.0098246900000000005, 0.010837299999999999, 0.0124084, 0.0153194, 0.0191541, 0.022629400000000001, 0.025616900000000001, 0.0275146, 0.032177999999999998, 0.043731899999999997, 0.0528613, 0.057785499999999997, 0.0621735, 0.061657799999999999, 0.089081400000000005, 0.102052, 0.10910400000000001, 0.13130700000000001, 0.12745600000000001, 0.184415, 0.212479, 0.221024, 0.284582, 0.316998, 0.38007400000000002, 0.54956400000000005, 0.60332200000000002])

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
l1.DrawLatex(0.18,0.89, "RS-graviton-like, f_{b#bar{b}}=" + str(BR))
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
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_RSG.eps')

