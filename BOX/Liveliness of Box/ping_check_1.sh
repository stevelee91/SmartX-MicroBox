#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#
# Name			: bandwidth-check.sh
# Description	: Script for playground bandwidth checking.
#
# Created by    : 
# Version       : 0.1
# Last Update	: MAY, 2018

# Configuration Parameter

#from kafka import KafkaProducer
#from kafka.errors import KafkaError
import datetime

LOGDIR="log"
LOGRES="/home/netcs/active_monitoring/result"
#BoxID_GIST1=1, BoxID_ID=2, BoxID_PH=3, BoxID_PKS=4, BoxID_HUST=5, BoxID_GIST2=6, BoxID_CHULA=7, BoxID_NCKU=8, BoxID_MY=9, BoxID_MYREN=10, BoxID_GIST3=11, BoxID_NUC=12
#WAN_BOXES="103.22.221.170 0 0 0 203.191.48.228 0 161.200.25.99 140.116.214.241 0 103.26.47.228 103.22.221.30 103.22.221.62"
#WAN_BOXES="103.22.221.170 0 0 0 0 0 0 0 0 0 103.22.221.30 103.22.221.62"


WAN_BOXES="103.22.221.170 0 202.90.150.4 0 203.191.48.228 0 161.200.25.99 140.116.214.241 0 103.26.47.228 103.22.221.30 103.22.221.62"
#WAN_BOXES="103.22.221.151 0 202.90.150.4 0 103.22.221.149 0 103.22.221.49 140.116.214.241 0 103.26.47.228 103.22.221.30 103.22.221.53"


#WAN_BOXES="103.22.221.170"


#WAN_BOXES="103.26.47.228"
#WAN_BOXES="103.26.47.228 161.200.25.99 203.191.48.228 103.22.221.170"
#WAN_BOXES="103.22.221.170 203.191.48.228 161.200.25.99 140.116.214.241 203.80.21.4"
#WAN_BOXES="103.22.221.170"

CLOUD_BOXES=""
ACCESS_BOXES=""
FROM_BOX="103.22.221.170"
FROM_BOX_SITE="SmartX-Box-GIST1"
daily_report=""
#d = date.fromtimestamp(time.time())
A="";

if [ ! -f "$LOGRES/IPERF_TCP_RESULT_WAN_BOX.log" ]
then
	touch $LOGRES/IPERF_TCP_RESULT_WAN_BOX.log
	touch $LOGRES/IPERF_UDP_RESULT_WAN_BOX.log
	echo "$file found."
fi

#if [ ! -f "$LOGRES/IPERF_TCP_RESULT_CLOUD_BOX.log" ]
#then
#	touch $LOGRES/IPERF_TCP_RESULT_CLOUD_BOX.log
#	touch $LOGRES/IPERF_UDP_RESULT_CLOUD_BOX.log
#	echo "$file found."
#fi

#if [ ! -f "$LOGRES/IPERF_TCP_RESULT_ACCESS_BOX.log" ]
#then
#	touch $LOGRES/IPERF_TCP_RESULT_ACCESS_BOX.log
#	touch $LOGRES/IPERF_UDP_RESULT_ACCESS_BOX.log
#	echo "$file found."
#fi


#
# [1] Bandwidth Checking
#
function check_box_bandwidth {
        TIME=`date +%Y/%m/%d`
	echo -e "\n"
        echo -e "------------------------------------------------------------"
        echo -e "|               Start Ping+Latency Test For SD-WAN (Boxes)           |"
        echo -e "------------------------------------------------------------"
#        iperf3 -s -p 30000 &

	for TO_BOX in $WAN_BOXES
   	do
			echo -e "------------------------"
			echo -e "Checking for $TO_BOX"
			echo -e "------------------------"
          if [ "$TO_BOX" == 0 ]; then
                        echo "**********Box IP is 0************"
                        ping_grid+=-1
                        ping_grid+=" "
			latency_grid+=-1
			latency_grid+=" "
                        echo $Value_grid
          fi
	  if [ "$TO_BOX" != "$FROM_BOX" ]&& [ "$TO_BOX" != 0 ] ; then
	  	PING_RESULT2=`ping $TO_BOX -c 2 -s 10 -W 5 | grep 'Unreachable\|not reachable'`
		PING_RESULT1=`ping $TO_BOX -c 1 | grep ttl`
		echo -e "PING_RESULT2: $PING_RESULT2"
		echo -e "PING_RESULT1:$PING_RESULT1"


                if [ -z "$PING_RESULT1" ] && [ ! -z "$PING_RESULT2" ] && [ "$TO_BOX" != 0 ]; then
                        echo "Loop: Host $TO_BOX is not reachable from $FROM_BOX."
                                        ping_grid+=0
                                        ping_grid+=" "
                                        latency_grid+=0
                                        latency_grid+=" "
                else if [ -z "$PING_RESULT1" ] && [  -z "$PING_RESULT2" ] && [ "$TO_BOX" != 0 ]; then
					ping_grid+=0
                                        ping_grid+=" "
                                        latency_grid+=0
                                        latency_grid+=" "

                else if [ ! -z "$PING_RESULT1" ] && [  -z "$PING_RESULT2" ] && [ "$TO_BOX" != 0 ]; then
                        echo "Loop: Connection found."
			ping_grid+="1 "
			latency_grid+=`echo $PING_RESULT1 | grep -o -P '(?<=time=).*(?=ms)'`
		fi
                fi
                fi
          else if [ "$TO_BOX" == "$FROM_BOX" ]; then
                        ping_grid+="-"
                        ping_grid+=" "
			latency_grid+="-"
                        latency_grid+=" "
                        echo $Value_grid

          fi
          fi
	  echo "************Ping_grid(1:UP, 0:Down)***********:$ping_grid"
	  echo "************Latency_grid (ms)***********:$latency_grid"
 	done
#        only_date = d.date()
        echo "END of LOOP SEND Daily Ping report:$Value_grid"
	echo $PING_RESULT
        echo $PING_RESULT >> $LOGRES/PING_$FROM_BOX.log
	python /home/tein/active_monitoring/check_daily_report.py "ping_latency" "$FROM_BOX_SITE" "$ping_grid" "$latency_grid"
#        echo " Terminate iperf Server on the $FROM_BOX"
#	killall -r -s KILL iperf3
}
#
# Main Script
#

echo -e "\n"
echo -e "#######################################################"
echo -e "#       Checking Playground Resources Ping+ Latency       #"
echo -e "#######################################################"

check_box_bandwidth

echo -e "Checking Playground Resources Ping latency is Completed.\n"
echo -e "\n"
