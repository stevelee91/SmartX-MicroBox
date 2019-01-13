#!/usr/bin/env python
import time
import datetime
from kafka import KafkaProducer
from kafka.errors import KafkaError
import sys


print "\n\n\033[1;35m ******SENDING AGENT REPORT To API CENTER*********\033[1;m"
#print sys.argv[0]
#	time_=time.ctime()
time_=datetime.datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
#print sys.argv[1]
#print sys.argv[2]
#print sys.argv[3]
MESSAGE=sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+time_
print "\033[1;37;40m Sending: {0} \033[0;37;40m".format(MESSAGE)
producer=KafkaProducer(bootstrap_servers=['103.22.221.56:9092'])
if  sys.argv[1]=="agent_report":
# producer.send('agent_report_faunctions',key=b'agent_report',MESSAGE)
 print " DONE"
## producer.flush();
#else:
# producer.send('active_monitoring_throughput_udp', key=b'throughput_udp', value=sys.argv[1])
# producer.flush();

producer.close();

