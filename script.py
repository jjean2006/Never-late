# Idea: this is a script that will check the current day of the weak and time and store 
# zoom link for the class I need to join in a text file.
import webbrowser
import os
import subprocess
import platform
import configparser
import datetime
from datetime import datetime

cwd = os.path.realpath(__file__).removesuffix('script.py')
configfile = cwd + 'config.ini'
delimiter = ", "
classindex = None

# get timetable from config file
subs = configparser.ConfigParser()
subs.read(configfile)

monday = subs.get('timetable', 'monday').split(delimiter)
tuesday = subs.get('timetable','tuesday').split(delimiter)
wednesday = subs.get('timetable', 'wednesday').split(delimiter)
thursday = subs.get('timetable', 'thursday').split(delimiter)
friday = subs.get('timetable', 'friday').split(delimiter)

# get starttimes from config file
starttimes = configparser.ConfigParser()
starttimes.read(configfile)
times = starttimes.get('starttimes', 'starttimes').split(delimiter)

# get links from config file
sublinks = configparser.ConfigParser()
sublinks.read(configfile)


now = datetime.now()
current_time = now.strftime("%H%M")
today = now.strftime("%A")

todaystt = globals().get(today.lower())


for time in times:
    if int(current_time) <= int(time):
        classindex = times.index(time)
        break

sublink = sublinks.get('sublinks', todaystt[classindex])

webbrowser.open(sublink)