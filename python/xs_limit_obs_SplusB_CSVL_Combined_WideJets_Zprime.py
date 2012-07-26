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

sys = True
#sys = False

BR = [0.2, 0.5, 0.75, 1.]

masses = array('d')
xs_limits = {}

########################################################
## Uncomment this part if running the limit code

#mass_start = 1000.
#mass_step = 100.
#steps = 30

### for running the limit code
##for br in range(0,len(BR)):

  ##xs_limits_array = array('d')

  ##for i in range(0,steps+1):

    ##mass = mass_start + float(i)*mass_step

    ##if(br==0): masses.append(mass)

    ##cmd = "./stats " + str(mass) + " " + str(BR[br]) + " qq"
    ##print "Running: " + cmd
    ##proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
    ##output = proc.communicate()[0]
    ##if proc.returncode != 0:
      ##print output
      ##sys.exit(1)
    ###print output
    ##outputlines =  output.split("\n")

    ##for line in outputlines:
      ##if re.search("^Data fit status:", line):
        ##if re.search("FAILED", line.split()[3]):
          ##print line
      ##if re.search("observed bound =", line):
        ##xs_limits_array.append(float(line.split()[6]))

  ##xs_limits[br] = xs_limits_array


## for reading the limit code log files
#for br in range(0,len(BR)):

  #xs_limits_array = array('d')

  #for i in range(0,steps+1):

    #mass = mass_start + float(i)*mass_step

    #if(br==0): masses.append(mass)

    #log_file_name = "stats_" + str(int(mass)) + "_" + str(BR[br]) + "_qq.log"
    #print "Reading: " + log_file_name
    #log_file = open(log_file_name,'r')
    #outputlines = log_file.readlines()
    #log_file.close()

    #for line in outputlines:
      #if re.search("^Data fit status:", line):
        #if re.search("FAILED", line.split()[3]):
          #print line
      #if re.search("observed bound =", line):
        #xs_limits_array.append(float(line.split()[6]))

  #xs_limits[br] = xs_limits_array


#print "masses:"
#print masses
#for br in range(0,len(BR)):
  #print "xs_limits, BR="+str(BR[br])+":"
  #print xs_limits[br]

##
########################################################

########################################################
## Comment out this part if running the limit code

