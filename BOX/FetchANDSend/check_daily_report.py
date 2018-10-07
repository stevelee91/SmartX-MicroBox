

#!/usr/bin/env python

from kafka import KafkaProducer
from kafka.errors import KafkaError
from datetime import datetime
import sys

print "******SENDING THROUGHPUT DAILY REPORT THROUGH KAFKA*********"
#print sys.argv[1]
#print sys.argv[2]
#print sys.argv[3]
#print sys.argv[4]

i = datetime.now()
date=i.strftime('%Y/%m/%d %H:%M:%S')
MESSAGE_TCP= date+" "+sys.argv[2]+" "+sys.argv[3]
MESSAGE_UDP= date+" "+sys.argv[2]+" "+sys.argv[4]
#print MESSAGE
producer=KafkaProducer(bootstrap_servers=['103.22.221.56:9092'])

if sys.argv[1]=="ping_latency":
	 print "TRUE"
	 MESSAGE_ping= date+" "+sys.argv[2]+" "+sys.argv[3]
	 MESSAGE_latency= date+" "+sys.argv[2]+" "+sys.argv[4]
	 print MESSAGE_ping
	 print MESSAGE_latency
	 producer.send('daily_report_ping', key=b'ping', value=MESSAGE_ping)
	 producer.send('daily_report_latency', key=b'latency', value=MESSAGE_latency)
elif sys.argv[1]=="tcp_udp":
	 print MESSAGE_TCP
	 print MESSAGE_UDP
	 producer.send('daily_report_throughput_tcp', key=b'throughput_tcp', value=MESSAGE_TCP)
#else if sys.argv[1]=="udp":
#         print MESSAGE
         producer.send('daily_report_throughput_udp', key=b'throughput_udp', value=MESSAGE_UDP)
producer.flush();
producer.close();




