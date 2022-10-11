#Apple scripts: https://eastmanreference.com/complete-list-of-applescript-key-codes

import os
import time

#os.system("open /Applications/OBS.app")

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
time.sleep(5)
os.system(record)
time.sleep(5)
os.system(stop)