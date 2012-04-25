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
xs_limits[0] = array('d', [0.96745000000000003, 0.92661000000000004, 0.84275199999999995, 0.66218600000000005, 0.369255, 0.29673100000000002, 0.28335399999999999, 0.24437, 0.17801500000000001, 0.13400100000000001, 0.111599, 0.100065, 0.081945299999999999, 0.067054299999999997, 0.052121899999999999, 0.050708900000000001, 0.047150600000000001, 0.037793899999999998, 0.0292036, 0.0248501, 0.023033499999999998, 0.021172199999999999, 0.017711999999999999, 0.0146666, 0.012727799999999999, 0.0104078, 0.0086978899999999998, 0.0069849200000000004, 0.0055877599999999998, 0.0041907799999999999, 0.0037251300000000001])
xs_limits[1] = array('d', [0.74594099999999997, 0.59671700000000005, 0.54289799999999999, 0.40492899999999998, 0.23539199999999999, 0.192019, 0.19419, 0.160495, 0.11916599999999999, 0.096803399999999998, 0.081912100000000002, 0.068404000000000006, 0.0577335, 0.048420900000000003, 0.042838599999999998, 0.038483299999999998, 0.035971999999999997, 0.0292035, 0.0243991, 0.020703200000000001, 0.0185892, 0.016761499999999999, 0.014922400000000001, 0.012900200000000001, 0.0106234, 0.0091475399999999991, 0.0074899500000000004, 0.0060534500000000002, 0.0046564500000000003, 0.0041909499999999997, 0.0032594999999999998])
xs_limits[2] = array('d', [0.70401100000000005, 0.49738300000000002, 0.43649700000000002, 0.32877099999999998, 0.191666, 0.163131, 0.162939, 0.13347500000000001, 0.096766900000000003, 0.078165200000000004, 0.067010799999999995, 0.058620199999999997, 0.048417799999999997, 0.042836800000000001, 0.035392300000000002, 0.034781100000000002, 0.0311793, 0.025555000000000001, 0.020636999999999999, 0.018038999999999999, 0.017172199999999999, 0.0154871, 0.0135713, 0.011320200000000001, 0.0100441, 0.0080600800000000007, 0.0065191499999999996, 0.0055877799999999997, 0.0046565499999999998, 0.0037251300000000001, 0.0032594799999999999])
xs_limits[3] = array('d', [0.53950600000000004, 0.40980899999999998, 0.36340299999999998, 0.27390500000000001, 0.16217899999999999, 0.14152500000000001, 0.13924300000000001, 0.115623, 0.085639999999999994, 0.067027799999999998, 0.059601599999999998, 0.0508703, 0.0428324, 0.037253099999999997, 0.031668099999999998, 0.0308814, 0.027544800000000001, 0.0231419, 0.018643099999999999, 0.016212899999999999, 0.0156945, 0.0142837, 0.012315400000000001, 0.0102208, 0.0090085800000000004, 0.0074947199999999999, 0.0060535099999999998, 0.0051221599999999997, 0.0041908500000000003, 0.0037252299999999999, 0.0032595100000000002])

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
legend2.AddEntry(graph_rsg,"RS Graviton (f_{b#bar{b}} #approx 0.1)","l")
#legend2.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.50, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.88, "RS-graviton-like")
l1.SetTextSize(0.04)
l1.DrawLatex(0.19,0.43, "CMS Preliminary")
l1.DrawLatex(0.19,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.20,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.19,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.19,0.20, "Wide Jets, CSVL 1-tag")

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obs_WideJets_RSG.eps')
#c.SaveAs('CSVL_1Tag_limit_obs_sys_WideJets_RSG.eps')

