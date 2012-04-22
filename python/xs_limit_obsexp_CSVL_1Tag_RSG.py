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

  #cmd = "./stats " + str(mass) + " " + " " + str(BR)
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
xs_obs_limits = array('d', [0.73904400000000003, 0.59667000000000003, 0.53606799999999999, 0.42071500000000001, 0.23511899999999999, 0.19206899999999999, 0.19875499999999999, 0.16716700000000001, 0.11912200000000001, 0.096748799999999996, 0.081894599999999998, 0.071845599999999996, 0.057729799999999998, 0.0484191, 0.042836300000000001, 0.040340800000000003, 0.036011899999999999, 0.029237200000000001, 0.024362999999999999, 0.020646399999999999, 0.018585500000000001, 0.016813100000000001, 0.014968199999999999, 0.012957, 0.010663799999999999, 0.0091739200000000003, 0.0075089800000000002, 0.0060534400000000002, 0.00512226, 0.0041909399999999998, 0.0032594999999999998])
xs_exp_limits = array('d', [0.89590899999999996, 0.62436499999999995, 0.47930600000000001, 0.38750699999999999, 0.29630600000000001, 0.23743700000000001, 0.19939999999999999, 0.16270200000000001, 0.12192, 0.103796, 0.087466500000000003, 0.068556300000000001, 0.052127, 0.044690399999999998, 0.040967799999999999, 0.036641399999999998, 0.031837600000000001, 0.028100799999999999, 0.022349399999999998, 0.020316799999999999, 0.017687499999999998, 0.016519800000000001, 0.0131173, 0.011811, 0.0102779, 0.0086142700000000003, 0.0069853399999999996, 0.0060597300000000002, 0.0056042699999999997, 0.0051223400000000004, 0.0048496499999999996])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.72635400000000006, 0.53785099999999997, 0.39971000000000001, 0.321301, 0.234844, 0.191301, 0.17035800000000001, 0.12626000000000001, 0.096478800000000003, 0.081858200000000006, 0.066960400000000003, 0.055862799999999997, 0.0446439, 0.037218599999999998, 0.032550799999999998, 0.029794899999999999, 0.0260729, 0.020485900000000001, 0.0167636, 0.016762599999999999, 0.0130384, 0.0121076, 0.0102443, 0.0093126600000000004, 0.0074503299999999998, 0.0065192599999999998, 0.0055876800000000003, 0.0046566000000000003, 0.0041909, 0.0037253099999999999, 0.00372514, 0.0061669899999999998, 0.0064849499999999997,
0.0070939799999999997, 0.0078773200000000002, 0.0093966399999999995, 0.010571000000000001, 0.013477899999999999, 0.0147458, 0.0164125, 0.0204078, 0.021660100000000002, 0.025153100000000001, 0.028093300000000002, 0.034058900000000003, 0.0422482, 0.050583599999999999, 0.051902799999999999, 0.059300800000000001, 0.069646200000000005, 0.086341600000000004, 0.10915800000000001, 0.13536699999999999, 0.15593099999999999, 0.19709199999999999, 0.22597200000000001, 0.29889900000000003, 0.36706499999999997, 0.45404, 0.56299100000000002, 0.70119699999999996, 0.97425700000000004])
xs_exp_limits_2sigma = array('d', [0.62227900000000003, 0.427784, 0.36734299999999998, 0.27634900000000001, 0.20372299999999999, 0.16020799999999999, 0.13347800000000001, 0.10467899999999999, 0.0824019, 0.066791299999999998, 0.0523712, 0.048657800000000001, 0.037206799999999998, 0.029765799999999999, 0.026216099999999999, 0.024350900000000002, 0.020480100000000001, 0.018620600000000001, 0.014897199999999999, 0.0130367, 0.0112485, 0.011174999999999999, 0.0083811800000000002, 0.0074501200000000002, 0.0065188499999999996, 0.00558757, 0.0046563899999999998, 0.0037620100000000001, 0.0037250400000000002, 0.0027939200000000001,
0.0028209099999999998, 0.0078059699999999997, 0.0091494499999999999, 0.0107078, 0.0117816, 0.0122474, 0.0143669, 0.016473600000000001, 0.018067699999999999, 0.020560100000000001, 0.025884399999999998, 0.028313100000000001, 0.030816199999999998, 0.035685700000000001, 0.042853599999999999, 0.052082700000000003, 0.062208100000000002, 0.064361699999999994, 0.075031600000000004, 0.096128000000000005, 0.10898099999999999, 0.12277399999999999, 0.158304, 0.18582799999999999, 0.2235, 0.272372, 0.33233499999999999, 0.418404, 0.53278499999999995, 0.64193500000000003, 0.776814, 1.10304])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL 1-tag, RSG-like resonances")
graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,10)

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

legend = TLegend(.50,.67,.80,.80)
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
l1.DrawLatex(0.19,0.88, "RS-graviton-like, f_{b#bar{b}}=" + str(BR))
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.43, "CMS Preliminary")
l1.DrawLatex(0.19,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.20,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.19,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL 1-tag")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obsexp_WideJets_RSG.eps')

