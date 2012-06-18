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
xs_obs_limits = array('d', [1.92899, 0.46571000000000001, 0.34418199999999999, 0.214311, 0.15690299999999999, 0.16734399999999999, 0.137465, 0.095585600000000007, 0.0680423, 0.053004799999999998, 0.073309299999999994, 0.090698899999999999, 0.068774799999999997, 0.048376599999999999, 0.043616599999999998, 0.049422800000000003, 0.043897600000000002, 0.029521599999999999, 0.017050200000000001, 0.012001899999999999, 0.0087794499999999994, 0.0064427900000000003, 0.0046331200000000001, 0.0042112900000000003, 0.0041866300000000002, 0.0039735899999999999, 0.0035994, 0.00337449, 0.0031745200000000001, 0.0028415900000000002, 0.0024463599999999999])
xs_exp_limits = array('d', [0.55163499999999999, 0.399785, 0.32835399999999998, 0.23843300000000001, 0.19237299999999999, 0.17569000000000001, 0.13170299999999999, 0.100481, 0.082810099999999998, 0.077056899999999998, 0.056060400000000003, 0.049362299999999998, 0.037326699999999997, 0.032968600000000001, 0.027611799999999999, 0.023858799999999999, 0.020653899999999999, 0.018373500000000001, 0.017529599999999999, 0.012863100000000001, 0.011343900000000001, 0.0093021700000000002, 0.0080198500000000002, 0.0066647499999999997, 0.0057494399999999998, 0.0050854999999999997, 0.0044630900000000003, 0.0038278800000000001, 0.0032757099999999998, 0.0029319799999999998, 0.0027474999999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.50165000000000004, 0.36879200000000001, 0.25897399999999998, 0.19997100000000001, 0.16383600000000001, 0.13364100000000001, 0.111683, 0.0866532, 0.068486400000000003, 0.0568513, 0.046849099999999998, 0.039355099999999997, 0.0292702, 0.0263591, 0.021970199999999999, 0.018643699999999999, 0.015920500000000001, 0.0134298, 0.0127379, 0.010849900000000001, 0.0089307899999999992, 0.0070188400000000001, 0.0059257800000000003, 0.00500966, 0.0044441799999999998, 0.00370668, 0.00328189, 0.0029744699999999999, 0.0026132099999999999, 0.0023038899999999998, 0.0021461599999999998, 0.0036609099999999999, 0.0043519400000000003, 0.0051265499999999997, 0.0057631599999999998, 0.0062225600000000002, 0.0074185099999999997, 0.0085931199999999992, 0.0100757, 0.011955500000000001, 0.013621899999999999, 0.016945499999999999, 0.0197512, 0.0252708, 0.0311489, 0.031300300000000003, 0.039888600000000003, 0.049816100000000002, 0.050434800000000002, 0.057890400000000002, 0.075019100000000005, 0.0817026, 0.116754, 0.14447199999999999, 0.18355399999999999, 0.21564700000000001, 0.26275700000000002, 0.32564900000000002, 0.39923199999999998, 0.59128199999999997, 0.834866, 1.64635])
xs_exp_limits_2sigma = array('d', [0.44670399999999999, 0.30881999999999998, 0.22750899999999999, 0.177372, 0.13544800000000001, 0.11332, 0.091206599999999999, 0.071418099999999998, 0.0541757, 0.047659300000000002, 0.037935299999999998, 0.030891100000000001, 0.024913000000000001, 0.0211837, 0.016321499999999999, 0.0162781, 0.012064699999999999, 0.0114292, 0.010146499999999999, 0.0081461399999999996, 0.0073334799999999999, 0.0061578700000000002, 0.0048176299999999998, 0.0043826300000000002, 0.0036805000000000002, 0.0031735800000000001, 0.0026906399999999998, 0.0022634500000000002, 0.0020616100000000002, 0.0018393999999999999, 0.00170846, 0.0051863500000000002, 0.00572048, 0.0068999999999999999, 0.0080438999999999997, 0.0101041, 0.0116325, 0.013942299999999999, 0.015127, 0.018220699999999999, 0.020118, 0.023538699999999999, 0.029315600000000001, 0.034552199999999998, 0.040940299999999999, 0.047058799999999998, 0.056080900000000003, 0.063014899999999999, 0.067488800000000002, 0.084964700000000004, 0.093201300000000001, 0.096417500000000003, 0.168154, 0.232261, 0.25875900000000002, 0.33038600000000001, 0.384739, 0.45113599999999998, 0.52163300000000001, 0.98339399999999999, 1.3124499999999999, 2.6468400000000001])

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
c.SaveAs('Inclusive_limit_obsexp_SplusB_WideJets_Zprime_fbb1.0.eps')