#stat only
masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
# S > 0
#xs_limits[0] = array('d', [1.26494, 0.51744500000000004, 0.24494099999999999, 0.15290899999999999, 0.11716699999999999, 0.127417, 0.0980293, 0.074709399999999995, 0.052263499999999997, 0.047051599999999999, 0.077230499999999994, 0.074166700000000002, 0.047022000000000001, 0.033457899999999999, 0.034281499999999999, 0.038926099999999998, 0.030869500000000001, 0.0180441, 0.0115011, 0.0081844799999999992, 0.00617397, 0.0043310700000000002, 0.0035545199999999998, 0.0033220699999999999, 0.0034729100000000001, 0.0033162199999999999, 0.0031368400000000001, 0.0028479400000000002, 0.0025428299999999998, 0.0021667800000000001, 0.0018278700000000001])
#xs_limits[1] = array('d', [1.0946800000000001, 0.76459699999999997, 0.22778000000000001, 0.12812100000000001, 0.095530799999999999, 0.0988319, 0.092431600000000003, 0.081632499999999997, 0.058480200000000003, 0.049614800000000001, 0.076134900000000005, 0.073108599999999996, 0.048631199999999999, 0.035808800000000002, 0.036747500000000002, 0.0420127, 0.033803899999999998, 0.020277199999999999, 0.012253200000000001, 0.0090612899999999996, 0.00661912, 0.00490407, 0.0038571299999999998, 0.0037078900000000001, 0.0038175700000000002, 0.0036000200000000002, 0.0032749200000000002, 0.0030875899999999999, 0.0027491400000000002, 0.0023425400000000002, 0.0019850800000000002])
#xs_limits[2] = array('d', [0.79585600000000001, 0.70464899999999997, 0.19602600000000001, 0.10609, 0.074375999999999998, 0.073743799999999998, 0.078085100000000005, 0.090339699999999995, 0.060399899999999999, 0.049777299999999997, 0.067712400000000006, 0.064921099999999995, 0.046178499999999997, 0.035585899999999997, 0.037168899999999998, 0.041651300000000002, 0.034167700000000002, 0.021440799999999999, 0.0130528, 0.0097073899999999998, 0.0070924899999999999, 0.0054531900000000001, 0.0042293599999999997, 0.0040089499999999998, 0.0041018199999999999, 0.0038613100000000002, 0.0034375999999999999, 0.0031454400000000002, 0.0029437999999999999, 0.00249454, 0.00212824])
#xs_limits[3] = array('d', [0.56668799999999997, 0.58086000000000004, 0.17114699999999999, 0.089566499999999993, 0.059730699999999998, 0.056915300000000002, 0.064923800000000004, 0.091563800000000001, 0.066524299999999995, 0.051226899999999999, 0.056009000000000003, 0.053176099999999997, 0.041119599999999999, 0.033465799999999997, 0.034853299999999997, 0.038552099999999999, 0.032492, 0.0215675, 0.0135388, 0.010174300000000001, 0.0076462500000000003, 0.0060970299999999998, 0.0046936, 0.0043732399999999996, 0.0043788999999999998, 0.0040874099999999997, 0.0036084099999999998, 0.0032902000000000001, 0.0031122300000000001, 0.0026434700000000002, 0.0022806300000000001])
# S unconstrained
xs_limits[0] = array('d', [1.2636799999999999, 0.51735900000000001, 0.24467900000000001, 0.11035, 0.086079699999999995, 0.12742500000000001, 0.097502599999999995, 0.066894499999999996, 0.042850100000000002, 0.039650400000000002, 0.077264299999999994, 0.074559399999999998, 0.047017999999999997, 0.033449100000000002, 0.034284799999999997, 0.038927799999999999, 0.030872, 0.018045499999999999, 0.011383799999999999, 0.0072917399999999997, 0.0050720399999999999, 0.0035789900000000002, 0.00276057, 0.0029268699999999998, 0.0032743500000000001, 0.00323771, 0.0030343599999999998, 0.0028428099999999999, 0.0025424200000000001, 0.0021240999999999999, 0.00180471])
xs_limits[1] = array('d', [1.09518, 0.75600900000000004, 0.22772000000000001, 0.078358399999999995, 0.056206100000000002, 0.076980800000000002, 0.089873400000000006, 0.082002699999999998, 0.052744899999999997, 0.047103600000000002, 0.076137999999999997, 0.073090500000000003, 0.048633599999999999, 0.035783799999999998, 0.036751899999999997, 0.042021700000000002, 0.033784500000000002, 0.020299500000000002, 0.0122358, 0.0080739699999999998, 0.0055857099999999998, 0.0038210499999999999, 0.0030126900000000002, 0.0031754600000000002, 0.0035115599999999999, 0.0034622199999999998, 0.0031509400000000001, 0.0030235800000000001, 0.0027444700000000002, 0.00227539, 0.0019239999999999999])
xs_limits[2] = array('d', [0.79559199999999997, 0.68790899999999999, 0.196378, 0.061234200000000003, 0.0404114, 0.052843899999999999, 0.072661900000000001, 0.090256799999999998, 0.0607305, 0.049879699999999999, 0.067714399999999994, 0.064909900000000006, 0.0463509, 0.035589200000000001, 0.037157700000000002, 0.041603599999999998, 0.034241199999999999, 0.0214384, 0.013043600000000001, 0.0086865599999999994, 0.0060248200000000002, 0.0041162600000000001, 0.0032441900000000001, 0.0034152700000000002, 0.0037747200000000001, 0.0037031400000000002, 0.0033336799999999999, 0.0031687299999999998, 0.00288186, 0.00239617, 0.0020388400000000001])
xs_limits[3] = array('d', [0.57004900000000003, 0.61349500000000001, 0.16109100000000001, 0.051637599999999999, 0.031774400000000001, 0.037227000000000003, 0.059446600000000002, 0.091739600000000004, 0.066630599999999998, 0.053002899999999999, 0.056009799999999998, 0.0531668, 0.041123699999999999, 0.033461499999999998, 0.034853700000000001, 0.038552500000000003, 0.032478300000000002, 0.021654699999999999, 0.0135269, 0.0092532599999999993, 0.0064902600000000003, 0.0043945099999999999, 0.00353075, 0.0035843300000000002, 0.0040222299999999999, 0.0039244600000000003, 0.0034550499999999999, 0.0032657300000000001, 0.00298782, 0.0025001400000000001, 0.00214554])

