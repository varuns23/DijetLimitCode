#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import CMS_lumi

CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "1 fb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

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


mass_start = 1200
mass_step = 100
steps = 58

########################################################
## Uncomment this part if running the limit code


### for running the limit code
#for i in range(0,steps+1):

  #mass = mass_start + float(i)*mass_step

  #masses.append(mass)
  #masses_exp.append(mass)

  #cmd = "./stats " + str(int(mass)) + " qg | tee stats_" + str(int(mass)) + "_qg.log"
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
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

### for reading the limit code log files
#for i in range(0,steps+1):

  #mass = mass_start + i*mass_step

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(int(mass)) + "_qg.log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

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

masses = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
xs_obs_limits = array('d', [20.9545, 2.45626, 0.416225, 1.01931, 2.82771, 2.19572, 1.16475, 0.465517, 0.312011, 0.257445, 0.232343, 0.186241, 0.14177, 0.161448, 0.223433, 0.235894, 0.22298, 0.192951, 0.164016, 0.141445, 0.132672, 0.144567, 0.154099, 0.139979, 0.109849, 0.0806352, 0.0624284, 0.0528164, 0.0509088, 0.0567577, 0.0680257, 0.0716774, 0.0677652, 0.0582306, 0.0484861, 0.0427263, 0.0406525, 0.0400296, 0.0383613, 0.0356998, 0.0308406, 0.0253015, 0.0198666, 0.0152415, 0.0123197, 0.0110247, 0.00929554, 0.00821889, 0.00775016, 0.00722283, 0.00679991, 0.00656296, 0.00640062, 0.00628973, 0.0062155, 0.00616987, 0.00614263, 0.00613129, 0.00613597])
xs_exp_limits = array('d', [2.63206, 2.14471, 1.63841, 1.48217, 1.05316, 0.81135, 0.67681, 0.62097, 0.513012, 0.431082, 0.38607, 0.341819, 0.298624, 0.270375, 0.245451, 0.199897, 0.178578, 0.172584, 0.150738, 0.130131, 0.118085, 0.100697, 0.0934993, 0.0868947, 0.0863419, 0.0747488, 0.0630101, 0.0636891, 0.051635, 0.0489897, 0.0445535, 0.0413454, 0.0356299, 0.0323483, 0.0317702, 0.028163, 0.0258878, 0.0248127, 0.0219089, 0.0212312, 0.0193777, 0.0184784, 0.0187839, 0.0172933, 0.0165523, 0.0149275, 0.0144313, 0.0136047, 0.013115, 0.0127536, 0.0121895, 0.0116958, 0.0112944, 0.010989, 0.010528, 0.0103265, 0.00995773, 0.00966355, 0.00945783])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.582579, 0.906007, 0.676217, 0.649467, 0.52863, 0.46215, 0.416948, 0.408659, 0.306885, 0.275154, 0.233431, 0.206204, 0.190651, 0.164217, 0.140298, 0.126542, 0.119121, 0.113958, 0.0995277, 0.0914361, 0.0754675, 0.0652763, 0.0631411, 0.0579616, 0.0546781, 0.0512499, 0.0410984, 0.0388752, 0.0364113, 0.0309487, 0.0286315, 0.027126, 0.0253184, 0.0210344, 0.0199897, 0.0186182, 0.0180375, 0.0156908, 0.0145542, 0.014889, 0.0141613, 0.0131457, 0.0131473, 0.0120202, 0.0115124, 0.0110107, 0.0106245, 0.0100374, 0.00943959, 0.00938658, 0.00888066, 0.00873425, 0.00849187, 0.00833962, 0.00797341, 0.00772045, 0.00772853, 0.00759191, 0.0076484, 0.0134944, 0.0138873, 0.0141335, 0.0144972, 0.0146058, 0.0152178, 0.0153998, 0.0159748, 0.0165577, 0.0170761, 0.0178538, 0.0190144, 0.0202857, 0.0213109, 0.0252275, 0.0246771, 0.0275916, 0.02712, 0.0274571, 0.0312225, 0.0323616, 0.0353988, 0.0410767, 0.040909, 0.0488502, 0.0522759, 0.0546616, 0.0576525, 0.0691449, 0.0725319, 0.0791983, 0.0951626, 0.107324, 0.111736, 0.129323, 0.141654, 0.142059, 0.163174, 0.185876, 0.196008, 0.246579, 0.260876, 0.288542, 0.318517, 0.404868, 0.448757, 0.505804, 0.587693, 0.667822, 0.771271, 0.834923, 0.983574, 1.20454, 1.38088, 2.04241, 3.02663, 3.80997, 4.3922, 10.8601])
xs_exp_limits_2sigma = array('d', [0.304105, 0.505705, 0.346595, 0.418537, 0.287031, 0.302376, 0.291666, 0.253468, 0.221616, 0.167241, 0.140807, 0.141968, 0.125778, 0.117572, 0.0976915, 0.0908769, 0.087221, 0.0797414, 0.0724456, 0.066167, 0.058566, 0.0503008, 0.0468465, 0.0456055, 0.0401798, 0.0342022, 0.0298217, 0.0275258, 0.026044, 0.0230015, 0.0214502, 0.0187373, 0.017661, 0.0154657, 0.0153469, 0.0143449, 0.0134694, 0.0121761, 0.012212, 0.0118835, 0.0112004, 0.0109006, 0.0105163, 0.00976393, 0.00929094, 0.00893986, 0.00835628, 0.00821979, 0.00781762, 0.0075346, 0.00728246, 0.00682364, 0.00659758, 0.00642935, 0.00631419, 0.00623839, 0.00617555, 0.00614071, 0.00617174, 0.0169686, 0.0175849, 0.0177768, 0.0181333, 0.0186732, 0.0190931, 0.0200604, 0.0210758, 0.0218479, 0.0228189, 0.0243923, 0.0252882, 0.0274636, 0.0295942, 0.032357, 0.0348368, 0.0372234, 0.0376283, 0.0371354, 0.0550674, 0.04461, 0.0552547, 0.0597302, 0.0636562, 0.0687621, 0.0798454, 0.076603, 0.0777872, 0.10755, 0.112975, 0.124024, 0.138019, 0.143293, 0.166326, 0.184478, 0.199701, 0.236542, 0.233212, 0.288949, 0.320863, 0.353619, 0.380252, 0.425382, 0.456848, 0.534726, 0.667662, 0.741382, 0.965891, 0.94609, 1.05887, 1.24716, 1.43139, 1.73634, 2.15742, 2.87907, 4.57325, 5.70807, 7.22611, 19.0147])

