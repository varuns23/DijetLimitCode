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


BR = 0.1

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

### for running the limit code
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
xs_obs_limits = array('d', [1.2053199999999999, 0.35755500000000001, 0.242893, 0.15651200000000001, 0.12450700000000001, 0.141904, 0.097775100000000004, 0.070582300000000001, 0.049754399999999997, 0.044631499999999998, 0.075410699999999997, 0.073136999999999994, 0.045515, 0.032278800000000003, 0.032827000000000002, 0.037334899999999997, 0.0295289, 0.0172234, 0.011028, 0.0078927800000000003, 0.00595884, 0.0041605499999999998, 0.00342327, 0.0033452299999999998, 0.0033715300000000002, 0.00325407, 0.0030435499999999999, 0.00276027, 0.0024713399999999998, 0.0021106499999999999, 0.0017792800000000001])
xs_exp_limits = array('d', [0.4289, 0.32401400000000002, 0.240568, 0.18908900000000001, 0.15723100000000001, 0.12995399999999999, 0.099915100000000007, 0.081588300000000002, 0.063999899999999998, 0.051599899999999997, 0.049041899999999999, 0.034229900000000001, 0.031110200000000001, 0.0249704, 0.022138600000000001, 0.01754, 0.017239500000000001, 0.0123388, 0.010970199999999999, 0.0096643700000000003, 0.0078150300000000006, 0.00677715, 0.0060796000000000001, 0.0049029800000000004, 0.00416096, 0.0037323399999999998, 0.00328773, 0.0029468200000000002, 0.0025079199999999999, 0.0021405500000000002, 0.0018841800000000001])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.391094, 0.27349299999999999, 0.20328599999999999, 0.15327099999999999, 0.119453, 0.101534, 0.083105200000000004, 0.062737399999999999, 0.052166200000000003, 0.043495199999999998, 0.031784800000000002, 0.026373199999999999, 0.0243447, 0.020936699999999999, 0.016988300000000001, 0.0140321, 0.0128106, 0.0102176, 0.0081297799999999996, 0.0071516899999999996, 0.0062388599999999997, 0.0053172599999999999, 0.0043218900000000001, 0.0035168600000000001, 0.0032726500000000002, 0.0028572099999999998, 0.00244385, 0.00204974, 0.00177859, 0.0016300399999999999, 0.0014295099999999999, 0.0025477899999999999, 0.0029604399999999999, 0.00345489, 0.0037594099999999999, 0.0042788799999999997, 0.0049936099999999999, 0.0063345700000000003, 0.0073080100000000002, 0.0080865199999999998, 0.0094621400000000008, 0.011563500000000001, 0.0140751, 0.016096699999999999, 0.0178199, 0.024037900000000001, 0.025048999999999998, 0.033313200000000001, 0.038131600000000002, 0.048466200000000001, 0.057641299999999999, 0.068587599999999999, 0.080982200000000004, 0.088642600000000002, 0.12817700000000001, 0.15363199999999999, 0.243899, 0.25618099999999999, 0.28251100000000001, 0.41382600000000003, 0.64995000000000003, 0.96424799999999999])
xs_exp_limits_2sigma = array('d', [0.35326999999999997, 0.24547099999999999, 0.18160299999999999, 0.13064700000000001, 0.098341100000000001, 0.081939999999999999, 0.067774100000000004, 0.0460203, 0.041403500000000003, 0.0354212, 0.026114100000000001, 0.0190589, 0.0195795, 0.0150733, 0.0136163, 0.0120839, 0.0106237, 0.0079410599999999998, 0.0070137000000000003, 0.0060508799999999998, 0.0050726299999999998, 0.0040084099999999996, 0.0033164700000000002, 0.0029924499999999998, 0.0025138700000000001, 0.0022835500000000001, 0.0020488799999999999, 0.0018316999999999999, 0.0015657500000000001, 0.00132967, 0.0011472399999999999, 0.00362292, 0.0036189400000000002, 0.0040633900000000001, 0.0050143100000000001, 0.0062124600000000004, 0.0070694599999999996, 0.0087606100000000003, 0.00980579, 0.011195999999999999, 0.0148597, 0.018209699999999999, 0.0178706, 0.021457799999999999, 0.025735600000000001, 0.037061999999999998, 0.032414600000000002, 0.044182399999999997, 0.0515404, 0.065758399999999995, 0.070777499999999993, 0.094765799999999997, 0.122599, 0.128798, 0.17974599999999999, 0.22448299999999999, 0.33995900000000001, 0.34651399999999999, 0.45460899999999999, 0.56087299999999995, 0.91252, 1.4174800000000001])

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
c.SaveAs('CSVL_Combined_limit_obsexp_SplusB_WideJets_Zprime_fbb0.1.eps')

