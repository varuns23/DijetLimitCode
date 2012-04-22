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
xs_limits[0] = array('d', [0.84455400000000003, 0.56903199999999998, 0.39066400000000001, 0.25126100000000001, 0.16100200000000001, 0.17108599999999999, 0.155197, 0.11843099999999999, 0.081854899999999994, 0.055785099999999997, 0.059570600000000001, 0.075924400000000003, 0.064021300000000003, 0.046294599999999998, 0.037637799999999999, 0.036692700000000002, 0.036055499999999997, 0.027880200000000001, 0.018584, 0.0130381, 0.0102442, 0.0069846800000000001, 0.00512212, 0.0041908900000000001, 0.0041909499999999997, 0.0041909399999999998, 0.0037252600000000002, 0.0034924499999999998, 0.0032596299999999999, 0.0027939599999999998, 0.0025611399999999999])
xs_limits[1] = array('d', [0.432533, 0.38002399999999997, 0.23693, 0.14812900000000001, 0.095907300000000001, 0.096360699999999994, 0.104253, 0.101704, 0.075647199999999998, 0.055842999999999997, 0.057180000000000002, 0.062090199999999998, 0.0492615, 0.038636999999999998, 0.034674299999999998, 0.034761300000000002, 0.031689700000000001, 0.023953599999999999, 0.016654599999999999, 0.012107100000000001, 0.0088473100000000006, 0.0065191199999999998, 0.00512226, 0.0041908700000000002, 0.0041909, 0.0041909399999999998, 0.0037252700000000001, 0.0032596499999999998, 0.0030268299999999999, 0.0027939599999999998, 0.0023283000000000002])
xs_limits[2] = array('d', [0.308861, 0.277221, 0.18126600000000001, 0.103701, 0.074312799999999998, 0.070635699999999996, 0.081929500000000002, 0.083182599999999995, 0.064928100000000002, 0.053013699999999997, 0.054078899999999999, 0.0510549, 0.041157600000000003, 0.034181999999999997, 0.031474299999999997, 0.031844499999999998, 0.028106099999999998, 0.020654499999999999, 0.0144446, 0.011176200000000001, 0.0083819700000000007, 0.0065191900000000002, 0.0046564900000000001, 0.0041908800000000001, 0.0041909099999999999, 0.0041909499999999997, 0.00372529, 0.00325962, 0.0030267900000000001, 0.0025611200000000001, 0.0023283000000000002])
xs_limits[3] = array('d', [0.23540800000000001, 0.22064300000000001, 0.141955, 0.089298299999999997, 0.059579699999999999, 0.055848200000000001, 0.063300599999999999, 0.068544999999999995, 0.055856500000000003, 0.047780000000000003, 0.045319100000000001, 0.041353500000000001, 0.035121100000000002, 0.028977300000000001, 0.027883600000000001, 0.0285983, 0.024207200000000002, 0.017708100000000001, 0.012898700000000001, 0.0093129700000000003, 0.0074504300000000001, 0.0055876600000000004, 0.0046565699999999996, 0.0041908900000000001, 0.0041909199999999999, 0.0039581, 0.0034924399999999999, 0.00325962, 0.00302681, 0.00256113, 0.0020954599999999999])

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

graph_rsg.Draw("L")

legend = TLegend(.45,.55,.85,.75)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader("Obs. 95% CL Upper Limits (stat. only)")
#legend.SetHeader("Obs. 95% CL Upper Limits")
for br in range(0,len(BR)):
  legend.AddEntry(graphs[br], "f_{b#bar{b}} = " + str(BR[br]),"lp")
legend.Draw()

legend2 = TLegend(.45,.75,.85,.8)
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
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL Combined")

c.SetLogy()
c.SaveAs('CSVL_Combined_limit_obs_WideJets_RSG.eps')
c.SaveAs('CSVL_Combined_limit_obs_syst_WideJets_RSG.eps')

