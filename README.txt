Instructions:
-------------
Please refer to https://twiki.cern.ch/twiki/bin/view/CMS/DijetLimitCode for additional instructions and description.


1) Set up your CMSSW working area:

   setenv SCRAM_ARCH slc6_amd64_gcc481
   cmsrel CMSSW_7_0_9
   cd CMSSW_7_0_9/test
   cmsenv

   NOTE: You can skip this step if you already have your working area set up. Nevertheless,
         you will still need to initialize the CMSSW environment by calling 'cmsenv'.
         CMSSW_7_0_9 is used just as an example. Any CMSSW_7_0_X release should work.

2) Install BAT (Bayesian Analysis Toolkit):

   wget --no-check-certificate http://www.mppmu.mpg.de/bat/source/BAT-0.9.2.tar.gz
   tar xvzf BAT-0.9.2.tar.gz
   cd BAT-0.9.2
   ./configure --prefix=$HOME
   make
   make install
   cd -

   setenv BATINSTALLDIR    $HOME
   setenv LD_LIBRARY_PATH  {$LD_LIBRARY_PATH}:{$BATINSTALLDIR}/lib
   setenv CPATH            {$BATINSTALLDIR}/include

   Alternatively, instead of executing the above three lines, you can just source BAT_init.csh

   source ./BAT_init.csh

   NOTE: BAT needs to be installed only once. However, every time before compiling or using
         the limit code, you will need to initialize the above environment variables.

3) Checkout the limit code package:

   git clone git://github.com/CMSDIJET/DijetLimitCode.git LimitCode

   Enter the package directory:

   cd LimitCode

   The package has the following contents:

   Data_and_ResonanceShapes/
   plots/
   jobs/
   BAT_init.csh
   Makefile
   README.txt
   binneddata.cc
   binneddata.hh
   fit.cc
   fit.hh
   statistics.cc
   statistics.hh
   stats.cc

   The plots/ subdirectory contains some ROOT plotting macros and scripts and the jobs/ subdirectory
   contains some Condor job submission scripts.

   To start developing your own code, you can start from the stats.cc file.

4) Compile the code:

   make

5) Run the code:

   ./stats MASS FINAL_STATE

   where MASS is the resonance mass in GeV and FINAL_STATE is the type of two-parton final state, for instance

   ./stats 4000 qg
