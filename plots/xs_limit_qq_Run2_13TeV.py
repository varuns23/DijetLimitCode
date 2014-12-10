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
c.SaveAs('xs_limit_qq_exp_Run2_13TeV.eps')
