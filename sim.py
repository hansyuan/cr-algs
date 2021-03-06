#!/usr/local/bin/python3


from time import time, sleep
import sys
import random
from enum import Enum
from amb_enums import *
from read2017data import read2017
from amb_status import amb_status
import gui
# from IPython import embed
# from ipdb import set_trace


def prologue(num_ambs, data_set):
    """ The previous problem with the clock was that I executed the clock 
    every single time a simulator second goes off. 

    Since I know that the ambulance runtime will be hardcoded to 20 min, 
    and then random events can occur every five minutes, the loop can rise
    once every five minutes. 

    Furthermore, I can make the program wait for the time the next ambulance 
    will take, rather than hardcoding some random amount of time. 
    """
    
    print("Reading data set: %s" % data_set)
    calls = read2017(data_set)
    
    ambulances = []

    for num in range(num_ambs):
        ambulances.append(amb_status())

    return calls, ambulances




def pick_ambulance():
    return 0 



def one_loop_per_second(calls_all_time, ambulances):

    """ 
        calls_all_time: list of Call_events of (gps lat longs, date time)
            see call_event.py

        ambulances: list of amb_status of (deployed, location, time deployed)
            see amb_status.py
            
    """ 
    second = 0
    temporary_second = 0
    case_number = 0
    next_occurring_call = calls_all_time[case_number].waittime
    count_most_simultaneous_calls = 0
    
    while case_number < len(calls_all_time):
        # For the current second, determine whether dispatcher receives a new call. If it does, 
        # then assign an ambulance for it for 20 minutes (20min * 60sec/min = 1200 sec)

        if next_occurring_call == temporary_second:

            # Clear ambulances TODO
            # Call ambulance.finish()

            # Find all events occurring at this time. 

            calls_received = []   
            calls_received.append(calls_all_time[case_number])         

            print('case: ', case_number + 1, 'of', len(calls_all_time))
            check_data = case_number
            while (0 == calls_all_time[check_data].waittime 
                    and case_number + 1 < len(calls_all_time)):
                calls_received.append(calls_all_time[check_data + 1])
                check_data += 1


            if False: 
                for call in calls_received: print(call)

            # Assign an ambulance TODO
            # Call ambulance.deploy(time, lat, lon)

            for case in calls_received:
                chosen_ambulance = pick_ambulance()

            
            # Clean up: save next case number. Set next wait time. Reset temp time.
            case_number += len(calls_received)
            next_occurring_call = calls_all_time[check_data].waittime
            temporary_second = 0
            
        # t <- t + 1 (sec)
        second += 1
        temporary_second += 1

        
def write_info():
    if False: 
        log = ""
        count = 0

        for i in range(len(data)):
            if data[i].waittime == 0:
                count += 1
                log += data[i].__str__() + '\n\n'
                try: 
                    log += data[i + 1].__str__() + '\n'
                except Exception:
                    log += "Hopefully the last count. \n"
                log += '----------------------------------------\n'

        with  open('zero_wait.txt', 'w') as counter_file:
            counter_file.write(str(count) + '\n\n')
            counter_file.write(log)
            
            
def run_through_cases():
    number_of_ambulances = 11
    # speed1 = 5000
    # speed2 = 999999999
    # speed = speed2

    smalldata = "../data/small_datos.csv"
    newdata = "../data/tabladedatos.csv"

    data, ambulances = prologue(number_of_ambulances, smalldata)
    # clockloop(data, ambulances, speed)
    # Calculate the number of 0 waittimes, and their events. 
    one_loop_per_second(data, ambulances)


if __name__ == "__main__": run_through_cases()
