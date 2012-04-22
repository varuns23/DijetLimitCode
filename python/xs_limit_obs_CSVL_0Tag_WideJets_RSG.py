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


BR = [0.1, 0.5, 0.75, 1.]

masses = array('d')
xs_limits = {}

########################################################
## Uncomment this part if running the limit code

#mass_start = 1000.
#mass_step = 100.
#steps = 30

#for br in range(0,len(BR)):

  #xs_limits_array = array('d')
 
  #for i in range(0,steps+1):

    #mass = mass_start + float(i)*mass_step

    #if(br==0): masses.append(mass)

    #cmd = "./stats " + str(mass) + " " + " " + str(BR[br])
    #print "Running: " + cmd
    #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
    #output = proc.communicate()[0]
    #if proc.returncode != 0:
      #print output
      #sys.exit(1)
    ##print output
    #outputlines =  output.split("\n")

    #for line in outputlines:
      #if re.search("observed bound =", line):
        #xs_limits_array.append(float(line.split()[6]))

  #xs_limits[br] = xs_limits_array


#print "masses:"
#print masses
#for br in range(0,len(BR)):
  #print "xs_limits, BR="+str(BR[br])+":"
  #print xs_limits[br]

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_limits[0] = array('d', [0.92874199999999996, 0.62878800000000001, 0.40017900000000001, 0.27797500000000003, 0.250915, 0.24896799999999999, 0.210754, 0.148449, 0.10424899999999999, 0.074073399999999998, 0.091264100000000001, 0.094143900000000003, 0.0892347, 0.073208999999999996, 0.055544700000000002, 0.046589499999999999, 0.0432062, 0.0390912, 0.0334116, 0.024611299999999999, 0.018625599999999999, 0.0130264, 0.0074468700000000004, 0.00558685, 0.0051220199999999997, 0.0051221699999999997, 0.0051221699999999997, 2.3708999999999864e-310, 2.3462900000000008e-310, 2.3700400000000076e-310, 2.3575100000000106e-310])
xs_limits[1] = array('d', [1.4005399999999999, 0.89487499999999998, 0.51598299999999997, 0.44567600000000002, 0.34542499999999998, 0.333735, 0.27648299999999998, 0.19139500000000001, 0.11734600000000001, 0.096251500000000004, 0.111668, 0.116525, 0.10648000000000001, 0.089807600000000001, 0.066659499999999997, 0.058584400000000002, 0.051985200000000002, 0.0458147, 0.039011299999999999, 0.0276858, 0.020483399999999999, 0.0148921, 0.0093107999999999993, 0.0065179399999999998, 0.0055874599999999998, 0.0055876099999999998, 0.0055877899999999996, 0.00558786, 0.0054203599999999999, 2.3700599999999773e-310, 0.0052139300000000003])
xs_limits[2] = array('d', [1.83256, 1.22027, 0.67835299999999998, 0.52399600000000002, 0.454011, 0.444328, 0.33168300000000001, 0.238122, 0.146121, 0.11768099999999999, 0.13591500000000001, 0.139547, 0.12618599999999999, 0.10399899999999999, 0.075838000000000003, 0.066569299999999998, 0.060065100000000003, 0.051823000000000001, 0.042484399999999999, 0.029779300000000002, 0.022344800000000001, 0.0148971, 0.0093107999999999993, 0.00745029, 0.0065188599999999996, 0.0065192000000000002, 0.0060535199999999997, 0.0060535600000000004, 0.0060025, 2.3189399999999759e-310, 0.00539157])
xs_limits[3] = array('d', [1.8963399999999999, 1.01139, 0.62498200000000004, 0.74349900000000002, 0.70381499999999997, 0.652443, 0.46548200000000001, 0.27313999999999999, 0.20443900000000001, 0.170154, 0.177175, 0.17220099999999999, 0.14990200000000001, 0.118579, 0.092372099999999999, 0.080055699999999994, 0.070419499999999996, 0.059425699999999998, 0.047353899999999997, 0.033526599999999997, 0.022278300000000001, 0.0148862, 0.0102419, 0.0074489100000000004, 0.0069845100000000002, 0.0069849100000000004, 0.0065191700000000003, 0.0065208799999999997, 0.00636149, 2.3701899999999775e-310, 0.0053248000000000002])

##
########################################################

m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
zprime = array('d', [0.2555E+02, 0.1211E+02, 0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
rsg = array('d', [0.4828E+02, 0.1862E+02, 0.8100E+01, 0.3852E+01, 0.1961E+01, 0.1053E+01, 0.5905E+00, 0.3426E+00, 0.2044E+00, 0.1248E+00, 0.7770E-01, 0.4911E-01, 0.3145E-01, 0.2036E-01, 0.1330E-01, 0.8743E-02, 0.5781E-02, 0.3840E-02, 0.2559E-02, 0.1708E-02, 0.1142E-02, 0.7635E-03, 0.5101E-03, 0.3402E-03, 0.2264E-03, 0.1501E-03, 0.9913E-04, 0.6512E-04, 0.4253E-04, 0.2759E-04, 0.1775E-04])
  
graphs = {}

for br in range(0,len(BR)):
  graphs[br] = TGraph(len(masses),masses,xs_limits[br])
  graphs[br].SetMarkerStyle(24+br)
  graphs[br].SetMarkerColor(kRed)
  graphs[br].SetLineWidth(2)
  graphs[br].SetLineStyle(1+br)
  graphs[br].SetLineColor(kRed)
  if br==0:
    graphs[br].GetXaxis().SetTitle("Resonance Mass [GeV]")
    graphs[br].GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
    graphs[br].GetYaxis().SetRangeUser(1e-03,10)

graph_zprime = TGraph(len(m_x),m_x,zprime)
graph_zprime.SetLineWidth(2)
graph_zprime.SetLineStyle(4)
graph_zprime.SetLineColor(38)

graph_rsg = TGraph(len(m_x),m_x,rsg)
graph_rsg.SetLineWidth(2)
graph_rsg.SetLineStyle(8)
graph_rsg.SetLineColor(32)

c = TCanvas("c", "",800,800)
c.cd()

for br in range(0,len(BR)):
  if br==0:
    graphs[br].Draw("ALP")
  else:
    graphs[br].Draw("LP")

#graph_rsg.Draw("L")

legend = TLegend(.50,.55,.90,.75)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
#legend.SetHeader("Obs. 95% CL Upper Limits (stat. only)")
legend.SetHeader("Obs. 95% CL Upper Limits")
for br in range(0,len(BR)):
  legend.AddEntry(graphs[br], "f_{b#bar{b}} = " + str(BR[br]),"lp")
legend.Draw()

legend2 = TLegend(.50,.75,.90,.8)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
legend2.SetFillStyle(0)
legend2.SetTextFont(42)
legend2.SetTextSize(0.03)
legend2.AddEntry(graph_rsg,"RS Graviton (f_{b#bar{b}} #approx 0.1)","l")
legend2.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.7,0.88, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.88, "RS-graviton-like")
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.43, "CMS Preliminary")
l1.DrawLatex(0.19,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.20,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.19,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL 0-tag")

c.SetLogy()
#c.SaveAs('CSVL_0Tag_limit_obs_WideJets_RSG.eps')
c.SaveAs('CSVL_0Tag_limit_obs_syst_WideJets_RSG.eps')

