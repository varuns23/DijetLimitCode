#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
#gStyle.SetOptTitle(0)
gStyle.SetPalette(1)
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1);
gStyle.SetPadTickY(1);
#gStyle.SetPadLeftMargin(0.13);
#gStyle.SetPadRightMargin(0.07);
gStyle.SetTitleFont(42)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetLabelFont(42, "XYZ")


BR = 0.5

#masses = array('d')
#xs_obs_limits = array('d')
#xs_exp_limits = array('d')
#masses_exp = array('d')
#xs_exp_limits_1sigma = array('d')
#xs_exp_limits_1sigma_up = array('d')
#xs_exp_limits_2sigma = array('d')
#xs_exp_limits_2sigma_up = array('d')

#mass_start = 1000.
#mass_step = 100.
#steps = 30

#for i in range(0,steps+1):

  #mass = mass_start + float(i)*mass_step

  #masses.append(mass)
  #masses_exp.append(mass)

  #cmd = "./stats " + str(mass) + " " + " " + str(BR)
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

#for i in range(0,len(masses)):
  #masses_exp.append( masses[len(masses)-i-1] )
  #xs_exp_limits_1sigma.append( xs_exp_limits_1sigma_up[len(masses)-i-1] )
  #xs_exp_limits_2sigma.append( xs_exp_limits_2sigma_up[len(masses)-i-1] )

  
#print "masses:"
#print masses
#print "xs_obs_limits, BR=" + str(BR) + ":"
#print xs_obs_limits
#print "xs_exp_limits, BR=" + str(BR) + ":"
#print xs_exp_limits
#print ""
#print "masses_exp:"
#print masses_exp
#print "xs_exp_limits_1sigma, BR=" + str(BR) + ":"
#print xs_exp_limits_1sigma
#print "xs_exp_limits_2sigma, BR=" + str(BR) + ":"
#print xs_exp_limits_2sigma


masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_obs_limits = array('d', [0.86196899999999999, 0.65867600000000004, 0.57860199999999995, 0.464227, 0.24893399999999999, 0.20746800000000001, 0.21402299999999999, 0.179373, 0.12650800000000001, 0.0966833, 0.089395699999999995, 0.0771791, 0.0595819, 0.050279799999999999, 0.042826900000000001, 0.039688899999999999, 0.038232500000000003, 0.030439999999999998, 0.023666699999999999, 0.020066400000000002, 0.019188500000000001, 0.017895299999999999, 0.0152199, 0.012912399999999999, 0.0106785, 0.0093031599999999996, 0.0076646700000000002, 0.0060536100000000001, 0.0046564600000000003, 0.0037251599999999999, 0.0037252000000000001])
xs_exp_limits = array('d', [0.91356199999999999, 0.71726800000000002, 0.54131300000000004, 0.433863, 0.32630500000000001, 0.25379299999999999, 0.21595, 0.17464499999999999, 0.130663, 0.109723, 0.091292700000000004, 0.076229000000000005, 0.055860699999999999, 0.048417500000000002, 0.042837800000000002, 0.037634800000000003, 0.034569999999999997, 0.028535999999999999, 0.0236619, 0.019712500000000001, 0.018104599999999998, 0.016325200000000002, 0.0141044, 0.011745200000000001, 0.010533799999999999, 0.0086005300000000003, 0.0069848899999999997, 0.0060535500000000004, 0.0055879199999999997, 0.0050809999999999996, 0.0046565])
masses_exp = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0, 1100.0, 1000.0])
xs_exp_limits_1sigma = array('d', [0.803539, 0.60346, 0.43462000000000001, 0.34296700000000002, 0.25078099999999998, 0.19079599999999999, 0.17654700000000001, 0.133602, 0.10402, 0.081886799999999996, 0.070760100000000006, 0.063295699999999996, 0.048367300000000002, 0.037229900000000003, 0.033515000000000003, 0.031655500000000003, 0.025590700000000001, 0.022346299999999999, 0.0186231, 0.014899900000000001, 0.013969000000000001, 0.0130385, 0.0111751, 0.0091921399999999997, 0.0074503499999999997, 0.0069847299999999998, 0.00558773, 0.0046565599999999997, 0.0041908800000000001, 0.0037252299999999999, 0.0037251300000000001,
0.0060732199999999998, 0.0063990599999999998, 0.0069960999999999999, 0.0077127200000000002, 0.0092307299999999995, 0.0108574, 0.0137982, 0.014792400000000001, 0.017663600000000002, 0.020819500000000001, 0.023182100000000001, 0.026157799999999998, 0.030596399999999999, 0.0376142, 0.042600699999999998, 0.048176900000000002, 0.053835899999999999, 0.063547199999999998, 0.072657600000000003, 0.096334400000000001, 0.11802799999999999, 0.14674000000000001, 0.17065900000000001, 0.20572299999999999, 0.25484699999999999, 0.321936, 0.40698899999999999, 0.51143099999999997, 0.60814999999999997, 0.81713800000000003, 1.0768])
xs_exp_limits_2sigma = array('d', [0.646671, 0.48453200000000002, 0.36740800000000001, 0.31106899999999998, 0.20649500000000001, 0.17421700000000001, 0.147366, 0.110876, 0.088986800000000005, 0.066700599999999999, 0.052643200000000001, 0.045129099999999998, 0.040906900000000003, 0.030075600000000001, 0.026214000000000001, 0.026066599999999999, 0.018616899999999999, 0.018622199999999998, 0.014897000000000001, 0.0131112, 0.012105400000000001, 0.0103175, 0.0075233499999999998, 0.0070214300000000004, 0.0056610899999999997, 0.0055875200000000003, 0.0046565299999999999, 0.0037251699999999999, 0.0037129699999999999,
0.0028307200000000001, 0.00279386, 0.0076832999999999997, 0.0091138899999999995, 0.010587299999999999, 0.011853499999999999, 0.0122471, 0.014917400000000001, 0.016788999999999998, 0.018920800000000002, 0.0223813, 0.0269485, 0.030721499999999999, 0.030986699999999999, 0.038679600000000001, 0.043771200000000003, 0.058074500000000001, 0.059060000000000001, 0.069067799999999999, 0.078058199999999994, 0.100289, 0.117911, 0.13201399999999999, 0.17085400000000001, 0.19955999999999999, 0.24041199999999999, 0.30260500000000001, 0.37340499999999999, 0.45495799999999997, 0.60330799999999996, 0.75990899999999995, 0.91417400000000004, 1.26346])


graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.SetTitle("CSVL 1-tag, RSG-like resonances")
graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,10)

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


legend = TLegend(.45,.72,.85,.85)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(graph_obs,"Observed (F_{b#bar{b}}=" + str(BR) + ")","lp")
legend.AddEntry(graph_exp,"Expected (F_{b#bar{b}}=" + str(BR) + ")","lp")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.03)
l1.DrawLatex(0.17,0.33, "CMS Preliminary")
l1.DrawLatex(0.17,0.27, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.17,0.23, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.17,0.19, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.17,0.15, "Wide Jets")

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('CSVL_1Tag_limit_obsexp_WideJets_RSG.png')

