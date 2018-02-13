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

def execute(speed):
    """ 
    Run on a clock the simulation. When I run the simulator, the program
    itself should be understood to be running at a faster speed than real time. 
    """
    amount = 5

    now = time()
    
    times = []

    while True:
        print("Sleep for %f" %(amount/speed))
        
        old = time()
        sleep(amount/speed)
        new = time()
        
        print("%f seconds has passed" %(new-old))
        times.append(new-old)

    sum = 0
    for x in times:
        sum += x

    sum /= len(times)

    print ("Average: %f" %sum)
    print ("Goalwas: %f" %(amount/speed))

if __name__ == "__main__": 
    data = prologue()
    speed = 2
    # execute(data, speed)




