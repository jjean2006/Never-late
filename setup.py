# Import needed built-in modules 
import platform
import subprocess 
import sys
import os

def divider():
    print('-----------------------------------------------------------------\n\n')

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("configparser") # install configparser, needed module for the *main* script, i.e, not the setup script.


cwd = os.path.realpath(__file__).removesuffix('setup.py') # get the current working directory of the script.
daysoftheweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
classes = []
classno = int(input('How many classes do you have per day? Ans: '))

divider()

with open(cwd + 'config.ini', 'w') as configfile:
    configfile.write('')

with open(cwd + 'config.ini', 'a') as configfile:
    configfile.write('[timetable]\n')


for i in daysoftheweek:
    classind = 1
    while len(globals().get(i)) < classno:
        classinp = input('What is the ' + str(classind) + '(st/nd/rd/th) you have on ' + i + '? \nBe sure to be consistent with short forms, for example, if you prefer to use "bio" instead of "biology", use "bio" throughout the script.\nAns: ')
        divider()
        classind = classind + 1
        globals().get(i).append(classinp)
        if classinp not in classes:
            classes.append(classinp)

for i in daysoftheweek:
    with open(cwd + 'config.ini', 'a') as configfile:
        strlist = str(globals().get(i)).replace("'", "")
        strlist2 = strlist.replace("[", "")
        strlistfinal = strlist2.replace("]", "")
        configfile.write(i + ' = ' + strlistfinal + '\n')

with open(cwd + 'config.ini', 'a') as configfile:
    configfile.write('\n[sublinks]\n')

for i in classes:
    sublink = input('Please enter the link to join ' + i + ' class: ').replace(" ", "")
    divider()
    with open(cwd + 'config.ini', 'a') as configfile:
        configfile.write(i + ' = ' + sublink + '\n')