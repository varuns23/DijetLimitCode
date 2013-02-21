Instructions:
-------------
Please refer to https://twiki.cern.ch/twiki/bin/view/CMS/DijetLimitCode for more detailed instructions and description.


1) Set up your CMSSW working area:

   scram project -n CMSSW_5_3_8_MyAnalysis CMSSW CMSSW_5_3_8
   cd CMSSW_5_3_8_MyAnalysis/test
   cmsenv

   NOTE: You can skip this step if you already have your working area set up. Nevertheless,
         you will still need to initialize the CMSSW environment by calling 'cmsenv'.
         CMSSW_5_3_8 is used just as an example. Any CMSSW_5_3_X release should work.

2) Install BAT (Bayesian Analysis Toolkit):

   NOTE: This step is only needed if you plan to use MCMC. Otherwise, proceed to step 3).

   wget http://www.mppmu.mpg.de/bat/source/BAT-0.9.2.tar.gz
   tar xvzf BAT-0.9.2.tar.gz
   cd BAT-0.9.2
   ./configure --prefix=$HOME
   make
   make install

   setenv BATINSTALLDIR    $HOME
   setenv LD_LIBRARY_PATH  {$LD_LIBRARY_PATH}:{$BATINSTALLDIR}/lib
   setenv CPATH            {$BATINSTALLDIR}/include

   NOTE: BAT needs to be installed only once. However, every time before compiling or using
         the limit code, you will need to initialize the above environment variables.

3) Checkout the limit code package:

   If you plan to use MCMC

   cvs co -d LimitCode UserCode/ferencek/MyAnalysis/tools/LimitCode

   else

   cvs co -r NoMCMC -d LimitCode UserCode/ferencek/MyAnalysis/tools/LimitCode

   Enter the package directory:

   cd LimitCode

   The package has the following contents:

   Data_and_ResonanceShapes/
   python/
   src/
   Makefile
   README.txt
   binneddata.cc
   binneddata.hh
   cls.cc
   fit.cc
   fit.hh
   statistics.cc
   statistics.hh
   stats.cc

   The src/ subdirectory contains some old limit-setting code and the python/ subdirectory
   contains scripts that run the code and produce various limit plots.

   To start developing your own code, you can start from the stats.cc file.

4) Compile the code:

   make

5) Run the code:

   ./stats MASS BR ResShapeType

   where MASS is the resonance mass in GeV, BR is the branching fraction to the final state of interest,
   and ResShapeType is the resonance shape type. A more concrete example of running the code would be

   ./stats 2000 1.0 qq
