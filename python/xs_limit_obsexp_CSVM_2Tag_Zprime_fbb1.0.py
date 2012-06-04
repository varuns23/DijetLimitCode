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
xs_obs_limits = array('d', [0.200239, 0.20419300000000001, 0.16483300000000001, 0.14266799999999999, 0.081956399999999999, 0.059604900000000002, 0.059604799999999999, 0.059604600000000001, 0.067055199999999995, 0.078239600000000006, 0.098421800000000004, 0.096363500000000005, 0.083772100000000002, 0.064931900000000001, 0.048428800000000001, 0.0447035, 0.0447035, 0.037253000000000001, 0.037252899999999999, 0.037252899999999999, 0.037252899999999999, 0.037252899999999999, 0.042058999999999999, 0.043184300000000002, 0.046155000000000002, 0.050916200000000002, 0.051430299999999998, 0.055376700000000001, 0.055751299999999997, 0.059577100000000001, 0.063847799999999996])
xs_exp_limits = array('d', [0.18832699999999999, 0.16728499999999999, 0.14446899999999999, 0.12576699999999999, 0.104308, 0.095136899999999996, 0.091980900000000004, 0.081961300000000001, 0.081543099999999993, 0.080988000000000004, 0.096234700000000006, 0.087099499999999996, 0.080792600000000006, 0.056304100000000003, 0.052666200000000003, 0.048469100000000001, 0.045097499999999999, 0.0447035, 0.041127499999999997, 0.0387097, 0.037252899999999999, 0.037252899999999999, 0.037254099999999998, 0.0423404, 0.0447035, 0.045686299999999999, 0.049987900000000002, 0.051667400000000002, 0.054117600000000002, 0.055552200000000003, 0.059604600000000001])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.16391700000000001, 0.14156099999999999, 0.11921, 0.104308, 0.089407, 0.074506100000000006, 0.070780800000000005, 0.059604600000000001, 0.059604999999999998, 0.063329899999999995, 0.074505799999999997, 0.070780499999999996, 0.063329999999999997, 0.0447035, 0.0447035, 0.040978199999999999, 0.037252899999999999, 0.036099699999999998, 0.033527599999999998, 0.0298023, 0.0298023, 0.0298023, 0.0298023, 0.0298023, 0.033527599999999998, 0.0298023, 0.036288099999999997, 0.037252899999999999, 0.040978199999999999, 0.040978199999999999, 0.0447035, 0.079239699999999996, 0.073506600000000005, 0.068316399999999999, 0.064942, 0.065964999999999996, 0.063500299999999996, 0.058063299999999998, 0.056495400000000001, 0.047017200000000002, 0.046202600000000003, 0.047500399999999998, 0.049411799999999999, 0.0496896, 0.054332100000000001, 0.058964599999999999, 0.062661499999999995, 0.067028099999999993, 0.074451500000000004, 0.10294499999999999, 0.104515, 0.115603, 0.10248699999999999, 0.10591200000000001, 0.112577, 0.107629, 0.113375, 0.13245399999999999, 0.158247, 0.16756599999999999, 0.19609599999999999, 0.20763899999999999])
xs_exp_limits_2sigma = array('d', [0.14901200000000001, 0.12665999999999999, 0.104308, 0.089995599999999995, 0.074505799999999997, 0.060193200000000002, 0.052154100000000002, 0.045292100000000002, 0.052154100000000002, 0.052154100000000002, 0.055879400000000003, 0.0561737, 0.052448399999999999, 0.037252899999999999, 0.033527599999999998, 0.0298023, 0.0263713, 0.026076999999999999, 0.026076999999999999, 0.026076999999999999, 0.026076999999999999, 0.026076999999999999, 0.0263713, 0.0298023, 0.0298023, 0.0298023, 0.0298023, 0.0298023, 0.037252899999999999, 0.037252899999999999, 0.040978199999999999, 0.097804600000000005, 0.093984200000000004, 0.089842500000000006, 0.091135599999999997, 0.079810699999999998, 0.079143199999999997, 0.074252600000000002, 0.067880700000000002, 0.062794600000000006, 0.0580192, 0.056054800000000002, 0.058163199999999998, 0.060875100000000001, 0.063520800000000002, 0.0682228, 0.071992399999999998, 0.077671599999999993, 0.088263800000000003, 0.115671, 0.12545300000000001, 0.13908999999999999, 0.12037399999999999, 0.13172200000000001, 0.129719, 0.136215, 0.13264999999999999, 0.146316, 0.18643799999999999, 0.20844299999999999, 0.21954499999999999, 0.234763])

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
c.SaveAs('CSVM_Combined_limit_obsexp_WideJets_Zprime_fbb1.0.eps')