if sys:
 # sys + stat
 masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
 # S > 0
 #xs_limits[0] = array('d', [1.3648100000000001, 0.58711899999999995, 0.27155200000000002, 0.183139, 0.13209099999999999, 0.12962000000000001, 0.108418, 0.0842802, 0.060856199999999999, 0.0575132, 0.077734600000000001, 0.078043399999999999, 0.060779100000000003, 0.040989100000000001, 0.0360913, 0.038837299999999998, 0.035022699999999997, 0.026342399999999998, 0.0167986, 0.0113588, 0.0075952099999999998, 0.0055416399999999996, 0.0040954900000000002, 0.0035792699999999998, 0.00344086, 0.0033120699999999999, 0.0031159500000000001, 0.0029412100000000001, 0.0026468500000000001, 0.0023606199999999999, 0.00205522])
 #xs_limits[1] = array('d', [1.1756500000000001, 0.86084899999999998, 0.263907, 0.155894, 0.10377500000000001, 0.099532300000000004, 0.095978599999999997, 0.086569999999999994, 0.067128099999999996, 0.058552699999999999, 0.076283799999999999, 0.076775300000000005, 0.059325799999999998, 0.042446299999999999, 0.038846899999999997, 0.041987999999999998, 0.038195699999999999, 0.032306700000000001, 0.018825100000000001, 0.0128694, 0.0085677400000000008, 0.0061665399999999999, 0.0045899699999999996, 0.0039427000000000004, 0.0037603900000000002, 0.0035897799999999999, 0.0033545900000000002, 0.0032012899999999999, 0.0028911200000000001, 0.0025480199999999998, 0.0022226799999999999])
 #xs_limits[2] = array('d', [0.86296600000000001, 0.79286900000000005, 0.233573, 0.12772800000000001, 0.085305099999999995, 0.079887600000000003, 0.083033200000000001, 0.092668299999999995, 0.068289699999999995, 0.056228100000000003, 0.069396799999999995, 0.068206799999999998, 0.053856300000000003, 0.040979500000000002, 0.038738599999999998, 0.0417236, 0.0383007, 0.031675099999999998, 0.019021900000000001, 0.0131915, 0.0092612000000000007, 0.00685442, 0.00507845, 0.0042973100000000004, 0.0040595800000000001, 0.0038376600000000001, 0.0035878400000000001, 0.0032773400000000001, 0.00307354, 0.0027201700000000001, 0.0023685400000000001])
 #xs_limits[3] = array('d', [0.61651699999999998, 0.64604499999999998, 0.21223, 0.106056, 0.0684279, 0.063028699999999993, 0.069857000000000002, 0.093030399999999999, 0.073984900000000006, 0.055434499999999998, 0.058917700000000003, 0.056365800000000001, 0.046353699999999998, 0.037593399999999999, 0.036586, 0.038987599999999997, 0.036139200000000003, 0.029617399999999999, 0.018850599999999999, 0.013448099999999999, 0.0097049700000000003, 0.0070975300000000003, 0.0057316299999999997, 0.0046952699999999997, 0.0043628499999999997, 0.0040803899999999997, 0.0037947599999999999, 0.003447, 0.0032466299999999999, 0.0028686499999999999, 0.0025190299999999998])
 # S unconstrained
 xs_limits[0] = array('d', [1.3632500000000001, 0.58689100000000005, 0.27131300000000003, 0.122947, 0.099289600000000006, 0.12962299999999999, 0.107922, 0.075514800000000007, 0.0506471, 0.049593400000000003, 0.077767100000000006, 0.078216400000000005, 0.0607824, 0.040975699999999997, 0.036094000000000001, 0.038838900000000003, 0.035016100000000001, 0.026345, 0.016574200000000001, 0.0097907600000000008, 0.0062757799999999999, 0.00414256, 0.0032166600000000001, 0.00313058, 0.0033359700000000002, 0.0032036500000000002, 0.0031378199999999999, 0.0029355900000000001, 0.00264642, 0.00229708, 0.002006])
 xs_limits[1] = array('d', [1.1760299999999999, 0.85427299999999995, 0.26400899999999999, 0.090243500000000004, 0.061438, 0.081730700000000003, 0.096682299999999999, 0.086995100000000006, 0.060671799999999998, 0.054067700000000003, 0.076326199999999997, 0.076759599999999997, 0.059323800000000003, 0.042440600000000002, 0.038919700000000002, 0.041997199999999998, 0.0381301, 0.032338899999999997, 0.018790999999999999, 0.010960599999999999, 0.0069272400000000003, 0.0045547199999999999, 0.0035533499999999998, 0.0034031, 0.0034889000000000001, 0.0034277800000000001, 0.00325603, 0.0031329800000000001, 0.0028855700000000001, 0.0024722400000000001, 0.0021414200000000002])
 xs_limits[2] = array('d', [0.87196300000000004, 0.77605900000000005, 0.230992, 0.068682000000000007, 0.045793300000000002, 0.054545299999999998, 0.077714800000000001, 0.092566399999999993, 0.068677500000000002, 0.056358699999999998, 0.069397600000000004, 0.068204500000000001, 0.054203300000000003, 0.040978800000000003, 0.038749800000000001, 0.041698800000000001, 0.038364099999999998, 0.031665499999999999, 0.019008199999999999, 0.011739100000000001, 0.0074542799999999998, 0.0049242699999999997, 0.00382935, 0.0035298899999999999, 0.0037447399999999999, 0.0036768700000000001, 0.0034465300000000002, 0.0031871299999999998, 0.00302207, 0.0025842899999999999, 0.00225604])
 xs_limits[3] = array('d', [0.619479, 0.68008900000000005, 0.19694999999999999, 0.059652999999999998, 0.036709499999999999, 0.041013399999999998, 0.064202899999999993, 0.093175499999999994, 0.0741338, 0.057632299999999997, 0.058910900000000002, 0.056352600000000003, 0.0463574, 0.037584800000000002, 0.036586100000000003, 0.038988599999999998, 0.036123299999999997, 0.029706799999999998, 0.0188428, 0.0123483, 0.0076790299999999999, 0.0051573900000000004, 0.0039712699999999998, 0.0037152299999999999, 0.0040185500000000001, 0.0039134699999999996, 0.0036181099999999999, 0.0033015399999999999, 0.0031119799999999999, 0.0026994599999999999, 0.0023629800000000002])

