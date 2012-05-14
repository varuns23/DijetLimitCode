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
xs_obs_limits = array('d', [0.89414899999999997, 0.65586800000000001, 0.55800000000000005, 0.420846, 0.25332100000000002, 0.208616, 0.20999399999999999, 0.17535700000000001, 0.12665999999999999, 0.096857600000000002, 0.089407700000000007, 0.076122800000000004, 0.059604699999999997, 0.052154100000000002, 0.044703699999999999, 0.043428899999999999, 0.039156499999999997, 0.032226400000000002, 0.025870500000000001, 0.023134200000000001, 0.020968199999999999, 0.0189772, 0.015819, 0.013831, 0.0119985, 0.0099084800000000008, 0.0083819099999999994, 0.0065192599999999998, 0.0055879399999999996, 0.0046566200000000002, 0.0041909499999999997])
xs_exp_limits = array('d', [0.92388899999999996, 0.65566199999999997, 0.48404799999999998, 0.39074799999999998, 0.29802299999999998, 0.22351699999999999, 0.20505699999999999, 0.159585, 0.119209, 0.104308, 0.089408199999999993, 0.074507900000000002, 0.057742000000000002, 0.052154100000000002, 0.0447035, 0.041498500000000001, 0.034412400000000003, 0.029914900000000001, 0.025804899999999999, 0.021420700000000001, 0.019764500000000001, 0.017849, 0.0147815, 0.0132946, 0.011618699999999999, 0.0095733499999999996, 0.0076834900000000003, 0.0069849700000000001, 0.0065192599999999998, 0.0063000699999999996, 0.00577964])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.77486100000000002, 0.50663999999999998, 0.41723399999999999, 0.34273100000000001, 0.22351699999999999, 0.178816, 0.163913, 0.119209, 0.096857499999999999, 0.081956399999999999, 0.067055199999999995, 0.055879400000000003, 0.048428800000000001, 0.037253099999999997, 0.034907899999999999, 0.031664999999999999, 0.026076999999999999, 0.024214400000000001, 0.0204891, 0.016281400000000001, 0.0149012, 0.013969799999999999, 0.011866, 0.0102446, 0.0087269900000000004, 0.00745058, 0.0065192599999999998, 0.0055879399999999996, 0.0051222699999999999, 0.0046566100000000003, 0.0041909499999999997, 0.0075619399999999996, 0.0077393699999999998, 0.00844431, 0.0090048300000000001, 0.0101145, 0.012489800000000001, 0.015361100000000001, 0.017018800000000001, 0.019080900000000001, 0.023017599999999999, 0.0261283, 0.028381400000000001, 0.033450899999999999, 0.0382254, 0.045865999999999997, 0.052546500000000003, 0.057502999999999999, 0.065816200000000005, 0.076571100000000003, 0.0915691, 0.113723, 0.13602400000000001, 0.15268300000000001, 0.19770099999999999, 0.25089600000000001, 0.300367, 0.36655599999999999, 0.47461199999999998, 0.588889, 0.73504899999999995, 1.0138199999999999])
xs_exp_limits_2sigma = array('d', [0.59604599999999996, 0.36233700000000002, 0.32782600000000001, 0.26822099999999999, 0.16508999999999999, 0.14901200000000001, 0.111759, 0.104308, 0.081956399999999999, 0.060193200000000002, 0.045292100000000002, 0.048723099999999998, 0.037252899999999999, 0.0298023, 0.022645999999999999, 0.0262242, 0.022498899999999999, 0.018626500000000001, 0.016763799999999999, 0.0131121, 0.011175900000000001, 0.0121808, 0.0083818999999999994, 0.0083818999999999994, 0.00745058, 0.0055879399999999996, 0.0055879399999999996, 0.0046566100000000003, 0.00372529, 0.00372529, 0.00372529, 0.0092335500000000001, 0.0099225500000000005, 0.012519600000000001, 0.0138566, 0.015326299999999999, 0.016532499999999999, 0.018359500000000001, 0.022951800000000001, 0.024867899999999998, 0.0309018, 0.0337808, 0.034455600000000003, 0.042879899999999999, 0.045943400000000002, 0.054043000000000001, 0.063940300000000005, 0.073314400000000002, 0.089927099999999996, 0.104494, 0.12041399999999999, 0.13223799999999999, 0.163712, 0.194244, 0.23447499999999999, 0.29205799999999998, 0.34052199999999999, 0.42341699999999999, 0.56260699999999997, 0.70239200000000002, 0.81906000000000001, 1.1574199999999999])

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
l1.DrawLatex(0.50,0.80, "1 b-tag")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obsexp_WideJets_RSG.eps')

