Instructions:
-------------
Please refer to https://twiki.cern.ch/twiki/bin/view/CMS/DijetLimitCode for more detailed instructions and description.


1) Set up your CMSSW working area:

   scram project -n CMSSW_5_3_8_MyAnalysis CMSSW CMSSW_5_3_8
   cd CMSSW_5_3_8_MyAnalysis/test
   cmsenv

   NOTE: You can skip this step if you already have your working area set up.
         CMSSW_5_3_8 is used just as an example. Any CMSSW_5_3_X release should work.

2) Checkout the package:

   cvs co -d LimitCode UserCode/ferencek/MyAnalysis/tools/LimitCode
   cd LimitCode

   The package has the following content

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
   current directory.

   cp -i src/EXAMPLECODE.cc stats.cc

3) Compile the code:

   make

4) Run the code:

   ./stats MASS BR ResShapeType

   where MASS is the resonance mass in GeV, BR is the branching fraction to the final state of interest,
   and ResShapeType is the resonance shape type. A more concrete example of running the code would be

   ./stats 2000 1.0 qq
