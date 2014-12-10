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
xs_obs_limits = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
xs_exp_limits = array('d', [4.21479, 2.68918, 2.07911, 1.58037, 1.25453, 1.12778, 0.851893, 0.781181, 0.642124, 0.558202, 0.445339, 0.406413, 0.347094, 0.308777, 0.274405, 0.246297, 0.226085, 0.206268, 0.178176, 0.158664, 0.138267, 0.121923, 0.105098, 0.0979816, 0.0869077, 0.0792691, 0.0736326, 0.0646779, 0.0569063, 0.0526865, 0.0496804, 0.0456634, 0.0408317, 0.0371618, 0.0350675, 0.032653, 0.0307214, 0.0290699, 0.0273465, 0.0255619, 0.0247638, 0.0229263, 0.0214206, 0.0205218, 0.0191157, 0.0175924, 0.016578, 0.0157793, 0.0149907, 0.0142235, 0.013998, 0.0136216, 0.013157, 0.0130271, 0.0128485, 0.0126089, 0.0121848, 0.0121288, 0.0119243])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.990577, 0.942143, 0.95941, 0.721132, 0.65313, 0.584519, 0.557572, 0.482757, 0.372509, 0.321431, 0.274723, 0.240704, 0.221686, 0.196098, 0.177605, 0.156113, 0.14164, 0.126637, 0.114746, 0.0988398, 0.0893049, 0.08094, 0.0719741, 0.0639834, 0.0615201, 0.0545797, 0.0513311, 0.0448606, 0.0420151, 0.0373056, 0.0340277, 0.0309306, 0.0284701, 0.0269205, 0.0245127, 0.0226353, 0.0222902, 0.0201962, 0.0183412, 0.0176101, 0.0159992, 0.0156453, 0.0147113, 0.0139138, 0.0136344, 0.0131635, 0.0123746, 0.0119088, 0.011318, 0.0110568, 0.0110674, 0.0106841, 0.0105673, 0.0102458, 0.0101233, 0.0100476, 0.0100215, 0.00995384, 0.00990291, 0.0150091, 0.0156032, 0.0155683, 0.0161914, 0.0167213, 0.0174869, 0.0180151, 0.0182267, 0.0193237, 0.0206563, 0.021484, 0.0226537, 0.0240176, 0.024827, 0.026779, 0.0282065, 0.0322245, 0.034589, 0.0371337, 0.0394661, 0.0425165, 0.0444446, 0.0501361, 0.0529827, 0.0544135, 0.0593379, 0.0637218, 0.0694159, 0.0763386, 0.0838134, 0.0977543, 0.105595, 0.115906, 0.130045, 0.147293, 0.158338, 0.171406, 0.193138, 0.212947, 0.241196, 0.280261, 0.305014, 0.335869, 0.399456, 0.478355, 0.50251, 0.56673, 0.648483, 0.80709, 0.920999, 1.09991, 1.22485, 1.5459, 1.97825, 2.41538, 3.3392, 4.17653, 6.3078, 16.0212])
xs_exp_limits_2sigma = array('d', [0.507784, 0.495869, 0.546778, 0.399355, 0.388584, 0.371832, 0.345324, 0.271475, 0.26234, 0.215701, 0.188636, 0.149382, 0.147679, 0.133929, 0.12803, 0.110069, 0.101442, 0.0859964, 0.0708157, 0.0662458, 0.0630295, 0.0608671, 0.0561633, 0.0486937, 0.0443621, 0.0395808, 0.035498, 0.0320656, 0.0298916, 0.0267541, 0.0254726, 0.0242713, 0.0221618, 0.0214431, 0.0182901, 0.0155183, 0.0143645, 0.014162, 0.0128088, 0.0134592, 0.0118326, 0.0114521, 0.0113385, 0.0107055, 0.010485, 0.0100448, 0.00969678, 0.00909918, 0.00935738, 0.00939822, 0.00922179, 0.00912686, 0.00896409, 0.00893645, 0.00832446, 0.00851848, 0.00851546, 0.00810072, 0.00846953, 0.0198114, 0.0203114, 0.0212294, 0.0220742, 0.0222423, 0.0224742, 0.0238797, 0.0250164, 0.0255294, 0.0259626, 0.0275163, 0.0299739, 0.0315567, 0.0334531, 0.037863, 0.0397516, 0.0445687, 0.0481526, 0.0524835, 0.0552076, 0.0599203, 0.0673721, 0.0735567, 0.0801157, 0.0852903, 0.0896526, 0.0977343, 0.0964338, 0.10813, 0.12069, 0.138791, 0.156615, 0.168877, 0.180559, 0.196936, 0.221085, 0.242163, 0.269163, 0.29232, 0.316856, 0.368206, 0.455741, 0.480387, 0.595232, 0.693408, 0.771077, 0.914026, 0.995442, 1.19267, 1.38786, 1.70786, 1.95202, 2.32268, 2.80446, 4.32132, 5.38015, 7.35259, 10.6113, 27.1717])

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
