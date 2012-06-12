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
xs_obs_limits = array('d', [1.3033999999999999, 1.4607000000000001, 0.29347299999999998, 0.18501600000000001, 0.13832700000000001, 0.127994, 0.140462, 0.225103, 0.22576399999999999, 0.200655, 0.16195000000000001, 0.128662, 0.10584399999999999, 0.093475000000000003, 0.10101, 0.097293599999999994, 0.075715900000000003, 0.0539578, 0.040704299999999999, 0.030914299999999999, 0.024624099999999999, 0.020415599999999999, 0.019240299999999998, 0.019855999999999999, 0.021440000000000001, 0.021494200000000001, 0.020771000000000001, 0.019616999999999999, 0.018928199999999999, 0.018233699999999999, 0.017810900000000001])
xs_exp_limits = array('d', [0.511131, 0.37864100000000001, 0.32063000000000003, 0.24046600000000001, 0.206285, 0.19025800000000001, 0.166911, 0.13968900000000001, 0.11504200000000001, 0.111122, 0.103783, 0.089461200000000005, 0.082004999999999995, 0.066895099999999999, 0.060632499999999999, 0.053127500000000001, 0.052086500000000001, 0.047447499999999997, 0.041319300000000003, 0.036096200000000002, 0.033337199999999997, 0.0305069, 0.028662300000000002, 0.0276677, 0.0262312, 0.0236566, 0.023486900000000002, 0.022561600000000001, 0.0218146, 0.0209535, 0.020712899999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.40055499999999999, 0.30239700000000003, 0.266733, 0.20149900000000001, 0.17175199999999999, 0.14923900000000001, 0.130966, 0.11462600000000001, 0.097671999999999995, 0.085721000000000006, 0.087543999999999997, 0.071119399999999999, 0.058695299999999999, 0.052585199999999999, 0.048513199999999999, 0.042504800000000002, 0.041308999999999998, 0.036178399999999999, 0.032398999999999997, 0.0292527, 0.027084400000000002, 0.025460799999999999, 0.022871800000000001, 0.022590300000000001, 0.021045700000000001, 0.018307500000000001, 0.0178035, 0.017477400000000001, 0.016993600000000001, 0.016714199999999999, 0.016666, 0.028260299999999999, 0.028338200000000001, 0.029233700000000001, 0.030281700000000002, 0.0291375, 0.031440299999999997, 0.033790500000000001, 0.037671799999999998, 0.043135800000000002, 0.0465548, 0.049483199999999998, 0.053953300000000003, 0.065639100000000006, 0.071084700000000001, 0.076355199999999998, 0.077854900000000005, 0.090063599999999994, 0.106019, 0.127807, 0.155224, 0.16192500000000001, 0.14870900000000001, 0.191386, 0.213564, 0.25297399999999998, 0.298595, 0.35317199999999999, 0.41493799999999997, 0.59637700000000005, 0.71134399999999998, 1.0761799999999999])
xs_exp_limits_2sigma = array('d', [0.38239499999999998, 0.25071900000000003, 0.236484, 0.169321, 0.13272600000000001, 0.12957299999999999, 0.105458, 0.092753000000000002, 0.085424100000000003, 0.074057399999999995, 0.065966800000000006, 0.056510499999999998, 0.047501500000000002, 0.0435076, 0.038376899999999999, 0.0336155, 0.032450300000000001, 0.028650999999999999, 0.0242384, 0.023042699999999999, 0.022070800000000002, 0.021718899999999999, 0.019180699999999998, 0.01687, 0.0156206, 0.0153653, 0.015284799999999999, 0.0146783, 0.0147218, 0.014770500000000001, 0.0152052, 0.035700900000000001, 0.035635899999999998, 0.038283900000000003, 0.040887699999999999, 0.036837300000000003, 0.041189499999999997, 0.046952399999999998, 0.050542799999999999, 0.053278100000000002, 0.062602500000000005, 0.071091199999999993, 0.077244699999999999, 0.081417500000000004, 0.086751700000000001, 0.112057, 0.11620800000000001, 0.12561, 0.16820099999999999, 0.173955, 0.19869400000000001, 0.23787900000000001, 0.25254599999999999, 0.25552900000000001, 0.32247999999999999, 0.370419, 0.40991300000000003, 0.60130499999999998, 0.56918800000000003, 0.83737700000000004, 1.02138, 1.8149999999999999])

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
l1.DrawLatex(0.18,0.89, "gg/bb, f_{b#bar{b}}=" + str(BR))
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
c.SaveAs('CSVL_2Tag_limit_obsexp_SplusB_WideJets_RSG.eps')

