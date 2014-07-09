#!/bin/bash

CONDOR_PROCESS=$1
RUN_DIR=$2


START_TIME=`/bin/date`
echo "started at $START_TIME"
echo ""

source /uscmst1/prod/sw/cms/shrc prod
cd $RUN_DIR
eval `scramv1 runtime -sh`
cd -

export BATINSTALLDIR=/uscms_data/d2/ferencek/BAT
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$BATINSTALLDIR/lib
export CPATH=$BATINSTALLDIR/include

let "MASS = $CONDOR_PROCESS*100 + 300"
LOG=`echo "stats_${MASS}.log"`

echo "Running: stats $MASS > $LOG 2>&1"
$RUN_DIR/stats $MASS > $LOG 2>&1
exitcode=$?

echo ""
END_TIME=`/bin/date`
echo "finished at $END_TIME"
exit $exitcode
