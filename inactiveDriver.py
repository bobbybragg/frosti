#!/usr/bin/python3

# FROSTi Passive Driver
# This driver is a neutered version of the full frosti driver,
# originally designed for testing and now used to spoof an
# active driver on a pi without read access to the thermistors.
# This is needed because redundancy checking was designed with
# two active pis in mind, and though that's not currently
# feasible I've decided to not change the design in the hope
# that one day the two active pi design will be implemented.
#
# Addendum: Huzzah, both Pis can read temps now. This will
# stay in the repo because it's good for testing if you
# don't have access to the lab, but this should no longer
# be necessary on the production system
#
# This version operates the same as the active driver, but
# instead of reading from thermistors it just injects '-80.0'
# for each thermistor in all read operations.

#from readSrc.temp import *
#from readSrc.read import *
from loggerSrc.logger import *
from alertSrc.alert import *

import datetime

#IP address of other pi
#init other

#true if active pi
active = True

#directory of log files
logDir = "/home/bmcc0605/frosti/logs/"

def run():
    #read.gpio_init()
    #freezers_init()
    #thermistors_init()         
    tempList = []
    for freezer in range (0,3):
        time = datetime.datetime.now()
        temperature = -80.0 #insert test value instead of calc_temp(freezer)
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

def check_partner(other):
    #ping other
    if fail:
        #ping again, break if success
        active = true
        error = "Warning: Pi " + str(other) + " is down. Please replace soon."
        n = send(error, "all")
        if n == -1:
            #email error
            print("Email failed to send.")
        elif n == -2:
            #text error
            print("SMS failed to send.")
        elif n == -3:
            #email and text error
            print("Email and SMS failed to send.")
    
run()
