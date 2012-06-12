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
xs_limits[0] = array('d', [0.85445099999999996, 0.78585099999999997, 0.96811800000000003, 0.409306, 0.23324700000000001, 0.21260399999999999, 0.25726700000000002, 0.16900399999999999, 0.113299, 0.094995200000000002, 0.083703899999999998, 0.069852899999999996, 0.054756600000000002, 0.047963499999999999, 0.040799799999999997, 0.043386000000000001, 0.036624700000000003, 0.026113399999999998, 0.021159799999999999, 0.019002399999999999, 0.019168899999999999, 0.0170061, 0.013731699999999999, 0.0106233, 0.0089007400000000007, 0.0072428800000000002, 0.0060652900000000001, 0.0047389600000000004, 0.0038748099999999998, 0.0033785199999999999, 0.0030287600000000001])
xs_limits[1] = array('d', [0.75467799999999996, 0.58679800000000004, 0.84500399999999998, 0.38989400000000002, 0.20621400000000001, 0.18512999999999999, 0.21431500000000001, 0.14908099999999999, 0.10109799999999999, 0.083003400000000005, 0.073210999999999998, 0.062308700000000002, 0.050050600000000001, 0.043575200000000001, 0.0372498, 0.038969799999999999, 0.034799099999999999, 0.0260472, 0.020568900000000001, 0.018407199999999999, 0.018806699999999999, 0.017017299999999999, 0.013887399999999999, 0.010777399999999999, 0.00911672, 0.0074973399999999999, 0.0063600499999999999, 0.0049948600000000003, 0.00407216, 0.00361933, 0.0031963299999999998])
xs_limits[2] = array('d', [0.65947299999999998, 0.49587999999999999, 0.76022599999999996, 0.37096899999999999, 0.192137, 0.161028, 0.18387700000000001, 0.14260999999999999, 0.095855200000000002, 0.075128200000000006, 0.065991800000000003, 0.057003499999999999, 0.048269600000000003, 0.040273499999999997, 0.034602800000000003, 0.0363256, 0.033225900000000003, 0.025217, 0.020076799999999999, 0.017844599999999999, 0.0184292, 0.016918800000000001, 0.0139337, 0.010843800000000001, 0.0092527800000000004, 0.00767097, 0.0063374299999999998, 0.0052072799999999999, 0.0042720800000000001, 0.0036376199999999998, 0.00334287])
xs_limits[3] = array('d', [0.58825499999999997, 0.430425, 0.67470699999999995, 0.35361399999999998, 0.17224100000000001, 0.141795, 0.15926499999999999, 0.130971, 0.086877700000000002, 0.0682059, 0.059833799999999999, 0.052392300000000003, 0.044436799999999999, 0.037442299999999998, 0.032192100000000001, 0.033875599999999999, 0.031557700000000001, 0.0243699, 0.019467100000000001, 0.0172281, 0.017908, 0.0167256, 0.0139174, 0.011453100000000001, 0.0093498399999999999, 0.0078174999999999998, 0.0064651400000000003, 0.0054389299999999998, 0.0044727300000000003, 0.0038051399999999998, 0.0035272900000000002])

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
l1.DrawLatex(0.73,0.89, "1 b-tag")

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obs_SplusB_WideJets_Zprime.eps')
#c.SaveAs('CSVL_1Tag_limit_obs_SplusB_sys_WideJets_Zprime.eps')

