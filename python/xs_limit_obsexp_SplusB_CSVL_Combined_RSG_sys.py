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
xs_obs_limits = array('d', [1.28007, 1.1842699999999999, 0.367566, 0.192186, 0.119537, 0.10804, 0.114817, 0.13850999999999999, 0.098569799999999999, 0.075354599999999994, 0.081570000000000004, 0.091896099999999994, 0.077500299999999994, 0.060370100000000003, 0.052438199999999997, 0.054162200000000001, 0.050496100000000002, 0.040505100000000002, 0.026117100000000001, 0.018084599999999999, 0.013157500000000001, 0.0092849600000000001, 0.0073081800000000001, 0.0058640000000000003, 0.0052933700000000004, 0.0049809800000000003, 0.0046586700000000002, 0.0042748999999999999, 0.0039435299999999998, 0.0036223100000000001, 0.0034042199999999999])
xs_exp_limits = array('d', [0.440994, 0.34998699999999999, 0.27173000000000003, 0.21809100000000001, 0.180034, 0.14833399999999999, 0.13386600000000001, 0.106514, 0.092760400000000007, 0.076925099999999996, 0.065739900000000004, 0.054181100000000003, 0.045620399999999998, 0.040349299999999998, 0.033154000000000003, 0.027929099999999998, 0.024542499999999998, 0.022678899999999998, 0.018492499999999999, 0.0155476, 0.013814399999999999, 0.0123325, 0.0107601, 0.0091562399999999995, 0.0077484099999999998, 0.0068576799999999997, 0.0061747399999999997, 0.0054503800000000003, 0.0048219300000000003, 0.0040332099999999997, 0.0036583000000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.421155, 0.298761, 0.24068700000000001, 0.193102, 0.14782300000000001, 0.122099, 0.10549, 0.091769100000000006, 0.074103000000000002, 0.061994800000000003, 0.052280300000000002, 0.045176899999999999, 0.036279400000000003, 0.032445300000000003, 0.026644600000000001, 0.023305099999999999, 0.019342000000000002, 0.017682699999999999, 0.014821600000000001, 0.0127598, 0.0111418, 0.0098598999999999996, 0.0082790899999999994, 0.0071230499999999997, 0.0062052000000000001, 0.00521705, 0.00457823, 0.00398161, 0.0035544000000000001, 0.0030060600000000001, 0.00282271, 0.0049998899999999999, 0.0054874299999999997, 0.0062067800000000003, 0.0071145499999999999, 0.0083412199999999999, 0.00957882, 0.0111973, 0.012432800000000001, 0.0146496, 0.017355700000000002, 0.019175500000000002, 0.0218181, 0.026986, 0.032091700000000001, 0.0347494, 0.040970100000000002, 0.051187299999999998, 0.056688500000000003, 0.064920000000000005, 0.076178599999999999, 0.097921999999999995, 0.111857, 0.13999700000000001, 0.16456899999999999, 0.20028799999999999, 0.237014, 0.29949199999999998, 0.33601799999999998, 0.44289200000000001, 0.60294000000000003, 0.829484])
xs_exp_limits_2sigma = array('d', [0.40967500000000001, 0.26647100000000001, 0.21495400000000001, 0.16745199999999999, 0.118996, 0.105724, 0.089118600000000006, 0.077897800000000003, 0.060982799999999997, 0.052549400000000003, 0.044213299999999997, 0.035762299999999997, 0.028986499999999998, 0.027305699999999999, 0.0221178, 0.018266899999999999, 0.0165988, 0.0145925, 0.012707, 0.0104124, 0.0087638899999999999, 0.0075136400000000002, 0.0065824500000000001, 0.0057628499999999999, 0.0050197200000000001, 0.0042156800000000003, 0.0035930100000000002, 0.0028634300000000001, 0.0025512899999999999, 0.0025477199999999998, 0.0023641399999999998, 0.0069969799999999999, 0.0079867600000000007, 0.00885383, 0.00977833, 0.0106452, 0.0118058, 0.0146296, 0.016024900000000002, 0.020168700000000001, 0.021318199999999999, 0.023354, 0.027903299999999999, 0.037067000000000003, 0.039010000000000003, 0.044553700000000002, 0.062622700000000003, 0.066350999999999993, 0.078320100000000004, 0.088825299999999996, 0.107581, 0.13328699999999999, 0.15464600000000001, 0.18812100000000001, 0.22075900000000001, 0.26645400000000002, 0.28184799999999999, 0.42444500000000002, 0.51239100000000004, 0.67269100000000004, 0.85950800000000005, 1.36775])

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
l1.DrawLatex(0.18,0.89, "gg/bb, f_{b#bar{b}}=" + str(BR))
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
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_sys_WideJets_RSG.eps')

