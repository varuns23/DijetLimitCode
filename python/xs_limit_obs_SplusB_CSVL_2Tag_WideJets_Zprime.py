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
xs_limits[0] = array('d', [2.90082, 2.9872800000000002, 0.59982899999999995, 0.37243399999999999, 0.27665600000000001, 0.25980199999999998, 0.28221000000000002, 0.44855099999999998, 0.39683200000000002, 0.329845, 0.25688, 0.190578, 0.15870999999999999, 0.14032800000000001, 0.15323300000000001, 0.13967099999999999, 0.099022899999999997, 0.065516900000000003, 0.0496476, 0.037160400000000003, 0.0290733, 0.024192700000000001, 0.023491399999999999, 0.024993600000000001, 0.025384299999999999, 0.025332500000000001, 0.023451900000000001, 0.021084499999999999, 0.019074600000000001, 0.017622700000000002, 0.0167466])
xs_limits[1] = array('d', [1.28383, 1.40899, 0.283391, 0.177841, 0.133105, 0.124541, 0.13644700000000001, 0.22184699999999999, 0.21121300000000001, 0.18620900000000001, 0.14754400000000001, 0.11654100000000001, 0.095602199999999998, 0.085517899999999994, 0.093782500000000005, 0.088273500000000005, 0.066692000000000001, 0.046254099999999999, 0.0349444, 0.026463799999999999, 0.020531400000000002, 0.017371000000000001, 0.016812000000000001, 0.0177041, 0.018889800000000002, 0.018755899999999999, 0.017786099999999999, 0.016527799999999999, 0.015620800000000001, 0.014930499999999999, 0.0144882])
xs_limits[2] = array('d', [0.87878299999999998, 0.97362899999999997, 0.1956, 0.120749, 0.095921500000000007, 0.089155700000000004, 0.098942199999999994, 0.15573300000000001, 0.15298600000000001, 0.13705500000000001, 0.10968799999999999, 0.086130700000000004, 0.070879399999999995, 0.063948000000000005, 0.071501099999999998, 0.068053699999999995, 0.052450499999999997, 0.036315199999999999, 0.027562400000000001, 0.021820200000000001, 0.0165621, 0.0148234, 0.0140333, 0.0143982, 0.0153229, 0.015433499999999999, 0.014871000000000001, 0.014185700000000001, 0.0135689, 0.013563, 0.0133607])
xs_limits[3] = array('d', [0.66451700000000002, 0.74971500000000002, 0.15204999999999999, 0.095940600000000001, 0.071796100000000002, 0.067025000000000001, 0.073977200000000007, 0.12003999999999999, 0.118339, 0.107485, 0.086550799999999997, 0.068635299999999996, 0.0575513, 0.051684000000000001, 0.056857499999999998, 0.054828200000000001, 0.042849400000000003, 0.029999000000000001, 0.0237816, 0.0180587, 0.0139991, 0.012295499999999999, 0.011739899999999999, 0.012433899999999999, 0.012970300000000001, 0.013180300000000001, 0.012853399999999999, 0.0127292, 0.012452, 0.012067700000000001, 0.012049000000000001])

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
    graphs[br].GetYaxis().SetRangeUser(1e-03,20)
    graphs[br].GetXaxis().SetNdivisions(1005)

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

legend = TLegend(.45,.61,.85,.81)
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
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.89, "qq/bb")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.055)
l1.DrawLatex(0.73,0.89, "2 b-tags")

c.SetLogy()
c.SaveAs('CSVL_2Tag_limit_obs_SplusB_WideJets_Zprime.eps')
#c.SaveAs('CSVL_2Tag_limit_obs_SplusB_sys_WideJets_Zprime.eps')

