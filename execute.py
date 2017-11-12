# this file defines starting points of execution
# for example, finding the optimal 8 ambulances starts its execution 
# in one of the methods defined here 
import copy
from operator import itemgetter
from scipy.cluster.vq import vq, kmeans, whiten
from scipy import cluster
from numpy import array
from matplotlib import pyplot as plt


import read_data
import search


def set_coverage():
    (calls, bases, demands, times, converted_calls) = read_data.populate_data()

    # Reorder calls by x or y coordinate
    temp_calls = copy.deepcopy(demands)
    temp_calls.sort(key=itemgetter(0))
    re_x = copy.deepcopy(temp_calls)
    temp_calls.sort(key=itemgetter(1))
    re_y = temp_calls
    
    # Points of all the bases
    x_bases = [b[0] for b in bases]
    y_bases = [b[1] for b in bases]
    plt.scatter(x_bases, y_bases, c='green')
    print("All the bases:")
    plt.show()

    # Points of all the calls
    x_all = [calls[0] for calls in converted_calls]
    y_all = [calls[1] for calls in converted_calls]

    print("Every single call:")
    plt.scatter(x_all, y_all, c = 'blue')
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
    x_k = [k[0] for k in kd]
    y_k = [k[1] for k in kd]
    
    print("Clustered calls represented by %d points:" %(rep_calls))
    plt.scatter(x_k, y_k, c = 'red') 
    
    plt.show()
    
    print("Overlay the bases by the clustered demand points:")
    plt.scatter(x_all, y_all, c = 'blue')
    plt.scatter(x_k, y_k, c = 'red')
    plt.show()


def find_starting_set():
    # For of the 100 clustered demands points,
    
    # Determine whether a base in the set of n bases 
    # can reach that demand point within r1. 
    
    # As soon as a demand point cannot be reached by a base
    # within r1, throw that set of bases out
    
    # There is no way to brute force every combination of 8 ambulances
    # But instead use the demand points, find the surrounding bases,
    # and check whether that fulfills the set coverage. 
    
    # Reorder the bases list, and then randomize it.
    pass
