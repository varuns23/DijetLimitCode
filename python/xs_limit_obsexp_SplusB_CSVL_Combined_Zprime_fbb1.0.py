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
xs_obs_limits = array('d', [0.56668799999999997, 0.58086000000000004, 0.17114699999999999, 0.089566499999999993, 0.059730699999999998, 0.056915300000000002, 0.064923800000000004, 0.091563800000000001, 0.066524299999999995, 0.051226899999999999, 0.056009000000000003, 0.053176099999999997, 0.041119599999999999, 0.033465799999999997, 0.034853299999999997, 0.038552099999999999, 0.032492, 0.0215675, 0.0135388, 0.010174300000000001, 0.0076462500000000003, 0.0060970299999999998, 0.0046936, 0.0043732399999999996, 0.0043788999999999998, 0.0040874099999999997, 0.0036084099999999998, 0.0032902000000000001, 0.0031122300000000001, 0.0026434700000000002, 0.0022806300000000001])
xs_exp_limits = array('d', [0.230407, 0.16552, 0.14075199999999999, 0.106697, 0.092528899999999997, 0.080888000000000002, 0.073737200000000003, 0.061639699999999999, 0.054559799999999999, 0.048937399999999999, 0.041352699999999999, 0.032641799999999999, 0.0290809, 0.024971699999999999, 0.023012999999999999, 0.018338699999999999, 0.016216100000000001, 0.013420899999999999, 0.012352200000000001, 0.010660299999999999, 0.0092406299999999997, 0.0079368200000000007, 0.0069036000000000002, 0.0060510099999999999, 0.0051682899999999999, 0.0046795099999999996, 0.0042695900000000002, 0.0036036100000000001, 0.0031934200000000002, 0.0028628299999999998, 0.0024946299999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.19465399999999999, 0.14331099999999999, 0.116091, 0.092244199999999998, 0.078032099999999993, 0.064212199999999997, 0.057154200000000002, 0.048913900000000003, 0.043119499999999998, 0.039581100000000001, 0.032548199999999999, 0.026677900000000001, 0.023544599999999999, 0.0202647, 0.017460699999999999, 0.0146146, 0.0126763, 0.0111022, 0.0096865200000000005, 0.0081025899999999998, 0.0073671500000000003, 0.00630381, 0.00549658, 0.0045591299999999998, 0.0039068100000000001, 0.0035856799999999999, 0.0032409800000000001, 0.0029089900000000002, 0.0023502900000000001, 0.0020915500000000002, 0.00187871, 0.00345438, 0.0039131399999999998, 0.0044372700000000001, 0.00502879, 0.00569857, 0.0068173000000000001, 0.0081866500000000002, 0.0091912699999999996, 0.0098577200000000004, 0.0118198, 0.0130901, 0.0153171, 0.0214541, 0.0200824, 0.024547200000000002, 0.028276699999999998, 0.033666300000000003, 0.0408776, 0.046293300000000003, 0.054552299999999998, 0.064017400000000002, 0.077648200000000001, 0.084354600000000002, 0.088277400000000006, 0.113694, 0.138793, 0.156444, 0.189251, 0.205563, 0.28437099999999998, 0.479269])
xs_exp_limits_2sigma = array('d', [0.17013700000000001, 0.124655, 0.10019500000000001, 0.080127900000000002, 0.064453499999999997, 0.057340299999999997, 0.049465000000000002, 0.03984, 0.034267699999999998, 0.0295874, 0.025922500000000001, 0.021103299999999998, 0.017214199999999999, 0.015436099999999999, 0.014682600000000001, 0.0128953, 0.0105948, 0.0084157999999999993, 0.0082007599999999996, 0.0068189499999999998, 0.0060358599999999997, 0.0051804900000000003, 0.0045771900000000001, 0.0038073600000000001, 0.0034033599999999998, 0.0029960199999999998, 0.0027498599999999998, 0.0023998999999999999, 0.0020761299999999998, 0.00184611, 0.00164419, 0.0048410199999999997, 0.0050032399999999999, 0.00558072, 0.0065823599999999998, 0.0078283099999999998, 0.0096726699999999995, 0.0097860299999999994, 0.0115269, 0.0147149, 0.0166912, 0.0175079, 0.020091899999999999, 0.028635600000000001, 0.0305337, 0.0318207, 0.040344699999999997, 0.0473033, 0.053582200000000003, 0.066514799999999999, 0.076245400000000005, 0.088421600000000003, 0.114411, 0.118863, 0.123374, 0.14536499999999999, 0.20960500000000001, 0.23374, 0.30381599999999997, 0.34836899999999998, 0.48494500000000001, 0.98218300000000003])

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
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_WideJets_Zprime_fbb1.0.eps')

