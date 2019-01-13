

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
# connections_max_idle_ms: Close idle connections after the number of
#            milliseconds specified by this config. The broker closes idle
#            connections after connections.max.idle.ms, so this avoids hitting
#            unexpected socket disconnected errors on the client.
#            Default: 540000

#retries (int): Setting a value greater than zero will cause the client
#            to resend any record whose send fails with a potentially transient
#            error. Note that this retry is no different than if the client
#            resent the record upon receiving the error. Allowing retries
#            without setting max_in_flight_requests_per_connection to 1 will
#            potentially change the ordering of records because if two batches
#            are sent to a single partition, and the first fails and is retried
#            but the second succeeds, then the records in the second batch may
#            appear first.
#            Default: 0.

#acks (0, 1, 'all'): The number of acknowledgments the producer requires
#            the leader to have received before considering a request complete.
#            This controls the durability of records that are sent. The
#            following settings are common:

#            0: Producer will not wait for any acknowledgment from the server.
#                The message will immediately be added to the socket
#                buffer and considered sent. No guarantee can be made that the
#                server has received the record in this case, and the retries
#                configuration will not take effect (as the client won't
#                generally know of any failures). The offset given back for each
#                record will always be set to -1.
#            1: Wait for leader to write the record to its local log only.
#                Broker will respond without awaiting full acknowledgement from
#                all followers. In this case should the leader fail immediately
#                after acknowledging the record but before the followers have
#                replicated it then the record will be lost.
#            all: Wait for the full set of in-sync replicas to write the record.
#                This guarantees that the record will not be lost as long as at
#                least one in-sync replica remains alive. This is the strongest
#                available guarantee.
#            If unset, defaults to acks=1

#request_timeout_ms (int): Client request timeout in milliseconds.
#            Default: 30000.
#reconnect_backoff_max_ms (int): The maximum amount of time in
#            milliseconds to wait when reconnecting to a broker that has
#            repeatedly failed to connect. If provided, the backoff per host
#            will increase exponentially for each consecutive connection
#            failure, up to this maximum. To avoid connection storms, a
#            randomization factor of 0.2 will be applied to the backoff
#            resulting in a random range between 20% below and 20% above
#            the computed value. Default: 1000.

producer=KafkaProducer(bootstrap_servers=['103.22.221.56:9092'],
connections_max_idle_ms=40100000,
retries=100,
reconnect_backoff_max=60000,
acks='all',
request_timeout_ms=300000)

if sys.argv[1]=="ping_latency":
	 print "TRUE"
	 MESSAGE_ping= date+" "+sys.argv[2]+" "+sys.argv[3]
	 MESSAGE_latency= date+" "+sys.argv[2]+" "+sys.argv[4]
	 MESSAGE_vcenter= date+" "+sys.argv[2]+" "+sys.argv[5]
	 print MESSAGE_ping
	 print MESSAGE_latency
         print MESSAGE_vcenter
	 producer.send('daily_report_ping', key=b'ping', value=MESSAGE_ping)
	 producer.send('daily_report_latency', key=b'latency', value=MESSAGE_latency)
         producer.send('daily_report_latency_extended_sites', key=b'latency', value=MESSAGE_latency)
	 producer.send('daily_report_vcenter', key=b'vcenter', value=MESSAGE_vcenter)
elif sys.argv[1]=="tcp_udp":
	 print MESSAGE_TCP
	 print MESSAGE_UDP
	 producer.send('daily_report_throughput_tcp', key=b'throughput_tcp', value=MESSAGE_TCP)
#else if sys.argv[1]=="udp":
#         print MESSAGE
         producer.send('daily_report_throughput_udp', key=b'throughput_udp', value=MESSAGE_UDP)
producer.flush();
producer.close();




