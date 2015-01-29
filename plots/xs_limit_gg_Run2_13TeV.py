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

#-------------------------------------------------------

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

#-------------------------------------------------------

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
xs_obs_limits = array('d', [2.86333, 2.1576, 1.78722, 1.43075, 1.04834, 0.844258, 0.720716, 0.610737, 0.527007, 0.47314, 0.448075, 0.415106, 0.380189, 0.336253, 0.294093, 0.257656, 0.229792, 0.206938, 0.188841, 0.170909, 0.157819, 0.144506, 0.130808, 0.117838, 0.10632, 0.096842, 0.0866674, 0.0781594, 0.070526, 0.0639157, 0.0586091, 0.0537512, 0.0496165, 0.0460685, 0.0413765, 0.0374146, 0.0338005, 0.0308365, 0.0282643, 0.0263774, 0.0257882, 0.0240236, 0.0224569, 0.021064, 0.0198109, 0.0186811, 0.0176674, 0.0167405, 0.0158993, 0.0154838, 0.015125, 0.0148423, 0.0146249, 0.0146226, 0.0145355, 0.0145103, 0.0145567, 0.0146659, 0.0148405])
xs_exp_limits = array('d', [2.97268, 1.81914, 1.64436, 1.29696, 1.08154, 0.970865, 0.787051, 0.688185, 0.588951, 0.49651, 0.424271, 0.381047, 0.351821, 0.319222, 0.275842, 0.248464, 0.213577, 0.195843, 0.179553, 0.159482, 0.139467, 0.128977, 0.117306, 0.106526, 0.100923, 0.0909531, 0.0866393, 0.0760187, 0.0721094, 0.0648381, 0.0567892, 0.0521928, 0.0490538, 0.0455894, 0.0414427, 0.0376891, 0.0371815, 0.0344149, 0.0314333, 0.0284366, 0.0274359, 0.0257611, 0.0245909, 0.0230563, 0.022689, 0.0217088, 0.0212839, 0.0202393, 0.0198483, 0.018658, 0.01869, 0.0185101, 0.0185773, 0.0182271, 0.0179613, 0.0181113, 0.0179119, 0.0186691, 0.0188179])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.669131, 0.804385, 0.797706, 0.527333, 0.568676, 0.526652, 0.441827, 0.423537, 0.349575, 0.289842, 0.253937, 0.225301, 0.213995, 0.184421, 0.165842, 0.147552, 0.135036, 0.120682, 0.111464, 0.105587, 0.0936354, 0.0823853, 0.0740996, 0.0681831, 0.0641442, 0.0597737, 0.054431, 0.0511683, 0.0465766, 0.0417288, 0.0381228, 0.0339538, 0.0319198, 0.0300913, 0.0288143, 0.0271103, 0.0250782, 0.0230386, 0.0214329, 0.0199356, 0.0183139, 0.018101, 0.017893, 0.016701, 0.0160864, 0.0156083, 0.0157269, 0.0152935, 0.014519, 0.0143235, 0.014298, 0.0144705, 0.0143781, 0.0143247, 0.0143358, 0.0148335, 0.0146168, 0.0147393, 0.0151308, 0.0251933, 0.0254681, 0.0257065, 0.0255538, 0.024977, 0.024861, 0.0243988, 0.0250501, 0.0255499, 0.0257494, 0.0263759, 0.0276381, 0.0288446, 0.0309217, 0.0327669, 0.0323702, 0.0346666, 0.037102, 0.0395845, 0.0439301, 0.0491028, 0.0518334, 0.0570212, 0.0615351, 0.0637673, 0.0660384, 0.0725736, 0.0766723, 0.0868849, 0.0953966, 0.104465, 0.117839, 0.127898, 0.131095, 0.151437, 0.15996, 0.183856, 0.212905, 0.231342, 0.243013, 0.272895, 0.315026, 0.358619, 0.423588, 0.461855, 0.527053, 0.594307, 0.706429, 0.772674, 0.948215, 1.03393, 1.31432, 1.5, 1.70445, 2.41247, 3.39617, 3.70601, 5.34909, 11.2132])
xs_exp_limits_2sigma = array('d', [0.420868, 0.442211, 0.437717, 0.330223, 0.361333, 0.332027, 0.286023, 0.260614, 0.237801, 0.201782, 0.176971, 0.143792, 0.123862, 0.11046, 0.108436, 0.105843, 0.0884401, 0.0890871, 0.0730426, 0.0663913, 0.0645411, 0.0568418, 0.0482026, 0.0474223, 0.0448735, 0.0418721, 0.0386019, 0.036036, 0.0328163, 0.0295294, 0.0268118, 0.0253271, 0.0241055, 0.0224228, 0.0190525, 0.0177799, 0.016077, 0.015847, 0.0149705, 0.0148268, 0.0143166, 0.0139182, 0.0138203, 0.0134956, 0.0136539, 0.012882, 0.0126562, 0.0128897, 0.0124834, 0.012151, 0.0119442, 0.0122302, 0.0123422, 0.0122359, 0.0121837, 0.0125088, 0.013237, 0.0133663, 0.0123676, 0.0347963, 0.0328335, 0.0329927, 0.0332878, 0.0334918, 0.0336258, 0.0341137, 0.0344721, 0.03491, 0.0354194, 0.0370839, 0.037744, 0.0399791, 0.0431183, 0.0454447, 0.0498823, 0.0520308, 0.0546204, 0.0569191, 0.0628995, 0.0704545, 0.0782214, 0.0867644, 0.0943726, 0.0973302, 0.109968, 0.107318, 0.110079, 0.122845, 0.131671, 0.137298, 0.150111, 0.18301, 0.218534, 0.227325, 0.232828, 0.257818, 0.289992, 0.325855, 0.371269, 0.428812, 0.451056, 0.476505, 0.542817, 0.670093, 0.811648, 0.917911, 1.00987, 1.14634, 1.47301, 1.68847, 1.92183, 2.44208, 2.50935, 3.90984, 5.2176, 5.60382, 8.39836, 20.5008])

##
########################################################

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,1e+02)
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
c.SaveAs('xs_limit_gg_exp_Run2_13TeV.pdf')
