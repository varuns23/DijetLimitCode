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

  #cmd = "./stats " + str(int(mass)) + " qq | tee stats_" + str(int(mass)) + "_qq.log"
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
xs_obs_limits = array('d', [1.38379, 1.24173, 1.02206, 0.736203, 0.54147, 0.435898, 0.377457, 0.325409, 0.282114, 0.269605, 0.254996, 0.22827, 0.208752, 0.179774, 0.155, 0.135834, 0.121019, 0.10804, 0.101126, 0.0929693, 0.0858061, 0.0777961, 0.069394, 0.061842, 0.0553618, 0.0513585, 0.0459987, 0.04137, 0.0375407, 0.0342498, 0.0313689, 0.0287582, 0.0261014, 0.0245321, 0.0218044, 0.0196816, 0.0178383, 0.0163219, 0.0150744, 0.0139762, 0.0131803, 0.0127585, 0.0118847, 0.0111061, 0.0104158, 0.00978419, 0.0092016, 0.00866899, 0.00818424, 0.00780129, 0.00745886, 0.00722949, 0.00691957, 0.0069574, 0.00672669, 0.00651929, 0.00633675, 0.00617576, 0.00603377])
xs_exp_limits = array('d', [1.32662, 1.04712, 0.871841, 0.763378, 0.604613, 0.512415, 0.409525, 0.37813, 0.316492, 0.26821, 0.225702, 0.211224, 0.191192, 0.164255, 0.153885, 0.130094, 0.112727, 0.100721, 0.0938818, 0.0842736, 0.0748789, 0.0696973, 0.0614141, 0.0571298, 0.050609, 0.0505873, 0.0447526, 0.042153, 0.0378959, 0.0336265, 0.0299338, 0.0268022, 0.02538, 0.0243622, 0.0223201, 0.0214262, 0.0200042, 0.0183909, 0.0167132, 0.0157053, 0.0144776, 0.0137304, 0.0128506, 0.0127121, 0.0125366, 0.0117526, 0.0114608, 0.01069, 0.0101056, 0.00964305, 0.00943109, 0.00907362, 0.00881578, 0.00861468, 0.00836653, 0.00817389, 0.00810625, 0.00773308, 0.00740899])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.553149, 0.605472, 0.497907, 0.422065, 0.398728, 0.320402, 0.277444, 0.246079, 0.214258, 0.186131, 0.153546, 0.136212, 0.122603, 0.110795, 0.103033, 0.0890766, 0.0802147, 0.071061, 0.0650772, 0.0580888, 0.0531488, 0.048257, 0.0432737, 0.0400999, 0.0367421, 0.0341905, 0.0300707, 0.0275631, 0.025648, 0.0235605, 0.0209099, 0.0189808, 0.0179832, 0.0171848, 0.0163242, 0.0145224, 0.0136786, 0.0130967, 0.0118534, 0.0110431, 0.010331, 0.0102679, 0.00989325, 0.00923333, 0.00916755, 0.00890107, 0.00867183, 0.00818125, 0.00783081, 0.00783335, 0.00752358, 0.00726917, 0.00726596, 0.0070215, 0.00685178, 0.00684056, 0.00678929, 0.00669672, 0.00674289, 0.00997627, 0.0101936, 0.0108436, 0.0111022, 0.01123, 0.0115576, 0.01179, 0.0118285, 0.0125744, 0.0129947, 0.0134875, 0.0144099, 0.0149177, 0.0155073, 0.0162546, 0.0171011, 0.0174576, 0.0185693, 0.0198373, 0.0216297, 0.0243775, 0.0268857, 0.0276908, 0.0308872, 0.0330253, 0.0337157, 0.0354153, 0.0382883, 0.0415162, 0.0475708, 0.0522095, 0.0582035, 0.0641816, 0.0726146, 0.074319, 0.0817582, 0.0893393, 0.103364, 0.115419, 0.129459, 0.136164, 0.151049, 0.17436, 0.199272, 0.225797, 0.250063, 0.298848, 0.330151, 0.378977, 0.433209, 0.501443, 0.571799, 0.662882, 0.813026, 0.999567, 1.38064, 1.51157, 1.86801, 3.73806])
xs_exp_limits_2sigma = array('d', [0.303257, 0.333564, 0.308249, 0.284194, 0.284076, 0.228811, 0.22371, 0.190595, 0.149008, 0.129182, 0.116426, 0.0880984, 0.082164, 0.0762827, 0.067161, 0.058025, 0.0569503, 0.0479491, 0.045974, 0.0412997, 0.0365193, 0.0300626, 0.0293357, 0.0291251, 0.0279327, 0.0250099, 0.0226732, 0.0211706, 0.0186569, 0.0166135, 0.0157665, 0.0153359, 0.0141636, 0.0117988, 0.011454, 0.0101554, 0.0100318, 0.0101838, 0.00901634, 0.00861373, 0.00818359, 0.00823463, 0.00809799, 0.00781348, 0.0076614, 0.00764531, 0.00735599, 0.00719641, 0.00699316, 0.00695484, 0.00664164, 0.00655023, 0.00622805, 0.00630133, 0.00640057, 0.00619872, 0.006306, 0.00629481, 0.00603722, 0.0135155, 0.0136707, 0.0135331, 0.0137574, 0.0141109, 0.0149767, 0.0157097, 0.0166216, 0.0167861, 0.0172544, 0.017919, 0.0195609, 0.0206231, 0.0219158, 0.0230054, 0.0229214, 0.0255058, 0.027298, 0.0303744, 0.0310706, 0.0335566, 0.0388273, 0.0425648, 0.047078, 0.0464156, 0.0508704, 0.0556305, 0.0543938, 0.0573703, 0.0671378, 0.071207, 0.0731614, 0.0836527, 0.100902, 0.110668, 0.118719, 0.127573, 0.145331, 0.15612, 0.178156, 0.194352, 0.210187, 0.227486, 0.26114, 0.306397, 0.362231, 0.428333, 0.4689, 0.509276, 0.589829, 0.781116, 0.836453, 1.11005, 1.09308, 1.42221, 1.91646, 2.20672, 2.80414, 6.15124])

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

