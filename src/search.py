import read_data

import copy
import time

from operator import itemgetter
from scipy.cluster.vq import vq, kmeans, whiten
from scipy import cluster
from numpy import array
from matplotlib import pyplot as plt

# This file contains utilities to work with the data.

from math import sin, cos, sqrt, atan2, radians
import geopy.distance
import copy

debug=True

def dist(first: tuple, second: tuple) -> (float, str):
    """ Given two GPS coords, returns float dist in kilometers"""
    return geopy.distance.vincenty(first, second).km


def diff_dist(data, base_index, demand_index):
    """Calculates the Euclidean GPS distance difference. Based on raw given data. """
    (calls, bases, demands, times) = data
    demand_point = demands[demand_index]
    base_point = bases[base_index]
    (x,y) = (demand_point[0]- base_point[0], demand_point[1] - base_point[1])
    return (x,y)


def diff_time(times, base_index, demand_index):
    """ Returns time diff by database lookup. Based on raw given data. """
    #(calls, bases, demands, times) = data
    diff = times[base_index][demand_index] 
    return diff


def surrounding_points(
    point: tuple, 
    delta: float, 
    data: list, 
    reordered_data: list = None
) -> [[]]:
    """ Given a point, a delta, and the set of points to work with, return
    a list of tuples containing all surrounding points.
    This should work for both bases and demands. """
    x = point[0]
    y = point[1]

    index_of_center = 0
    count_found = 0
    print_found = False
    # print (point)

    # let's find the surrounding x coordinates
    if reordered_data:
        x_ordered = reordered_data
    else:
        x_ordered = copy.deepcopy(data)
        x_ordered.sort(key=itemgetter(0))

    for i in range(len(x_ordered)):
        if x_ordered[i][0] == x:
            index_of_center = i
            break;

    if not index_of_center:
        # print(x_ordered)
        while x_ordered[index_of_center][0] < x:
            if index_of_center == len(x_ordered) - 1: break;
            # print(index_of_center,x_ordered[index_of_center][0],x )
            index_of_center += 1
        #print(index_of_center)
        i = index_of_center

    # Go forwards and backwards. For each point, calculate the distance.
    # If the distance exceeds the delta, then stop
    curr_x = index_of_center + 1
    all_the_surrounding_points = []
    while True:

        # Check that only the x diff > delta in x
        if curr_x < 0 or curr_x >= len(x_ordered):
            break
        # Check if the x_edge is delta away
        if dist(x_ordered[i],
                     (x_ordered[curr_x][0], x_ordered[i][1])
                     ) > delta:
            break

        distance = dist((x,y), x_ordered[curr_x])
        count_found = 0
        if distance < delta:

            if print_found: 
                print("Found: ", (x,y), x_ordered[curr_x], 
                      "\tDistance:\t", distance)
            count_found += 1
            all_the_surrounding_points.append((x_ordered[curr_x], distance))

        curr_x += 1

    curr_x = index_of_center - 1
    #Identical loop, but going the other direction
    while True:
        if curr_x < 0 or curr_x >= len(x_ordered):
            break
        if dist(x_ordered[i],
                     (x_ordered[curr_x][0], x_ordered[i][1])
                     ) > delta:
            break
        distance = dist(x_ordered[i], x_ordered[curr_x])

        if distance < delta:
            if print_found: 
                print("Found: ", 
                      x_ordered[i], x_ordered[curr_x], 
                      "\tDistance:\t", distance)
            count_found += 1
            all_the_surrounding_points.append((x_ordered[curr_x], distance))
        curr_x -= 1

    if print_found: print (count_found, (x,y), all_the_surrounding_points)

    all_the_surrounding_points.sort(key=itemgetter(1))

    return all_the_surrounding_points