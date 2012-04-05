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


BR = [0.2, 0.5, 0.9]

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
xs_limits[0] = array('d', [0.50783599999999995, 0.34006900000000001, 0.23968500000000001, 0.148955, 0.11122700000000001, 0.123711, 0.096838499999999994, 0.070740300000000006, 0.048370999999999997, 0.044660100000000001, 0.0611446, 0.055596100000000002, 0.0388622, 0.030060699999999999, 0.028590899999999999, 0.029869199999999999, 0.023289000000000001, 0.015781900000000001, 0.0111766, 0.0079160700000000007, 0.0060534400000000002, 0.0041908700000000002, 0.0034924600000000002, 0.00325961, 0.00325961, 0.0032596299999999999, 0.0030267900000000001, 0.0027939699999999998, 0.0023286600000000002, 0.0020954900000000002, 0.0017462300000000001])
xs_limits[1] = array('d', [0.39133299999999999, 0.29750300000000002, 0.19945399999999999, 0.111266, 0.081364000000000006, 0.096820900000000001, 0.089407399999999998, 0.072364800000000007, 0.052127100000000003, 0.044679900000000002, 0.056972799999999997, 0.050021500000000003, 0.036442099999999998, 0.0289039, 0.027762599999999998, 0.028678700000000001, 0.022878099999999998, 0.015081000000000001, 0.0111758, 0.0079161100000000005, 0.0060534500000000002, 0.0041908600000000002, 0.0034924299999999999, 0.0032596000000000001, 0.0034924499999999998, 0.00325962, 0.0030267900000000001, 0.0027939699999999998, 0.0023283000000000002, 0.0020954699999999999, 0.0017462300000000001])
xs_limits[2] = array('d', [0.25046499999999999, 0.21282699999999999, 0.14024500000000001, 0.081737000000000004, 0.055721600000000003, 0.059510500000000001, 0.067862900000000004, 0.063094499999999998, 0.049590299999999997, 0.044045399999999998, 0.047011400000000002, 0.039945899999999999, 0.029965800000000001, 0.0259256, 0.0247513, 0.025495400000000001, 0.020074499999999999, 0.0136116, 0.010245000000000001, 0.0074504799999999998, 0.0060535299999999997, 0.0041908600000000002, 0.00349242, 0.0034924600000000002, 0.0034924499999999998, 0.0032596299999999999, 0.0030267900000000001, 0.00256113, 0.0023283599999999998, 0.00186265, 0.0017462300000000001])


m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
m_zprime = array('d', [700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800.])
#zprime = array('d', [0.2555E+02, 0.1211E+02, 0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
zprime = array('d', [0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
rsg = array('d', [0.4828E+02, 0.1862E+02, 0.8100E+01, 0.3852E+01, 0.1961E+01, 0.1053E+01, 0.5905E+00, 0.3426E+00, 0.2044E+00, 0.1248E+00, 0.7770E-01, 0.4911E-01, 0.3145E-01, 0.2036E-01, 0.1330E-01, 0.8743E-02, 0.5781E-02, 0.3840E-02, 0.2559E-02, 0.1708E-02, 0.1142E-02, 0.7635E-03, 0.5101E-03, 0.3402E-03, 0.2264E-03, 0.1501E-03, 0.9913E-04, 0.6512E-04, 0.4253E-04, 0.2759E-04, 0.1775E-04])
  

graph_1 = TGraph(len(masses),masses,xs_limits[0])
graph_1.SetMarkerStyle(24)
graph_1.SetMarkerColor(2)
graph_1.SetLineWidth(2)
#graph_1.SetLineStyle(1)
graph_1.SetLineColor(2)
graph_1.SetTitle("CSVL Combined, Z'-like resonances")
graph_1.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_1.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_1.GetYaxis().SetRangeUser(1e-03,100)

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

graph_zprime = TGraph(len(m_zprime),m_zprime,zprime)
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
graph_zprime.Draw("L")

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

legend2 = TLegend(.6,.8,.85,.85)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
legend2.SetFillStyle(0)
legend2.SetTextFont(42)
legend2.SetTextSize(0.035)
legend2.AddEntry(graph_zprime,"Z' (F_{b#bar{b}}#approx0.2)","l")
legend2.Draw()

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
c.SaveAs('CSVL_Combined_limit_obs_WideJets_Zprime.png')

