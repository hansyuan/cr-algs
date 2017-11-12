# To get a general sense of the data. Doesn't actually contribute anything.
import read
import util
import copy
import time
from operator import itemgetter
from scipy.cluster.vq import vq, kmeans, whiten
from scipy import cluster
from numpy import array
from matplotlib import pyplot as plt


debug = True
"""
    bases = set of (x1,y1) of all the bases
    demands = set of (x2,y2) of all the bases
    times = based on indices of bases and demands, returns the times. 
"""


def print_lines(items: list) -> None:
    for i in items:
        print(i)


def surrounding_points(point: tuple, delta: float, data: list, reordered_data: list) -> [[]]:
    """ Given a point, a delta, and the set of points to work with, return
    a list of tuples containing all surrounding points.
    This should work for both bases and demands. """
    x = point[0]
    y = point[1]

    index_of_center = 0
    count_found = 0
    print_found = True
    # print (point)

    # let's find the surrounding x coordinates
    if reordered_data:
        x_ordered = reordered_data
    else:
        x_ordered = util.reorder(data, 0)

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
        if util.dist(x_ordered[i],
                     (x_ordered[curr_x][0], x_ordered[i][1])
                     ) > delta:
            break

        distance = util.dist((x,y), x_ordered[curr_x])
        count_found = 0
        if distance < delta:

            if print_found: print("Found: ", (x,y), x_ordered[curr_x], "\tDistance:\t", distance)
            count_found += 1
            all_the_surrounding_points.append(x_ordered[curr_x])

        curr_x += 1

    curr_x = index_of_center - 1
    #Identical loop, but going the other direction
    while True:
        if curr_x < 0 or curr_x >= len(x_ordered):
            break
        if util.dist(x_ordered[i],
                     (x_ordered[curr_x][0], x_ordered[i][1])
                     ) > delta:
            break
        distance = util.dist(x_ordered[i], x_ordered[curr_x])

        if distance < delta:
            if print_found: print("Found: ", x_ordered[i], x_ordered[curr_x], "\tDistance:\t", distance)
            count_found += 1
            all_the_surrounding_points.append(x_ordered[curr_x])
        curr_x -= 1

    print (count_found, (x,y), all_the_surrounding_points)
    print("\n")


    return all_the_surrounding_points


def main():
    print("Called main")

    data = (calls, bases, demands, times) = read.populate_data()



    converted_calls = []
    first = True
    for tup in calls:
        if first:
            first = False
            continue

        x = ([float(tup[1]), float(tup[2])])

        converted_calls.append(x)



    # re_x = util.reorder(calls, 0)
    # for x in range(len(bases)):
    #     surrounding = surrounding_points(calls[x], 0.2, bases, reordered_data=re_x)
    #     if surrounding:
    #         print("Result of search with the delta: " , surrounding)

    # Generate a list of calls, using the list of tuples of GPS coordinates of string. 

    temp_calls = copy.deepcopy(demands)

    temp_calls.sort(key=itemgetter(0))
    re_x = copy.deepcopy(temp_calls)

    temp_calls.sort(key=itemgetter(1))
    re_y = temp_calls


    # for each_point in converted_calls:
    #     nearby_demand_points = surrounding_points(
    #                 each_point,
    #                 0.3  ,
    #                 [],
    #                 reordered_data = re_x)
    #     for each_nearby in nearby_demand_points:
    #         time = times[500][each_nearby[2]]
    #         if time < 600:
    #             print("Time: " , time)

    # exit()

    # Plot all calls

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



    # for c in converted_calls:
    #     print (c)
    #
    #
    # print("wow")

    # for i in range(len(calls)):
    #     print(i)
    #     surrounding = surrounding_points(
    #         converted_calls[i],
    #         0.3,
    #         [],
    #         reordered_data=converted_calls)
    #
    #     if surrounding:
    #         print("Result of search with the delta: ", surrounding)


    # re_x = util.reorder(demands, 0)
    # for x in range(len(demands)):
        # surrounding = surrounding_points(demands[x], 1, demands, reordered_data=re_x)
        # if surrounding:
        #     print("Result of search with the delta: ", surrounding)
    # exit()

    # print("Reorder x")
    # reordered_bases_x = util.reorder(bases, 0)
    # with open("tmp_base_x.txt", 'w') as output:
    #     for each in reordered_bases_x:
    #         output.write(str(each).replace(" ", "\t") + "\n")
    #     output.write(str(len(reordered_bases_x)))

    # print("Reorder y")
    # reordered_bases_y = util.reorder(bases, 1)
    # with open("tmp_base_y.txt", 'w') as output_y:
    #     for each in reordered_bases_y:
    #         output_y.write(str(each).replace(" ", "\t") + "\n")
    #     output_y.write(str(len(reordered_bases_y)))


    # x = util.diff_dist(data, 575, 54)
    # print(x)
    # x2 = util.diff_time(data, 575, 54)
    # print(x2)

    print("Done with main.")
    
    
if __name__ == "__main__":
    main()