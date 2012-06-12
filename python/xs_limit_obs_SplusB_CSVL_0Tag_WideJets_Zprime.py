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
xs_limits[0] = array('d', [1.5998000000000001, 0.38508100000000001, 0.29321999999999998, 0.21040800000000001, 0.210123, 0.26554899999999998, 0.118214, 0.082263699999999995, 0.060567099999999999, 0.053768700000000003, 0.097873699999999994, 0.10087400000000001, 0.064444799999999997, 0.043681999999999999, 0.040763500000000001, 0.043915500000000003, 0.036867499999999997, 0.023626100000000001, 0.014848200000000001, 0.0108936, 0.0073457499999999998, 0.0051171999999999997, 0.0040557500000000003, 0.0039549399999999997, 0.0041649900000000004, 0.00423749, 0.0043254599999999997, 0.0045079500000000002, 0.0045787800000000002, 0.0042236699999999997, 0.0036154])
xs_limits[1] = array('d', [2.3970400000000001, 0.55914799999999998, 0.41513600000000001, 0.30263299999999999, 0.28721999999999998, 0.36632599999999998, 0.16723199999999999, 0.109402, 0.083221400000000001, 0.070849899999999993, 0.123665, 0.13082299999999999, 0.085431800000000002, 0.059068200000000001, 0.053275099999999999, 0.056575899999999998, 0.047436699999999998, 0.031457600000000002, 0.019466399999999998, 0.013558799999999999, 0.0095207699999999996, 0.0066265400000000002, 0.0050254000000000002, 0.0047861800000000001, 0.0049607499999999999, 0.0049728000000000003, 0.0050108499999999999, 0.0051881599999999998, 0.0052490999999999996, 0.0048159800000000001, 0.00413014])
xs_limits[2] = array('d', [4.1207500000000001, 0.88513600000000003, 0.66249400000000003, 0.453573, 0.40537200000000001, 0.54061199999999998, 0.23985699999999999, 0.15992600000000001, 0.11347699999999999, 0.097030099999999994, 0.15374199999999999, 0.17300099999999999, 0.11791500000000001, 0.078646999999999995, 0.070085900000000007, 0.074074200000000007, 0.062968200000000002, 0.0417504, 0.025873400000000001, 0.017846899999999999, 0.0126543, 0.0082157700000000007, 0.0063725099999999996, 0.0058917400000000003, 0.0059161700000000001, 0.0058248500000000003, 0.00576838, 0.0059174900000000001, 0.0059704199999999997, 0.0054497, 0.0047564599999999997])
xs_limits[3] = array('d', [13.6807, 2.1728999999999998, 1.5054099999999999, 0.92987600000000004, 0.74583600000000005, 0.96355400000000002, 0.46631, 0.27215299999999998, 0.19447999999999999, 0.139261, 0.19076499999999999, 0.24138499999999999, 0.182144, 0.122752, 0.101424, 0.102705, 0.090271000000000004, 0.062883400000000006, 0.038600799999999998, 0.024863199999999998, 0.017242400000000001, 0.0116696, 0.0081960599999999998, 0.0072483399999999998, 0.0068859500000000001, 0.0066315599999999999, 0.0064130300000000001, 0.0065288100000000003, 0.00669683, 0.0062202500000000001, 0.0054759199999999996])

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
    graphs[br].GetYaxis().SetRangeUser(1e-03,40)
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
l1.DrawLatex(0.73,0.89, "0 b-tags")

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obs_SplusB_WideJets_Zprime.eps')
#c.SaveAs('CSVL_0Tag_limit_obs_SplusB_sys_WideJets_Zprime.eps')

