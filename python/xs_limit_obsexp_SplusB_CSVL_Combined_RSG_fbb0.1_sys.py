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


BR = 0.1

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
xs_obs_limits = array('d', [4.2118200000000003, 1.6541300000000001, 0.55755999999999994, 0.34149800000000002, 0.22600600000000001, 0.201904, 0.20349400000000001, 0.167043, 0.12089999999999999, 0.095278500000000002, 0.100101, 0.14135400000000001, 0.122973, 0.090197700000000006, 0.068269499999999997, 0.066832699999999995, 0.063813099999999998, 0.052602400000000001, 0.033411499999999997, 0.022763499999999999, 0.015803600000000001, 0.011833, 0.0086662800000000002, 0.0070455600000000002, 0.0062736500000000004, 0.0059306599999999999, 0.00561737, 0.0052350599999999997, 0.0049350699999999997, 0.00461809, 0.0042270800000000002])
xs_exp_limits = array('d', [0.95862000000000003, 0.64417000000000002, 0.48893500000000001, 0.37749899999999997, 0.30451400000000001, 0.24513699999999999, 0.201153, 0.16877200000000001, 0.134076, 0.10868, 0.088698600000000002, 0.076403799999999994, 0.059183699999999999, 0.052827199999999998, 0.042977500000000002, 0.036554900000000001, 0.0296172, 0.027383600000000001, 0.022863499999999998, 0.020380100000000002, 0.017330499999999999, 0.014916199999999999, 0.0131766, 0.011784899999999999, 0.00985194, 0.0082619200000000007, 0.0074617499999999996, 0.0065446100000000002, 0.0058451500000000003, 0.0051588700000000003, 0.0048868000000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.90259999999999996, 0.57547899999999996, 0.43295699999999998, 0.33155099999999998, 0.25339499999999998, 0.20496300000000001, 0.16805700000000001, 0.13469999999999999, 0.107956, 0.092256900000000003, 0.073701299999999997, 0.060578100000000003, 0.049748800000000003, 0.044142300000000002, 0.035722900000000002, 0.0301225, 0.024877, 0.021842500000000001, 0.0188855, 0.0155037, 0.0138748, 0.0124111, 0.010593200000000001, 0.0086272299999999996, 0.0072385399999999999, 0.0064130799999999998, 0.0057228899999999996, 0.0049896699999999999, 0.0044013699999999999, 0.0038900499999999999, 0.0035988999999999999, 0.0065653700000000001, 0.0070061200000000002, 0.0078419300000000004, 0.0088626599999999996, 0.010130200000000001, 0.0120169, 0.0140711, 0.015976600000000001, 0.017963799999999999, 0.021345599999999999, 0.024803700000000001, 0.0273697, 0.032944099999999997, 0.041770599999999998, 0.0434762, 0.058073, 0.064144000000000007, 0.0747945, 0.084785399999999997, 0.111595, 0.124222, 0.161604, 0.20121700000000001, 0.271534, 0.29214299999999999, 0.39366400000000001, 0.492896, 0.60609900000000005, 0.89045300000000005, 1.3520300000000001, 2.20377])
xs_exp_limits_2sigma = array('d', [0.87707500000000005, 0.54510800000000004, 0.39612799999999998, 0.285634, 0.221002, 0.17325399999999999, 0.14243800000000001, 0.115337, 0.090807200000000005, 0.069638900000000004, 0.0617913, 0.0534151, 0.0391349, 0.037799100000000002, 0.028505900000000001, 0.024601499999999998, 0.020415800000000001, 0.018429999999999998, 0.016016900000000001, 0.013867600000000001, 0.011630100000000001, 0.0089800599999999998, 0.0078480100000000007, 0.0068190200000000003, 0.00617207, 0.0058163800000000003, 0.0043296000000000003, 0.0041449099999999999, 0.0037061400000000001, 0.0033430199999999999, 0.0031119899999999998, 0.0087014199999999996, 0.0089404700000000007, 0.010448499999999999, 0.011501900000000001, 0.013494600000000001, 0.014387199999999999, 0.018122599999999999, 0.020767899999999999, 0.024672400000000001, 0.027883399999999999, 0.031332699999999998, 0.0357805, 0.0422212, 0.056217700000000002, 0.064100900000000002, 0.073914499999999994, 0.085338600000000001, 0.102149, 0.113457, 0.14396300000000001, 0.18201300000000001, 0.21795200000000001, 0.28249299999999999, 0.33883000000000002, 0.39798299999999998, 0.57666700000000004, 0.73131699999999999, 0.85119999999999996, 1.3172299999999999, 1.9366099999999999, 2.8450199999999999])

##
########################################################

m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
rsg = array('d', [0.4828E+02, 0.1862E+02, 0.8100E+01, 0.3852E+01, 0.1961E+01, 0.1053E+01, 0.5905E+00, 0.3426E+00, 0.2044E+00, 0.1248E+00, 0.7770E-01, 0.4911E-01, 0.3145E-01, 0.2036E-01, 0.1330E-01, 0.8743E-02, 0.5781E-02, 0.3840E-02, 0.2559E-02, 0.1708E-02, 0.1142E-02, 0.7635E-03, 0.5101E-03, 0.3402E-03, 0.2264E-03, 0.1501E-03, 0.9913E-04, 0.6512E-04, 0.4253E-04, 0.2759E-04, 0.1775E-04])

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

graph_rsg = TGraph(len(m_x),m_x,rsg)
graph_rsg.SetLineWidth(2)
graph_rsg.SetLineStyle(8)
graph_rsg.SetLineColor(46)

c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")

graph_rsg.Draw("L")

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

legend2 = TLegend(.50,.83,.80,.88)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
legend2.SetFillStyle(0)
legend2.SetTextFont(42)
legend2.SetTextSize(0.03)
legend2.AddEntry(graph_rsg,"RS Graviton (f_{b#bar{b}} #approx 0.1)","l")
legend2.Draw()

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
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_sys_WideJets_RSG_fbb0p1.eps')

