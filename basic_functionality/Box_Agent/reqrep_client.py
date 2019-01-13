#Commands
#service --status-all
#pgrep -af java | grep test1.jar
import time
import sys
import re
import psutil
import os
import zmq
import sys
import time
import sys
from subprocess import call
import subprocess
from datetime import datetime, timedelta
import time, threading


FROM_BOX_SITE="SmartX-Box-GIST1"
snap_counter=0
zookeeper_counter=0
data_plane_counter=0
management_plane_counter=0
control_plane_counter=0
perfosnar_counter=0
# update_counter
#global update_counter
update_counter=0

#python /home/tein/active_monitoring/check_daily_report.py "ping_latency" "$FROM_BOX_SITE" "$ping_grid" "$latency_grid" "$vcenter_check"
port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://103.22.221.56:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("tcp://103.22.221.56:%s" % port1)

#  Do 10 requests, waiting each time for a response
#for request in range (1,2):
#    print "Sending request ", request,"..."
#    socket.send ("Hello from Client")
    #  Get the reply.
#    message = socket.recv()
#    print "Received reply ", request, "[", message, "]"

#while True:

#p = subprocess.Popen("pgrep -af python | grep watch_for_changes.py", stdout=subprocess.PIPE, shell=True)
#(output, err) = p.communicate()
#p_status = p.wait()
#if 'watch_for_changes.py"' in output:
# print 'Update local watch  is running'
#else:
# print 'Update local watch  is NOT running'
#	 os.system("python watch_for_changes.py &") #********start the jar in screen*************

def foo():
#    print "\n******************************************"
    print("\033[1;37;40m \033[4mFunction\033[0m \033[0;37;40m 				\033[1;37;40m \033[4mStatus\033[0m \033[0;37;40m \n")
#    print("\033[2;37;40m Function \033[0;37;40m" + "\033[2;37;40m Status \033[0;37;40m\n")
#    print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
#    print("\033[1;32;40m Bright Green  \n")
    time_=" "+time.ctime()
    print(time_)
