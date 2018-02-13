#!/usr/local/bin/python3


from time import time, sleep
import sys
import random
from enum import Enum
from amb_enums import *
from read2017data import read2017

def prologue():
    """ The previous problem with the clock was that I executed the clock 
    every single time a simulator second goes off. 

    Since I know that the ambulance runtime will be hardcoded to 20 min, 
    and then random events can occur every five minutes, the loop can rise
    once every five minutes. 

    Furthermore, I can make the program wait for the time the next ambulance 
    will take, rather than hardcoding some random amount of time. 
    """

    calls = read2017()
    return calls


def change_states():
    pass

def clockloop(data, speed):
    """ 
    Run on a clock the simulation. When I run the simulator, the program
    itself should be understood to be running at a faster speed than real time. 
    """

    now = time() 

    # The original starting time of the clock is called now

    # All events that occurred from the data will be an offset from the 
    # original starting event. The first case's call time shall be the 
    # starting time stored in now (approximately.)

    for call_event in data:
        # Do the thing, then sleep.
        change_states()
        print("The event is located at %f, %f" %(call_event.lat, call_event.lon))

        sleep_time = call_event.waittime / speed
        print("Sleep for %.2f simulator seconds or %1.2f real seconds" 
            %(call_event.waittime, sleep_time))
        
        old = time()
        sleep(sleep_time) # in units of seconds
        new = time()
        
        print("%5f real seconds has passed \n" %(new - old))


if __name__ == "__main__": 
    data = prologue()
    speed = 7000

    print("Start the clock:")
    clockloop(data, speed)




