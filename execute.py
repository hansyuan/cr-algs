# this file defines starting points of execution
# for example, finding the optimal 8 ambulances starts its execution 
# in one of the methods defined here 
import copy
from operator import itemgetter
from scipy.cluster.vq import vq, kmeans, whiten
from scipy import cluster
from numpy import array
from matplotlib import pyplot as plt
from sys import exit

import read_data
import search

# Given a list of points (x,y) , plot them.
def plot(list_of_points: list, color=None) -> None:        
    x = [p[0] for p in list_of_points]
    y = [p[1] for p in list_of_points]
    plt.scatter(x, y, c=color)
    

def initial(run=True):
    if not run:
        return
    
    (calls, bases, demands, times, converted_calls) = read_data.populate_data()

    # Reorder calls by x or y coordinate
    temp_calls = copy.deepcopy(demands)
    temp_calls.sort(key=itemgetter(0))
    re_x = copy.deepcopy(temp_calls)
    temp_calls.sort(key=itemgetter(1))
    re_y = temp_calls
    
    # Points of all the bases
    plot(bases, "green")
    print("All the bases:")
    plt.show()

    # Points of all the calls
    plot(converted_calls, "blue")
    print("Every single call:")
    plt.show()

    # Begin using clustering methods here.
    a = array(converted_calls)
    w = whiten(a)
    Z = cluster.hierarchy.linkage(converted_calls, "complete")
    cut = cluster.hierarchy.fcluster(Z, 10, criterion="distance")

    # k-means on the converted calls
    rep_calls = 10
    kd = kmeans(a, rep_calls)
    kd = [k for k in kd[0]]
    
    plot(kd, "red")
    print("Clustered calls represented by %d points:" %(rep_calls)) 
    plt.show()
    
    print("Overlay the demand points by the clustered demand points:")
    plot(converted_calls, "blue")
    plot(kd, "red")
    plt.show()
    
    print("Overlay the bases by the clustered demand points:")
    plot(bases, "green")
    plot(kd, "red")
    plt.show()
    
    print(" I did not remove the redundant Mexico City data yet. ")


def find_starting_set(run=True):
    """ For of the 100 clustered demands points,
    
    Determine whether a base in the set of n bases 
    can reach that demand point within r1. 
    
    As soon as a demand point cannot be reached by a base
    within r1, throw that set of bases out
    
    There is no way to brute force every combination of 8 ambulances
    But instead use the demand points, find the surrounding bases,
    and check whether that fulfills the set coverage. 
    
    Reorder the bases list, and then randomize it. """
    
    if not run: return
    r1 = 600 
    top_n = 10
    delta = 0.6
    
    (calls, bases, demands, times, converted_calls) = read_data.populate_data()
    call_array = array(converted_calls)
    calls_kmeans = kmeans(call_array, top_n)
    
    # Get the first coordinate, then find the closest actual base. 
    calls_clustered_list = calls_kmeans[0]
    
    
    print(
        "For each representative call point, find the bases. \n")
    for each_call in calls_clustered_list:
        actual = search.surrounding_points(
            each_call,
            delta,
            bases
        )
        
        plot([each_call], "red")
        
        print(each_call, " with distance of {d}\n\n".format(d=delta))
        for each in actual:
            print(each)
            plot([each[0]], "green")
            
        
        
        plt.show()
        
        print("----------------------------------------")
    
    
    
    
    pass
