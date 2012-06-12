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
xs_obs_limits = array('d', [0.90750799999999998, 0.68018800000000001, 1.02485, 0.58159400000000006, 0.259799, 0.21059700000000001, 0.22375, 0.205813, 0.12785099999999999, 0.10019, 0.090565599999999996, 0.078652299999999994, 0.063189400000000007, 0.053393999999999997, 0.047377099999999998, 0.048242699999999999, 0.045711099999999998, 0.036026500000000003, 0.027143400000000002, 0.024130100000000002, 0.024403000000000001, 0.022865400000000001, 0.018425799999999999, 0.0141981, 0.0125425, 0.010423099999999999, 0.00855326, 0.00695855, 0.00609072, 0.0050527599999999999, 0.00459341])
xs_exp_limits = array('d', [0.95850500000000005, 0.68704799999999999, 0.496919, 0.39244000000000001, 0.33507599999999998, 0.24924099999999999, 0.19419700000000001, 0.16566, 0.13798199999999999, 0.113357, 0.094843899999999995, 0.075861399999999996, 0.061410899999999997, 0.050872399999999998, 0.047201199999999999, 0.0421512, 0.034399100000000002, 0.0283214, 0.024642799999999999, 0.0218216, 0.017371500000000002, 0.015172400000000001, 0.0134821, 0.0129006, 0.011890100000000001, 0.0098731300000000008, 0.0081835399999999996, 0.0073717899999999996, 0.0067938599999999997, 0.0063559200000000001, 0.0063323299999999997])

masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.88308600000000004, 0.59843900000000005, 0.42592600000000003, 0.338167, 0.25199100000000002, 0.19923299999999999, 0.16727500000000001, 0.13192899999999999, 0.10699500000000001, 0.090469800000000003, 0.073923000000000003, 0.063133999999999996, 0.051192599999999998, 0.041979500000000003, 0.037981599999999997, 0.032744299999999997, 0.0258117, 0.0233633, 0.020070500000000002, 0.017787000000000001, 0.014408000000000001, 0.012862800000000001, 0.011608200000000001, 0.0099948899999999993, 0.0085986900000000008, 0.0076240400000000003, 0.0067080999999999998, 0.0058714400000000003, 0.0053561199999999998, 0.0048889700000000003, 0.00460788, 0.0080693399999999995, 0.0084833200000000008, 0.0090608100000000007, 0.0095585700000000006, 0.011056, 0.01387, 0.019204100000000002, 0.018585399999999998, 0.0201835, 0.025488199999999999, 0.028816600000000001, 0.032062899999999998, 0.034492099999999998, 0.042038300000000001, 0.056801400000000002, 0.062857999999999997, 0.072486300000000004, 0.076712100000000005, 0.096226599999999995, 0.10974399999999999, 0.15131, 0.21567900000000001, 0.24290300000000001, 0.29620200000000002, 0.36731399999999997, 0.441303, 0.59266399999999997, 0.75858000000000003, 1.2620199999999999, 1.46062, 2.4878999999999998])
xs_exp_limits_2sigma = array('d', [0.80014399999999997, 0.52066699999999999, 0.40330500000000002, 0.29433199999999998, 0.21113799999999999, 0.182227, 0.14305300000000001, 0.10653799999999999, 0.0968329, 0.075962100000000005, 0.054656799999999998, 0.052928799999999998, 0.038289700000000003, 0.032582, 0.029248799999999998, 0.024925599999999999, 0.021395299999999999, 0.020056399999999999, 0.0177825, 0.014572699999999999, 0.013299699999999999, 0.010385399999999999, 0.0093713200000000007, 0.0081296800000000002, 0.0075864000000000001, 0.0065824000000000004, 0.0057532900000000003, 0.0047146599999999999, 0.0041897499999999999, 0.0038415099999999998, 0.0038071200000000002, 0.010430699999999999, 0.0113721, 0.0151561, 0.0173571, 0.0195713, 0.020211, 0.0237647, 0.027998800000000001, 0.027000900000000001, 0.033377200000000003, 0.041972099999999998, 0.048486599999999998, 0.062829999999999997, 0.076244900000000004, 0.083585000000000007, 0.080803600000000003, 0.100606, 0.114843, 0.13139100000000001, 0.16984399999999999, 0.19265599999999999, 0.278779, 0.33441799999999999, 0.40260499999999999, 0.56746600000000003, 0.61752399999999996, 0.78413100000000002, 1.2642199999999999, 1.7155899999999999, 2.2888500000000001, 4.1962400000000004])

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
l1.DrawLatex(0.50,0.80, "1 b-tag")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obsexp_SplusB_WideJets_RSG.eps')

