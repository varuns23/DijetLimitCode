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


BR = [0.2, 0.5, 0.75, 1.]

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

    #cmd = "./stats " + str(mass) + " " + str(BR[br]) + " qq"
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
xs_limits[0] = array('d', [0.70464700000000002, 0.40021200000000001, 0.29255900000000001, 0.20538600000000001, 0.20568, 0.20778199999999999, 0.12659999999999999, 0.081620399999999996, 0.0594178, 0.055867300000000002, 0.079219800000000007, 0.079516699999999996, 0.056551900000000002, 0.042545699999999999, 0.037728200000000003, 0.036620800000000002, 0.031417500000000001, 0.022860599999999998, 0.015871900000000001, 0.011174999999999999, 0.0074500699999999996, 0.0055878300000000002, 0.0041908400000000004, 0.0041909399999999998, 0.0041908700000000002, 0.0041908800000000001, 0.0044237599999999997, 0.0047135199999999997, 0.0044657899999999999, 0.0043142600000000003, 0.0037470699999999999])
xs_limits[1] = array('d', [0.99092499999999994, 0.53476999999999997, 0.40276400000000001, 0.287188, 0.28316999999999998, 0.27951300000000001, 0.178789, 0.11136500000000001, 0.081525, 0.070646100000000003, 0.098027799999999998, 0.10118000000000001, 0.073833999999999997, 0.055069, 0.047863900000000001, 0.046469700000000003, 0.039215699999999999, 0.028492, 0.0202658, 0.0139691, 0.0102445, 0.0065185599999999996, 0.0051220500000000004, 0.0046564099999999997, 0.0051222400000000001, 0.0051222500000000001, 0.0051222500000000001, 0.0053317800000000004, 0.0052072100000000003, 0.0048408599999999998, 0.00426919])
xs_limits[2] = array('d', [1.6298900000000001, 0.81216299999999997, 0.67333299999999996, 0.42422500000000002, 0.39669500000000002, 0.40598899999999999, 0.23630100000000001, 0.16314200000000001, 0.111081, 0.096546699999999999, 0.12259399999999999, 0.126466, 0.095592899999999995, 0.071042300000000003, 0.060760599999999998, 0.057215200000000001, 0.048915500000000001, 0.035801300000000001, 0.025181200000000001, 0.018626299999999998, 0.0130378, 0.0083814800000000002, 0.0065190600000000001, 0.0055874699999999998, 0.0055875999999999999, 0.0055877399999999999, 0.0055878500000000001, 0.0058815100000000004, 0.0056908000000000002, 0.0053538600000000002, 0.0045573599999999999])
xs_limits[3] = array('d', [3.9859200000000001, 1.7854699999999999, 0.97744399999999998, 0.75950099999999998, 0.64393900000000004, 0.68518299999999999, 0.41724699999999998, 0.26599600000000001, 0.19323799999999999, 0.13311200000000001, 0.16105800000000001, 0.17013300000000001, 0.13617399999999999, 0.101036, 0.081640400000000002, 0.076597499999999999, 0.066855999999999999, 0.048355700000000001, 0.034414800000000002, 0.024212399999999999, 0.016762300000000001, 0.011174, 0.0074491100000000001, 0.0065185299999999998, 0.0065189999999999996, 0.0065191800000000003, 0.0060534600000000001, 0.0065201299999999998, 0.00658962, 0.0058647200000000003, 0.0053180399999999996])

##
########################################################

m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
m_zprime = array('d', [700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800.])
#zprime = array('d', [0.2555E+02, 0.1211E+02, 0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
zprime = array('d', [0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
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

graph_zprime = TGraph(len(m_zprime),m_zprime,zprime)
graph_zprime.SetLineWidth(2)
graph_zprime.SetLineStyle(4)
graph_zprime.SetLineColor(30)

graph_rsg = TGraph(len(m_x),m_x,rsg)
graph_rsg.SetLineWidth(2)
graph_rsg.SetLineStyle(8)
graph_rsg.SetLineColor(46)

c = TCanvas("c", "",800,800)
c.cd()

for br in range(0,len(BR)):
  if br==0:
    graphs[br].Draw("ALP")
  else:
    graphs[br].Draw("LP")

#graph_zprime.Draw("L")

legend = TLegend(.45,.60,.85,.80)
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

legend2 = TLegend(.45,.80,.85,.85)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
legend2.SetFillStyle(0)
legend2.SetTextFont(42)
legend2.SetTextSize(0.03)
legend2.AddEntry(graph_zprime,"Z' (f_{b#bar{b}} #approx 0.2)","l")
#legend2.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.50, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.88, "Z'-like")
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.43, "CMS Preliminary")
l1.DrawLatex(0.19,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.20,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.19,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL 0-tag")

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obs_WideJets_Zprime.eps')
#c.SaveAs('CSVL_0Tag_limit_obs_sys_WideJets_Zprime.eps')
