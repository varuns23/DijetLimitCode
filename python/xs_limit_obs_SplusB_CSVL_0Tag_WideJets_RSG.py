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
xs_limits[0] = array('d', [5.7052199999999997, 0.76829599999999998, 0.53834000000000004, 0.38891999999999999, 0.30699100000000001, 0.419852, 0.26358700000000002, 0.16619400000000001, 0.114814, 0.093189099999999997, 0.100038, 0.18947900000000001, 0.15043200000000001, 0.099625000000000005, 0.077364100000000005, 0.074862100000000001, 0.068885000000000002, 0.052365000000000002, 0.030424099999999999, 0.021361999999999999, 0.016102600000000002, 0.0116752, 0.0083452800000000001, 0.0072781900000000004, 0.0073233999999999999, 0.0073699899999999999, 0.0066096799999999997, 0.0078755300000000004, 0.0078886200000000007, 0.0072563100000000002, 0.0071528399999999997])
xs_limits[1] = array('d', [7.9084599999999998, 1.0408999999999999, 0.75112900000000005, 0.51186500000000001, 0.407723, 0.57094800000000001, 0.32891100000000001, 0.20019600000000001, 0.14044599999999999, 0.10757700000000001, 0.12765499999999999, 0.21018100000000001, 0.16479099999999999, 0.108873, 0.086758299999999997, 0.085432999999999995, 0.077850699999999995, 0.056861599999999998, 0.034578499999999998, 0.0232851, 0.0166269, 0.0116968, 0.0082666900000000001, 0.0071024699999999996, 0.0071609000000000004, 0.0070475199999999998, 0.00653047, 0.0072489399999999997, 0.00723005, 0.00670413, 0.0063935399999999996])
xs_limits[2] = array('d', [10.1937, 1.44557, 0.98761900000000002, 0.67476199999999997, 0.52472799999999997, 0.71476099999999998, 0.375027, 0.22928299999999999, 0.16339899999999999, 0.12086, 0.15559000000000001, 0.225075, 0.17462900000000001, 0.116019, 0.093592800000000004, 0.093631000000000006, 0.0842556, 0.0598512, 0.0348662, 0.0247046, 0.0169365, 0.0116937, 0.0082033899999999996, 0.0071779599999999997, 0.0069974700000000004, 0.0068375800000000002, 0.0064738399999999998, 0.0068834500000000002, 0.0068993300000000004, 0.0064722900000000003, 0.0058353199999999997])
xs_limits[3] = array('d', [13.6807, 2.1728999999999998, 1.5054099999999999, 0.92987600000000004, 0.74583600000000005, 0.96355400000000002, 0.46631, 0.27215299999999998, 0.19447999999999999, 0.139261, 0.19076499999999999, 0.24138499999999999, 0.182144, 0.122752, 0.101424, 0.102705, 0.090271000000000004, 0.062883400000000006, 0.038600799999999998, 0.024863199999999998, 0.017242400000000001, 0.0116696, 0.0081960599999999998, 0.0072483399999999998, 0.0068859500000000001, 0.0066315599999999999, 0.0064130300000000001, 0.0065288100000000003, 0.00669683, 0.0062202500000000001, 0.0054759199999999996])

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
    graphs[br].GetYaxis().SetRangeUser(1e-03,40)
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
l1.DrawLatex(0.18,0.89, "gg/bb")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.055)
l1.DrawLatex(0.73,0.89, "0 b-tags")

c.SetLogy()
c.SaveAs('CSVL_0Tag_limit_obs_SplusB_WideJets_RSG.eps')
#c.SaveAs('CSVL_0Tag_limit_obs_SplusB_sys_WideJets_RSG.eps')

