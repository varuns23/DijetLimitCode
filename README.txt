Instructions:
-------------

1) Set up your CMSSW working area:

   scram project -n CMSSW_4_2_8_MyAnalysis CMSSW CMSSW_4_2_8
   cd CMSSW_4_2_8_MyAnalysis/test
   cmsenv

   NOTE: You can skip this step if you already have your working area set up.
         CMSSW_4_2_8 is used just as an example.

2) Checkout the package:

   cvs co -d LimitCode UserCode/ferencek/MyAnalysis/tools/LimitCode
   cd LimitCode

   The package has the following content:

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

   The src/ subdirectory contains some example limit-setting code and the python/ subdirectory
   contains example scripts that run the code and produce final plots.

   To start developing your own code, you can either starts directly from the stats.cc file or
   you can start from one of the example files in the src/ subdirectory by copying it to the
   current directory

   cp -i src/EXAMPLECODE.cc stats.cc

4) Compile the code:

   make

5) Run the code:

   ./stats MASS BR LFRS
