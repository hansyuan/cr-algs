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

    #
    temp_calls = copy.deepcopy(demands)

    temp_calls.sort(key=itemgetter(0))
    re_x = copy.deepcopy(temp_calls)

    temp_calls.sort(key=itemgetter(1))
    re_y = temp_calls
    
    x_bases = [b[0] for b in bases]
    y_bases = [b[1] for b in bases]

    plt.scatter(x_bases, y_bases, c='blue')

    x_all = [calls[0] for calls in converted_calls]
    y_all = [calls[1] for calls in converted_calls]

    # plt.scatter(x_all, y_all, c = 'green')

    # Begin using clustering methods here.

    a = array(converted_calls)
    w = whiten(a)



    Z = cluster.hierarchy.linkage(converted_calls, "complete")

    cut = cluster.hierarchy.fcluster(Z, 10, criterion="distance")

    # exit()

    # k-means
    kd = kmeans(a, 100)
    kd = [k for k in kd[0]]

    x_k = [k[0] for k in kd]
    y_k = [k[1] for k in kd]

    plt.scatter(x_k, y_k, c = 'red') # Clustered portions of the calls

    plt.show()

def main():
    print("<< all starts here in main >>")

    

