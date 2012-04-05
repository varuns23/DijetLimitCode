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


#masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_obs_limits = array('d', [0.497419, 0.44541999999999998, 0.265345, 0.160297, 0.11683399999999999, 0.117953, 0.13366900000000001, 0.16183500000000001, 0.15035999999999999, 0.136351, 0.11988, 0.10208299999999999, 0.086324700000000004, 0.073954599999999995, 0.076249300000000006, 0.069350200000000001, 0.0571908, 0.045409900000000003, 0.035387099999999998, 0.026066800000000001, 0.0204767, 0.016752599999999999, 0.016758800000000001, 0.0167578, 0.0186254, 0.018399599999999999, 0.016989799999999999, 0.014896899999999999, 0.014897499999999999, 0.0148998, 0.0130323])
xs_exp_limits = array('d', [0.41603800000000002, 0.34290500000000002, 0.28102899999999997, 0.23049, 0.20103499999999999, 0.17646999999999999, 0.154362, 0.14907100000000001, 0.14091500000000001, 0.12646099999999999, 0.1143, 0.097321400000000002, 0.085272799999999996, 0.069825200000000004, 0.065616900000000006, 0.0619023, 0.050248599999999997, 0.037237899999999997, 0.033523200000000003, 0.029799599999999999, 0.027013800000000001, 0.0257626, 0.023683200000000001, 0.020487399999999999, 0.0204791, 0.018625800000000001, 0.018622099999999999, 0.016759799999999998, 0.016758200000000001, 0.014899000000000001, 0.014894599999999999])
masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.35250199999999998, 0.29341600000000001, 0.23494300000000001, 0.19107199999999999, 0.17677599999999999, 0.14809, 0.12418, 0.118979, 0.11171200000000001, 0.100494, 0.096827899999999995, 0.074495800000000001, 0.059565399999999998, 0.0521188, 0.052125600000000001, 0.048418299999999997, 0.037232399999999999, 0.029778800000000001, 0.026073599999999999, 0.024201, 0.022329499999999999, 0.020480499999999999, 0.018376900000000002, 0.0167584, 0.016754499999999999, 0.014895200000000001, 0.0139665, 0.013030999999999999, 0.013029900000000001, 0.0130308, 0.013028, 0.020097500000000001,
0.020886800000000001, 0.021635100000000001, 0.021872200000000001, 0.022868800000000002, 0.024341399999999999, 0.024875499999999998, 0.026991500000000002, 0.0279423, 0.030132599999999999, 0.033305599999999998, 0.037946899999999999, 0.042224200000000003, 0.053017599999999998, 0.063009700000000002, 0.081302200000000005, 0.081036800000000006, 0.093583200000000005, 0.102186, 0.114519, 0.14256199999999999, 0.16416, 0.18609999999999999, 0.17837700000000001, 0.18207200000000001, 0.20769000000000001, 0.23266300000000001, 0.28057599999999999, 0.30850899999999998, 0.393069, 0.46870099999999998])
xs_exp_limits_2sigma = array('d', [0.309365, 0.229351, 0.20400199999999999, 0.161468, 0.13319, 0.13344, 0.103671, 0.096324099999999996, 0.089954099999999995, 0.081602999999999995, 0.074249999999999997, 0.059467899999999997, 0.044882499999999999, 0.041238999999999998, 0.040939200000000002, 0.033500000000000002, 0.026350100000000001, 0.022612899999999998, 0.020625600000000001, 0.018762000000000001, 0.016754100000000001, 0.016754600000000001, 0.016752300000000001, 0.014889599999999999, 0.0130303, 0.013030099999999999, 0.011169, 0.0111691, 0.011169200000000001, 0.0111691, 0.0111681,
0.023688799999999999, 0.0242618, 0.025405299999999999, 0.026248199999999999, 0.028028500000000001, 0.0295635, 0.030343200000000001, 0.0308779, 0.035011300000000002, 0.039059700000000003, 0.044993499999999999, 0.048889000000000002, 0.052095099999999998, 0.067479499999999998, 0.077891500000000002, 0.097621299999999994, 0.10059899999999999, 0.11525299999999999, 0.124433, 0.14094699999999999, 0.15973000000000001, 0.193772, 0.22320000000000001, 0.230881, 0.247784, 0.2646, 0.278534, 0.32236100000000001, 0.355076, 0.44351800000000002, 0.52138799999999996])



graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL 2-tag, RSG-like resonances")
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
c.SaveAs('CSVL_2Tag_limit_obsexp_WideJets_RSG.png')

