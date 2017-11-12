# This file contains utilities to work with the data.

from math import sin, cos, sqrt, atan2, radians
import geopy.distance
import copy

debug=True

def dist(first: tuple, second: tuple) -> (float, str):
    """ Given two GPS coords, returns float dist in kilometers"""
    return geopy.distance.vincenty(first, second).km

def reorder(input:list, position: int):
    """ Given a list of tuple and the position, reorder the list of tuple
    in numerical order based on the parameter. """

    if debug: print("reordering ")

    tuples = []
    for each in input:
        t = copy.deepcopy(each)
        tuples.append(t)

    return_list = []

    # Find the lowest specific parameter value
    count_loops = 0
    for i in tuples:
        print(count_loops)
        count_loops += 1
       
        min_val = tuples[0][position]
        min_pos = 0

        for index in range(len(tuples)):
            # find the next highest value
            if tuples[index][position] < min_val: # find the lowest item
                min_val = tuples[index][position]
                min_pos = index
            t = copy.deepcopy(tuples[min_pos])
            #print(t)
        return_list.append(t)
            #print (return_list)
        for each in range(len(tuples[min_pos])): # erase from iterating
            tuples[min_pos] = (99,99)

    return return_list



def diff_dist(data, base_index, demand_index):
    """Calculates the Euclidean GPS distance difference. Based on raw given data. """
    (calls, bases, demands, times) = data
    demand_point = demands[demand_index]
    base_point = bases[base_index]
    (x,y) = (demand_point[0]- base_point[0], demand_point[1] - base_point[1])
    return (x,y)


def diff_time(data, base_index, demand_index):
    """ Returns time diff by database lookup. Based on raw given data. """
    (calls, bases, demands, times) = data
    diff = times[base_index][demand_index] / 60.0
    return diff

