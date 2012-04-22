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

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_obs_limits = array('d', [0.49890899999999999, 0.47944900000000001, 0.28042099999999998, 0.176038, 0.13312599999999999, 0.117995, 0.13362199999999999, 0.15631800000000001, 0.15501499999999999, 0.142313, 0.125303, 0.10308100000000001, 0.087036600000000006, 0.076908699999999997, 0.077139299999999994, 0.072316099999999994, 0.060379200000000001, 0.049076700000000001, 0.037243100000000001, 0.027927899999999999, 0.022338199999999999, 0.0186237, 0.016757299999999999, 0.0167566, 0.018624100000000001, 0.018547500000000001, 0.017507499999999999, 0.0167619, 0.014896400000000001, 0.0148968, 0.0139659])
xs_exp_limits = array('d', [0.43347999999999998, 0.37278299999999998, 0.29033399999999998, 0.240456, 0.211094, 0.181421, 0.153868, 0.140483, 0.13186700000000001, 0.119503, 0.114966, 0.100199, 0.084937799999999994, 0.072824200000000006, 0.070489700000000002, 0.062307099999999997, 0.053282099999999999, 0.044130999999999997, 0.037248299999999998, 0.0316631, 0.029796099999999999, 0.0269714, 0.0242128, 0.024206499999999999, 0.022679999999999999, 0.0223456, 0.020060600000000001, 0.018622400000000001, 0.0167619, 0.016756, 0.0148997])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.40289199999999997, 0.32378099999999999, 0.25146200000000002, 0.206174, 0.170373, 0.145958, 0.12643499999999999, 0.118812, 0.10423, 0.096813899999999994, 0.089271199999999995, 0.078146900000000005, 0.059522199999999997, 0.052131499999999997, 0.052115500000000002, 0.050124500000000002, 0.040933200000000003, 0.033512899999999998, 0.029782400000000001, 0.0260705, 0.024203599999999999, 0.022341400000000001, 0.020532399999999999, 0.018667699999999999, 0.018412899999999999, 0.016273099999999999, 0.0148953, 0.0148956, 0.0130335, 0.0130315, 0.013032200000000001,
0.020831700000000002, 0.021641199999999999, 0.022175500000000001, 0.023174699999999999, 0.0257059, 0.026009399999999998, 0.0270209, 0.029740200000000001, 0.032412099999999999, 0.035541200000000002, 0.038788599999999999, 0.042836399999999997, 0.046040499999999998, 0.056510299999999999, 0.068328100000000003, 0.076938199999999998, 0.088123599999999996, 0.092253600000000005, 0.10392899999999999, 0.121297, 0.139732, 0.15585099999999999, 0.16819899999999999, 0.171013, 0.18104100000000001, 0.214286, 0.235932, 0.286213, 0.32678499999999999, 0.41026299999999999, 0.47900500000000001])
xs_exp_limits_2sigma = array('d', [0.342779, 0.27800399999999997, 0.21920200000000001, 0.174901, 0.13470199999999999, 0.117689, 0.11133999999999999, 0.097324300000000002, 0.096484600000000004, 0.081572900000000004, 0.074197799999999994, 0.0593857, 0.044547700000000003, 0.041239600000000001, 0.041491500000000001, 0.033646099999999998, 0.030060699999999999, 0.0260535, 0.022325399999999999, 0.020484599999999999, 0.020479399999999998, 0.0186161, 0.016754600000000001, 0.0148862, 0.0131767, 0.0130314, 0.0113154, 0.0111685, 0.011168900000000001, 0.011169699999999999, 0.011169500000000001,
0.024498499999999999, 0.024756199999999999, 0.026853599999999998, 0.028499300000000002, 0.031082599999999998, 0.032499, 0.0322169, 0.033440499999999998, 0.037884000000000001, 0.041975899999999997, 0.048856299999999998, 0.052253000000000001, 0.0561708, 0.072081900000000004, 0.084544499999999995, 0.096368099999999998, 0.107589, 0.106682, 0.12731400000000001, 0.14841499999999999, 0.16154299999999999, 0.184721, 0.20746400000000001, 0.19911699999999999, 0.23149800000000001, 0.24889800000000001, 0.29291400000000001, 0.32680300000000001, 0.36876599999999998, 0.479744, 0.53837000000000002])

##
########################################################

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

legend = TLegend(.50,.67,.80,.80)
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
l1.DrawLatex(0.19,0.88, "RS-graviton-like, f_{b#bar{b}}=" + str(BR))
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.43, "CMS Preliminary")
l1.DrawLatex(0.19,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.20,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.19,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL 2-tag")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_2Tag_limit_obsexp_WideJets_RSG.eps')

