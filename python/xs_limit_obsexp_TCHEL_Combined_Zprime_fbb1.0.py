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
xs_obs_limits = array('d', [0.454702, 0.34599800000000003, 0.24789600000000001, 0.214812, 0.13411000000000001, 0.104308, 0.089407, 0.074505799999999997, 0.059604699999999997, 0.052154199999999998, 0.068035499999999999, 0.067871600000000004, 0.052210399999999997, 0.0374542, 0.0324978, 0.034124799999999997, 0.030315700000000001, 0.021884500000000001, 0.014767499999999999, 0.0107102, 0.0074505999999999999, 0.0055879399999999996, 0.0041909699999999996, 0.00372529, 0.0037253, 0.00372529, 0.0030268000000000001, 0.0027939699999999998, 0.0025611399999999999, 0.0020954799999999998, 0.00186265])
xs_exp_limits = array('d', [0.42854399999999998, 0.32816400000000001, 0.23841899999999999, 0.20111200000000001, 0.161249, 0.13428699999999999, 0.110601, 0.094774999999999998, 0.075028600000000001, 0.0596053, 0.058742599999999999, 0.0553499, 0.044483799999999997, 0.033877200000000003, 0.028496299999999999, 0.0285784, 0.024027, 0.0184548, 0.014345500000000001, 0.0111764, 0.0097789000000000001, 0.0083818999999999994, 0.0069849200000000004, 0.0062009500000000002, 0.0055524900000000002, 0.0047083899999999998, 0.0041578199999999996, 0.0034924600000000002, 0.0030268399999999998, 0.0027939699999999998, 0.0023508600000000002])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.38744400000000001, 0.28312599999999999, 0.208616, 0.17688400000000001, 0.13411000000000001, 0.109829, 0.089407, 0.074505799999999997, 0.059604799999999999, 0.048428800000000001, 0.048428800000000001, 0.044704000000000001, 0.033527599999999998, 0.026076999999999999, 0.022351699999999999, 0.023639500000000001, 0.0199188, 0.0149012, 0.0121072, 0.00872706, 0.00745058, 0.0065192599999999998, 0.0055879399999999996, 0.0046566200000000002, 0.0037253099999999999, 0.0034924600000000002, 0.0032596299999999999, 0.0027939699999999998, 0.0023283100000000001, 0.0020954799999999998, 0.00186265, 0.0032974900000000001, 0.0036777099999999998, 0.0043145600000000003, 0.0047575200000000003, 0.0051907200000000002, 0.0061888500000000001, 0.0070634900000000004, 0.0079106300000000001, 0.0094166600000000003, 0.0105028, 0.012973999999999999, 0.014554599999999999, 0.017727199999999999, 0.023402900000000001, 0.0297165, 0.035090700000000002, 0.036868100000000001, 0.046150200000000002, 0.056452200000000001, 0.068372199999999994, 0.075759999999999994, 0.073494400000000001, 0.088353000000000001, 0.109926, 0.13095799999999999, 0.15782599999999999, 0.197988, 0.23991999999999999, 0.28304099999999999, 0.36580000000000001, 0.47824100000000003])
xs_exp_limits_2sigma = array('d', [0.35762899999999997, 0.23841899999999999, 0.193715, 0.14156099999999999, 0.119209, 0.096857499999999999, 0.081956399999999999, 0.060193200000000002, 0.052154100000000002, 0.044997799999999998, 0.040978199999999999, 0.037252899999999999, 0.0262242, 0.020783699999999999, 0.0204891, 0.018626500000000001, 0.014974700000000001, 0.0112494, 0.0083819099999999994, 0.0065192799999999997, 0.00515906, 0.0042277499999999997, 0.0041909499999999997, 0.0034924600000000002, 0.0028307499999999999, 0.00257953, 0.0021138699999999999, 0.0021138699999999999, 0.0020954799999999998, 0.00186265, 0.0014153799999999999, 0.0045118600000000003, 0.0050443500000000004, 0.0052392999999999997, 0.0061561200000000002, 0.0069854100000000001, 0.0081029599999999993, 0.0091821000000000003, 0.0102287, 0.0108489, 0.0125235, 0.0150846, 0.0173519, 0.022245000000000001, 0.028969999999999999, 0.034554700000000001, 0.0457896, 0.045602900000000002, 0.053655899999999999, 0.0675843, 0.078901700000000005, 0.092382800000000001, 0.086663799999999999, 0.109027, 0.13828399999999999, 0.153199, 0.179342, 0.23100200000000001, 0.29827399999999998, 0.32129000000000002, 0.405777, 0.50067899999999999])

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

