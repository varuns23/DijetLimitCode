#!/usr/bin/env python

import sys, os, string, re
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

#mass_start = 1000
#mass_step = 100
#steps = 30

#for i in range(0,steps+1):

  #mass = mass_start + i*mass_step

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(mass) + "_" + str(BR) + "_gg.log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

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
xs_obs_limits = array('d', [0.46759899999999999, 0.42053800000000002, 0.291574, 0.178814, 0.111759, 0.104308, 0.111759, 0.108247, 0.092820600000000003, 0.070780899999999994, 0.069052699999999995, 0.067374799999999999, 0.059058699999999999, 0.049278299999999997, 0.041218900000000003, 0.038156099999999998, 0.035209900000000002, 0.0305682, 0.023938299999999999, 0.016763799999999999, 0.011175900000000001, 0.0083818999999999994, 0.0065192599999999998, 0.0055879399999999996, 0.0051222699999999999, 0.0046566100000000003, 0.0046566100000000003, 0.0041909499999999997, 0.0037253, 0.0034924600000000002, 0.0032596299999999999])
xs_exp_limits = array('d', [0.41725099999999998, 0.34849200000000002, 0.23841899999999999, 0.196238, 0.16888700000000001, 0.13411300000000001, 0.117143, 0.107048, 0.081956399999999999, 0.067055199999999995, 0.064565399999999995, 0.064897099999999999, 0.054803400000000002, 0.044862699999999998, 0.039726999999999998, 0.034869299999999999, 0.033647099999999999, 0.024659799999999999, 0.018626500000000001, 0.0139705, 0.0126613, 0.011175900000000001, 0.0094915599999999996, 0.0083446900000000001, 0.00732834, 0.0064231799999999997, 0.0055879399999999996, 0.0049172599999999997, 0.0046001699999999998, 0.00372529, 0.0035818099999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.32782600000000001, 0.24946099999999999, 0.178814, 0.13436500000000001, 0.119209, 0.104308, 0.081956399999999999, 0.074505799999999997, 0.059604600000000001, 0.052154100000000002, 0.048428800000000001, 0.048428800000000001, 0.037252899999999999, 0.0298023, 0.026076999999999999, 0.026603100000000001, 0.0249552, 0.019062200000000001, 0.0130385, 0.011175900000000001, 0.0093132300000000005, 0.00745058, 0.0065192599999999998, 0.0055879399999999996, 0.0055879399999999996, 0.0046566100000000003, 0.0037411200000000001, 0.0034924600000000002, 0.0032596299999999999, 0.0027939699999999998, 0.0025611399999999999, 0.0048665899999999996, 0.00529358, 0.0060846199999999998, 0.0068774999999999999, 0.0078358300000000002, 0.0089807499999999992, 0.00986683, 0.0113078, 0.0129319, 0.015800999999999999, 0.017548999999999999, 0.020591600000000002, 0.0249517, 0.032420999999999998, 0.041804099999999997, 0.045622599999999999, 0.050325700000000001, 0.055485600000000003, 0.070449499999999998, 0.083713499999999996, 0.092102400000000001, 0.094187699999999999, 0.10799300000000001, 0.144146, 0.15545800000000001, 0.17380999999999999, 0.22783400000000001, 0.27262700000000001, 0.33972000000000002, 0.47714899999999999, 0.60425499999999999])
xs_exp_limits_2sigma = array('d', [0.23841899999999999, 0.208616, 0.13411100000000001, 0.104308, 0.087395399999999998, 0.074505799999999997, 0.059604600000000001, 0.059604600000000001, 0.052154100000000002, 0.0447035, 0.033527599999999998, 0.040978199999999999, 0.031426500000000003, 0.022351699999999999, 0.019164799999999999, 0.0204891, 0.018626500000000001, 0.013459499999999999, 0.0093132300000000005, 0.0080326600000000005, 0.0069849200000000004, 0.0065192599999999998, 0.0053546399999999999, 0.0046566100000000003, 0.0041909499999999997, 0.00372529, 0.0027939699999999998, 0.0025611399999999999, 0.0023283100000000001, 0.0020954799999999998, 0.00186265, 0.00609963, 0.0065384099999999997, 0.0073525500000000002, 0.0083961699999999997, 0.0105837, 0.0118041, 0.013325399999999999, 0.0146442, 0.0166538, 0.0202198, 0.021567599999999999, 0.026225999999999999, 0.032555099999999997, 0.042769500000000002, 0.049254699999999998, 0.054210599999999998, 0.065330200000000005, 0.071333099999999997, 0.077689900000000006, 0.097852999999999996, 0.118617, 0.119796, 0.13253200000000001, 0.19517399999999999, 0.18543999999999999, 0.221078, 0.279111, 0.322764, 0.40659299999999998, 0.56779199999999996, 0.74842299999999995])

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
legend.SetHeader('95% CL Upper Limits')
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
c.SaveAs('CSVL_Combined_limit_obsexp_sys_WideJets_RSG.eps')

