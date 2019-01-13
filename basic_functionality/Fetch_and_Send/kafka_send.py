#!/usr/bin/env python

from kafka import KafkaProducer
from kafka.errors import KafkaError
import sys

print sys.argv[2]+"******SENDING THROUGH KAFKA*********"
#print sys.argv[1]
print sys.argv[2]
MESSAGE=sys.argv[1]
print MESSAGE
producer=KafkaProducer(bootstrap_servers=['103.22.221.56:9092'])
if  sys.argv[2]=="TCP":
 producer.send('active_monitoring_throughput_tcp', key=b'throughput_tcp', value=sys.argv[1])
 producer.flush();
else:
 producer.send('active_monitoring_throughput_udp', key=b'throughput_udp', value=sys.argv[1])
 producer.flush();

producer.close();

