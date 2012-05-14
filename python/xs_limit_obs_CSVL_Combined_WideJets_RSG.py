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

sys = True
#sys = False

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

# stat only
masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_limits[0] = array('d', [0.91840500000000003, 0.64281600000000005, 0.439716, 0.28312399999999999, 0.193718, 0.193715, 0.17894299999999999, 0.14064199999999999, 0.096857499999999999, 0.074507000000000004, 0.079943200000000006, 0.093831399999999995, 0.076404899999999998, 0.056770800000000003, 0.0477975, 0.045825999999999999, 0.040974299999999998, 0.031602900000000003, 0.022206500000000001, 0.015832499999999999, 0.0121072, 0.0093132300000000005, 0.0065192599999999998, 0.0055879399999999996, 0.0060536000000000001, 0.0060536000000000001, 0.0046566100000000003, 0.0051222999999999998, 0.0046566200000000002, 0.0037253299999999998, 0.0037253099999999999])
xs_limits[1] = array('d', [0.43779699999999999, 0.38328499999999999, 0.24687100000000001, 0.14901200000000001, 0.096857499999999999, 0.096857499999999999, 0.104308, 0.104522, 0.081644700000000001, 0.063330300000000006, 0.065327399999999994, 0.065512200000000007, 0.053470700000000003, 0.042758999999999998, 0.038424899999999998, 0.038156099999999998, 0.033347300000000003, 0.0249803, 0.017419, 0.0121072, 0.0093132400000000004, 0.00745058, 0.0055879399999999996, 0.0051222699999999999, 0.0051222699999999999, 0.0046566100000000003, 0.0041909499999999997, 0.0041909499999999997, 0.0037253, 0.0032596299999999999, 0.0027939699999999998])
xs_limits[2] = array('d', [0.30549300000000001, 0.27995999999999999, 0.18288399999999999, 0.104308, 0.074505799999999997, 0.070780499999999996, 0.081956399999999999, 0.084280599999999997, 0.067239599999999997, 0.054213600000000001, 0.0537452, 0.051319499999999997, 0.042871100000000002, 0.0344374, 0.0320953, 0.033284599999999998, 0.028316299999999999, 0.020636600000000001, 0.0150832, 0.011175900000000001, 0.0083818999999999994, 0.0065192599999999998, 0.0051222699999999999, 0.0046566100000000003, 0.0046566100000000003, 0.0044237800000000004, 0.00372529, 0.00349256, 0.0032596299999999999, 0.0027939900000000001, 0.0025611399999999999])
xs_limits[3] = array('d', [0.23189299999999999, 0.21570400000000001, 0.142873, 0.089408199999999993, 0.059604600000000001, 0.055879400000000003, 0.063330200000000003, 0.068946099999999996, 0.055141500000000003, 0.047260700000000003, 0.045235699999999997, 0.041274600000000002, 0.034078700000000003, 0.028853400000000001, 0.027792399999999998, 0.028545000000000001, 0.024106300000000001, 0.017650699999999998, 0.0129011, 0.0093133699999999996, 0.0074505999999999999, 0.0055879399999999996, 0.0046566100000000003, 0.0041909499999999997, 0.0041909800000000004, 0.0039581199999999999, 0.0034924600000000002, 0.0032596399999999998, 0.0030268600000000001, 0.0025611399999999999, 0.0020954799999999998])

if sys:
 # sys + stat
 masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
 xs_limits[0] = array('d', [0.97800900000000002, 0.70242099999999996, 0.46951799999999999, 0.32782800000000001, 0.208619, 0.193715, 0.186394, 0.15554299999999999, 0.111759, 0.089408199999999993, 0.091119099999999995, 0.090106099999999995, 0.083855499999999999, 0.067946599999999996, 0.055247999999999998, 0.046757399999999998, 0.042837, 0.0362595, 0.028725799999999999, 0.021420399999999999, 0.0149012, 0.011175900000000001, 0.0083818999999999994, 0.0065192599999999998, 0.0055879399999999996, 0.0055879399999999996, 0.0055879399999999996, 0.0051222999999999998, 0.0046566200000000002, 0.0044238200000000002, 0.0041909699999999996])
 xs_limits[1] = array('d', [0.46759899999999999, 0.42053800000000002, 0.291574, 0.178814, 0.111759, 0.104308, 0.111759, 0.108247, 0.092820600000000003, 0.070780899999999994, 0.069052699999999995, 0.067374799999999999, 0.059058699999999999, 0.049278299999999997, 0.041218900000000003, 0.038156099999999998, 0.035209900000000002, 0.0305682, 0.023938299999999999, 0.016763799999999999, 0.011175900000000001, 0.0083818999999999994, 0.0065192599999999998, 0.0055879399999999996, 0.0051222699999999999, 0.0046566100000000003, 0.0046566100000000003, 0.0041909499999999997, 0.0037253, 0.0034924600000000002, 0.0032596299999999999])
 xs_limits[2] = array('d', [0.33529500000000001, 0.302311, 0.21268699999999999, 0.13411000000000001, 0.081956399999999999, 0.074505799999999997, 0.0856817, 0.084280599999999997, 0.074690199999999998, 0.061664200000000002, 0.057470500000000001, 0.055044799999999998, 0.048459000000000002, 0.0400253, 0.034889299999999998, 0.033284599999999998, 0.0311103, 0.0271559, 0.020671100000000001, 0.0149012, 0.0107102, 0.00745058, 0.0055879399999999996, 0.0051222699999999999, 0.0046566100000000003, 0.0044237800000000004, 0.0039581199999999999, 0.0037253899999999999, 0.0032596299999999999, 0.0032596499999999998, 0.0027939699999999998])
 xs_limits[3] = array('d', [0.254245, 0.23805499999999999, 0.16522500000000001, 0.104309, 0.067055199999999995, 0.059604600000000001, 0.067055500000000004, 0.067083400000000001, 0.060729400000000003, 0.050985999999999997, 0.048960999999999998, 0.044999900000000002, 0.037803999999999997, 0.032578700000000002, 0.0296551, 0.028545000000000001, 0.026434599999999999, 0.023238700000000001, 0.018488999999999998, 0.0130387, 0.0093132500000000003, 0.0069849300000000003, 0.0055879399999999996, 0.0046566100000000003, 0.0041909800000000004, 0.00372529, 0.00372529, 0.0032596399999999998, 0.00325969, 0.0027939699999999998, 0.0023283100000000001])

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
graph_zprime.SetLineColor(32)

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

graph_rsg.Draw("L")

legend = TLegend(.45,.60,.85,.80)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
if sys: legend.SetHeader("Obs. 95% CL Upper Limits")
else:   legend.SetHeader("Obs. 95% CL Upper Limits (stat. only)")
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
legend2.Draw()

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
l1.DrawLatex(0.54,0.89, "0, 1 and 2 b-tags")

c.SetLogy()
if sys: c.SaveAs('CSVL_Combined_limit_obs_sys_WideJets_RSG.eps')
else:   c.SaveAs('CSVL_Combined_limit_obs_WideJets_RSG.eps')