xsAxi = array('d', [
0.1712E+03,
0.1144E+03,
0.7846E+02,
0.5497E+02,
0.3921E+02,
0.2842E+02,
0.2086E+02,
0.1550E+02,
0.1163E+02,
0.8802E+01,
0.6713E+01,
0.5157E+01,
0.3984E+01,
0.3095E+01,
0.2416E+01,
0.1894E+01,
0.1491E+01,
0.1177E+01,
0.9328E+00,
0.7410E+00,
0.5901E+00,
0.4710E+00,
0.3767E+00,
0.3019E+00,
0.2423E+00,
0.1947E+00,
0.1567E+00,
0.1262E+00,
0.1017E+00,
0.8207E-01,
0.6626E-01,
0.5352E-01,
0.4324E-01,
0.3494E-01,
0.2824E-01,
0.2283E-01,
0.1845E-01,
0.1490E-01,
0.1203E-01,
0.9711E-02,
0.7833E-02,
0.6314E-02,
0.5085E-02,
0.4091E-02,
0.3288E-02,
0.2639E-02,
0.2115E-02,
0.1693E-02,
0.1353E-02,
0.1079E-02,
0.8594E-03,
0.6830E-03,
0.5417E-03,
0.4286E-03,
0.3383E-03,
0.2664E-03,
0.2092E-03,
0.1638E-03,
0.1279E-03,
0.9958E-04,
0.7727E-04,
0.5977E-04,
0.4606E-04,
0.3537E-04,
0.2707E-04,
0.2064E-04,
0.1567E-04,
0.1185E-04,
0.8929E-05,
0.6698E-05,
0.5005E-05,
0.3724E-05,
0.2760E-05,
0.2037E-05,
0.1498E-05,
0.1097E-05,
0.8002E-06,
0.5820E-06,
0.4218E-06,
0.3046E-06,
0.2195E-06])

xsDiquark = array('d', [
0.5824E+02,
0.4250E+02,
0.3172E+02,
0.2411E+02,
0.1862E+02,
0.1457E+02,
0.1153E+02,
0.9211E+01,
0.7419E+01,
0.6019E+01,
0.4912E+01,
0.4031E+01,
0.3323E+01,
0.2750E+01,
0.2284E+01,
0.1903E+01,
0.1590E+01,
0.1331E+01,
0.1117E+01,
0.9386E+00,
0.7900E+00,
0.6658E+00,
0.5618E+00,
0.4745E+00,
0.4010E+00,
0.3391E+00,
0.2869E+00,
0.2428E+00,
0.2055E+00,
0.1740E+00,
0.1473E+00,
0.1246E+00,
0.1055E+00,
0.8922E-01,
0.7544E-01,
0.6376E-01,
0.5385E-01,
0.4546E-01,
0.3834E-01,
0.3231E-01,
0.2720E-01,
0.2288E-01,
0.1922E-01,
0.1613E-01,
0.1352E-01,
0.1132E-01,
0.9463E-02,
0.7900E-02,
0.6584E-02,
0.5479E-02,
0.4551E-02,
0.3774E-02,
0.3124E-02,
0.2581E-02,
0.2128E-02,
0.1750E-02,
0.1437E-02,
0.1177E-02,
0.9612E-03,
0.7833E-03,
0.6366E-03,
0.5160E-03,
0.4170E-03,
0.3360E-03,
0.2700E-03,
0.2162E-03,
0.1725E-03,
0.1372E-03,
0.1087E-03,
0.8577E-04,
0.6742E-04,
0.5278E-04,
0.4114E-04,
0.3192E-04,
0.2465E-04,
0.1894E-04,
0.1448E-04,
0.1101E-04,
0.8322E-05,
0.6253E-05,
0.4670E-05])

