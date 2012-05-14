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
xs_obs_limits = array('d', [0.65935699999999997, 0.407804, 0.322689, 0.208616, 0.14901200000000001, 0.156419, 0.12822600000000001, 0.089407799999999996, 0.067055199999999995, 0.052154100000000002, 0.062838900000000003, 0.066008600000000001, 0.053057800000000002, 0.039555600000000003, 0.034931499999999997, 0.035367900000000001, 0.031046199999999999, 0.022995700000000001, 0.015953100000000001, 0.011175900000000001, 0.0083819600000000008, 0.0055879399999999996, 0.0041909499999999997, 0.0041909499999999997, 0.00372529, 0.00372529, 0.0034924600000000002, 0.0032596499999999998, 0.0030268500000000002, 0.0027939699999999998, 0.0023283100000000001])
xs_exp_limits = array('d', [0.57566700000000004, 0.40233099999999999, 0.30438199999999999, 0.23469400000000001, 0.18626499999999999, 0.15815899999999999, 0.119268, 0.0968691, 0.081959299999999999, 0.068686399999999995, 0.057952200000000002, 0.052431899999999997, 0.047501500000000002, 0.037827600000000003, 0.031664600000000001, 0.0308247, 0.0263275, 0.020127200000000001, 0.0155575, 0.012587599999999999, 0.011059299999999999, 0.0092695599999999996, 0.0078386600000000008, 0.0065193899999999999, 0.0055879900000000001, 0.0049103200000000001, 0.0043328000000000004, 0.0037252299999999999, 0.0032596399999999998, 0.0028013999999999999, 0.0025611399999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.50666699999999998, 0.357628, 0.26822099999999999, 0.193715, 0.160053, 0.12665999999999999, 0.104308, 0.084716799999999995, 0.067055299999999998, 0.055879400000000003, 0.048428800000000001, 0.0447035, 0.036770499999999998, 0.027939700000000001, 0.0249045, 0.024454799999999999, 0.021250600000000001, 0.015832499999999999, 0.0121072, 0.0102445, 0.0083819500000000009, 0.0069849200000000004, 0.0055879500000000004, 0.0050016799999999997, 0.0041909499999999997, 0.0036649899999999999, 0.0032596299999999999, 0.0027939699999999998, 0.0025611399999999999, 0.0020954799999999998, 0.00186265, 0.00346196, 0.0039890799999999999, 0.0045392899999999996, 0.0051704999999999997, 0.0055773799999999998, 0.0065752600000000003, 0.0074195700000000003, 0.0085765900000000003, 0.0099597599999999998, 0.011564400000000001, 0.013374799999999999, 0.0152009, 0.0195023, 0.0250014, 0.032318300000000001, 0.038504700000000003, 0.042437999999999997, 0.046804499999999999, 0.059651799999999998, 0.067571800000000001, 0.069652199999999997, 0.0838671, 0.099088499999999996, 0.12386, 0.14698800000000001, 0.188751, 0.229131, 0.27568500000000001, 0.35398200000000002, 0.45117099999999999, 0.63062399999999996])
xs_exp_limits_2sigma = array('d', [0.47683700000000001, 0.32782600000000001, 0.22469500000000001, 0.163913, 0.13411000000000001, 0.098034700000000002, 0.089995599999999995, 0.067349500000000007, 0.055879400000000003, 0.048428800000000001, 0.037547200000000003, 0.037252899999999999, 0.0298023, 0.022498899999999999, 0.016911099999999998, 0.015048300000000001, 0.0149012, 0.0121809, 0.0093132300000000005, 0.0075241600000000002, 0.0069849200000000004, 0.0055879399999999996, 0.0046566100000000003, 0.0041909499999999997, 0.00372529, 0.0028307499999999999, 0.0025611399999999999, 0.0020954799999999998, 0.00186265, 0.00162981, 0.00162981, 0.0043469399999999997, 0.0050433800000000001, 0.0058773000000000002, 0.0065997499999999997, 0.0079938500000000003, 0.0090077000000000004, 0.010154699999999999, 0.011062499999999999, 0.013280699999999999, 0.014268100000000001, 0.0175821, 0.020270300000000002, 0.0264771, 0.030811700000000001, 0.0391315, 0.044477200000000001, 0.049547099999999997, 0.057189400000000001, 0.070911500000000002, 0.077488699999999994, 0.086965000000000001, 0.103404, 0.13125899999999999, 0.14622399999999999, 0.17003099999999999, 0.206678, 0.25988699999999998, 0.302568, 0.420157, 0.50534400000000002, 0.71689000000000003])

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
c.SaveAs('Inclusive_limit_obsexp_WideJets_Zprime_fbb1.0.eps')

