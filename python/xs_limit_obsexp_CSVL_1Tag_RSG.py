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

  #cmd = "./stats " + str(mass) + " " + str(BR) + " gg"
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
xs_obs_limits = array('d', [0.74594099999999997, 0.59671700000000005, 0.54289799999999999, 0.40492899999999998, 0.23539199999999999, 0.192019, 0.19419, 0.160495, 0.11916599999999999, 0.096803399999999998, 0.081912100000000002, 0.068404000000000006, 0.0577335, 0.048420900000000003, 0.042838599999999998, 0.038483299999999998, 0.035971999999999997, 0.0292035, 0.0243991, 0.020703200000000001, 0.0185892, 0.016761499999999999, 0.014922400000000001, 0.012900200000000001, 0.0106234, 0.0091475399999999991, 0.0074899500000000004, 0.0060534500000000002, 0.0046564500000000003, 0.0041909499999999997, 0.0032594999999999998])
xs_exp_limits = array('d', [0.84089700000000001, 0.59956699999999996, 0.47376600000000002, 0.377106, 0.27382800000000002, 0.22248999999999999, 0.192523, 0.150501, 0.11167000000000001, 0.096810599999999997, 0.082746100000000003, 0.0670486, 0.0521205, 0.048420400000000002, 0.040969899999999997, 0.036679499999999997, 0.032163400000000002, 0.028135400000000001, 0.021678699999999999, 0.019592200000000001, 0.017441399999999999, 0.0163488, 0.013219099999999999, 0.0121095, 0.0103847, 0.0088490900000000004, 0.0069849100000000004, 0.0060535199999999997, 0.0055879199999999997, 0.0049898, 0.0046723600000000004])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.56864899999999996, 0.46699600000000002, 0.378224, 0.32445600000000002, 0.21581400000000001, 0.17516799999999999, 0.14572199999999999, 0.11121300000000001, 0.096417799999999998, 0.074207400000000007, 0.059511500000000002, 0.054851900000000002, 0.044642399999999999, 0.034888099999999998, 0.029796300000000001, 0.029795200000000001, 0.0242139, 0.020485, 0.016762099999999999, 0.014898700000000001, 0.013038299999999999, 0.0130379, 0.0110545, 0.0093127399999999999, 0.0074502500000000003, 0.0065191800000000003, 0.0055876399999999996, 0.0046564900000000001, 0.0041908400000000004, 0.0037252100000000001, 0.0032595800000000002, 0.0062432399999999997, 0.00651426, 0.0070879999999999997, 0.0078715199999999999, 0.0092193299999999995, 0.0110863, 0.014028000000000001, 0.014898700000000001, 0.017683299999999999, 0.0203103, 0.022168199999999999, 0.026399300000000001, 0.029419799999999999, 0.035354299999999998, 0.044206299999999997, 0.049690199999999997, 0.053429699999999997, 0.061633199999999999, 0.0700157, 0.0882439, 0.106798, 0.12614400000000001, 0.14563499999999999, 0.18539700000000001, 0.23371900000000001, 0.28460400000000002, 0.345165, 0.45155000000000001, 0.56335500000000005, 0.69349799999999995, 0.96710099999999999])
xs_exp_limits_2sigma = array('d', [0.46710800000000002, 0.33800799999999998, 0.29922900000000002, 0.22845399999999999, 0.16303300000000001, 0.131053, 0.10378999999999999, 0.088748400000000005, 0.074004899999999998, 0.0560381, 0.044519099999999999, 0.048332800000000002, 0.03347, 0.0279183, 0.022330900000000001, 0.026070800000000002, 0.022342299999999999, 0.016758100000000001, 0.0139676, 0.0111723, 0.010317099999999999, 0.011174, 0.0084551000000000001, 0.0074499900000000001, 0.0065559299999999997, 0.0051220700000000003, 0.00465637, 0.0037620000000000002, 0.00329628, 0.0028306999999999998, 0.00279386, 0.0077418299999999999, 0.0089960700000000001, 0.0106173, 0.0122828, 0.013416600000000001, 0.0160958, 0.016599699999999998, 0.020892899999999999, 0.021895700000000001, 0.026616600000000001, 0.0285096, 0.031328700000000001, 0.036581000000000002, 0.042561099999999998, 0.056829499999999998, 0.0624018, 0.069067199999999995, 0.083963399999999994, 0.097814600000000002, 0.11262800000000001, 0.12634999999999999, 0.152224, 0.18204600000000001, 0.21791099999999999, 0.27982200000000002, 0.32669500000000001, 0.414296, 0.54131899999999999, 0.64944999999999997, 0.79453300000000004, 1.0972599999999999])

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

