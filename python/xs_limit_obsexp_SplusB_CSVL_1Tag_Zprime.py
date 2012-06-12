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
xs_obs_limits = array('d', [0.75467799999999996, 0.58679800000000004, 0.84500399999999998, 0.38989400000000002, 0.20621400000000001, 0.18512999999999999, 0.21431500000000001, 0.14908099999999999, 0.10109799999999999, 0.083003400000000005, 0.073210999999999998, 0.062308700000000002, 0.050050600000000001, 0.043575200000000001, 0.0372498, 0.038969799999999999, 0.034799099999999999, 0.0260472, 0.020568900000000001, 0.018407199999999999, 0.018806699999999999, 0.017017299999999999, 0.013887399999999999, 0.010777399999999999, 0.00911672, 0.0074973399999999999, 0.0063600499999999999, 0.0049948600000000003, 0.00407216, 0.00361933, 0.0031963299999999998])
xs_exp_limits = array('d', [0.78854400000000002, 0.56185499999999999, 0.41786299999999998, 0.31390400000000002, 0.26489000000000001, 0.20267299999999999, 0.19354199999999999, 0.13386400000000001, 0.112347, 0.092609999999999998, 0.073116600000000004, 0.059549999999999999, 0.048057700000000002, 0.041623399999999998, 0.036029800000000001, 0.032080900000000002, 0.0248407, 0.025233599999999998, 0.0199943, 0.0169289, 0.013228, 0.0124163, 0.0109248, 0.010164899999999999, 0.0082256599999999992, 0.0073764399999999997, 0.0061881599999999998, 0.0054734600000000003, 0.0050658200000000004, 0.0045686199999999998, 0.0043981100000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.70775500000000002, 0.49235200000000001, 0.369448, 0.26830399999999999, 0.206955, 0.16528799999999999, 0.13875100000000001, 0.11083999999999999, 0.085919999999999996, 0.073004899999999998, 0.058020700000000001, 0.050989600000000003, 0.038006900000000003, 0.032683999999999998, 0.029470799999999998, 0.025666399999999999, 0.0206667, 0.018524200000000001, 0.015886000000000001, 0.0132836, 0.0110925, 0.0098432099999999998, 0.0083327100000000001, 0.0072068699999999998, 0.0065750499999999998, 0.0059648000000000001, 0.0048410700000000003, 0.0041794199999999997, 0.0039274100000000001, 0.0035866600000000002, 0.0032385500000000002, 0.0057264799999999999, 0.0061013700000000001, 0.0067801600000000004, 0.0072474100000000001, 0.00791532, 0.0097640100000000001, 0.0123886, 0.016179099999999998, 0.0155047, 0.0201701, 0.021148199999999999, 0.0252602, 0.0288851, 0.038593799999999998, 0.039549500000000001, 0.047725200000000002, 0.056020899999999998, 0.060455099999999998, 0.072548299999999996, 0.090405799999999994, 0.114075, 0.17121700000000001, 0.18027299999999999, 0.23091900000000001, 0.29588100000000001, 0.34793099999999999, 0.449853, 0.49988300000000002, 0.88985599999999998, 1.12903, 1.6925399999999999])
xs_exp_limits_2sigma = array('d', [0.62556599999999996, 0.429564, 0.33083899999999999, 0.247141, 0.16716800000000001, 0.14250299999999999, 0.118468, 0.081595399999999998, 0.072564299999999998, 0.057190400000000002, 0.0433336, 0.038860400000000003, 0.031311199999999997, 0.02579, 0.023974100000000002, 0.021254200000000001, 0.015711800000000001, 0.0151673, 0.0131187, 0.011275200000000001, 0.0086129899999999992, 0.0079860899999999995, 0.0064874900000000003, 0.00631388, 0.0051878799999999997, 0.0046194900000000004, 0.0039945800000000002, 0.0034521700000000001, 0.0031074800000000001, 0.0027889400000000002, 0.0026132799999999999, 0.0072020299999999999, 0.0081748900000000006, 0.010789699999999999, 0.0124446, 0.0141896, 0.014900699999999999, 0.015575800000000001, 0.019296000000000001, 0.021936799999999999, 0.026258799999999999, 0.033530900000000002, 0.040870700000000003, 0.040491100000000002, 0.051690899999999998, 0.0679593, 0.069238099999999997, 0.073821899999999996, 0.094810800000000001, 0.10859000000000001, 0.13796800000000001, 0.15276500000000001, 0.211453, 0.26172699999999999, 0.30256100000000002, 0.42668699999999998, 0.48072599999999999, 0.61806799999999995, 0.753826, 1.4024399999999999, 1.76315, 2.7854999999999999])

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
l1.DrawLatex(0.18,0.89, "qq/bb, f_{b#bar{b}}=" + str(BR))
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.055)
l1.DrawLatex(0.50,0.80, "1 b-tag")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obsexp_SplusB_WideJets_Zprime.eps')

