#!/usr/bin/python3

# FROSTi Driver

from temp import *
from read import *
from logger import *
from alert import *
import datetime

#IP address of other pi
#init other

#true if active pi
active = True

#directory of log files
logDir = "/home/pi/frosti/logs/"
    
def run():
    read.gpio_init()
    freezers_init()
    thermistors_init()         
    tempList = []
    for freezer in range (0,3):
        time = datetime.datetime.now()
        temperature = calc_temp(freezer)
        tempList.append(temperature)
        if temperature > -60.0:
            if active: #moved active check here to ensure logging happens on inactive pi
                #need to sleep and retake temp
                error = "Warning: Freezer " + str(freezer) + " has reached " + str('%.1f'%(temperature)) + "*C at " + str(time)[10:19] + "."
                n = send(error, "freezer")
                if n == -1:
                    #email error
                    print("Email failed to send.")
                elif n == -2:
                    #text error
                    print("SMS failed to send.")
                elif n == -3:
                    #email and text error
                    print("Email and SMS failed to send.")
    n = log(logDir, tempList[0], tempList[1], tempList[2])
    if n == -1:
        print("error")
        #check_partner(other)
    
run()
