#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
#gStyle.SetOptTitle(0)
gStyle.SetPalette(1)
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1);
gStyle.SetPadTickY(1);
#gStyle.SetPadLeftMargin(0.13);
#gStyle.SetPadRightMargin(0.07);
gStyle.SetTitleFont(42)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetLabelFont(42, "XYZ")


BR = 0.5

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


masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_obs_limits = array('d', [1.6256200000000001, 0.89347600000000005, 0.59616100000000005, 0.39439800000000003, 0.34607599999999999, 0.36633300000000002, 0.25987700000000002, 0.17072100000000001, 0.111279, 0.089118100000000006, 0.101201, 0.13009200000000001, 0.099416400000000002, 0.071455900000000003, 0.057708700000000002, 0.0551163, 0.052176399999999998, 0.0415168, 0.028389999999999999, 0.0214196, 0.0149003, 0.0093119899999999992, 0.00651835, 0.0055875200000000003, 0.0055876600000000004, 0.0055876900000000002, 0.0055878100000000003, 0.0055878400000000002, 0.0059861999999999997, 0.0055272400000000001, 0.0050129800000000002])
xs_exp_limits = array('d', [1.2287300000000001, 0.88024000000000002, 0.64929300000000001, 0.49753599999999998, 0.38503300000000001, 0.335588, 0.24191199999999999, 0.19555, 0.16073299999999999, 0.12759000000000001, 0.100546, 0.103419, 0.084483299999999997, 0.065870700000000004, 0.054471199999999997, 0.048812700000000001, 0.042401399999999999, 0.036692500000000003, 0.0257269, 0.0217457, 0.0182972, 0.0151667, 0.0128748, 0.011175900000000001, 0.0097921199999999996, 0.0085891300000000004, 0.0074688200000000001, 0.0062542800000000001, 0.0062954100000000004, 0.0057769600000000003, 0.0048469200000000002])
masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [1.0056799999999999, 0.73521300000000001, 0.52998699999999999, 0.39774599999999999, 0.31938, 0.26521800000000001, 0.19098699999999999, 0.163053, 0.12614400000000001, 0.104002, 0.081722699999999995, 0.0846668, 0.063287999999999997, 0.052119100000000002, 0.042342200000000003, 0.035381999999999997, 0.033524600000000002, 0.027937, 0.022106600000000001, 0.014900500000000001, 0.013727400000000001, 0.012106, 0.010243800000000001, 0.0083817300000000004, 0.0069848499999999999, 0.0065191399999999997, 0.0055877100000000001, 0.0046565499999999998, 0.0046313600000000002, 0.0041909900000000003,
0.0033951099999999998, 0.0064924600000000002, 0.0073018800000000002, 0.0080493100000000005, 0.0088236700000000005, 0.0096765900000000005, 0.0113274, 0.013295899999999999, 0.0152599, 0.0179659, 0.020653899999999999, 0.023988800000000001, 0.026156700000000001, 0.035179000000000002, 0.045663299999999997, 0.056586499999999998, 0.062072799999999997, 0.070878399999999994, 0.085398399999999999, 0.11010200000000001, 0.13584499999999999, 0.129105, 0.153914, 0.20705899999999999, 0.247032, 0.29335800000000001, 0.40082299999999998, 0.453623, 0.58705099999999999, 0.76810699999999998, 0.98499000000000003, 1.41856])
xs_exp_limits_2sigma = array('d', [0.88389700000000004, 0.57413199999999998, 0.43986399999999998, 0.32969599999999999, 0.26346599999999998, 0.21936600000000001, 0.16065099999999999, 0.117589, 0.103634, 0.081616599999999997, 0.059310000000000002, 0.067322999999999994, 0.052424199999999997, 0.040927999999999999, 0.033498600000000003, 0.029787600000000001, 0.027931600000000001, 0.0206287, 0.016907200000000001, 0.0130364, 0.010243, 0.0093121599999999999, 0.0074501300000000001, 0.0065559099999999999, 0.0055874999999999996, 0.0051220399999999996, 0.0046932600000000003, 0.0037251699999999999, 0.0034863699999999999,
0.00279394, 0.0027938699999999999, 0.0083936299999999991, 0.0105802, 0.010022400000000001, 0.0104961, 0.0122016, 0.014867999999999999, 0.017266, 0.019499699999999998, 0.021860399999999999, 0.0249149, 0.031563500000000001, 0.036012099999999998, 0.042462800000000002, 0.056266299999999998, 0.064989699999999997, 0.073748400000000006, 0.084355299999999994, 0.101909, 0.13609099999999999, 0.15213299999999999, 0.16062699999999999, 0.19208600000000001, 0.25128200000000001, 0.30160799999999999, 0.39839400000000003, 0.486319, 0.54717499999999997, 0.67988400000000004, 0.86397299999999999, 1.1261000000000001, 1.57609])


graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL 0-tag, RSG-like resonances")
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


legend = TLegend(.45,.72,.85,.85)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(graph_obs,"Observed (F_{b#bar{b}}=" + str(BR) + ")","lp")
legend.AddEntry(graph_exp,"Expected (F_{b#bar{b}}=" + str(BR) + ")","lp")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.03)
l1.DrawLatex(0.17,0.33, "CMS Preliminary")
l1.DrawLatex(0.17,0.27, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.17,0.23, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.17,0.19, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.17,0.15, "Wide Jets")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obsexp_WideJets_RSG.png')

