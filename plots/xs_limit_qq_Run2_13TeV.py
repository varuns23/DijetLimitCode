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
xs_obs_limits = array('d', [2.86512, 1.50033, 1.80137, 2.14495, 1.25857, 0.914904, 0.628719, 0.44046, 0.297468, 0.237641, 0.243617, 0.276154, 0.253665, 0.238523, 0.232066, 0.227078, 0.213942, 0.200874, 0.182034, 0.159149, 0.137782, 0.123089, 0.107089, 0.0935793, 0.0809659, 0.0692999, 0.0605518, 0.0523666, 0.0465787, 0.04118, 0.036616, 0.0331825, 0.0301382, 0.027427, 0.0249535, 0.0228527, 0.020685, 0.0186828, 0.0170483, 0.0155215, 0.0145954, 0.0137682, 0.0128416, 0.0124373, 0.0116551, 0.0108846, 0.0102499, 0.00965813, 0.00910222, 0.00864305, 0.00821755, 0.00783931, 0.00750921, 0.00730182, 0.00707342, 0.00682146, 0.00690062, 0.00671508, 0.00654024])
xs_exp_limits = array('d', [2.58995, 1.64618, 1.80626, 1.99323, 1.21414, 0.969169, 0.660705, 0.427358, 0.295538, 0.239453, 0.230943, 0.24889, 0.246179, 0.232858, 0.236765, 0.236446, 0.219174, 0.198999, 0.178163, 0.15662, 0.132482, 0.122486, 0.110946, 0.0967772, 0.0817682, 0.0703221, 0.0616981, 0.0527179, 0.0477485, 0.0407065, 0.036649, 0.0318333, 0.0292487, 0.0270423, 0.0251021, 0.0218565, 0.019543, 0.0179856, 0.016715, 0.0159383, 0.0148838, 0.0140352, 0.0134442, 0.0127579, 0.0123932, 0.0116278, 0.0111261, 0.0105266, 0.0103889, 0.0103603, 0.00974895, 0.00917788, 0.00867985, 0.00855991, 0.00843632, 0.00815041, 0.00800882, 0.0079026, 0.00771105])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.586318, 0.851374, 0.933776, 1.04511, 0.759932, 0.59742, 0.415935, 0.290486, 0.221332, 0.171857, 0.159996, 0.156937, 0.15797, 0.162645, 0.162126, 0.154973, 0.143437, 0.142064, 0.124973, 0.103933, 0.0949479, 0.0829211, 0.071889, 0.0631825, 0.0571722, 0.0510041, 0.0450729, 0.035938, 0.0303564, 0.0273917, 0.0259181, 0.023134, 0.0205345, 0.0183543, 0.0170531, 0.0155919, 0.0143504, 0.01371, 0.012883, 0.0121761, 0.0112996, 0.0103646, 0.0100338, 0.0100452, 0.0096403, 0.00915592, 0.00879404, 0.00850726, 0.00818613, 0.00819429, 0.00802071, 0.00757807, 0.00741306, 0.00730568, 0.00724783, 0.00716236, 0.00692303, 0.00669045, 0.00671879, 0.00978471, 0.00989573, 0.0101421, 0.0105737, 0.0107509, 0.0109765, 0.0114822, 0.0121151, 0.0127942, 0.0133178, 0.0133064, 0.0139979, 0.014551, 0.0151977, 0.0154915, 0.0168042, 0.0180609, 0.0188937, 0.0210373, 0.0233526, 0.0242224, 0.025639, 0.0284924, 0.0303857, 0.034682, 0.0387447, 0.0436275, 0.0490795, 0.0531428, 0.062272, 0.0683433, 0.0754139, 0.0894416, 0.103188, 0.117075, 0.133956, 0.153094, 0.16941, 0.188418, 0.214153, 0.249491, 0.278876, 0.326243, 0.34578, 0.35688, 0.374361, 0.389553, 0.392826, 0.393359, 0.38709, 0.449951, 0.680196, 1.03763, 1.44534, 1.92454, 3.13548, 3.12362, 3.15966, 9.4129])
xs_exp_limits_2sigma = array('d', [0.340914, 0.492988, 0.547434, 0.571998, 0.440164, 0.406252, 0.319196, 0.232174, 0.16635, 0.125112, 0.114173, 0.117986, 0.114356, 0.113393, 0.102004, 0.10273, 0.099337, 0.0924994, 0.0914771, 0.0746021, 0.0631579, 0.0549768, 0.0505808, 0.0433411, 0.0382931, 0.0345097, 0.0309857, 0.0281686, 0.0230951, 0.0204262, 0.018358, 0.016562, 0.0159492, 0.0148816, 0.0135079, 0.011979, 0.0121336, 0.0103967, 0.0107144, 0.00981326, 0.00909979, 0.00888, 0.00839559, 0.00831796, 0.00797103, 0.00769491, 0.00767468, 0.00739759, 0.00713358, 0.00725845, 0.0072071, 0.00689827, 0.00689761, 0.00656229, 0.00687759, 0.00641171, 0.00621896, 0.00620628, 0.00602948, 0.0110098, 0.0115175, 0.012131, 0.0132361, 0.0138875, 0.0149739, 0.01595, 0.0169147, 0.0178316, 0.0183445, 0.0178564, 0.0183468, 0.0187909, 0.0197962, 0.0210298, 0.0239916, 0.0264513, 0.0267368, 0.0280078, 0.0319428, 0.0364792, 0.0380753, 0.0460231, 0.0481536, 0.0527758, 0.0551826, 0.057605, 0.0630491, 0.073492, 0.0872401, 0.0985782, 0.104607, 0.115602, 0.133453, 0.169491, 0.196838, 0.202161, 0.226478, 0.2403, 0.279103, 0.310176, 0.366109, 0.41119, 0.461136, 0.49107, 0.535891, 0.557771, 0.597571, 0.65381, 0.641248, 0.751453, 0.972327, 1.5146, 2.10013, 2.61867, 4.5147, 4.29732, 5.19928, 16.2084])
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
