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

  #cmd = "./stats " + str(mass) + "qg"
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
xs_obs_limits = array('d', [5.8357, 2.26807, 1.82723, 3.08801, 2.06973, 1.19145, 0.813096, 0.556971, 0.374301, 0.27502, 0.263001, 0.300988, 0.34256, 0.322529, 0.313904, 0.307176, 0.296814, 0.285121, 0.263446, 0.235145, 0.203461, 0.174825, 0.151236, 0.134154, 0.118603, 0.101383, 0.0835957, 0.0714082, 0.0614886, 0.0541265, 0.048716, 0.0448183, 0.0405726, 0.0366388, 0.0330405, 0.0297684, 0.0269889, 0.0256544, 0.0231401, 0.0205713, 0.0190573, 0.0177508, 0.0166392, 0.0156097, 0.015148, 0.0139509, 0.0135894, 0.0133964, 0.0126518, 0.0119122, 0.011634, 0.0111572, 0.0105139, 0.0103356, 0.0100433, 0.00968389, 0.00957805, 0.00942026, 0.00925948])
xs_exp_limits = array('d', [5.49428, 2.87069, 1.99697, 2.75279, 1.9376, 1.15308, 0.814333, 0.51933, 0.374552, 0.281278, 0.254761, 0.282769, 0.322801, 0.304961, 0.335533, 0.332617, 0.30904, 0.285892, 0.267048, 0.233669, 0.202294, 0.173592, 0.155174, 0.138055, 0.119727, 0.0993967, 0.0877933, 0.0737052, 0.0650873, 0.0562692, 0.0500698, 0.0439948, 0.0386713, 0.0356506, 0.0322019, 0.028858, 0.0260175, 0.0232132, 0.0213234, 0.0204363, 0.0193587, 0.0184558, 0.0172987, 0.016602, 0.0155854, 0.0146468, 0.0140748, 0.0136054, 0.0131692, 0.0128282, 0.013155, 0.0127052, 0.0122513, 0.0117197, 0.0117344, 0.0116043, 0.0114626, 0.0112942, 0.0110754])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [1.15097, 0.921738, 0.931601, 1.23697, 0.870519, 0.681758, 0.486401, 0.34965, 0.247234, 0.197112, 0.176574, 0.171435, 0.188099, 0.198344, 0.204213, 0.201084, 0.198032, 0.193185, 0.177329, 0.150794, 0.129465, 0.112222, 0.0998127, 0.0887309, 0.0792437, 0.0672039, 0.0594065, 0.0522709, 0.0411201, 0.0356296, 0.0319232, 0.0287068, 0.0272449, 0.0244427, 0.0215157, 0.0206984, 0.0188959, 0.0171768, 0.0160632, 0.0153854, 0.0143295, 0.0131542, 0.0128682, 0.0125702, 0.0122088, 0.0114262, 0.0111656, 0.0106913, 0.0104312, 0.0105113, 0.0104716, 0.0101664, 0.00992708, 0.00988074, 0.00977497, 0.00974691, 0.00960548, 0.00944704, 0.00909565, 0.0140324, 0.0144208, 0.0146401, 0.0147239, 0.0148923, 0.0151592, 0.0156284, 0.0159209, 0.0165362, 0.0167364, 0.0168453, 0.0180227, 0.0190787, 0.0198775, 0.0205249, 0.0225796, 0.0236846, 0.0255539, 0.0286647, 0.0299053, 0.0311831, 0.0331987, 0.0378962, 0.0414433, 0.0472396, 0.0553212, 0.0629286, 0.0680183, 0.0735351, 0.0839411, 0.0905146, 0.112966, 0.132214, 0.150576, 0.173391, 0.189979, 0.214348, 0.238162, 0.278249, 0.321753, 0.369476, 0.435745, 0.486547, 0.489664, 0.517924, 0.558523, 0.513226, 0.507143, 0.467732, 0.453921, 0.612832, 0.933549, 1.52609, 2.13342, 3.22066, 4.99773, 4.46337, 7.06901, 17.9638])
xs_exp_limits_2sigma = array('d', [0.514163, 0.503321, 0.538438, 0.627464, 0.477941, 0.436864, 0.362943, 0.251391, 0.196109, 0.137995, 0.12451, 0.122449, 0.122811, 0.131256, 0.12925, 0.127874, 0.125884, 0.113848, 0.112769, 0.105276, 0.0909158, 0.0749828, 0.0618512, 0.0567046, 0.0496851, 0.0458451, 0.0398341, 0.0359025, 0.0317863, 0.0275975, 0.0245739, 0.0221733, 0.0204046, 0.0190723, 0.017429, 0.0152707, 0.0140089, 0.0132043, 0.0126466, 0.0126308, 0.0114457, 0.0107962, 0.0108998, 0.0102381, 0.00964135, 0.00953691, 0.00935686, 0.00901059, 0.00886945, 0.00876895, 0.00847496, 0.0085089, 0.00846527, 0.00852912, 0.00863349, 0.00836444, 0.00827123, 0.00818482, 0.00826533, 0.017129, 0.0176682, 0.0189627, 0.0196829, 0.0202639, 0.0209192, 0.0216854, 0.0227731, 0.0236145, 0.0241076, 0.0243461, 0.0251499, 0.0251922, 0.0264235, 0.0302103, 0.0332579, 0.0346577, 0.0355388, 0.0386929, 0.0417018, 0.0475798, 0.0558397, 0.0585792, 0.0661989, 0.0709148, 0.0730699, 0.0784018, 0.0907673, 0.105559, 0.125227, 0.136802, 0.149604, 0.165086, 0.203862, 0.247893, 0.265831, 0.284705, 0.318329, 0.36128, 0.410473, 0.484627, 0.545968, 0.612429, 0.67787, 0.741814, 0.785145, 0.828191, 0.865012, 0.904879, 0.838634, 1.12782, 1.5122, 2.21203, 2.99317, 4.65755, 7.08353, 7.21468, 11.713, 32.7353])

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
graph_xsTh.Draw("L")

legend = TLegend(.50,.63,.80,.76)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
#legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected quark-gluon","lp")
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
c.SaveAs('xs_limit_qg_exp_Run2_13TeV.eps')
