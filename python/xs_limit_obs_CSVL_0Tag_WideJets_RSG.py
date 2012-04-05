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


BR = [0.1, 0.5, 0.9]

masses = array('d')
xs_limits = {}

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


masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_limits[0] = array('d', [1.0177499999999999, 0.60202, 0.41259600000000002, 0.29283599999999999, 0.23530300000000001, 0.26408900000000002, 0.186449, 0.118809, 0.0815361, 0.067048399999999994, 0.078725400000000001, 0.098862599999999995, 0.078056799999999996, 0.0565791, 0.046109700000000003, 0.044136799999999997, 0.042512899999999999, 0.033280799999999999, 0.0237717, 0.0176949, 0.0121063, 0.0083816199999999993, 0.0055874100000000001, 0.0046563799999999999, 0.0046564299999999996, 0.0051222400000000001, 0.0046565, 0.0051222300000000002, 0.0054449900000000002, 0.0049794699999999997, 0.0047173500000000004])
xs_limits[1] = array('d', [1.6256200000000001, 0.89347600000000005, 0.59616100000000005, 0.39439800000000003, 0.34607599999999999, 0.36633300000000002, 0.25987700000000002, 0.17072100000000001, 0.111279, 0.089118100000000006, 0.101201, 0.13009200000000001, 0.099416400000000002, 0.071455900000000003, 0.057708700000000002, 0.0551163, 0.052176399999999998, 0.0415168, 0.028389999999999999, 0.0214196, 0.0149003, 0.0093119899999999992, 0.00651835, 0.0055875200000000003, 0.0055876600000000004, 0.0055876900000000002, 0.0055878100000000003, 0.0055878400000000002, 0.0059861999999999997, 0.0055272400000000001, 0.0050129800000000002])
xs_limits[2] = array('d', [2.8420100000000001, 1.48421, 1.04617, 0.79918199999999995, 0.62235700000000005, 0.64567699999999995, 0.41905300000000001, 0.26566699999999999, 0.17696600000000001, 0.117315, 0.14196400000000001, 0.18292600000000001, 0.13848199999999999, 0.098211599999999996, 0.078342400000000006, 0.072125800000000004, 0.067129900000000006, 0.052198599999999998, 0.036279899999999997, 0.0260763, 0.0186248, 0.011172700000000001, 0.0074494699999999997, 0.0065184800000000001, 0.0065187500000000002, 0.0065191700000000003, 0.0065191700000000003, 0.0060534999999999999, 0.00654304, 0.0060945699999999997, 0.0055277599999999996])


m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
zprime = array('d', [0.2555E+02, 0.1211E+02, 0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
rsg = array('d', [0.4828E+02, 0.1862E+02, 0.8100E+01, 0.3852E+01, 0.1961E+01, 0.1053E+01, 0.5905E+00, 0.3426E+00, 0.2044E+00, 0.1248E+00, 0.7770E-01, 0.4911E-01, 0.3145E-01, 0.2036E-01, 0.1330E-01, 0.8743E-02, 0.5781E-02, 0.3840E-02, 0.2559E-02, 0.1708E-02, 0.1142E-02, 0.7635E-03, 0.5101E-03, 0.3402E-03, 0.2264E-03, 0.1501E-03, 0.9913E-04, 0.6512E-04, 0.4253E-04, 0.2759E-04, 0.1775E-04])
  

graph_1 = TGraph(len(masses),masses,xs_limits[0])
graph_1.SetMarkerStyle(24)
graph_1.SetMarkerColor(2)
graph_1.SetLineWidth(2)
#graph_1.SetLineStyle(1)
graph_1.SetLineColor(2)
graph_1.SetTitle("CSVL 0-tag, RSG-like resonances")
graph_1.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_1.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_1.GetYaxis().SetRangeUser(1e-03,10)

graph_2 = TGraph(len(masses),masses,xs_limits[1])
graph_2.SetMarkerStyle(25)
graph_2.SetMarkerColor(1)
graph_2.SetLineWidth(2)
#graph_2.SetLineStyle(5)
graph_2.SetLineColor(1)

graph_3 = TGraph(len(masses),masses,xs_limits[2])
graph_3.SetMarkerStyle(26)
graph_3.SetMarkerColor(4)
graph_3.SetLineWidth(2)
#graph_3.SetLineStyle(5)
graph_3.SetLineColor(4)

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

graph_1.Draw("ALP")
graph_2.Draw("LP")
graph_3.Draw("LP")
#graph_rsg.Draw("L")

legend = TLegend(.6,.52,.85,.65)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(graph_1,"F_{b#bar{b}}=" + str(BR[0]),"lp")
legend.AddEntry(graph_2,"F_{b#bar{b}}=" + str(BR[1]),"lp")
legend.AddEntry(graph_3,"F_{b#bar{b}}=" + str(BR[2]),"lp")
legend.Draw()

legend2 = TLegend(.45,.8,.85,.85)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
legend2.SetFillStyle(0)
legend2.SetTextFont(42)
legend2.SetTextSize(0.035)
legend2.AddEntry(graph_rsg,"RS Graviton (F_{b#bar{b}}#approx0.1)","l")
#legend2.Draw()

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

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obs_WideJets_RSG.png')

