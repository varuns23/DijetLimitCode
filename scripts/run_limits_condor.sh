#!/bin/bash

CONDOR_PROCESS=$1
BR=$2
FINAL_STATE=$3
RUN_DIR=$4


START_TIME=`/bin/date`
echo "started at $START_TIME"
echo ""

source /uscmst1/prod/sw/cms/shrc prod
cd $RUN_DIR
eval `scramv1 runtime -sh`
cd -


let "MASS = $CONDOR_PROCESS*250 + 1000"
LOG=`echo "stats_${MASS}_${BR}_${FINAL_STATE}.log"`

echo "Running: stats $MASS $BR $FINAL_STATE > $LOG 2>&1"
/uscms_data/d3/gurpinar/work/Dijet/CMSSW_5_3_7/src/limit/LimitCode/stats $MASS $BR $FINAL_STATE > $LOG 2>&1
exitcode=$?

echo ""
END_TIME=`/bin/date`
echo "finished at $END_TIME"
exit $exitcode