##
########################################################

m_x = array('d', [500., 600.,  700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600., 3700., 3800., 3900., 4000., 4100., 4200., 4300., 4400., 4500.])
m_zprime = array('d', [700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800.])
m_s8 = array('d', [700., 1000., 1200., 1400., 1700., 2100., 2700.])
#zprime = array('d', [0.2555E+02, 0.1211E+02, 0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
zprime = array('d', [0.6246E+01, 0.3427E+01, 0.1969E+01, 0.1172E+01, 0.7171E+00, 0.4486E+00, 0.2857E+00, 0.1845E+00, 0.1206E+00, 0.7961E-01, 0.5295E-01, 0.3545E-01, 0.2386E-01, 0.1611E-01, 0.1092E-01, 0.7413E-02, 0.5039E-02, 0.3426E-02, 0.2329E-02, 0.1580E-02, 0.1070E-02, 0.7231E-03, 0.4867E-03, 0.3261E-03, 0.2174E-03, 0.1440E-03, 0.9477E-04, 0.6190E-04, 0.4007E-04])
rsg = array('d', [0.4828E+02, 0.1862E+02, 0.8100E+01, 0.3852E+01, 0.1961E+01, 0.1053E+01, 0.5905E+00, 0.3426E+00, 0.2044E+00, 0.1248E+00, 0.7770E-01, 0.4911E-01, 0.3145E-01, 0.2036E-01, 0.1330E-01, 0.8743E-02, 0.5781E-02, 0.3840E-02, 0.2559E-02, 0.1708E-02, 0.1142E-02, 0.7635E-03, 0.5101E-03, 0.3402E-03, 0.2264E-03, 0.1501E-03, 0.9913E-04, 0.6512E-04, 0.4253E-04, 0.2759E-04, 0.1775E-04])
s8 = array('d', [6.52288, 0.995265, 0.319478, 0.108527, 0.0235598, 0.00331955, 0.000188328])


