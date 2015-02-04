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
xs_obs_limits = array('d', [1.86325, 1.56564, 1.28752, 0.972255, 0.739279, 0.585745, 0.483064, 0.417617, 0.381021, 0.346899, 0.32619, 0.29872, 0.265589, 0.234737, 0.207129, 0.184716, 0.163163, 0.145055, 0.130288, 0.119732, 0.111059, 0.104013, 0.0931989, 0.0832613, 0.0742003, 0.0662683, 0.0598146, 0.0541417, 0.0506755, 0.0458979, 0.041732, 0.0381887, 0.034748, 0.0314966, 0.0285166, 0.0258759, 0.0245475, 0.0222264, 0.020406, 0.0188927, 0.0175679, 0.0164078, 0.0153956, 0.0144034, 0.0135911, 0.0129604, 0.0126767, 0.0119384, 0.011309, 0.0107868, 0.0103641, 0.00999536, 0.00967439, 0.00939046, 0.00914949, 0.00894144, 0.00876195, 0.00861028, 0.00848003])
xs_exp_limits = array('d', [2.53057, 1.35961, 1.17456, 0.957121, 0.779983, 0.682322, 0.554131, 0.486514, 0.401778, 0.355749, 0.301611, 0.27008, 0.24647, 0.21522, 0.195772, 0.180178, 0.152819, 0.135282, 0.122006, 0.106746, 0.0980299, 0.0945691, 0.0830991, 0.075883, 0.0700194, 0.0636377, 0.0582284, 0.0543043, 0.0515312, 0.0452936, 0.0411678, 0.0368652, 0.0344719, 0.0308413, 0.0284004, 0.0266468, 0.026426, 0.0250325, 0.0228407, 0.0207904, 0.0196287, 0.0181444, 0.0171867, 0.016162, 0.0155728, 0.0152351, 0.014709, 0.0140935, 0.0136142, 0.0129895, 0.0128992, 0.0126822, 0.0124685, 0.0119289, 0.0118748, 0.0115604, 0.0113587, 0.0111597, 0.0108696])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.444525, 0.654636, 0.566726, 0.420915, 0.444933, 0.407616, 0.327824, 0.287058, 0.256692, 0.218829, 0.194959, 0.170684, 0.151578, 0.138104, 0.119198, 0.109306, 0.103351, 0.0932325, 0.0812321, 0.0739296, 0.0658216, 0.0581174, 0.0538981, 0.0524619, 0.0484492, 0.045435, 0.0401784, 0.0351565, 0.0321271, 0.0292072, 0.0271985, 0.0249192, 0.0231538, 0.0222345, 0.0213038, 0.0192723, 0.0174331, 0.0162227, 0.0154401, 0.0140839, 0.013468, 0.0134745, 0.0129423, 0.0123238, 0.011722, 0.0113695, 0.0114222, 0.0109383, 0.0104267, 0.0101766, 0.0101588, 0.00975921, 0.00948669, 0.00933432, 0.00937215, 0.00930467, 0.00904083, 0.00904476, 0.00911176, 0.0146772, 0.0150387, 0.0154472, 0.0158382, 0.0159666, 0.0161107, 0.0160171, 0.0165852, 0.0170242, 0.0173674, 0.0180303, 0.0187606, 0.019792, 0.020927, 0.0227376, 0.0231147, 0.0244451, 0.0258894, 0.0277892, 0.0304443, 0.033998, 0.0360244, 0.0390178, 0.0422839, 0.0450225, 0.0476585, 0.0503137, 0.0536049, 0.0594698, 0.0665416, 0.071304, 0.0805836, 0.0873129, 0.0895806, 0.104711, 0.111731, 0.125658, 0.147969, 0.157118, 0.170009, 0.186229, 0.210545, 0.238399, 0.28432, 0.322688, 0.351021, 0.411779, 0.473045, 0.519629, 0.606226, 0.688811, 0.848131, 1.01308, 1.15004, 1.43839, 2.1686, 2.22151, 3.31537, 8.60527])
xs_exp_limits_2sigma = array('d', [0.229932, 0.328557, 0.33016, 0.28523, 0.296721, 0.247731, 0.239568, 0.210908, 0.185124, 0.148727, 0.132903, 0.106657, 0.0998131, 0.0932812, 0.0807836, 0.0735303, 0.0678438, 0.0623868, 0.0531498, 0.0500301, 0.046006, 0.0391843, 0.0351825, 0.0338641, 0.0328946, 0.0297451, 0.0289223, 0.0269901, 0.0240256, 0.0210968, 0.0191982, 0.0182715, 0.0169963, 0.0157171, 0.0141379, 0.0132122, 0.0119665, 0.011581, 0.0117998, 0.01061, 0.0101384, 0.00972152, 0.00975563, 0.00997083, 0.00919016, 0.00881832, 0.00890984, 0.00884779, 0.00856065, 0.00807198, 0.00813502, 0.00828223, 0.00795341, 0.00771688, 0.00808643, 0.00831003, 0.00803174, 0.00792793, 0.00779238, 0.0196767, 0.0193172, 0.0193738, 0.0204472, 0.0207731, 0.021039, 0.0217064, 0.02241, 0.0230742, 0.0237958, 0.0247435, 0.0261381, 0.0275734, 0.0295421, 0.0318623, 0.0342572, 0.0362914, 0.0385477, 0.0412242, 0.0433008, 0.0484467, 0.0544326, 0.0584088, 0.0643373, 0.0676149, 0.0744475, 0.0763146, 0.0779152, 0.0812049, 0.0938607, 0.0948415, 0.103512, 0.121057, 0.14326, 0.155622, 0.164072, 0.180132, 0.200001, 0.216698, 0.240751, 0.283939, 0.308734, 0.331104, 0.360435, 0.437793, 0.528572, 0.573384, 0.619673, 0.763437, 0.966698, 1.10271, 1.25057, 1.52783, 1.61133, 2.29362, 3.45741, 3.72495, 4.81157, 15.535])

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
graph_xsQstar.Draw("L")

legend = TLegend(.50,.59,.80,.68)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
#legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected quark-gluon","lp")
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