#    global update_couner


    for process in psutil.process_iter():
      if process.cmdline() == ['python', '*watch_for_changes.py']:
         sys.exit('Process found: exiting.')

    p = subprocess.Popen("sudo systemctl status snapd.service", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if 'active (running)' in output:
      print '\n\033[1;33;40m SNAP \033[0m                          is \033[1;32;40m	running \033[0m'
      snap_counter=0
    else:
      print 'SNAP is NOT running'
      os.system("echo 'SNAP is NOT running'")
      os.system("sudo systemctl start snapd.service")    
      snap_counter=snap_count+1
      if int(snap_couner)==3:
        print"SNAP is not running for 10 minutes"
        os.system("python /home/tein/active_monitoring/agent/agent_report.py agent_report snapd service -{0} -{1}".format(FROM_BOX_SITE,time_))
	snap_counter=0





    p = subprocess.Popen("service zookeeper status", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if 'active (running)' in output:
      print '\n\033[1;33;40m ZooKeeper \033[0m  			is \033[1;32;40m 	running \033[0m'
    else:
      print 'Zookeper is NOT running'
      os.system("echo 'Zookeeper is NOT running'")
      os.system("sudo systemctl start zookeeper")


    p = subprocess.Popen("sudo systemctl status control-plane-tracing.service", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if 'active (running)' in output:
      print '\n\033[1;33;40m control-plane-tracing \033[0m		is \033[1;32;40m 	running \033[0m'
    else:
      print ' control-plane-tracing	is 	NOT running'
      os.system("echo ' control-plane-tracing is NOT running'")
      os.system("sudo systemctl start control-plane-tracing.service")

    p = subprocess.Popen("sudo systemctl status data-plane-tracing.service", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if 'active (running)' in output:
      print '\n\033[1;33;40m data-plane-tracing \033[0m  		is \033[1;32;40m 	running \033[0m'
    else:
      print 'data-plane-tracing is NOT running'
      os.system("echo 'data-plane-tracing is NOT running'")
      os.system("sudo systemctl start data-plane-tracing.service")

    p = subprocess.Popen("sudo systemctl status management-plane-tracing.service", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if 'active (running)' in output:
      print '\n\033[1;33;40m management-plane-tracing \033[0m 	is \033[1;32;40m 	running \033[0m'
    else:
      print 'management-plane-tracing is NOT running'
      os.system("echo 'management-plane-tracing is NOT running'")
      os.system("sudo systemctl start management-plane-tracing.service")

    for process in psutil.process_iter():
      if process.cmdline() == ['python', '*watch_for_changes.py']:
         sys.exit('Process found: exiting.')

    p = subprocess.Popen("sudo systemctl status perfsonar-toolkit-config-daemon.service", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if 'active (exited)' in output:
      print '\n\033[1;33;40m perfsonar-toolkit \033[0m		is \033[1;32;40m     running \033[0m'
    else:
      print 'perfsonar-toolkit is NOT running'
      os.system("echo 'perfsonar-toolkit is NOT running'")
#      os.system("sudo systemctl start perfsonar-toolkit-config-daemon.service")

#    print "First way"
    p = subprocess.Popen("pgrep -af python | grep watch_for_changes.py", stdout=subprocess.PIPE, shell=True)
#    p = subprocess.Popen("ps -aux | grep watch_for_changes.py | grep python", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
##    print output
##    print output.split('\n', 1)[0]
    find= re.search(r'\b(watch_for_changes.py)\b', output)
##    print (find.start())
    
    line=output.split('\n', 1)[0]
    word= line.split(' ')
##    print word
    length = len(word)
##    print length

    

#    string = output.split(" ")
#    index = string.index('watch_for_changes.py')
#    print index
    
##    print "Second way"
##    pipe1 = subprocess.Popen("ps -aux | grep watch_for_changes.py | grep python", shell=True, stdout=subprocess.PIPE).stdout
##    count1 = pipe1.read()
##    print count1.splitlines()[0]

##    print "third way"
##   print output.splitlines()[0]

##    print 'fourth way'
##    print output
#    for line in output
#     print line.readline()[1:]



#    count = subprocess.check_output("ps -aux | grep -c watch_for_changes.py")
#    cmd = [ 'ps','-aux','|','grep','-c','watch_for_changes.py']
#    count= subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    pipe = subprocess.Popen("ps -aux | grep -c watch_for_changes.py", shell=True, stdout=subprocess.PIPE).stdout
    count = pipe.read()
##    print count
#    if int(count) < 3:
#     print ("NOT Running")
#    elif int(count)>2:
#     print ("Running")
#    search = 
    if ("watch_for_changes.py" in output) & (int(count)>2) & (length == 3) :
      print '\n\033[1;33;40m local Update  \033[0m		        is \033[1;32;40m     running \033[0m'
    else:
      print '\n\033[1;33;40m local update watch \033[0m  		is \033[1;31;40m 	NOT running \033[0m'
      global update_counter
      update_counter=update_counter+1
##      print update_counter
#      global update_couner
      if int(update_counter)==3:
        print"\n\033[0;37;44m Update local Watch is not running for 10 minutes \033[0;m"
	os.system("python /home/tein/active_monitoring/agent/agent_report.py agent_report update_watch_service {0}".format(FROM_BOX_SITE))
#        global    update_couner
        update_counter=0
      os.system("python /home/tein/update/watch_for_changes.py &")


    toolbar_width = 40

# setup toolbar
    sys.stdout.write("\n")
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    for i in xrange(toolbar_width):
     time.sleep(1.15) # do real work here
    # update the bar
     sys.stdout.write("-")
     sys.stdout.flush()

    sys.stdout.write("\n")



    threading.Timer(0, foo).start()
foo()

