import time
import random
import os
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from SMWinservice import SMWinservice
import glob
import win32print
import subprocess
import win32service
import win32serviceutil
import win32event
import servicemanager

pdf_files  = glob.glob('/Users/katie.pederson/OneDrive - Simms Fishing Products/TestPowerappsPythonFlow/*') #this gets all files in the folder
latest_file = max(pdf_files, key=os.path.getctime) #this gets the most recently created/modified file in the folder
acrobat = 'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'
name = win32print.GetDefaultPrinter()
cmd = '"{}" /n /h /s /o  /t "{}" "{}"'.format(acrobat, latest_file, name)

class PythonCornerExample(SMWinservice):
    _svc_name_ = "KatieTest3"
    _svc_display_name_ = "KatieTest3"
    _svc_description_ = "KatieTest3"


    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        w = Watcher()
        w.run()

        while self.isrunning:
            # random.seed()
            # x = random.randint(1, 1000000)
            # Path(f'c:\\test_py\\{x}.txt').touch()
            time.sleep(1)
            


class Watcher:
    DIRECTORY_TO_WATCH = "/Users/katie.pederson/OneDrive - Simms Fishing Products/TestPowerappsPythonFlow"
    # DIRECTORY_TO_WATCH = "C:\\test_py"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
   
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            # print ("Received created event - %s.") % event.src_path
            # f = open("C:\\Users\\katie.pederson\\OneDrive - Simms Fishing Products\\TestPowerappsPythonFlow\\test.txt","a+")
            # f.write("Change2!! \n")
            # f.close()
            for i in range(1):
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':
    PythonCornerExample.parse_command_line()