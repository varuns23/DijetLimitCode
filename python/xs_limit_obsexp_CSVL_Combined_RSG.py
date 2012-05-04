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

  #log_file = open("stats_" + str(mass) + "_" + str(BR) + ".log",'w')
  #log_file.write(output)
  #log_file.close()

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
xs_obs_limits = array('d', [0.43775900000000001, 0.37281999999999998, 0.23666599999999999, 0.14894499999999999, 0.096033599999999997, 0.096353099999999997, 0.104292, 0.099076800000000007, 0.074681800000000007, 0.055851699999999997, 0.057693500000000002, 0.062416199999999998, 0.049212499999999999, 0.038623299999999999, 0.033942399999999998, 0.034602000000000001, 0.031336799999999998, 0.023645099999999999, 0.016089200000000001, 0.0111754, 0.0088473900000000001, 0.0065191499999999996, 0.0046564400000000004, 0.0041908700000000002, 0.0041909, 0.0041909499999999997, 0.0037252800000000001, 0.00325962, 0.0030267900000000001, 0.0027939699999999998, 0.0023283000000000002])
xs_exp_limits = array('d', [0.37387500000000001, 0.30032799999999998, 0.21524599999999999, 0.187781, 0.15964700000000001, 0.124393, 0.108724, 0.100865, 0.0714365, 0.0615425, 0.055542899999999999, 0.053433000000000001, 0.045612100000000003, 0.036732500000000001, 0.033321799999999999, 0.030138100000000001, 0.0305787, 0.022291200000000001, 0.014436900000000001, 0.012107, 0.0107101, 0.0088474599999999997, 0.0078215799999999999, 0.0065500300000000001, 0.0060354299999999996, 0.0051438899999999999, 0.00443597, 0.0039581800000000004, 0.0036247599999999999, 0.00304258, 0.0027939599999999998])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.32397599999999999, 0.24658099999999999, 0.163156, 0.138658, 0.111664, 0.096636200000000005, 0.081670300000000001, 0.074434500000000001, 0.059537, 0.048384799999999999, 0.040958300000000003, 0.040482200000000003, 0.031663999999999998, 0.027453600000000002, 0.026418899999999999, 0.0245656, 0.020894800000000002, 0.0170475, 0.011174999999999999, 0.0093126000000000007, 0.0074502300000000004, 0.0065191399999999997, 0.0055878300000000002, 0.0046565799999999996, 0.0041909199999999999, 0.0037252299999999999, 0.00325961, 0.00279394, 0.0023282899999999998, 0.0020954699999999999, 0.0018626300000000001, 0.0036241899999999998, 0.00410502,
0.0046118000000000001, 0.0053428800000000004, 0.0062491999999999999, 0.0071279999999999998, 0.0083786299999999998, 0.0093285999999999994, 0.010625000000000001, 0.0123567, 0.0150105, 0.0175522, 0.0204253, 0.029635700000000001, 0.040064599999999999, 0.040998399999999997, 0.045126899999999998, 0.050651500000000002, 0.063004500000000005, 0.071600800000000006, 0.074583499999999997, 0.087660199999999994, 0.101974, 0.132298, 0.14260200000000001, 0.165576, 0.20172999999999999, 0.24046600000000001, 0.293989, 0.39736500000000002, 0.45556400000000002])
xs_exp_limits_2sigma = array('d', [0.21868799999999999, 0.20413000000000001, 0.116214, 0.103035, 0.088148299999999999, 0.081563200000000002, 0.059337399999999998, 0.056107600000000001, 0.0412415, 0.037191700000000001, 0.0334968, 0.033662699999999997, 0.0243494, 0.022342000000000001, 0.022346299999999999, 0.0177679, 0.0168366, 0.012253399999999999, 0.0093122499999999993, 0.0065557999999999996, 0.0056613699999999998, 0.0051222100000000003, 0.0041908500000000003, 0.00376202, 0.0034924299999999999, 0.0027939000000000002, 0.0025795000000000002, 0.0023282799999999998, 0.0018810299999999999, 0.001639, 0.0013969799999999999, 0.0045703100000000002, 0.0052989600000000001,
0.0061144399999999996, 0.0074960199999999999, 0.0083506699999999993, 0.0093238499999999998, 0.0105883, 0.013580699999999999, 0.0169721, 0.020391300000000001, 0.022440100000000001, 0.024129299999999999, 0.0280889, 0.034199500000000001, 0.050920600000000003, 0.054851200000000003, 0.059733500000000002, 0.062457800000000001, 0.077057200000000006, 0.092909599999999995, 0.091051000000000007, 0.12081799999999999, 0.158945, 0.16719100000000001, 0.199548, 0.21309500000000001, 0.273644, 0.30269299999999999, 0.364921, 0.52786599999999995, 0.58952000000000004])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL Combined, RSG-like resonances")
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
l1.DrawLatex(0.19,0.20, "Wide Jets")
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.50, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.05)
l1.DrawLatex(0.52,0.20, "0, 1 and 2 b-tags")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obsexp_WideJets_RSG.png')

