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
xs_obs_limits = array('d', [2.3970400000000001, 0.55914799999999998, 0.41513600000000001, 0.30263299999999999, 0.28721999999999998, 0.36632599999999998, 0.16723199999999999, 0.109402, 0.083221400000000001, 0.070849899999999993, 0.123665, 0.13082299999999999, 0.085431800000000002, 0.059068200000000001, 0.053275099999999999, 0.056575899999999998, 0.047436699999999998, 0.031457600000000002, 0.019466399999999998, 0.013558799999999999, 0.0095207699999999996, 0.0066265400000000002, 0.0050254000000000002, 0.0047861800000000001, 0.0049607499999999999, 0.0049728000000000003, 0.0050108499999999999, 0.0051881599999999998, 0.0052490999999999996, 0.0048159800000000001, 0.00413014])
xs_exp_limits = array('d', [0.80873099999999998, 0.59795799999999999, 0.45289499999999999, 0.35319800000000001, 0.27471800000000002, 0.22443399999999999, 0.196302, 0.14796500000000001, 0.114262, 0.090267799999999995, 0.077769400000000002, 0.060296599999999999, 0.052429000000000003, 0.042957099999999998, 0.036516300000000002, 0.028848800000000001, 0.025002, 0.021925300000000002, 0.0192587, 0.0160736, 0.0140576, 0.011939399999999999, 0.0107292, 0.0089249900000000007, 0.0081441299999999994, 0.0067559300000000003, 0.0060282900000000004, 0.0051341099999999999, 0.0042208799999999998, 0.0039322899999999997, 0.00351915])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.739846, 0.51393900000000003, 0.387679, 0.296732, 0.228273, 0.19269, 0.14652599999999999, 0.108991, 0.086305800000000002, 0.0674429, 0.059359000000000002, 0.0499128, 0.039728399999999997, 0.034013700000000001, 0.028963200000000001, 0.0246731, 0.019904100000000001, 0.017536199999999998, 0.014940699999999999, 0.0126143, 0.0108328, 0.0094469099999999993, 0.0081994600000000004, 0.0068272599999999999, 0.0060850499999999998, 0.0050990699999999998, 0.0043024500000000002, 0.0037926399999999999, 0.0033511999999999999, 0.0031646500000000002, 0.00285462, 0.0045135799999999997, 0.0057108300000000001, 0.0058658, 0.0068676299999999996, 0.0083713999999999993, 0.0096272700000000003, 0.0113647, 0.013165, 0.0164009, 0.017988799999999999, 0.021398, 0.025393700000000002, 0.029030899999999998, 0.039072599999999999, 0.039338499999999998, 0.048907899999999997, 0.055473300000000003, 0.065316700000000005, 0.077329300000000004, 0.094357999999999997, 0.115133, 0.14415900000000001, 0.189385, 0.28434300000000001, 0.31454100000000002, 0.34814800000000001, 0.45956399999999997, 0.52690099999999995, 0.78262299999999996, 1.2401500000000001, 1.79227])
xs_exp_limits_2sigma = array('d', [0.66697799999999996, 0.465864, 0.29387000000000002, 0.23236200000000001, 0.177123, 0.14588000000000001, 0.115757, 0.084995600000000004, 0.071099300000000004, 0.054528100000000003, 0.049499399999999999, 0.036709600000000002, 0.033130699999999999, 0.027294700000000002, 0.0254145, 0.019440700000000002, 0.0173064, 0.0140362, 0.013363999999999999, 0.0097143699999999999, 0.0085168699999999993, 0.0082769999999999996, 0.0067028799999999996, 0.0051724199999999996, 0.0043211999999999999, 0.00422932, 0.0037257200000000001, 0.0033725299999999999, 0.0025468299999999999, 0.00241953, 0.00250578, 0.0058134299999999996, 0.0072133500000000003, 0.0081140099999999996, 0.0085367399999999993, 0.0106284, 0.013544199999999999, 0.0168413, 0.0205627, 0.021474300000000002, 0.024238300000000001, 0.032050200000000001, 0.042407599999999997, 0.046267500000000003, 0.049464300000000003, 0.054915199999999997, 0.072745099999999993, 0.066453700000000004, 0.088245000000000004, 0.098296999999999995, 0.133741, 0.15912200000000001, 0.19650699999999999, 0.26877000000000001, 0.372392, 0.46378200000000003, 0.460899, 0.62878100000000003, 0.82667000000000002, 1.1792199999999999, 2.26736, 3.43933])

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
l1.DrawLatex(0.18,0.89, "qq/bb, f_{b#bar{b}}=" + str(BR))
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
c.SaveAs('CSVL_0Tag_limit_obsexp_SplusB_WideJets_Zprime.eps')

