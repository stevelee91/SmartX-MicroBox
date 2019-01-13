#!/bin/sh
 
# -q quiet
# -c nb of pings to perform
 
ping -q -c5 103.22.221.56 > /dev/null
 
if [ $? -eq 0 ]
then
	echo "ok"
fi
