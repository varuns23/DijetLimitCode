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

  #cmd = "./stats " + str(int(mass)) + " gg | tee stats_" + str(int(mass)) + "_gg.log"
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

  #log_file = open("stats_" + str(int(mass)) + "_gg.log",'r')
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
xs_obs_limits = array('d', [30.303, 7.06149, 0.551883, 0.826844, 3.9482, 3.31129, 2.0955, 0.713729, 0.443153, 0.357982, 0.330766, 0.258931, 0.186376, 0.197092, 0.291734, 0.323995, 0.303538, 0.277921, 0.237822, 0.2052, 0.181507, 0.196302, 0.222027, 0.211771, 0.173583, 0.125038, 0.0978138, 0.0787462, 0.0722822, 0.076304, 0.0949005, 0.103527, 0.102056, 0.0883539, 0.0710818, 0.0608987, 0.0568118, 0.0562941, 0.0541762, 0.0505432, 0.044734, 0.0373533, 0.0287415, 0.0237149, 0.0179518, 0.014523, 0.0142933, 0.0124812, 0.0112436, 0.0106327, 0.0101725, 0.00996536, 0.00986499, 0.00985501, 0.00992039, 0.0100315, 0.0101831, 0.0104826, 0.010764])
xs_exp_limits = array('d', [3.18953, 2.75638, 1.97588, 2.07047, 1.51395, 1.13639, 1.02512, 0.825541, 0.687576, 0.645197, 0.52206, 0.45338, 0.455349, 0.364867, 0.337383, 0.318141, 0.265012, 0.258696, 0.210641, 0.197798, 0.17854, 0.148266, 0.131337, 0.12382, 0.106044, 0.0991548, 0.0998414, 0.0819558, 0.074092, 0.0665097, 0.0616004, 0.0510265, 0.0497565, 0.0490886, 0.042432, 0.0388045, 0.0357015, 0.0345422, 0.030691, 0.0286476, 0.0273476, 0.0260991, 0.0252136, 0.0259524, 0.0235038, 0.0227757, 0.0207493, 0.0197729, 0.0187126, 0.0181336, 0.0181289, 0.017387, 0.0168164, 0.0168141, 0.0166783, 0.0163614, 0.0163255, 0.0162972, 0.0163624])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.92675, 1.07912, 0.875113, 0.79568, 0.643925, 0.621072, 0.583495, 0.465348, 0.399138, 0.380553, 0.31397, 0.266502, 0.251536, 0.218273, 0.198158, 0.172352, 0.165263, 0.156552, 0.137063, 0.121283, 0.110607, 0.0969931, 0.0837733, 0.0776243, 0.0717328, 0.0657792, 0.056891, 0.0544657, 0.0528249, 0.0429157, 0.0386041, 0.0362338, 0.0333393, 0.0308605, 0.0276556, 0.0266546, 0.0253472, 0.0235314, 0.021869, 0.0196722, 0.0189195, 0.0187874, 0.0179675, 0.0166828, 0.0156377, 0.0157203, 0.0150242, 0.0142598, 0.0138672, 0.0136716, 0.0136185, 0.0135333, 0.0132134, 0.0132861, 0.0130784, 0.0128314, 0.0127504, 0.0128941, 0.0133706, 0.0236609, 0.0234541, 0.0232593, 0.0232251, 0.0230493, 0.0236303, 0.0243243, 0.0243606, 0.0243461, 0.025529, 0.0262255, 0.0280958, 0.0296425, 0.0315176, 0.0351479, 0.0353947, 0.0393814, 0.0388165, 0.0385375, 0.0424694, 0.0470359, 0.0524257, 0.0588874, 0.0630769, 0.0693283, 0.0762464, 0.0852505, 0.0808484, 0.0960194, 0.114013, 0.12063, 0.127179, 0.148758, 0.16348, 0.177555, 0.197633, 0.228961, 0.250484, 0.295711, 0.28524, 0.337058, 0.401707, 0.439778, 0.539385, 0.562894, 0.635817, 0.777838, 0.807491, 0.995907, 1.07924, 1.3029, 1.49379, 1.97757, 2.15351, 3.18469, 4.26746, 5.01286, 6.72243, 16.3617])
xs_exp_limits_2sigma = array('d', [0.491101, 0.612456, 0.446368, 0.510541, 0.367059, 0.366956, 0.410485, 0.324747, 0.249501, 0.221656, 0.206094, 0.189425, 0.165019, 0.139687, 0.124433, 0.118122, 0.117315, 0.109781, 0.0963524, 0.094903, 0.0744745, 0.0669173, 0.0649246, 0.0592594, 0.0446075, 0.0466091, 0.0433929, 0.0363256, 0.0341118, 0.03109, 0.030171, 0.0283862, 0.025997, 0.0243644, 0.0214383, 0.0192648, 0.0180521, 0.0167399, 0.0160263, 0.0157086, 0.0153643, 0.0150957, 0.0146627, 0.0139579, 0.0130886, 0.0129654, 0.0122948, 0.0118467, 0.0115478, 0.0110868, 0.0106094, 0.0102141, 0.00993031, 0.00985453, 0.00995876, 0.00999859, 0.00995129, 0.0103464, 0.0107431, 0.0299356, 0.029447, 0.0294108, 0.0300319, 0.0300347, 0.0301243, 0.0309404, 0.0319548, 0.0329909, 0.0335785, 0.0353476, 0.0373127, 0.0402128, 0.0454758, 0.0516417, 0.0484547, 0.0497256, 0.0533581, 0.0548264, 0.0570833, 0.0654322, 0.0731721, 0.0888387, 0.0945732, 0.100108, 0.11371, 0.126986, 0.117143, 0.149656, 0.162984, 0.174211, 0.198035, 0.212405, 0.23656, 0.240578, 0.304074, 0.336122, 0.375516, 0.42234, 0.491147, 0.502052, 0.551025, 0.676475, 0.805594, 0.819855, 0.984709, 1.18111, 1.2831, 1.43437, 1.50466, 2.1181, 2.4472, 2.87506, 3.17949, 4.89896, 6.4903, 8.21251, 11.2743, 28.708])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("gg resonance mass [GeV]")
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

#l1 = TLatex()
#l1.SetTextAlign(12)
#l1.SetTextFont(42)
#l1.SetNDC()
#l1.SetTextSize(0.04)
#l1.SetTextSize(0.04)
#l1.DrawLatex(0.18,0.40, "CMS Preliminary")
#l1.DrawLatex(0.18,0.32, "#intLdt = 1 fb^{-1}")
#l1.DrawLatex(0.19,0.27, "#sqrt{s} = 13 TeV")

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('xs_limit_gg_exp_Run2_13TeV.pdf')
