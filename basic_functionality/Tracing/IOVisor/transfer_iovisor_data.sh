#!/bin/bash
VISIBILITY_CENTER_IP='103.22.221.56'
VISIBILITY_CENTER_USER='netcs'
PASS="fn!xo!ska!"

TARGETFOLDERDP='/home/netcs/IOVisor-Data/Data-Plane'
TARGETFOLDERCP='/home/netcs/IOVisor-Data/Control-Plane'
TARGETFOLDERDPL='/home/netcs/IOVisor-Data/Data-Plane-Latest'
TARGETFOLDERCPL='/home/netcs/IOVisor-Data/Control-Plane-Latest'
SOURCEFOLDER='/opt/IOVisor-Data'

Minute="$(date +'%M')"
Hour="$(date +'%H')"
cDate="$(date +'%Y-%m-%d')"

host=`hostname`

echo "$cDate $Hour $Minute" >> transfer.log
#if [ "$Hour" -lt 10 ]
#    then 
#        Hour="0$Hour"
#        echo $Hour
#fi

if [ "$Minute" -eq 00 ]
    then
	if [ "$Hour" -eq 00 ]
        then
                PREVIOUS_HOUR=23
                PREVIOUS_MINUTE=55
                PREVIOUS_DAY="$(date +'%d')"
                PREVIOUS_DAY=$((PREVIOUS_DAY - 1))
                if [ "$PREVIOUS_DAY" -lt 10 ]
                then
                        PREVIOUS_DAY="0$PREVIOUS_DAY"
                fi
        #        echo "In if $PREVIOUS_HOUR $PREVIOUS_MINUTE $PREVIOUS_DAY"
        else
                PREVIOUS_HOUR=$((Hour - 1))
                PREVIOUS_MINUTE=55
                PREVIOUS_DAY="$(date +'%d')"
                if [ "$PREVIOUS_HOUR" -lt 10 ]
                then
                        PREVIOUS_HOUR="0$PREVIOUS_HOUR"
                fi
        #        echo "In else $PREVIOUS_HOUR $PREVIOUS_MINUTE $PREVIOUS_DAY"
        fi
        cDate="$(date +'%Y-%m')"
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$PREVIOUS_DAY-$PREVIOUS_HOUR-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$PREVIOUS_DAY-$PREVIOUS_HOUR-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 5 ]
    then
        PREVIOUS_MINUTE=00
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 10 ]
    then
        PREVIOUS_MINUTE=05
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 15 ]
    then
        PREVIOUS_MINUTE=10
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 20 ]
    then
        PREVIOUS_MINUTE=15
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 25 ]
    then 
        PREVIOUS_MINUTE=20
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE" 
elif [ "$Minute" -eq 30 ]
    then
        PREVIOUS_MINUTE=25
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 35 ]
    then
        PREVIOUS_MINUTE=30
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 40 ]
    then
        PREVIOUS_MINUTE=35
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 45 ]
    then 
        PREVIOUS_MINUTE=40
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 50 ]
    then
        PREVIOUS_MINUTE=45
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
elif [ "$Minute" -eq 55 ]
    then
        PREVIOUS_MINUTE=50
        PREVIOUS_FILE1="/opt/IOVisor-Data/$host-mc-$cDate-$Hour-$PREVIOUS_MINUTE"
        PREVIOUS_FILE2="/opt/IOVisor-Data/$host-data-$cDate-$Hour-$PREVIOUS_MINUTE"
fi

echo "$PREVIOUS_FILE1 $PREVIOUS_FILE2"

sshpass -p $PASS scp $PREVIOUS_FILE1 $VISIBILITY_CENTER_USER@$VISIBILITY_CENTER_IP:$TARGETFOLDERCP
sshpass -p $PASS scp $PREVIOUS_FILE2 $VISIBILITY_CENTER_USER@$VISIBILITY_CENTER_IP:$TARGETFOLDERDP
sshpass -p $PASS scp $PREVIOUS_FILE1 $VISIBILITY_CENTER_USER@$VISIBILITY_CENTER_IP:$TARGETFOLDERCPL
sshpass -p $PASS scp $PREVIOUS_FILE2 $VISIBILITY_CENTER_USER@$VISIBILITY_CENTER_IP:$TARGETFOLDERDPL
sleep 20

shopt -s extglob; set -H
cd $SOURCEFOLDER
CURRENT_FILES=`ls -t1 | head -n 2 | sed 'N; s/\n/|/'`
sudo rm -v !($CURRENT_FILES)

if [ $? -eq 0 ]; then
    echo OK
else
    echo FAIL
fi
