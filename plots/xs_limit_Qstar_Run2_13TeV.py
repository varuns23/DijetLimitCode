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

masses = array('d')
xs_obs_limits = array('d')
xs_exp_limits = array('d')
masses_exp = array('d')
xs_exp_limits_1sigma = array('d')
xs_exp_limits_1sigma_up = array('d')
xs_exp_limits_2sigma = array('d')
xs_exp_limits_2sigma_up = array('d')


mass_points = [3000, 4000, 5000]

plot_exp = True

########################################################
## Uncomment this part if running the limit code


### for running the limit code
#for mass in mass_points:

  #masses.append(mass)
  #masses_exp.append(mass)

  #cmd = "./stats " + str(mass)
  #print "Running: " + cmd
  #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  #output = proc.communicate()[0]
  #if proc.returncode != 0:
    #print output
    #sys.exit(1)
  ##print output

  #outputlines = output.split("\n")

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if plot_exp:
      #if re.search("median:", line):
        #xs_exp_limits.append(float(line.split()[1]))
      #if re.search("1 sigma band:", line):
        #xs_exp_limits_1sigma.append(float(line.split()[4]))
        #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
      #if re.search("2 sigma band:", line):
        #xs_exp_limits_2sigma.append(float(line.split()[4]))
        #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

### for reading the limit code log files
#for mass in mass_points:

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_dir = ('logs_obs_exp' if plot_exp else 'logs_obs')

  #log_file = open(log_dir + "/stats_" + str(int(mass)) + ".log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if plot_exp:
      #if re.search("median:", line):
        #xs_exp_limits.append(float(line.split()[1]))
      #if re.search("1 sigma band:", line):
        #xs_exp_limits_1sigma.append(float(line.split()[4]))
        #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
      #if re.search("2 sigma band:", line):
        #xs_exp_limits_2sigma.append(float(line.split()[4]))
        #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

#if plot_exp:
  #for i in range(0,len(masses)):
    #masses_exp.append( masses[len(masses)-i-1] )
    #xs_exp_limits_1sigma.append( xs_exp_limits_1sigma_up[len(masses)-i-1] )
    #xs_exp_limits_2sigma.append( xs_exp_limits_2sigma_up[len(masses)-i-1] )


#print "masses:"
#print masses
#print "xs_obs_limits:"
#print xs_obs_limits
#print "xs_exp_limits:"
#print xs_exp_limits
#print ""
#print "masses_exp:"
#print masses_exp
#print "xs_exp_limits_1sigma:"
#print xs_exp_limits_1sigma
#print "xs_exp_limits_2sigma:"
#print xs_exp_limits_2sigma

##
########################################################

########################################################
## Comment out this part if running the limit code

if plot_exp:
  masses = array('d', [3000.0, 4000.0, 5000.0])
  xs_obs_limits = array('d', [0.262507, 0.0605923, 0.0215759])
  xs_exp_limits = array('d', [0.263263, 0.0630194, 0.022037])
else:
  masses = array('d', [3000.0, 4000.0, 5000.0])
  xs_obs_limits = array('d', [0.262507, 0.0605923, 0.0215759])

masses_exp = array('d', [3000.0, 4000.0, 5000.0, 5000.0, 4000.0, 3000.0])
xs_exp_limits_1sigma = array('d', [0.162642, 0.039277, 0.0157349, 0.0316386, 0.0978435, 0.372206])
xs_exp_limits_2sigma = array('d', [0.101982, 0.0266121, 0.0117184, 0.0484176, 0.144175, 0.505288])

##
########################################################

masses_xsTh = array('d', [
1000.0,
1100.0,
1200.0,
1300.0,
1400.0,
1500.0,
1600.0,
1700.0,
1800.0,
1900.0,
2000.0,
2100.0,
2200.0,
2300.0,
2400.0,
2500.0,
2600.0,
2700.0,
2800.0,
2900.0,
3000.0,
3100.0,
3200.0,
3300.0,
3400.0,
3500.0,
3600.0,
3700.0,
3800.0,
3900.0,
4000.0,
4100.0,
4200.0,
4300.0,
4400.0,
4500.0,
4600.0,
4700.0,
4800.0,
4900.0,
5000.0,
5100.0,
5200.0,
5300.0,
5400.0,
5500.0,
5600.0,
5700.0,
5800.0,
5900.0,
6000.0,
6100.0,
6200.0,
6300.0,
6400.0,
6500.0,
6600.0,
6700.0,
6800.0,
6900.0,
7000.0,
7100.0,
7200.0,
7300.0,
7400.0,
7500.0,
7600.0,
7700.0,
7800.0,
7900.0,
8000.0,
8100.0,
8200.0,
8300.0,
8400.0,
8500.0,
8600.0,
8700.0,
8800.0,
8900.0,
9000.0])

