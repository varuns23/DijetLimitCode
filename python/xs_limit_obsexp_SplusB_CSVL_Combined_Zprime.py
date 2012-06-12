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

  ##cmd = "./stats " + str(mass) + " " + str(BR) + " qq"
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

  #log_file = open("stats_" + str(int(mass)) + "_" + str(BR) + "_qq.log",'r')
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
xs_obs_limits = array('d', [1.0946800000000001, 0.76459699999999997, 0.22778000000000001, 0.12812100000000001, 0.095530799999999999, 0.0988319, 0.092431600000000003, 0.081632499999999997, 0.058480200000000003, 0.049614800000000001, 0.076134900000000005, 0.073108599999999996, 0.048631199999999999, 0.035808800000000002, 0.036747500000000002, 0.0420127, 0.033803899999999998, 0.020277199999999999, 0.012253200000000001, 0.0090612899999999996, 0.00661912, 0.00490407, 0.0038571299999999998, 0.0037078900000000001, 0.0038175700000000002, 0.0036000200000000002, 0.0032749200000000002, 0.0030875899999999999, 0.0027491400000000002, 0.0023425400000000002, 0.0019850800000000002])
xs_exp_limits = array('d', [0.35422399999999998, 0.28620099999999998, 0.20708299999999999, 0.161108, 0.13251299999999999, 0.117302, 0.101414, 0.082345500000000002, 0.073736200000000002, 0.053364399999999999, 0.051686700000000002, 0.037935000000000003, 0.031264599999999997, 0.0284435, 0.023755100000000001, 0.019333699999999999, 0.0172677, 0.0126905, 0.012134799999999999, 0.010438299999999999, 0.0090076600000000007, 0.0073799599999999996, 0.0064372500000000003, 0.0054594500000000002, 0.0046973600000000003, 0.0041725699999999996, 0.0036559800000000001, 0.0032034699999999999, 0.0028413000000000002, 0.0024087399999999999, 0.0021725199999999998])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.30835800000000002, 0.225353, 0.18213399999999999, 0.13061700000000001, 0.11165799999999999, 0.093836500000000003, 0.081489500000000006, 0.065467999999999998, 0.054778, 0.044065100000000003, 0.036540599999999999, 0.029758300000000001, 0.025003600000000001, 0.0232131, 0.0181902, 0.015138800000000001, 0.0131509, 0.0100608, 0.0090198899999999992, 0.0077824299999999999, 0.0066682900000000003, 0.0057172500000000001, 0.0048187400000000002, 0.0039932800000000001, 0.0035350099999999999, 0.0032608699999999999, 0.0027935600000000001, 0.0023187899999999998, 0.00200936, 0.0017818199999999999, 0.00162279, 0.0029558100000000001, 0.00335308, 0.00379168, 0.0043161600000000003, 0.0049439499999999999, 0.0057966500000000004, 0.0071943099999999998, 0.0083545500000000005, 0.0094921799999999994, 0.0109744, 0.0129146, 0.0150741, 0.017701999999999999, 0.0186464, 0.024528600000000001, 0.0282869, 0.034993900000000001, 0.042891800000000001, 0.0493385, 0.064471000000000001, 0.082721000000000003, 0.078511999999999998, 0.111029, 0.13103500000000001, 0.15223600000000001, 0.18904000000000001, 0.22611400000000001, 0.25413799999999998, 0.392181, 0.515899, 0.838557])
xs_exp_limits_2sigma = array('d', [0.26784799999999997, 0.202155, 0.15606500000000001, 0.111719, 0.088813900000000001, 0.079510399999999995, 0.061056899999999997, 0.046263800000000001, 0.047361300000000002, 0.036250499999999998, 0.027524900000000001, 0.025943399999999998, 0.019525000000000001, 0.019982699999999999, 0.0150113, 0.0129435, 0.010593399999999999, 0.0077463799999999998, 0.0076325100000000003, 0.0066523600000000004, 0.0053657799999999997, 0.0044086799999999999, 0.0040253800000000003, 0.0034065800000000002, 0.0029003700000000002, 0.0026282100000000002, 0.0023030400000000001, 0.00207968, 0.0018121000000000001, 0.00160958, 0.0013854900000000001, 0.00407552, 0.0041559800000000001, 0.0046386999999999999, 0.0056800799999999997, 0.0069903400000000003, 0.0082090099999999992, 0.0098666199999999996, 0.0103141, 0.013328, 0.017970300000000002, 0.0191173, 0.0188387, 0.0252573, 0.0299174, 0.035958900000000002, 0.043051199999999998, 0.047892700000000003, 0.067854800000000007, 0.072238800000000006, 0.086809600000000001, 0.11748500000000001, 0.121616, 0.14145099999999999, 0.17238000000000001, 0.183194, 0.26361499999999999, 0.35348600000000002, 0.44686799999999999, 0.54509600000000002, 0.68489699999999998, 1.19137])

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
l1.DrawLatex(0.50,0.80, "0, 1 and 2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_WideJets_Zprime.eps')

