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
xs_obs_limits = array('d', [1.28383, 1.40899, 0.283391, 0.177841, 0.133105, 0.124541, 0.13644700000000001, 0.22184699999999999, 0.21121300000000001, 0.18620900000000001, 0.14754400000000001, 0.11654100000000001, 0.095602199999999998, 0.085517899999999994, 0.093782500000000005, 0.088273500000000005, 0.066692000000000001, 0.046254099999999999, 0.0349444, 0.026463799999999999, 0.020531400000000002, 0.017371000000000001, 0.016812000000000001, 0.0177041, 0.018889800000000002, 0.018755899999999999, 0.017786099999999999, 0.016527799999999999, 0.015620800000000001, 0.014930499999999999, 0.0144882])
xs_exp_limits = array('d', [0.42205599999999999, 0.336426, 0.31717499999999998, 0.23430999999999999, 0.201989, 0.18076300000000001, 0.15861700000000001, 0.127743, 0.12256599999999999, 0.10084600000000001, 0.108635, 0.083949800000000005, 0.074023699999999998, 0.064547900000000005, 0.054240900000000002, 0.049187500000000002, 0.046210000000000001, 0.040054199999999998, 0.035918499999999999, 0.032310199999999997, 0.029479700000000001, 0.026957100000000001, 0.025110500000000001, 0.024518999999999999, 0.023156199999999998, 0.020504999999999999, 0.019421299999999999, 0.018341400000000001, 0.017713099999999999, 0.016660899999999999, 0.015907999999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.39469599999999999, 0.27849000000000002, 0.25878299999999999, 0.19980800000000001, 0.16375200000000001, 0.14528199999999999, 0.12588099999999999, 0.10313899999999999, 0.098247500000000001, 0.084763699999999997, 0.080769900000000006, 0.065504300000000001, 0.057644300000000002, 0.050419400000000003, 0.043639499999999998, 0.039676599999999999, 0.035395299999999998, 0.032125399999999998, 0.028681399999999999, 0.0261674, 0.0252848, 0.022562100000000002, 0.020714300000000001, 0.019066, 0.0178047, 0.0156028, 0.0151875, 0.015044800000000001, 0.014483899999999999, 0.013821399999999999, 0.0134965, 0.021919000000000001, 0.0231618, 0.024139000000000001, 0.025151400000000001, 0.0248005, 0.0262083, 0.0289967, 0.031601600000000001, 0.0370862, 0.040834200000000001, 0.043577900000000003, 0.048285700000000001, 0.058162600000000002, 0.059087099999999997, 0.064528299999999997, 0.068600999999999995, 0.082008399999999995, 0.095797400000000005, 0.11589000000000001, 0.137047, 0.16110099999999999, 0.169487, 0.18160799999999999, 0.20766299999999999, 0.24409900000000001, 0.28630499999999998, 0.309085, 0.44634400000000002, 0.58319299999999996, 0.71665800000000002, 0.93793099999999996])
xs_exp_limits_2sigma = array('d', [0.38194, 0.24492700000000001, 0.22891600000000001, 0.169238, 0.132852, 0.124957, 0.104092, 0.091288599999999998, 0.0845191, 0.067057199999999997, 0.063126199999999993, 0.052494600000000002, 0.046489900000000001, 0.041522299999999998, 0.035359599999999998, 0.032582300000000002, 0.0281245, 0.026377000000000001, 0.021692599999999999, 0.020413199999999999, 0.019052699999999999, 0.018240200000000002, 0.016368799999999999, 0.0150732, 0.013746, 0.0133858, 0.012775, 0.0122576, 0.0120655, 0.011963100000000001, 0.012135, 0.027926900000000001, 0.0293263, 0.031552999999999998, 0.034840200000000002, 0.029202100000000002, 0.037729199999999997, 0.041085799999999999, 0.042097999999999997, 0.045323799999999997, 0.0541612, 0.062688599999999997, 0.068841100000000002, 0.075619900000000004, 0.076570200000000005, 0.092467400000000005, 0.111903, 0.119007, 0.13206300000000001, 0.14519000000000001, 0.17479500000000001, 0.23735200000000001, 0.248617, 0.27555400000000002, 0.29424499999999998, 0.34842000000000001, 0.39347300000000002, 0.47636000000000001, 0.58795500000000001, 0.81636399999999998, 1.0462, 1.6814800000000001])

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
l1.DrawLatex(0.50,0.80, "2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_2Tag_limit_obsexp_SplusB_WideJets_Zprime.eps')

