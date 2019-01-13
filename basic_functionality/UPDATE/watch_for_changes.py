#!/usr/bin/python
import ntpath
import datetime
import os
import shutil
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
class MyHandler(PatternMatchingEventHandler): 
    date_time=datetime.datetime.now()
    patterns = ["*.sh", "*.py"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
	     home/tein/update/tufclient/tuftargets/
        """
        # the file will be processed there
        print event.src_path, event.event_type  # print now only for degug
        path= event.src_path



        print path
	print(ntpath.basename(path))
	date_time=datetime.datetime.now()
	filename=ntpath.basename(path)
	print"file",filename,"is updated"
	src="/home/tein/update/tufclient/tuftargets/"+filename

	if filename == "bandwidth-check.sh" or filename == "check_daily_report.py" or filename == "ping_check_1.sh":
         dest ="/home/tein/active_monitoring/"+filename
        elif filename == "snapChecker.sh":
         dest ="/home/tein/"+filename
        elif filename == "transfer_iovisor_data.sh":
         dest ="/home/tein/opt/FlowAgent/"+filename
        elif filename == "watch_for_changes.py":
         dest ="/home/tein/tufclient/"+filename
	elif filename == "testfile.py":
         dest ="/home/tein/temp/"+filename
	elif filename == "testfile1.py":
	 dest ="/home/tein/temp/"+filename
        else:
         dest ="/home/tein/"+filename


	print"src:",src,"dest:",dest
	shutil.copyfile(src,dest)
	print"file",filename,"copied to",dest, "at",date_time




    def on_modified(self, event):
	path= event.src_path
        self.process(event)
	print(ntpath.basename(path))
        date_time=datetime.datetime.now()
        filename=ntpath.basename(path)
        print"file",filename,"is updated"
	src="/home/tein/update/tufclient/tuftargets/"+filename

        if filename == "bandwidth-check.sh" or filename == "check_daily_report.py" or filename == "ping_check_1.sh":
         dest ="/home/tein/active_monitoring/"+filename
        elif (filename == "snapChecker.sh"):
         dest ="/home/tein/"+filename
        elif (filename == "transfer_iovisor_data.sh"):
         dest ="/home/tein/opt/FlowAgent/"+filename
        elif (filename == "watch_for_changes.py"):
         dest ="/home/tein/tufclient/"+filename
	elif (filename == "testfile.py"):
         dest ="/home/tein/temp/"+filename
	elif filename == "testfile1.py":
         dest ="/home/tein/temp/"+filename
	else:
	 dest ="/home/tein/"+filename
	

        print"src:",src,"dest:",dest
        shutil.copyfile(src,dest)
        print"file",filename,"copied to",dest, "at",date_time

    def on_created(self, event):
	path= event.src_path
        self.process(event)
	print(ntpath.basename(path))
        date_time=datetime.datetime.now()
        filename=ntpath.basename(path)
        print"file",filename,"is Created"
        src="/home/tein/update/tufclient/tuftargets/"+filename

        if filename == "bandwidth-check.sh" or filename == "check_daily_report.py" or filename == "ping_check_1.sh":
         dest ="/home/tein/active_monitoring/"+filename
        elif (filename == "snapChecker.sh"):
         dest ="/home/tein/"+filename
        elif (filename == "transfer_iovisor_data.sh"):
         dest ="/home/tein/opt/FlowAgent/"+filename
        elif (filename == "watch_for_changes.py"):
         dest ="/home/tein/tufclient/"+filename
	elif (filename == "testfile.py"):
         dest ="/home/tein/temp/"+filename
	elif filename == "testfile1.py":
	 dest ="/home/tein/temp/"+filename
        else:
         dest ="/home/tein/"+filename

        print"src:",src,"dest:",dest
        shutil.copyfile(src,dest)
        print"file",filename,"copied to",dest, "at",date_time

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '/home/tein/update/tufclient/tuftargets/')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
