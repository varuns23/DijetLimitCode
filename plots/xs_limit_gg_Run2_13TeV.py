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

  #cmd = "./stats " + str(mass) + "gg"
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
xs_obs_limits = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
xs_exp_limits = array('d', [6.99474, 3.82902, 3.03603, 2.30428, 1.77796, 1.59745, 1.26186, 1.08393, 0.930592, 0.791539, 0.654332, 0.573206, 0.491696, 0.440092, 0.394201, 0.357613, 0.324716, 0.292328, 0.251314, 0.228326, 0.201417, 0.183309, 0.158531, 0.138943, 0.125219, 0.112182, 0.104452, 0.0967555, 0.0838703, 0.0760002, 0.0689898, 0.0653226, 0.0570253, 0.0523951, 0.0499675, 0.0486485, 0.044669, 0.0419652, 0.0391761, 0.0363273, 0.0335853, 0.0324247, 0.0303027, 0.0293441, 0.0269595, 0.025731, 0.0244375, 0.0235415, 0.0224337, 0.0217286, 0.0212748, 0.0207938, 0.0200312, 0.0199964, 0.0200005, 0.0203834, 0.0202281, 0.0201226, 0.0207773])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [1.93162, 1.19778, 1.28714, 0.954322, 0.81335, 0.824215, 0.752044, 0.625641, 0.499815, 0.426168, 0.395858, 0.327409, 0.305909, 0.264987, 0.239659, 0.216455, 0.20037, 0.185845, 0.162845, 0.139141, 0.121826, 0.111728, 0.105548, 0.0929483, 0.0903812, 0.0782381, 0.0702173, 0.0623421, 0.0581838, 0.0538818, 0.0482233, 0.0445731, 0.0413846, 0.0385334, 0.0350073, 0.0306338, 0.0299107, 0.0285789, 0.0269498, 0.025186, 0.0239047, 0.0218548, 0.0212234, 0.0211443, 0.0189993, 0.0182912, 0.017381, 0.0165775, 0.0162925, 0.0157206, 0.0158588, 0.0157949, 0.0157077, 0.0160339, 0.0154641, 0.0157221, 0.0159059, 0.0163918, 0.0171671, 0.0266688, 0.0262723, 0.0262229, 0.0269863, 0.0276687, 0.028109, 0.0281842, 0.0283906, 0.0299864, 0.0307094, 0.031706, 0.0337603, 0.0344366, 0.0361014, 0.0386373, 0.0413995, 0.0456632, 0.051357, 0.052559, 0.058101, 0.0609598, 0.0665467, 0.0737359, 0.0735378, 0.0805557, 0.0868642, 0.0930136, 0.105177, 0.112894, 0.125872, 0.142074, 0.154676, 0.166371, 0.186927, 0.21473, 0.235696, 0.251042, 0.286805, 0.309874, 0.363843, 0.409315, 0.436971, 0.516886, 0.615772, 0.698842, 0.739534, 0.88184, 0.966394, 1.2181, 1.40442, 1.616, 1.81153, 2.46373, 2.9091, 3.75257, 5.30393, 6.72014, 10.3171, 21.0325])
xs_exp_limits_2sigma = array('d', [1.02597, 0.547663, 0.703662, 0.5145, 0.45153, 0.482748, 0.439625, 0.358158, 0.325316, 0.28853, 0.24592, 0.193397, 0.200367, 0.172649, 0.169763, 0.15394, 0.131714, 0.121745, 0.113583, 0.085309, 0.0862283, 0.0838711, 0.0738277, 0.0683319, 0.0607643, 0.0563091, 0.0532944, 0.0446018, 0.0419668, 0.0378744, 0.0348113, 0.0319157, 0.030575, 0.0294762, 0.0278673, 0.0233095, 0.0202158, 0.0186328, 0.0181512, 0.0177897, 0.0167666, 0.0157941, 0.0157188, 0.0152935, 0.0148458, 0.0146527, 0.0143837, 0.0132575, 0.0136157, 0.0135544, 0.0139627, 0.0134377, 0.0135412, 0.014112, 0.0133808, 0.0138025, 0.0131981, 0.014139, 0.014394, 0.0359574, 0.0352578, 0.0358794, 0.035849, 0.0354844, 0.0366128, 0.0376603, 0.0388377, 0.0391647, 0.0384847, 0.0400856, 0.04444, 0.0476719, 0.0497449, 0.0560518, 0.0572451, 0.068055, 0.0700616, 0.0776819, 0.0808299, 0.0882118, 0.0959387, 0.107895, 0.117919, 0.12323, 0.132243, 0.136739, 0.144783, 0.158832, 0.187987, 0.20916, 0.236074, 0.244013, 0.264209, 0.293238, 0.334117, 0.369428, 0.414476, 0.424391, 0.47406, 0.558165, 0.685145, 0.754166, 0.935203, 0.995595, 1.14963, 1.37483, 1.48577, 1.84356, 2.2253, 2.66065, 3.03794, 3.68395, 4.73879, 6.8474, 8.55839, 12.8913, 18.6271, 35.3481])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,1e+02)
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
#graph_obs.GetYaxis().SetRangeUser(1e-02,1e+03)
#graph_obs.GetXaxis().SetNdivisions(1005)


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
#graph_obs.Draw("LP")

legend = TLegend(.50,.59,.80,.68)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
#legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected gluon-gluon","lp")
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
c.SaveAs('xs_limit_gg_exp_Run2_13TeV.eps')
