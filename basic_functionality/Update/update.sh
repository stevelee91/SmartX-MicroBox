#!/bin/bash
#echo '$0 = ' $0
#uncomment these lines in Micro box
#client.py --repo http://103.22.221.51:8001 active_monitoring/bandwidth-check.sh #Function: Measurement
#client.py --repo http://103.22.221.51:8001 check_daily_report.py #Function: Measurement
#client.py --repo http://103.22.221.51:8001 active_monitoring/ping_check_1.sh #Function: Measurement
#client.py --repo http://103.22.221.51:8001 watch_for_changes.py #Function: Update
#client.py --repo http://103.22.221.51:8001 snapChecker.sh #Function: Tracing
#client.py --repo http://103.22.221.51:8001 transfer_iovisor_data.sh #Function: Tracing
#client.py --repo http://103.22.221.51:8001 reqrep_client.py #Function: Persistence Agent
#client.py --repo http://103.22.221.51:8001 testfile.py
#cd ../tufclient/ && client.py --repo http://103.22.221.51:8001 testfile.py


cd  tufclient/ && client.py --repo http://103.22.221.51:8001 testfile.py
cd  /tufclient/ && client.py --repo http://103.22.221.51:8001 testfile1.py
cd  /tufclient/ && client.py --repo http://103.22.221.51:8001 testfile2.py
cd  /tufclient/ && client.py --repo http://103.22.221.51:8001 testfile3.py





#client.py --repo http:// 103.22.221.51:8001
#client.py --repo http:// 103.22.221.51:8001
#client.py --repo http:// 103.22.221.51:8001
#client.py --repo http:// 103.22.221.51:8001


#Test
#echo "This is a shell script"  
#ls -lah  
#echo "I am done running ls"
#ls -tlr
#SOMEVAR='text stuff'  
#echo "$SOMEVAR"
