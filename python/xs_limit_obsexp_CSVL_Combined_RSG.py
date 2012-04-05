#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
#gStyle.SetOptTitle(0)
gStyle.SetPalette(1)
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1);
gStyle.SetPadTickY(1);
#gStyle.SetPadLeftMargin(0.13);
#gStyle.SetPadRightMargin(0.07);
gStyle.SetTitleFont(42)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetLabelFont(42, "XYZ")


BR = 0.5

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


masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_obs_limits = array('d', [0.44693899999999998, 0.36168899999999998, 0.230101, 0.14036299999999999, 0.095866999999999994, 0.096397499999999997, 0.105199, 0.10696700000000001, 0.0762766, 0.055833899999999999, 0.059891300000000001, 0.065470600000000004, 0.050852099999999997, 0.038609699999999997, 0.034711600000000002, 0.034657300000000002, 0.032001000000000002, 0.0237956, 0.015835700000000001, 0.012107, 0.0088474000000000001, 0.0065191600000000004, 0.0051222400000000001, 0.0041908800000000001, 0.0044237800000000004, 0.0041909299999999998, 0.0037252800000000001, 0.00325962, 0.0030267900000000001, 0.0027939800000000002, 0.00232832])
xs_exp_limits = array('d', [0.38113200000000003, 0.29581800000000003, 0.22239400000000001, 0.18689, 0.15733900000000001, 0.12937100000000001, 0.10807700000000001, 0.10147, 0.076586299999999996, 0.065504000000000007, 0.059664000000000002, 0.060212599999999998, 0.043876400000000003, 0.037448000000000002, 0.031413400000000001, 0.0292292, 0.026024100000000001, 0.020026200000000001, 0.0139696, 0.0126982, 0.0109465, 0.0090625600000000008, 0.0079162299999999998, 0.0065195399999999999, 0.0055884899999999998, 0.0050524300000000001, 0.0041909299999999998, 0.0037252800000000001, 0.0031702100000000001, 0.0027939699999999998, 0.0023283000000000002])
masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.33558100000000002, 0.264658, 0.19157099999999999, 0.16300600000000001, 0.119531, 0.103935, 0.090314199999999997, 0.081845299999999996, 0.059537, 0.048880699999999999, 0.048413400000000002, 0.047614900000000002, 0.0353809, 0.0297971, 0.0242134, 0.023282400000000002, 0.021373900000000001, 0.0159493, 0.012106499999999999, 0.0094305099999999996, 0.0083818799999999995, 0.0069848699999999998, 0.00605347, 0.0051221399999999999, 0.0041909199999999999, 0.0037252299999999999, 0.00325961, 0.00279394, 0.0023283000000000002, 0.0020954699999999999, 0.00186264, 0.0033232100000000001, 0.0035280099999999998,
0.0040913, 0.0046937799999999998, 0.0056382100000000003, 0.0066452400000000002, 0.0075183300000000002, 0.0086986300000000006, 0.0099720599999999996, 0.0120003, 0.014371, 0.016407499999999998, 0.017667200000000001, 0.024723599999999998, 0.032406900000000002, 0.036924899999999997, 0.0399505, 0.046858499999999997, 0.0554896, 0.070878800000000006, 0.076282900000000001, 0.086662400000000001, 0.094210799999999997, 0.122032, 0.13244600000000001, 0.15820699999999999, 0.18926399999999999, 0.220443, 0.263181, 0.34615400000000002, 0.43374000000000001])
xs_exp_limits_2sigma = array('d', [0.28446900000000003, 0.221057, 0.16140299999999999, 0.117725, 0.10353999999999999, 0.088756199999999993, 0.081603400000000006, 0.066923700000000003, 0.049814900000000002, 0.042382900000000001, 0.034978299999999997, 0.031249599999999999, 0.0279324, 0.024206800000000001, 0.020483700000000001, 0.018059200000000001, 0.016000400000000001, 0.0134047, 0.0093126300000000006, 0.00745, 0.0065190500000000002, 0.00577131, 0.0048400200000000004, 0.0041908400000000004, 0.0032595699999999998, 0.0027939000000000002, 0.0025611000000000002, 0.0021431800000000002, 0.0018626300000000001, 0.0016298, 0.00146426,
0.0047726599999999997, 0.0053582300000000003, 0.0059193500000000003, 0.0060497399999999996, 0.0068986100000000003, 0.0081162100000000004, 0.0095018800000000007, 0.0125678, 0.0145086, 0.016089599999999999, 0.017717799999999999, 0.022027399999999999, 0.0205603, 0.031435200000000003, 0.041631000000000001, 0.045597600000000002, 0.044700400000000001, 0.054920200000000002, 0.071545200000000003, 0.085518499999999997, 0.094353300000000001, 0.103185, 0.118136, 0.15185499999999999, 0.16316, 0.184396, 0.21912499999999999, 0.25580700000000001, 0.31396400000000002, 0.38527299999999998, 0.482518])


graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL Combined, RSG-like resonances")
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


legend = TLegend(.45,.72,.85,.85)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(graph_obs,"Observed (F_{b#bar{b}}=" + str(BR) + ")","lp")
legend.AddEntry(graph_exp,"Expected (F_{b#bar{b}}=" + str(BR) + ")","lp")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.03)
l1.DrawLatex(0.17,0.33, "CMS Preliminary")
l1.DrawLatex(0.17,0.27, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.17,0.23, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.17,0.19, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.17,0.15, "Wide Jets")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_RSG.png')