graphs = {}

for br in range(0,len(BR)):
  graphs[br] = TGraph(len(masses),masses,xs_limits[br])
  graphs[br].SetMarkerStyle(24+br)
  graphs[br].SetMarkerSize(1.2)
  graphs[br].SetMarkerColor(kRed)
  graphs[br].SetLineWidth(3)
  graphs[br].SetLineStyle(1+br)
  graphs[br].SetLineColor(kRed)
  if br==0:
    graphs[br].GetXaxis().SetTitle("Resonance Mass [GeV]")
    graphs[br].GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
    graphs[br].GetXaxis().SetRangeUser(850,4150)
    graphs[br].GetYaxis().SetRangeUser(1e-03,20)
    graphs[br].GetXaxis().SetNdivisions(1005)

graph_zprime = TGraph(len(m_zprime),m_zprime,zprime)
graph_zprime.SetLineWidth(3)
graph_zprime.SetLineStyle(8)
graph_zprime.SetLineColor(kTeal+3)

graph_rsg = TGraph(len(m_x),m_x,rsg)
graph_rsg.SetLineWidth(3)
graph_rsg.SetLineStyle(8)
graph_rsg.SetLineColor(46)

graph_s8 = TGraph(len(m_s8),m_s8,s8)
graph_s8.SetLineWidth(3)
graph_s8.SetLineStyle(6)
graph_s8.SetLineColor(kBlue)

c = TCanvas("c", "",800,800)
c.cd()

for br in range(0,len(BR)):
  if br==0:
    graphs[br].Draw("ALP")
  else:
    graphs[br].Draw("LP")

graph_zprime.Draw("L")
graph_s8.Draw("L")

legend = TLegend(.45,.52,.77,.72)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
if sys: legend.SetHeader("Observed 95% CL Upper Limits")
else:   legend.SetHeader("Obs. 95% CL Upper Limits (stat. only)")
for br in range(0,len(BR)):
  legend.AddEntry(graphs[br], "f_{b#bar{b}} = " + str(BR[br]),"lp")
legend.Draw()

legend2 = TLegend(.45,.74,.77,.84)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
legend2.SetFillStyle(0)
legend2.SetTextFont(42)
legend2.SetTextSize(0.03)
legend2.AddEntry(graph_zprime,"Z' (f_{b#bar{b}} #approx 0.2)","l")
legend2.AddEntry(graph_s8,"S8_{b} (f_{b#bar{b}} #approx 1.0)","l")
legend2.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.45, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.05)
l1.DrawLatex(0.18,0.89, "qq/bb")
l1.SetTextSize(0.05)
l1.DrawLatex(0.18,0.38, "CMS")
l1.SetTextSize(0.03)
l1.DrawLatex(0.18,0.32, "#scale[0.75]{#int}Ldt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.28, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.24, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.05)
l1.DrawLatex(0.57,0.89, "0, 1 and 2 b-tags")

c.SetLogy()
if sys: c.SaveAs('CSVL_Combined_limit_obs_SplusB_sys_WideJets_Zprime.eps')
else:   c.SaveAs('CSVL_Combined_limit_obs_SplusB_WideJets_Zprime.eps')