xsWprime = array('d', [
0.8811E+01,
0.6024E+01,
0.4216E+01,
0.3010E+01,
0.2185E+01,
0.1610E+01,
0.1200E+01,
0.9043E+00,
0.6875E+00,
0.5271E+00,
0.4067E+00,
0.3158E+00,
0.2464E+00,
0.1932E+00,
0.1521E+00,
0.1201E+00,
0.9512E-01,
0.7554E-01,
0.6012E-01,
0.4792E-01,
0.3827E-01,
0.3059E-01,
0.2448E-01,
0.1960E-01,
0.1571E-01,
0.1259E-01,
0.1009E-01,
0.8090E-02,
0.6483E-02,
0.5193E-02,
0.4158E-02,
0.3327E-02,
0.2660E-02,
0.2125E-02,
0.1695E-02,
0.1351E-02,
0.1075E-02,
0.8546E-03,
0.6781E-03,
0.5372E-03,
0.4248E-03,
0.3353E-03,
0.2642E-03,
0.2077E-03,
0.1629E-03,
0.1275E-03,
0.9957E-04,
0.7757E-04,
0.6027E-04,
0.4670E-04,
0.3610E-04,
0.2783E-04,
0.2140E-04,
0.1641E-04,
0.1254E-04,
0.9561E-05,
0.7269E-05,
0.5510E-05,
0.4167E-05,
0.3143E-05,
0.2364E-05,
0.1774E-05,
0.1329E-05,
0.9931E-06,
0.7411E-06,
0.5523E-06,
0.4108E-06,
0.3055E-06,
0.2271E-06,
0.1687E-06,
0.1254E-06,
0.9327E-07,
0.6945E-07,
0.5177E-07,
0.3863E-07,
0.2888E-07,
0.2162E-07,
0.1622E-07,
0.1218E-07,
0.9156E-08,
0.6893E-08])

xsZprime = array('d', [
0.5027E+01,
0.3398E+01,
0.2353E+01,
0.1663E+01,
0.1196E+01,
0.8729E+00,
0.6450E+00,
0.4822E+00,
0.3638E+00,
0.2769E+00,
0.2123E+00,
0.1639E+00,
0.1272E+00,
0.9933E-01,
0.7789E-01,
0.6134E-01,
0.4848E-01,
0.3845E-01,
0.3059E-01,
0.2440E-01,
0.1952E-01,
0.1564E-01,
0.1256E-01,
0.1010E-01,
0.8142E-02,
0.6570E-02,
0.5307E-02,
0.4292E-02,
0.3473E-02,
0.2813E-02,
0.2280E-02,
0.1848E-02,
0.1499E-02,
0.1216E-02,
0.9864E-03,
0.8002E-03,
0.6490E-03,
0.5262E-03,
0.4264E-03,
0.3453E-03,
0.2795E-03,
0.2260E-03,
0.1826E-03,
0.1474E-03,
0.1188E-03,
0.9566E-04,
0.7690E-04,
0.6173E-04,
0.4947E-04,
0.3957E-04,
0.3159E-04,
0.2516E-04,
0.2001E-04,
0.1587E-04,
0.1255E-04,
0.9906E-05,
0.7795E-05,
0.6116E-05,
0.4785E-05,
0.3731E-05,
0.2900E-05,
0.2247E-05,
0.1734E-05,
0.1334E-05,
0.1022E-05,
0.7804E-06,
0.5932E-06,
0.4492E-06,
0.3388E-06,
0.2544E-06,
0.1903E-06,
0.1417E-06,
0.1051E-06,
0.7764E-07,
0.5711E-07,
0.4186E-07,
0.3055E-07,
0.2223E-07,
0.1612E-07,
0.1164E-07,
0.8394E-08])

graph_xsAxi = TGraph(len(massesTh),massesTh,xsAxi)
graph_xsAxi.SetLineWidth(2)
graph_xsAxi.SetLineStyle(2)
graph_xsAxi.SetLineColor(2)

graph_xsDiquark = TGraph(len(massesTh),massesTh,xsDiquark)
graph_xsDiquark.SetLineWidth(2)
graph_xsDiquark.SetLineStyle(3)
graph_xsDiquark.SetLineColor(1)

graph_xsWprime = TGraph(len(massesTh),massesTh,xsWprime)
graph_xsWprime.SetLineWidth(2)
graph_xsWprime.SetLineStyle(4)
graph_xsWprime.SetLineColor(9)

graph_xsZprime = TGraph(len(massesTh),massesTh,xsZprime)
graph_xsZprime.SetLineWidth(2)
graph_xsZprime.SetLineStyle(5)
graph_xsZprime.SetLineColor(6)

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
graph_xsAxi.Draw("L")
graph_xsDiquark.Draw("L")
graph_xsWprime.Draw("L")
graph_xsZprime.Draw("L")

legend = TLegend(.50,.59,.80,.68)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
#legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected quark-quark","lp")
legend.Draw()

legendTh = TLegend(.50,.70,.80,.83)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.03)
legendTh.AddEntry(graph_xsAxi,"Axigluon/coloron","l")
legendTh.AddEntry(graph_xsDiquark,"Scalar diquark","l")
legendTh.AddEntry(graph_xsWprime,"W' SSM","l")
legendTh.AddEntry(graph_xsZprime,"Z' SSM","l")
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

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis();

c.SetLogy()
c.SaveAs('xs_limit_qq_exp_Run2_13TeV.pdf')
