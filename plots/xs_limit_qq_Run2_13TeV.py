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

  #cmd = "./stats " + str(mass) + "qq"
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

  #log_file = open("stats_" + str(int(mass)) + "_qq.log",'r')
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
xs_exp_limits = array('d', [2.46008, 1.73235, 1.53765, 1.16998, 0.943767, 0.83403, 0.663368, 0.566649, 0.48182, 0.398598, 0.356265, 0.30196, 0.264741, 0.227498, 0.204818, 0.192455, 0.169517, 0.149619, 0.130632, 0.115606, 0.101708, 0.0929185, 0.0812325, 0.071833, 0.0650646, 0.0608216, 0.0540723, 0.0488424, 0.0432894, 0.0401439, 0.0371489, 0.0328781, 0.0291085, 0.0282957, 0.0268465, 0.0252629, 0.0239975, 0.0224023, 0.0205171, 0.0184913, 0.0184571, 0.0165869, 0.0157073, 0.0148671, 0.0137324, 0.0131782, 0.012681, 0.0117763, 0.0112172, 0.0108539, 0.0104883, 0.00995058, 0.00975163, 0.00938701, 0.00901729, 0.00866289, 0.00837817, 0.00834533, 0.00821421])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.715002, 0.989937, 0.854983, 0.70639, 0.627167, 0.520808, 0.440446, 0.371269, 0.298263, 0.2663, 0.228905, 0.204534, 0.175699, 0.153856, 0.13382, 0.124067, 0.113111, 0.10291, 0.0880579, 0.0778157, 0.0701059, 0.0618407, 0.0560726, 0.0535292, 0.04845, 0.0432052, 0.0375774, 0.0344662, 0.031505, 0.0280481, 0.0267079, 0.0249131, 0.0227449, 0.0207528, 0.0185482, 0.0174672, 0.016238, 0.0150224, 0.0140276, 0.0135419, 0.0128518, 0.012604, 0.0115705, 0.0109719, 0.0103962, 0.010178, 0.00937364, 0.00889076, 0.00870718, 0.00852622, 0.00812153, 0.00792349, 0.00776385, 0.00759708, 0.0074205, 0.00736807, 0.00726839, 0.00728283, 0.00708312, 0.0102774, 0.0107541, 0.0109348, 0.0111399, 0.0114935, 0.0121393, 0.0130822, 0.0136507, 0.0138965, 0.01399, 0.0150364, 0.0159741, 0.0167902, 0.0172774, 0.0185151, 0.0200097, 0.0218562, 0.0242004, 0.0272411, 0.0294693, 0.0309159, 0.0332093, 0.0349514, 0.0382063, 0.041497, 0.0433546, 0.0466988, 0.050006, 0.0566244, 0.0601371, 0.0710365, 0.0770575, 0.0827333, 0.0894887, 0.101106, 0.116596, 0.122983, 0.141752, 0.153396, 0.17352, 0.194398, 0.220358, 0.24132, 0.291986, 0.327851, 0.375247, 0.402723, 0.464783, 0.531716, 0.637183, 0.741783, 0.868964, 1.06005, 1.35798, 1.58594, 1.99145, 2.75527, 3.60305, 8.81599])
xs_exp_limits_2sigma = array('d', [0.320067, 0.582407, 0.535713, 0.382775, 0.412129, 0.353582, 0.318796, 0.251774, 0.232243, 0.203039, 0.156873, 0.137485, 0.122768, 0.113803, 0.110029, 0.0903458, 0.0782404, 0.0691434, 0.0578816, 0.0548595, 0.0502931, 0.0479224, 0.03987, 0.0373294, 0.0348543, 0.0322337, 0.0270717, 0.026692, 0.023321, 0.0214896, 0.0190715, 0.0177832, 0.0180606, 0.0159739, 0.0137611, 0.012207, 0.0114138, 0.0107962, 0.0104234, 0.00987701, 0.00965523, 0.00925576, 0.00870975, 0.00848117, 0.00847509, 0.00812678, 0.00747329, 0.00756048, 0.00739805, 0.00732602, 0.00706009, 0.00709478, 0.00705715, 0.00692175, 0.00680627, 0.00676007, 0.00652266, 0.00660103, 0.00656829, 0.0136082, 0.0142208, 0.014754, 0.0152688, 0.0157566, 0.0155785, 0.0164627, 0.0169886, 0.0181608, 0.0183387, 0.0188602, 0.0197066, 0.021471, 0.0239423, 0.0258625, 0.028365, 0.0316212, 0.033576, 0.0365896, 0.0403611, 0.0425622, 0.046318, 0.0494012, 0.0535837, 0.0594951, 0.061968, 0.067935, 0.0730498, 0.077017, 0.0832737, 0.098227, 0.109565, 0.115658, 0.126822, 0.137921, 0.150023, 0.175757, 0.185468, 0.204233, 0.214507, 0.254864, 0.299499, 0.355849, 0.384787, 0.471611, 0.534188, 0.58186, 0.696398, 0.756052, 0.973305, 1.0928, 1.29901, 1.55866, 1.84011, 2.55417, 3.26891, 4.21907, 5.4625, 19.0247])

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
#graph_xsTh.Draw("L")

legend = TLegend(.50,.63,.80,.76)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
#legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected quark-quark","lp")
legend.Draw()

#legendTh = TLegend(.50,.83,.80,.88)
#legendTh.SetBorderSize(0)
#legendTh.SetFillColor(0)
#legendTh.SetFillStyle(0)
#legendTh.SetTextFont(42)
#legendTh.SetTextSize(0.03)
#legendTh.AddEntry(graph_xsTh,"Excited quark","l")
#legendTh.Draw()

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
c.SaveAs('xs_limit_qq_exp_Run2_13TeV.eps')
