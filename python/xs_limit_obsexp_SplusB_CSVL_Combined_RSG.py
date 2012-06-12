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

## for running the limit code
##for i in range(0,steps+1):

  ##mass = mass_start + float(i)*mass_step

  ##masses.append(mass)
  ##masses_exp.append(mass)

  ##cmd = "./stats " + str(mass) + " " + str(BR) + " gg"
  ##print "Running: " + cmd
  ##proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  ##output = proc.communicate()[0]
  ##if proc.returncode != 0:
    ##print output
    ##sys.exit(1)
  ###print output

  ##outputlines = output.split("\n")

  ##for line in outputlines:
    ##if re.search("observed bound =", line):
      ##xs_obs_limits.append(float(line.split()[6]))
    ##if re.search("median:", line):
      ##xs_exp_limits.append(float(line.split()[1]))
    ##if re.search("1 sigma band:", line):
      ##xs_exp_limits_1sigma.append(float(line.split()[4]))
      ##xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    ##if re.search("2 sigma band:", line):
      ##xs_exp_limits_2sigma.append(float(line.split()[4]))
      ##xs_exp_limits_2sigma_up.append(float(line.split()[6]))

## for reading the limit code log files
#for i in range(0,steps+1):

  #mass = mass_start + i*mass_step

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(int(mass)) + "_" + str(BR) + "_gg.log",'r')
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
xs_obs_limits = array('d', [1.18777, 1.0565599999999999, 0.30576399999999998, 0.155527, 0.10759100000000001, 0.100947, 0.107927, 0.135515, 0.084655900000000006, 0.065122600000000003, 0.076994599999999996, 0.090357499999999993, 0.069362199999999999, 0.051866799999999998, 0.048827299999999997, 0.053701600000000002, 0.047150200000000003, 0.031871299999999998, 0.018550299999999999, 0.0129099, 0.0100804, 0.0074750900000000002, 0.0059274699999999998, 0.0051902199999999997, 0.0053258100000000003, 0.00508882, 0.00434951, 0.0042000500000000003, 0.00380935, 0.0032894, 0.0030315300000000002])
xs_exp_limits = array('d', [0.41804000000000002, 0.318523, 0.23275999999999999, 0.19078400000000001, 0.156642, 0.14079700000000001, 0.13023000000000001, 0.101983, 0.089532100000000003, 0.069972000000000006, 0.065037800000000007, 0.0508826, 0.045179200000000003, 0.0369489, 0.029345799999999998, 0.024818300000000001, 0.0221482, 0.018787999999999999, 0.016892999999999998, 0.013635400000000001, 0.0120704, 0.0102115, 0.00886785, 0.0074112900000000001, 0.0064472499999999999, 0.0059119899999999998, 0.0053026999999999996, 0.0045694999999999998, 0.0040029899999999997, 0.0034037199999999998, 0.0032527900000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.35706100000000002, 0.25857200000000002, 0.203037, 0.15987399999999999, 0.13414000000000001, 0.106376, 0.098197199999999998, 0.078212699999999996, 0.067875400000000002, 0.056340399999999999, 0.048528399999999999, 0.040703900000000001, 0.036672000000000003, 0.029547199999999999, 0.024333, 0.0209407, 0.017918199999999999, 0.0143167, 0.0129605, 0.011007100000000001, 0.0096814199999999996, 0.0079939599999999996, 0.0068659200000000002, 0.0059228500000000003, 0.00506355, 0.0045388900000000003, 0.0038820999999999999, 0.00343326, 0.0030241999999999999, 0.00265497, 0.00240967, 0.0043878500000000004, 0.0049314800000000002, 0.00547921, 0.00621091, 0.0073111900000000004, 0.0084823199999999998, 0.0102646, 0.012182200000000001, 0.0123523, 0.015579300000000001, 0.017770899999999999, 0.021242500000000001, 0.0260588, 0.024855499999999999, 0.031443100000000002, 0.036307100000000002, 0.0459624, 0.050347299999999998, 0.069412000000000001, 0.072117500000000001, 0.107001, 0.105533, 0.145537, 0.15708900000000001, 0.18851100000000001, 0.225189, 0.27494499999999999, 0.31834499999999999, 0.43064200000000002, 0.65337500000000004, 0.70157800000000003])
xs_exp_limits_2sigma = array('d', [0.31581100000000001, 0.22029599999999999, 0.18409700000000001, 0.137069, 0.105478, 0.098743999999999998, 0.081465099999999999, 0.063166600000000003, 0.054801599999999999, 0.049696400000000002, 0.039823499999999998, 0.0323296, 0.027904000000000002, 0.025436400000000001, 0.0194667, 0.016960800000000002, 0.0138006, 0.0117438, 0.0113115, 0.0092024399999999992, 0.0075176599999999998, 0.0064920400000000001, 0.0059345200000000004, 0.0051972700000000004, 0.0041656200000000001, 0.0036662700000000001, 0.00337529, 0.00305835, 0.0026612300000000001, 0.0023189399999999998, 0.0021105299999999998, 0.0060991999999999999, 0.0062732300000000003, 0.0069956200000000001, 0.0085465599999999999, 0.0098172499999999996, 0.012607200000000001, 0.012915100000000001, 0.015195, 0.020364699999999999, 0.024018399999999999, 0.022838000000000001, 0.025571199999999999, 0.0401223, 0.0396361, 0.042745999999999999, 0.050571699999999997, 0.063838599999999995, 0.078500100000000003, 0.107109, 0.109537, 0.14582600000000001, 0.16227900000000001, 0.18071300000000001, 0.259994, 0.22720399999999999, 0.33687600000000001, 0.43994299999999997, 0.53952599999999995, 0.62004300000000001, 0.93263099999999999, 1.5501799999999999])

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
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_WideJets_RSG.eps')

