import os
import time
import datetime 

#Set the time when you want the recording to end below 
targetTime = 1517 
restIntervals = 10

quick_time_player = """
osascript -e 'tell application "System Events" to key code 23 using {command down, shift down}' 
"""

record = """
osascript -e 'tell application "System Events" to key code 36'
"""

stop = """
osascript -e 'tell application "System Events" to key code 53 using {command down, control down}'
"""

os.system(quick_time_player)
os.system(record)

string_currentTime = 0
while string_currentTime < targetTime:
    currentTime = datetime.datetime.now()
    string_currentTime = str(currentTime.time())
    string_currentTime = int((string_currentTime.replace(':',''))[0:4])
    time.sleep(restIntervals) 
    print(string_currentTime)
os.system(stop)