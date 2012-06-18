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
xs_obs_limits = array('d', [1.1579200000000001, 0.32903900000000003, 0.24489900000000001, 0.16009499999999999, 0.12693299999999999, 0.15915099999999999, 0.10544199999999999, 0.071115499999999998, 0.051394700000000001, 0.044006900000000002, 0.073586200000000004, 0.072086499999999998, 0.045339999999999998, 0.032437399999999998, 0.032730700000000001, 0.0370645, 0.029232600000000001, 0.0170849, 0.010964700000000001, 0.0078285999999999998, 0.0058694799999999998, 0.0040792299999999997, 0.0033536500000000001, 0.0032898599999999999, 0.0033681800000000001, 0.0032281200000000001, 0.00302565, 0.00275946, 0.0024808299999999998, 0.0021368200000000002, 0.0018087299999999999])
xs_exp_limits = array('d', [0.51581500000000002, 0.32366400000000001, 0.23811199999999999, 0.19048200000000001, 0.153582, 0.121658, 0.097132099999999999, 0.081093100000000001, 0.063999399999999998, 0.057239600000000002, 0.045206000000000003, 0.037742900000000003, 0.028114699999999999, 0.024686400000000001, 0.0227049, 0.0173267, 0.014837899999999999, 0.0130229, 0.011240099999999999, 0.0095978899999999995, 0.0081266199999999993, 0.0066717800000000004, 0.0060324699999999998, 0.0048620599999999996, 0.0043463099999999999, 0.0038874700000000001, 0.0032159900000000002, 0.0028833000000000001, 0.0024427199999999998, 0.0021274000000000002, 0.0020668499999999999])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.38921800000000001, 0.28332000000000002, 0.20285700000000001, 0.15174599999999999, 0.123404, 0.101894, 0.085744299999999996, 0.063979099999999997, 0.052325700000000003, 0.045159600000000001, 0.034841900000000002, 0.0284208, 0.023818499999999999, 0.019696700000000001, 0.0166689, 0.0137839, 0.0122434, 0.0107139, 0.0091527799999999992, 0.0077206499999999999, 0.0062499599999999997, 0.0049961500000000004, 0.0040804700000000001, 0.0035558999999999999, 0.0032332200000000002, 0.0027233499999999998, 0.0024571800000000002, 0.0020910099999999999, 0.00185527, 0.00172051, 0.00156022, 0.0026984700000000001, 0.0031493099999999998, 0.0036223900000000001, 0.0042080900000000003, 0.0046953000000000003, 0.0052203099999999997, 0.0062908599999999997, 0.0075724900000000003, 0.0083329700000000003, 0.010257799999999999, 0.0112599, 0.013231400000000001, 0.016824200000000001, 0.018977500000000001, 0.022470199999999999, 0.025919000000000001, 0.0344391, 0.036538300000000003, 0.0432916, 0.050677800000000002, 0.065587699999999999, 0.080489599999999994, 0.102232, 0.134798, 0.16412299999999999, 0.204897, 0.24311199999999999, 0.298933, 0.410555, 0.59743500000000005, 1.00183])
xs_exp_limits_2sigma = array('d', [0.33980300000000002, 0.22523899999999999, 0.18226300000000001, 0.12581400000000001, 0.10642, 0.079028399999999999, 0.074029800000000007, 0.0534964, 0.043596900000000001, 0.035725199999999999, 0.027644800000000001, 0.0234954, 0.0188224, 0.014342799999999999, 0.013326299999999999, 0.0101321, 0.00825007, 0.0077777799999999998, 0.0071354699999999997, 0.0059745299999999996, 0.00495357, 0.0039386500000000001, 0.0033540000000000002, 0.00314241, 0.0027267300000000001, 0.00216884, 0.00185801, 0.00168578, 0.00146086, 0.00134252, 0.0012088800000000001, 0.0036783900000000001, 0.0039332300000000002, 0.0049605600000000001, 0.0053919099999999998, 0.0066534100000000002, 0.0084607599999999995, 0.0100404, 0.0104613, 0.0131252, 0.0137112, 0.016816399999999999, 0.0216235, 0.0226494, 0.028717800000000002, 0.032664899999999997, 0.039195899999999999, 0.049169400000000002, 0.051135399999999998, 0.064867099999999997, 0.069808700000000001, 0.098762600000000006, 0.11527900000000001, 0.14865200000000001, 0.21105299999999999, 0.25422800000000001, 0.30155100000000001, 0.33953100000000003, 0.43132199999999998, 0.59130099999999997, 0.92331200000000002, 1.3285100000000001])

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
c.SaveAs('Inclusive_limit_obsexp_SplusB_WideJets_Zprime_fbb0.1.eps')

