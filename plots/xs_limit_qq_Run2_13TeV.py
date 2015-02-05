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
xs_obs_limits = array('d', [4.08257, 1.15721, 0.411506, 1.15263, 1.92977, 1.49016, 0.619607, 0.358359, 0.25801, 0.239432, 0.211465, 0.140706, 0.119473, 0.163481, 0.205587, 0.186243, 0.166694, 0.138751, 0.111409, 0.0986304, 0.104581, 0.11652, 0.113457, 0.0909747, 0.0661994, 0.0496412, 0.0398354, 0.03632, 0.0391764, 0.0470021, 0.0538693, 0.0533153, 0.0462661, 0.037536, 0.0318938, 0.0310645, 0.0324212, 0.0327933, 0.0311751, 0.0276193, 0.0229468, 0.0178672, 0.0133949, 0.0103379, 0.008632, 0.00751769, 0.00640263, 0.00573242, 0.00528528, 0.00497243, 0.00478172, 0.00464553, 0.00454648, 0.00447099, 0.0044117, 0.00436576, 0.00433159, 0.00430457, 0.00428106])
xs_exp_limits = array('d', [1.88695, 1.38645, 1.04097, 0.944241, 0.790821, 0.628347, 0.541367, 0.464813, 0.391869, 0.350656, 0.280238, 0.243175, 0.23424, 0.221311, 0.179991, 0.159704, 0.136738, 0.135707, 0.109479, 0.0996454, 0.0867903, 0.0767661, 0.0742238, 0.0665354, 0.061057, 0.0508328, 0.0484223, 0.0426503, 0.0407527, 0.0359847, 0.0320939, 0.0310224, 0.0271168, 0.0252927, 0.0231952, 0.0226623, 0.0203398, 0.0185865, 0.0170746, 0.0156388, 0.0147899, 0.013356, 0.0128138, 0.0132808, 0.0120217, 0.0115591, 0.0106948, 0.00998218, 0.00962778, 0.00915704, 0.00855671, 0.00809804, 0.00779993, 0.00758996, 0.00721888, 0.00714414, 0.00697149, 0.00681597, 0.00654551])

masses_exp = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0, 1200.0])
xs_exp_limits_1sigma = array('d', [0.627136, 0.789031, 0.612489, 0.538634, 0.462479, 0.419648, 0.366839, 0.310479, 0.254199, 0.216162, 0.197985, 0.169122, 0.154444, 0.138359, 0.11005, 0.106363, 0.0989591, 0.0905506, 0.0719866, 0.0672825, 0.0595586, 0.0541581, 0.0511453, 0.0473359, 0.0391299, 0.0349325, 0.0328176, 0.0306461, 0.0269011, 0.0257586, 0.0228719, 0.0203141, 0.0192502, 0.0166151, 0.0158395, 0.0155838, 0.0137977, 0.0124747, 0.0119487, 0.0113502, 0.0103418, 0.00999375, 0.00909468, 0.00924156, 0.00856971, 0.00815703, 0.00781915, 0.0073577, 0.00719931, 0.0069409, 0.00673095, 0.00659768, 0.0062153, 0.00581648, 0.00557198, 0.00547117, 0.00531664, 0.00516094, 0.00503687, 0.00873345, 0.00918933, 0.00969938, 0.0101199, 0.0103053, 0.0106009, 0.0109805, 0.0115454, 0.0119635, 0.0126226, 0.013038, 0.0138328, 0.0146126, 0.015499, 0.0162865, 0.0176884, 0.0183231, 0.0193571, 0.0213339, 0.0229902, 0.0235845, 0.0255932, 0.0298347, 0.0311565, 0.0339421, 0.0364137, 0.040597, 0.0435949, 0.0501805, 0.0528384, 0.0610318, 0.0666207, 0.0680055, 0.0742539, 0.0933756, 0.0936849, 0.112715, 0.109472, 0.133334, 0.147559, 0.166827, 0.195708, 0.208875, 0.2561, 0.281746, 0.325944, 0.370698, 0.376819, 0.456588, 0.533951, 0.598449, 0.690826, 0.868262, 1.00331, 1.4139, 1.59587, 1.88575, 2.74373, 4.6881])
xs_exp_limits_2sigma = array('d', [0.44951, 0.530281, 0.42308, 0.364427, 0.295894, 0.254408, 0.259795, 0.227148, 0.184907, 0.159666, 0.135171, 0.11709, 0.107479, 0.0962085, 0.0772022, 0.0673085, 0.06711, 0.0570475, 0.0529566, 0.0494856, 0.0435384, 0.0416115, 0.0355741, 0.0335442, 0.0307791, 0.0261614, 0.0268158, 0.0263764, 0.0188983, 0.0171455, 0.0161398, 0.0153896, 0.0140904, 0.0131912, 0.0126443, 0.010819, 0.0101149, 0.00979842, 0.00908458, 0.00889681, 0.00843834, 0.00808617, 0.00781342, 0.00755744, 0.00722989, 0.00704026, 0.00673008, 0.00604477, 0.00551764, 0.00537187, 0.00506482, 0.00483577, 0.00468139, 0.0045723, 0.00449247, 0.00443542, 0.00438704, 0.00435456, 0.0043309, 0.0113494, 0.0116983, 0.0124261, 0.0129134, 0.0135356, 0.013797, 0.014263, 0.015382, 0.0155359, 0.0164222, 0.0180454, 0.0191298, 0.0205624, 0.0214528, 0.0220958, 0.0256496, 0.0252002, 0.0265901, 0.0291303, 0.0328709, 0.0322281, 0.0386285, 0.0401192, 0.0469608, 0.0454273, 0.0523388, 0.0586189, 0.0660453, 0.0682886, 0.0826618, 0.0892733, 0.087334, 0.102922, 0.108068, 0.131689, 0.121352, 0.167133, 0.163599, 0.202703, 0.23405, 0.24277, 0.277455, 0.287161, 0.344358, 0.364686, 0.440983, 0.516736, 0.558649, 0.752073, 0.740225, 0.86742, 0.983738, 1.31643, 1.39311, 1.84224, 2.46701, 3.15961, 3.8324, 7.67883])

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
graph_exp_2sigma.GetXaxis().SetTitle("qq resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,2e+02)
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


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")
graph_xsAxi.Draw("L")
graph_xsDiquark.Draw("L")
graph_xsWprime.Draw("L")
graph_xsZprime.Draw("L")

legend = TLegend(.50,.55,.80,.68)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL Upper Limits (stat. only)')
legend.AddEntry(graph_obs,"Observed (pseudo-data)","lp")
legend.AddEntry(graph_exp,"Expected","lp")
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
