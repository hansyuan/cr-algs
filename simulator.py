#!/usr/local/bin/python3


import time
import sys
import random
from enum import Enum

class Status(Enum):
    """ For ambulances """
    IDLE = 1
    ACTIVE = 2

class DataSource(Enum):
    """ There are at least three sources of events for the simulation. """
    RANDOM = 1
    
def generate_random_amb_event(amb_status, ambulance_set, demand_set):
    """ Given the set of ambulances and the set of demand points, randomly generate an event """
    """ The return type should specify ambulance and demand point. """
    
    chosen_amb = random.randint(0,len(amb_status)-1)
    
    return (chosen_amb, 0)

def get_next_event(amb_status, data_source, ambulance_set, demand_set, src_file):
    """ Reads the next event from data set or generates one. """
    
    if data_source is DataSource.RANDOM:
        (amb, demand) = generate_random_amb_event(amb_status, ambulance_set, demand_set)
    
    else: 
        raise Exception ("This should not happen.")
        
    return (amb, demand)

def change_state(amb_status, chosen_amb):
    """ Takes the ambulance status dictionary, and an event. Toggles ambulance setting """    
    
    if type(amb_status) is not dict: raise Exception("Wrong type. ") 
        
    
    for each in amb_status:
        (status, time) = amb_status[each]
        if time > -1: amb_status[each] = (status, time + 1)
        if amb_status[each][1] >= 1200:
            amb_status[each] = (Status.IDLE, -1)
    
    if chosen_amb < 0: 
        return
    
    # TODO This line of code is not supposed to be here. 
    if amb_status[chosen_amb][1] == -1:
        amb_status[chosen_amb] = (Status.ACTIVE, 0)
        
def execute_simulation(run_time=1, speed_times=4, amb_status = None, 
              data_source = None, ambulance_set = None, demand_set = None):
    """ Starts a clock """
    """ Every unit of time, update the next ambulance event, print, update time. """
    """ Each ambulance should also know how long it's gone for. It should keep track of itself. """
    
    if amb_status == None: raise Exception ("param amb_status is None")
    if type(amb_status) is not dict: raise Exception ("amb_status wrong type")
    if type(run_time) is not int: raise Exception("run_time not int")
#     if type(speed_times) is not int: raise Exception("speed_times not int")

    start = time.time()
    time_diff = 0

    while True:
        (chosen_amb, demand_location) = (-1, -1)
        time.sleep(1/speed_times)
        
        if time_diff % 30 == 0:
            print ("Time: %3i seconds" %(time_diff))
        
        
        
        # Read the next event and then change the state:
        
        if time_diff % 300 == 0:
            (chosen_amb, demand_location) = get_next_event(
                amb_status, data_source, ambulance_set, demand_set, None)

        change_state(amb_status, chosen_amb)
        
        # Prints out all the ambulance's status every simulated minute
        
        if time_diff % 30 == 0:
            print("The amb-event is " , (chosen_amb, demand_location))
            for ID in amb_status: 
                print("Ambulance %2i\t" %(ID), amb_status[ID])        
        
            print()
            
        # Calculate the time passage.
        now = time.time()
        time_diff = int((now - start) * speed_times)

        if time_diff > run_time: break 
            
        


# In[2]:


# The following two variables will change the speed and amount of time the simulation is run.

# 2 hours
run_time = 28800 # in simulated seconds

speed = 40  # in (simulated seconds * speed) real seconds
# Dividing seconds by speed seems to be VERY detrimental

# It's still possible to change the granularity of this unit of time. 1/10 of a second granularity could be better.

ambulance_count = 10
amb_status = {} 

# Each ambulance maps to a tuple (status, time active)
for ID in range(0, ambulance_count):
    amb_status[ID] = (Status.IDLE, -1)

execute_simulation(run_time=run_time, speed_times=speed, amb_status = amb_status, data_source = DataSource.RANDOM)


# There is a bug with randomly generating events. If I choose an on-duty ambulance, the case is not well-defined. This program should really be running on terminal.
# 
# The unit of time should be seconds, since that is what the data uses and it seems granular yet efficient enough.
