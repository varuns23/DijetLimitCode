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
xs_obs_limits = array('d', [0.50142500000000001, 0.40581899999999999, 0.28312199999999998, 0.254025, 0.17136299999999999, 0.119209, 0.089407, 0.081956399999999999, 0.0856817, 0.093821600000000005, 0.109816, 0.091383300000000001, 0.064454800000000007, 0.043851599999999998, 0.035754899999999999, 0.038026600000000001, 0.033888399999999999, 0.026454600000000002, 0.0187954, 0.013969799999999999, 0.0102446, 0.00745058, 0.0069849200000000004, 0.0069849200000000004, 0.0065193300000000003, 0.0060536000000000001, 0.0051223299999999996, 0.0041909499999999997, 0.0032596299999999999, 0.0032596299999999999, 0.0027939699999999998])
xs_exp_limits = array('d', [0.47062100000000001, 0.37073800000000001, 0.283302, 0.235375, 0.196435, 0.159771, 0.13608100000000001, 0.113358, 0.092980900000000005, 0.086192900000000003, 0.088631000000000001, 0.071140900000000007, 0.052936900000000002, 0.043847299999999999, 0.037527400000000002, 0.033961600000000002, 0.028590600000000001, 0.0238616, 0.018418299999999999, 0.0149444, 0.013302899999999999, 0.011267299999999999, 0.0102446, 0.0088476400000000004, 0.0078916200000000002, 0.0069853600000000004, 0.0060973499999999996, 0.0055880900000000004, 0.0048958300000000003, 0.0044237900000000004, 0.0037253099999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.41723399999999999, 0.32782800000000001, 0.23841899999999999, 0.193715, 0.14901200000000001, 0.13411100000000001, 0.111759, 0.096857499999999999, 0.074505799999999997, 0.069816000000000003, 0.068299399999999996, 0.055879499999999999, 0.044221400000000001, 0.033527800000000003, 0.0274574, 0.027939700000000001, 0.024214400000000001, 0.0183853, 0.0139699, 0.0121072, 0.011175900000000001, 0.0093132300000000005, 0.0083818999999999994, 0.0069849200000000004, 0.0060537000000000004, 0.0055879399999999996, 0.0046566100000000003, 0.0041909499999999997, 0.00372529, 0.0034924600000000002, 0.0032596299999999999, 0.0052470199999999998, 0.0060419899999999997, 0.0066798099999999996, 0.0074810700000000003, 0.0085069599999999992, 0.0092633100000000003, 0.0103766, 0.011840399999999999, 0.0134257, 0.0152453, 0.017340399999999999, 0.019976399999999998, 0.022273000000000001, 0.030929700000000001, 0.037382699999999998, 0.043272100000000001, 0.0457153, 0.053910199999999998, 0.069646200000000005, 0.0931815, 0.10977099999999999, 0.110207, 0.107534, 0.13464599999999999, 0.157004, 0.19817100000000001, 0.22972799999999999, 0.265426, 0.31605800000000001, 0.41083900000000001, 0.52137500000000003])
xs_exp_limits_2sigma = array('d', [0.38743100000000003, 0.29802299999999998, 0.22351699999999999, 0.163913, 0.14156099999999999, 0.119209, 0.096857600000000002, 0.081956399999999999, 0.0601941, 0.052154100000000002, 0.055879400000000003, 0.048428800000000001, 0.0298024, 0.026077099999999999, 0.022351800000000002, 0.0204891, 0.0170581, 0.0149012, 0.0121808, 0.011175900000000001, 0.0093868000000000007, 0.00745058, 0.0065192599999999998, 0.0055879399999999996, 0.0051222799999999999, 0.0041909499999999997, 0.00372529, 0.00329642, 0.0032596299999999999, 0.0027939699999999998, 0.0027939699999999998, 0.0064582800000000003, 0.0071565700000000001, 0.0077368899999999997, 0.0084662599999999998, 0.0096574199999999999, 0.0106856, 0.012893699999999999, 0.014112700000000001, 0.016863900000000001, 0.019391200000000001, 0.021727799999999999, 0.0248934, 0.027541, 0.039111100000000003, 0.0472968, 0.051854699999999997, 0.053866400000000002, 0.062922400000000003, 0.087646000000000002, 0.10929899999999999, 0.12979099999999999, 0.12776799999999999, 0.13692099999999999, 0.14908299999999999, 0.190191, 0.22772800000000001, 0.27726800000000001, 0.30751499999999998, 0.36516900000000002, 0.48760399999999998, 0.577349])

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
c.SaveAs('TCHEL_Combined_limit_obsexp_WideJets_Zprime_fbb1.0.eps')

