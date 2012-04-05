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
xs_limits[0] = array('d', [1.18896, 0.90144400000000002, 0.86316400000000004, 0.67484, 0.33252300000000001, 0.29371700000000001, 0.295095, 0.24799599999999999, 0.178706, 0.134104, 0.111567, 0.10037, 0.078171299999999999, 0.063286300000000004, 0.052126499999999999, 0.050069900000000001, 0.045780399999999999, 0.036983700000000001, 0.028402899999999998, 0.023888800000000002, 0.022357399999999999, 0.0204061, 0.017530799999999999, 0.0140914, 0.012267500000000001, 0.0103552, 0.0081403699999999992, 0.0065191499999999996, 0.0051220800000000002, 0.0041908199999999996, 0.0037251799999999998])
xs_limits[1] = array('d', [0.86196899999999999, 0.65867600000000004, 0.57860199999999995, 0.464227, 0.24893399999999999, 0.20746800000000001, 0.21402299999999999, 0.179373, 0.12650800000000001, 0.0966833, 0.089395699999999995, 0.0771791, 0.0595819, 0.050279799999999999, 0.042826900000000001, 0.039688899999999999, 0.038232500000000003, 0.030439999999999998, 0.023666699999999999, 0.020066400000000002, 0.019188500000000001, 0.017895299999999999, 0.0152199, 0.012912399999999999, 0.0106785, 0.0093031599999999996, 0.0076646700000000002, 0.0060536100000000001, 0.0046564600000000003, 0.0037251599999999999, 0.0037252000000000001])
xs_limits[2] = array('d', [0.74908600000000003, 0.51893400000000001, 0.457036, 0.35646800000000001, 0.191135, 0.16267899999999999, 0.172653, 0.13731599999999999, 0.100545, 0.078146099999999996, 0.066999600000000006, 0.061770800000000001, 0.048416399999999998, 0.0428365, 0.035385, 0.033387600000000003, 0.031302700000000003, 0.026049099999999999, 0.019885900000000001, 0.0172018, 0.0165316, 0.0155703, 0.0139039, 0.0113087, 0.0096057, 0.0082821300000000004, 0.0067146300000000001, 0.0055878799999999999, 0.0046566000000000003, 0.0037251799999999998, 0.0032595100000000002])


m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
zprime = array('d', [0.2555E+02, 0.1211E+02, 0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
rsg = array('d', [0.4828E+02, 0.1862E+02, 0.8100E+01, 0.3852E+01, 0.1961E+01, 0.1053E+01, 0.5905E+00, 0.3426E+00, 0.2044E+00, 0.1248E+00, 0.7770E-01, 0.4911E-01, 0.3145E-01, 0.2036E-01, 0.1330E-01, 0.8743E-02, 0.5781E-02, 0.3840E-02, 0.2559E-02, 0.1708E-02, 0.1142E-02, 0.7635E-03, 0.5101E-03, 0.3402E-03, 0.2264E-03, 0.1501E-03, 0.9913E-04, 0.6512E-04, 0.4253E-04, 0.2759E-04, 0.1775E-04])
  

graph_1 = TGraph(len(masses),masses,xs_limits[0])
graph_1.SetMarkerStyle(24)
graph_1.SetMarkerColor(2)
graph_1.SetLineWidth(2)
#graph_1.SetLineStyle(1)
graph_1.SetLineColor(2)
graph_1.SetTitle("CSVL 1-tag, RSG-like resonances")
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
c.SaveAs('CSVL_1Tag_limit_obs_WideJets_RSG.png')

