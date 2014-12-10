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
xs_obs_limits = array('d', [10.5027, 4.26601, 2.27372, 3.93591, 3.25211, 1.70359, 1.22021, 0.815595, 0.537728, 0.388839, 0.347078, 0.403873, 0.427915, 0.429197, 0.438614, 0.440675, 0.437022, 0.407458, 0.385294, 0.351107, 0.306269, 0.267539, 0.230211, 0.203268, 0.177229, 0.152755, 0.130531, 0.107782, 0.096809, 0.083334, 0.0730329, 0.0640487, 0.0578645, 0.0526902, 0.0498375, 0.0443445, 0.0398526, 0.0347775, 0.0325168, 0.028741, 0.0278583, 0.0262532, 0.02454, 0.0230606, 0.021557, 0.0203361, 0.0199076, 0.0188611, 0.0179068, 0.0174541, 0.017023, 0.016633, 0.0163096, 0.0157769, 0.015666, 0.0158616, 0.0158776, 0.0159715, 0.0161389])
xs_exp_limits = array('d', [9.95128, 5.46362, 2.616, 3.44621, 3.05019, 1.68036, 1.20739, 0.815478, 0.526677, 0.402473, 0.337731, 0.379729, 0.416475, 0.417421, 0.460144, 0.453479, 0.457674, 0.42457, 0.388, 0.34551, 0.302448, 0.258442, 0.235407, 0.209608, 0.181151, 0.151763, 0.130819, 0.112648, 0.0969738, 0.087636, 0.0731962, 0.0652566, 0.0557987, 0.0517085, 0.0488232, 0.043072, 0.0380861, 0.0325525, 0.0298494, 0.0279302, 0.0272254, 0.0266263, 0.025565, 0.0242407, 0.0226104, 0.0215609, 0.0201612, 0.0196045, 0.0188383, 0.0182952, 0.0192062, 0.0187168, 0.0184784, 0.0182941, 0.0177369, 0.0182315, 0.0181882, 0.0188021, 0.0189411])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [2.45912, 1.2813, 1.02626, 1.44234, 1.13881, 0.868929, 0.681646, 0.478456, 0.343059, 0.269843, 0.237842, 0.228813, 0.236902, 0.248088, 0.276941, 0.273629, 0.275809, 0.2646, 0.259003, 0.225542, 0.194013, 0.170907, 0.150892, 0.12831, 0.109514, 0.102224, 0.0915855, 0.0756673, 0.0610256, 0.0543018, 0.0481412, 0.0420066, 0.0383726, 0.0343882, 0.030596, 0.0287606, 0.0273617, 0.0251276, 0.0229621, 0.0215959, 0.0202545, 0.018575, 0.0172703, 0.0169038, 0.0159396, 0.0162581, 0.0153401, 0.0154008, 0.0146059, 0.0147327, 0.0147369, 0.0147275, 0.0150599, 0.0150291, 0.0149809, 0.0154216, 0.0154093, 0.0155845, 0.0155873, 0.0243684, 0.0247257, 0.0240836, 0.023574, 0.0232493, 0.0239534, 0.0240083, 0.0241083, 0.0249345, 0.0244936, 0.0249244, 0.0263168, 0.0276118, 0.0281189, 0.0293794, 0.032179, 0.0336654, 0.0371653, 0.0407259, 0.0426101, 0.0452888, 0.0498378, 0.0551732, 0.0611507, 0.0719454, 0.0817356, 0.0897262, 0.0956085, 0.114897, 0.124681, 0.144171, 0.170473, 0.195268, 0.232767, 0.255164, 0.287348, 0.3266, 0.374121, 0.421052, 0.494212, 0.560734, 0.641971, 0.69323, 0.739131, 0.744336, 0.800188, 0.761448, 0.674738, 0.58607, 0.664699, 0.911698, 1.40765, 2.36857, 3.40724, 5.17649, 7.05864, 5.78335, 14.7026, 25.2612])
xs_exp_limits_2sigma = array('d', [1.09147, 0.732779, 0.559582, 0.675682, 0.57552, 0.519598, 0.473988, 0.349542, 0.282256, 0.200123, 0.168506, 0.148789, 0.164951, 0.169558, 0.172065, 0.17137, 0.170931, 0.158037, 0.156567, 0.15169, 0.126653, 0.108527, 0.0959857, 0.0824565, 0.0702657, 0.0642277, 0.0587964, 0.053483, 0.048353, 0.038195, 0.0341278, 0.0308314, 0.0289542, 0.027203, 0.025957, 0.0222351, 0.0195341, 0.0182464, 0.0174354, 0.0171011, 0.0159013, 0.0153336, 0.0147243, 0.0147774, 0.013961, 0.0132619, 0.0136004, 0.0128221, 0.0127303, 0.0128614, 0.0130667, 0.0129359, 0.0129037, 0.0131221, 0.013491, 0.0138553, 0.0136851, 0.0135989, 0.01454, 0.0305178, 0.0310801, 0.0323214, 0.0327646, 0.0328327, 0.0336341, 0.0340971, 0.0343621, 0.03495, 0.0349561, 0.0353593, 0.0359783, 0.0354598, 0.0391641, 0.0450589, 0.0465849, 0.0490807, 0.0509586, 0.0556721, 0.0636965, 0.0684724, 0.0830229, 0.0868219, 0.096858, 0.10022, 0.104035, 0.11684, 0.138748, 0.167045, 0.18376, 0.200549, 0.223088, 0.250479, 0.322852, 0.378443, 0.392236, 0.440211, 0.48111, 0.542202, 0.647739, 0.7527, 0.824093, 0.933633, 0.99722, 1.10772, 1.14933, 1.1956, 1.31011, 1.27367, 1.26986, 1.73682, 2.61342, 3.61835, 4.34814, 7.62971, 11.0121, 11.3899, 22.6464, 42.4446])
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
legend.AddEntry(graph_exp,"Expected gluon-gluon","lp")
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
c.SaveAs('xs_limit_gg_exp_Run2_13TeV.eps')
