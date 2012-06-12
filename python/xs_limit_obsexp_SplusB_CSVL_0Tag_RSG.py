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
xs_obs_limits = array('d', [7.9084599999999998, 1.0408999999999999, 0.75112900000000005, 0.51186500000000001, 0.407723, 0.57094800000000001, 0.32891100000000001, 0.20019600000000001, 0.14044599999999999, 0.10757700000000001, 0.12765499999999999, 0.21018100000000001, 0.16479099999999999, 0.108873, 0.086758299999999997, 0.085432999999999995, 0.077850699999999995, 0.056861599999999998, 0.034578499999999998, 0.0232851, 0.0166269, 0.0116968, 0.0082666900000000001, 0.0071024699999999996, 0.0071609000000000004, 0.0070475199999999998, 0.00653047, 0.0072489399999999997, 0.00723005, 0.00670413, 0.0063935399999999996])
xs_exp_limits = array('d', [1.55643, 1.02197, 0.76786600000000005, 0.59402500000000003, 0.45254100000000003, 0.35213899999999998, 0.292439, 0.217196, 0.19417799999999999, 0.14715, 0.11704100000000001, 0.0943721, 0.080771300000000004, 0.070768899999999996, 0.057498100000000003, 0.048724799999999999, 0.040978000000000001, 0.032779999999999997, 0.027985699999999999, 0.024382299999999999, 0.022120999999999998, 0.0178922, 0.0162484, 0.0140073, 0.0121791, 0.0103775, 0.0088575300000000006, 0.0075273800000000002, 0.0067754199999999999, 0.0062236599999999998, 0.0057062099999999998])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [1.40933, 0.92853699999999995, 0.67735100000000004, 0.49389100000000002, 0.39364399999999999, 0.29532000000000003, 0.23757700000000001, 0.19481299999999999, 0.139816, 0.11403199999999999, 0.092962799999999998, 0.073686199999999993, 0.0672122, 0.056527300000000003, 0.048250099999999997, 0.038665499999999998, 0.031987000000000002, 0.026205200000000001, 0.0234007, 0.019648599999999999, 0.016280599999999999, 0.014545000000000001, 0.012886, 0.011170100000000001, 0.0095006499999999994, 0.0078638600000000003, 0.0067491900000000004, 0.0059033699999999998, 0.0054865299999999999, 0.0048093099999999998, 0.0044085399999999999, 0.0072174500000000003, 0.0080459399999999997, 0.0093033200000000003, 0.010603, 0.013474399999999999, 0.014941299999999999, 0.017506799999999999, 0.0209943, 0.025421099999999999, 0.029519799999999999, 0.035138999999999997, 0.041204200000000003, 0.048703299999999998, 0.056816499999999999, 0.064613400000000001, 0.075876600000000002, 0.085635199999999995, 0.11358, 0.13850000000000001, 0.149057, 0.18571499999999999, 0.23544100000000001, 0.38068299999999999, 0.45700400000000002, 0.48607699999999998, 0.60058, 0.76153899999999997, 1.0905, 1.62642, 2.7348300000000001, 4.9698900000000004])
xs_exp_limits_2sigma = array('d', [1.3070900000000001, 0.83520799999999995, 0.56653299999999995, 0.43129600000000001, 0.33627600000000002, 0.25731999999999999, 0.20627799999999999, 0.14923, 0.124234, 0.098078799999999994, 0.073968400000000004, 0.063892599999999994, 0.056213399999999997, 0.048217500000000003, 0.036858000000000002, 0.033341099999999999, 0.027663900000000002, 0.022527999999999999, 0.019241500000000002, 0.0155158, 0.0136049, 0.012885300000000001, 0.0113629, 0.0086050799999999993, 0.00710329, 0.0064631899999999997, 0.00570193, 0.0040718899999999999, 0.0043670799999999997, 0.0040590499999999998, 0.0038150699999999998, 0.0093720100000000001, 0.010851100000000001, 0.0123316, 0.012594299999999999, 0.017364299999999999, 0.021323600000000002, 0.027473399999999999, 0.0302756, 0.033853599999999998, 0.043444099999999999, 0.056606499999999997, 0.071444400000000005, 0.066759499999999999, 0.080797400000000005, 0.093747999999999998, 0.10501099999999999, 0.12313, 0.18400900000000001, 0.19747700000000001, 0.25080799999999998, 0.24904200000000001, 0.34654499999999999, 0.49810700000000002, 0.65844100000000005, 0.71179800000000004, 0.920323, 1.09389, 1.71387, 2.4390700000000001, 4.4524900000000001, 8.0494599999999998])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,20)
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
l1.DrawLatex(0.50,0.80, "0 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obsexp_SplusB_WideJets_RSG.eps')