##
########################################################

massesTh = array('d', [
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

xsQstar = array('d', [
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

graph_xsQstar = TGraph(len(massesTh),massesTh,xsQstar)
graph_xsQstar.SetLineWidth(2)
graph_xsQstar.SetLineStyle(7)
graph_xsQstar.SetLineColor(2)

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("qg resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,2e+02)
#graph_exp_2sigma.GetXaxis().SetNdivisions(1005)

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


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")
graph_xsQstar.Draw("L")

legend = TLegend(.50,.55,.80,.68)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
legend.AddEntry(graph_obs,"Observed (pseudo-data)","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.Draw()

legendTh = TLegend(.50,.70,.80,.75)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.03)
legendTh.AddEntry(graph_xsQstar,"Excited quark","l")
legendTh.Draw()

#l1 = TLatex()
#l1.SetTextAlign(12)
#l1.SetTextFont(42)
#l1.SetNDC()
#l1.SetTextSize(0.04)
#l1.SetTextSize(0.04)
#l1.DrawLatex(0.18,0.40, "CMS Preliminary")
#l1.DrawLatex(0.18,0.32, "#intLdt = 1 fb^{-1}")
#l1.DrawLatex(0.19,0.27, "#sqrt{s} = 13 TeV")

# draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('xs_limit_qg_exp_Run2_13TeV.pdf')
