#!/usr/local/bin/python3


from time import time, sleep
import sys
import random
from enum import Enum
from amb_enums import *
from read2017data import read2017
from amb_status import amb_status
from IPython import embed
from ipdb import set_trace

def prologue(num_ambs, data_set):
    """ The previous problem with the clock was that I executed the clock 
    every single time a simulator second goes off. 

    Since I know that the ambulance runtime will be hardcoded to 20 min, 
    and then random events can occur every five minutes, the loop can rise
    once every five minutes. 

    Furthermore, I can make the program wait for the time the next ambulance 
    will take, rather than hardcoding some random amount of time. 
    """
    


    calls = read2017(data_set)


    ambulances = []

    for num in range(num_ambs):
        ambulances.append(amb_status())


    return calls, ambulances

def pick_ambulance():
    return 0 


def change_states(amb_status, amb_id):
    pass


def clockloop(data, ambs, speed):
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
        amb_id = pick_ambulance()
        change_states(amb_status, amb_id)
        print("The event is located at %f, %f" %(call_event.lat, call_event.lon))

        sleep_time = call_event.waittime / speed
        print("Sleep for %.2f simulator seconds or %1.2f real seconds" 
            %(call_event.waittime, sleep_time))
        
        old = time()
        sleep(sleep_time) # in units of seconds
        new = time()
        
        print("%5f real seconds has passed \n" %(new - old))

    # Loop one time per simulator second
    


def one_loop_per_second(calls_all_time, ambulances):
    second = 0
    temporary_second = 0
    case_number = 0
    next_occurring_call = calls_all_time[case_number].waittime
    count_most_simultaneous_calls = 0
    
    while case_number < len(calls_all_time):
        # For the current second, determine whether dispatcher receives a new call. If it does, 
        # then assign an ambulance for it for 20 minutes (20min * 60sec/min = 1200 sec)

        # print(second, next_occurring_call, "outer while ", next_occurring_call, temporary_second)

        if next_occurring_call == temporary_second:
            calls_received = []   
            calls_received.append(calls_all_time[case_number])         

            # If current waittime is 0, append the next event. If next event waittime is 0, 
            # append 3rd event. And so on.

            print('case: ', case_number + 1, 'of', len(calls_all_time))
            check_data = case_number
            while (0 == calls_all_time[check_data].waittime and 
                case_number + 1 < len(calls_all_time)):
                calls_received.append(calls_all_time[check_data + 1])
                check_data += 1

            if False: 
                for call in calls_received: print(call)

            case_number += len(calls_received)
            next_occurring_call = calls_all_time[check_data].waittime

            temporary_second = 0

        second += 1
        temporary_second += 1


if __name__ == "__main__": 
    number_of_ambulances = 11
    speed1 = 5000
    speed2 = 999999999

    speed = speed2

    smalldata = "../data/small_datos.csv"
    newdata = "../data/tabladedatos.csv"

    data, ambulances = prologue(number_of_ambulances, smalldata)


    # clockloop(data, ambulances, speed)
    # embed()

    # Calculate the number of 0 waittimes, and their events. 

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


    # embed()

    one_loop_per_second(data, ambulances)




