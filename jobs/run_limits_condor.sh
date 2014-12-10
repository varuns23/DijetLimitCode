#!/bin/bash

CONDOR_PROCESS=$1
FINAL_STATE=$2


START_TIME=`/bin/date`
echo "started at $START_TIME"
echo ""

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd ${_CONDOR_SCRATCH_DIR}
export SCRAM_ARCH=slc6_amd64_gcc481
scram p CMSSW_7_0_9
cd CMSSW_7_0_9
eval `scramv1 runtime -sh`
cd -
mkdir Data_and_ResonanceShapes
mv *.root Data_and_ResonanceShapes/

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${_CONDOR_SCRATCH_DIR}

let "MASS = $CONDOR_PROCESS*100 + 1200"
LOG=`echo "stats_${MASS}_${FINAL_STATE}.log"`

echo "Running: stats $MASS $FINAL_STATE > $LOG 2>&1"
./stats $MASS $FINAL_STATE > $LOG 2>&1
exitcode=$?

echo ""
END_TIME=`/bin/date`
echo "finished at $END_TIME"
exit $exitcode
