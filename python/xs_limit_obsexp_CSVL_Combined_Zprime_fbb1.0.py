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


BR = 1.0

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
xs_obs_limits = array('d', [0.23189299999999999, 0.21570400000000001, 0.142873, 0.089408199999999993, 0.059604600000000001, 0.055879400000000003, 0.063330200000000003, 0.068946099999999996, 0.055141500000000003, 0.047260700000000003, 0.045235699999999997, 0.041274600000000002, 0.034078700000000003, 0.028853400000000001, 0.027792399999999998, 0.028545000000000001, 0.024106300000000001, 0.017650699999999998, 0.0129011, 0.0093133699999999996, 0.0074505999999999999, 0.0055879399999999996, 0.0046566100000000003, 0.0041909499999999997, 0.0041909800000000004, 0.0039581199999999999, 0.0034924600000000002, 0.0032596399999999998, 0.0030268600000000001, 0.0025611399999999999, 0.0020954799999999998])
xs_exp_limits = array('d', [0.211867, 0.17444499999999999, 0.13428799999999999, 0.11565599999999999, 0.099118700000000004, 0.076368500000000006, 0.0684757, 0.068145899999999995, 0.056385299999999999, 0.050083500000000003, 0.042538300000000001, 0.038610800000000001, 0.032862000000000002, 0.027311200000000001, 0.027270599999999999, 0.026530999999999999, 0.023123999999999999, 0.0154284, 0.0134725, 0.0102446, 0.0088475800000000007, 0.0074508999999999999, 0.0069642200000000001, 0.0060536799999999997, 0.0054501000000000003, 0.0049948299999999996, 0.0041914600000000002, 0.0038072399999999999, 0.0034146300000000001, 0.00302681, 0.0025611399999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.17688499999999999, 0.14901200000000001, 0.104308, 0.081956399999999999, 0.070780499999999996, 0.063329899999999995, 0.052154100000000002, 0.051189400000000003, 0.0447035, 0.037252899999999999, 0.033045199999999997, 0.027939700000000001, 0.024214400000000001, 0.021420399999999999, 0.0195578, 0.018714100000000001, 0.017234300000000001, 0.012107400000000001, 0.0102446, 0.00745059, 0.0065192599999999998, 0.0055879500000000004, 0.0051222699999999999, 0.0041909499999999997, 0.00372529, 0.0034924600000000002, 0.0032596299999999999, 0.0025611599999999998, 0.0023283100000000001, 0.0020954799999999998, 0.00186265, 0.0035058400000000001, 0.0038846200000000001, 0.0043368399999999998, 0.00513409, 0.0059344100000000002, 0.0067556400000000003, 0.0076352199999999999, 0.0085171199999999996, 0.0099194799999999996, 0.0114322, 0.0129888, 0.014745400000000001, 0.016800099999999998, 0.0213952, 0.030108699999999999, 0.0332555, 0.036931499999999999, 0.037066799999999997, 0.045441500000000003, 0.053161600000000003, 0.059042299999999999, 0.062289799999999999, 0.0760628, 0.087989999999999999, 0.089423000000000002, 0.10559499999999999, 0.119324, 0.14493600000000001, 0.174263, 0.23075300000000001, 0.28071600000000002])
xs_exp_limits_2sigma = array('d', [0.11921, 0.12665999999999999, 0.089407, 0.059604600000000001, 0.052448399999999999, 0.052154100000000002, 0.041272499999999997, 0.040978199999999999, 0.0353903, 0.027939700000000001, 0.026076999999999999, 0.024214400000000001, 0.016910999999999999, 0.016763799999999999, 0.013969799999999999, 0.013112199999999999, 0.0121072, 0.0093132400000000004, 0.00745058, 0.0055879399999999996, 0.0047301899999999996, 0.0042277399999999998, 0.00372529, 0.00372529, 0.0032596299999999999, 0.0027939699999999998, 0.0025611399999999999, 0.0020954799999999998, 0.00186265, 0.00162981, 0.0013969799999999999, 0.0045503499999999999, 0.0053266700000000004, 0.0060296500000000001, 0.0070900299999999998, 0.0080610899999999999, 0.00892073, 0.010318900000000001, 0.011967800000000001, 0.0153864, 0.018273500000000002, 0.020357400000000001, 0.022432799999999999, 0.022889900000000001, 0.028448600000000001, 0.0368951, 0.044267800000000003, 0.052117999999999998, 0.052521499999999999, 0.061663599999999999, 0.067971100000000007, 0.077960600000000005, 0.076736100000000002, 0.094578700000000002, 0.12414699999999999, 0.13547699999999999, 0.13301299999999999, 0.18201000000000001, 0.184446, 0.21455199999999999, 0.31319399999999997, 0.34789900000000001])

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
l1.DrawLatex(0.50,0.80, "0, 1 and 2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_Zprime_fbb1.0.eps')

