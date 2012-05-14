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

    #cmd = "./stats " + str(mass) + " " + str(BR[br]) + " gg"
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
xs_limits[0] = array('d', [1.60934, 1.1325499999999999, 0.938527, 0.763042, 0.44703700000000002, 0.357628, 0.34501300000000001, 0.29028500000000002, 0.208616, 0.16392000000000001, 0.13411000000000001, 0.120104, 0.096857799999999994, 0.081956500000000002, 0.067055299999999998, 0.063472200000000006, 0.058194000000000003, 0.048683799999999999, 0.038522899999999999, 0.032048399999999998, 0.028959599999999999, 0.026836100000000002, 0.022471600000000001, 0.018886799999999999, 0.0154016, 0.013262400000000001, 0.011175900000000001, 0.0093132300000000005, 0.00745058, 0.0065192599999999998, 0.0055879399999999996])
xs_limits[1] = array('d', [0.89414899999999997, 0.65586800000000001, 0.55800000000000005, 0.420846, 0.25332100000000002, 0.208616, 0.20999399999999999, 0.17535700000000001, 0.12665999999999999, 0.096857600000000002, 0.089407700000000007, 0.076122800000000004, 0.059604699999999997, 0.052154100000000002, 0.044703699999999999, 0.043428899999999999, 0.039156499999999997, 0.032226400000000002, 0.025870500000000001, 0.023134200000000001, 0.020968199999999999, 0.0189772, 0.015819, 0.013831, 0.0119985, 0.0099084800000000008, 0.0083819099999999994, 0.0065192599999999998, 0.0055879399999999996, 0.0046566200000000002, 0.0041909499999999997])
xs_limits[2] = array('d', [0.71526000000000001, 0.50664200000000004, 0.43785000000000002, 0.32938699999999999, 0.193715, 0.17136399999999999, 0.17085700000000001, 0.13341700000000001, 0.10058300000000001, 0.081956399999999999, 0.070780700000000002, 0.0605599, 0.050291500000000003, 0.0447035, 0.037253000000000001, 0.035174999999999998, 0.032170900000000002, 0.026556400000000001, 0.0217019, 0.019181900000000002, 0.017833399999999999, 0.016099700000000002, 0.014037300000000001, 0.011798299999999999, 0.010514000000000001, 0.0084559300000000004, 0.0069851000000000002, 0.0060536000000000001, 0.0051222699999999999, 0.0041909499999999997, 0.00372529])
xs_limits[3] = array('d', [0.56625700000000001, 0.41724, 0.36601600000000001, 0.27472800000000003, 0.163913, 0.14156099999999999, 0.13936000000000001, 0.115624, 0.0856817, 0.067055199999999995, 0.059604900000000002, 0.0508809, 0.042843800000000001, 0.0372544, 0.031670200000000003, 0.030882099999999999, 0.027545300000000002, 0.023142099999999999, 0.018643699999999999, 0.0162133, 0.0156945, 0.014283799999999999, 0.0123155, 0.010220999999999999, 0.0090086300000000001, 0.0074947800000000004, 0.0060536000000000001, 0.0051222699999999999, 0.0041909499999999997, 0.00372529, 0.0032596299999999999])

##
########################################################

m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
zprime = array('d', [0.2555E+02, 0.1211E+02, 0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
rsg = array('d', [0.4828E+02, 0.1862E+02, 0.8100E+01, 0.3852E+01, 0.1961E+01, 0.1053E+01, 0.5905E+00, 0.3426E+00, 0.2044E+00, 0.1248E+00, 0.7770E-01, 0.4911E-01, 0.3145E-01, 0.2036E-01, 0.1330E-01, 0.8743E-02, 0.5781E-02, 0.3840E-02, 0.2559E-02, 0.1708E-02, 0.1142E-02, 0.7635E-03, 0.5101E-03, 0.3402E-03, 0.2264E-03, 0.1501E-03, 0.9913E-04, 0.6512E-04, 0.4253E-04, 0.2759E-04, 0.1775E-04])
  
graphs = {}

for br in range(0,len(BR)):
  graphs[br] = TGraph(len(masses),masses,xs_limits[br])
  graphs[br].SetMarkerStyle(24+br)
  graphs[br].SetMarkerColor(kGreen+2)
  graphs[br].SetLineWidth(2)
  graphs[br].SetLineStyle(1+br)
  graphs[br].SetLineColor(kGreen+2)
  if br==0:
    graphs[br].GetXaxis().SetTitle("Resonance Mass [GeV]")
    graphs[br].GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
    graphs[br].GetYaxis().SetRangeUser(1e-03,10)
    graphs[br].GetXaxis().SetNdivisions(1005)

graph_zprime = TGraph(len(m_x),m_x,zprime)
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

#graph_rsg.Draw("L")

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
legend2.AddEntry(graph_rsg,"RS Graviton (f_{b#bar{b}} #approx 0.1)","l")
#legend2.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.89, "RS-graviton-like")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.055)
l1.DrawLatex(0.73,0.89, "1 b-tag")

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obs_WideJets_RSG.eps')
#c.SaveAs('CSVL_1Tag_limit_obs_sys_WideJets_RSG.eps')