xsTh = array('d', [
0.4101E+03,
0.2620E+03,
0.1721E+03,
0.1157E+03,
0.7934E+02,
0.5540E+02,
0.3928E+02,
0.2823E+02,
0.2054E+02,
0.1510E+02,
0.1121E+02,
0.8390E+01,
0.6328E+01,
0.4807E+01,
0.3674E+01,
0.2824E+01,
0.2182E+01,
0.1694E+01,
0.1320E+01,
0.1033E+01,
0.8116E+00,
0.6395E+00,
0.5054E+00,
0.4006E+00,
0.3182E+00,
0.2534E+00,
0.2022E+00,
0.1616E+00,
0.1294E+00,
0.1038E+00,
0.8333E-01,
0.6700E-01,
0.5392E-01,
0.4344E-01,
0.3503E-01,
0.2827E-01,
0.2283E-01,
0.1844E-01,
0.1490E-01,
0.1205E-01,
0.9743E-02,
0.7880E-02,
0.6373E-02,
0.5155E-02,
0.4169E-02,
0.3371E-02,
0.2725E-02,
0.2202E-02,
0.1779E-02,
0.1437E-02,
0.1159E-02,
0.9353E-03,
0.7541E-03,
0.6076E-03,
0.4891E-03,
0.3935E-03,
0.3164E-03,
0.2541E-03,
0.2039E-03,
0.1635E-03,
0.1310E-03,
0.1049E-03,
0.8385E-04,
0.6699E-04,
0.5347E-04,
0.4264E-04,
0.3397E-04,
0.2704E-04,
0.2151E-04,
0.1709E-04,
0.1357E-04,
0.1077E-04,
0.8544E-05,
0.6773E-05,
0.5367E-05,
0.4251E-05,
0.3367E-05,
0.2666E-05,
0.2112E-05,
0.1673E-05,
0.1326E-05])

graph_xsTh = TGraph(len(masses_xsTh),masses_xsTh,xsTh)
graph_xsTh.SetLineWidth(2)
graph_xsTh.SetLineStyle(7)
graph_xsTh.SetLineColor(2)

if plot_exp:
  graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
  graph_exp_2sigma.SetFillColor(kYellow)
  graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
  graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
  graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,1e+01)
  graph_exp_2sigma.GetXaxis().SetNdivisions(1005)

  graph_exp_1sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_1sigma)
  graph_exp_1sigma.SetFillColor(kGreen+1)

  graph_exp = TGraph(len(masses),masses,xs_exp_limits)
  #graph_exp.SetMarkerStyle(24)
  graph_exp.SetLineWidth(2)
  graph_exp.SetLineStyle(2)
  graph_exp.SetLineColor(4)

graph_obs = TGraph(len(masses),masses,xs_obs_limits)
graph_obs.SetMarkerStyle(20)
graph_obs.SetLineWidth(2)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)
graph_obs.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_obs.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_obs.GetYaxis().SetRangeUser(1e-02,1e+03)
graph_obs.GetXaxis().SetNdivisions(1005)


c = TCanvas("c", "",800,800)
c.cd()

if plot_exp:
  graph_exp_2sigma.Draw("AF")
  graph_exp_1sigma.Draw("F")
  graph_exp.Draw("L")
  #graph_obs.Draw("LP")
  graph_xsTh.Draw("L")
else:
  graph_obs.Draw("ALP")

legend = TLegend(.50,.63,.80,.76)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
#legend.AddEntry(graph_obs,"Observed","lp")
if plot_exp:
  legend.AddEntry(graph_exp,"Expected","lp")
legend.Draw()

legendTh = TLegend(.50,.83,.80,.88)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.03)
legendTh.AddEntry(graph_xsTh,"Excited quark","l")
legendTh.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.04)
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.40, "CMS Preliminary")
l1.DrawLatex(0.18,0.32, "#intLdt = 1 fb^{-1}")
l1.DrawLatex(0.19,0.27, "#sqrt{s} = 13 TeV")


gPad.RedrawAxis();

c.SetLogy()
if plot_exp:
  c.SaveAs('xs_limit_obs_exp_Qstar_Run2_13TeV.eps')
else:
  c.SaveAs('xs_limit_obs_Qstar_Run2_13TeV.eps')
