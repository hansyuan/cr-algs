# To get a general sense of the data. Doesn't actually contribute anything.
import read
import util
import copy
import time
from operator import itemgetter

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
    (x,y) = point
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

    # Go forwards and backwards. For each point, calculate the distance.
    # If the distance exceeds the delta, then stop
    curr_x = index_of_center + 1
    all_the_surrounding_points = []
    while True:

        # Check that only the x diff > delta in x
        if curr_x < 0 or curr_x >= len(x_ordered):
            break
        if util.dist(x_ordered[i], (x_ordered[curr_x][0], x_ordered[i][1])) > delta:
            break

        distance = util.dist(x_ordered[i], x_ordered[curr_x])
        if distance < delta:
            print("Found: ", x_ordered[i], x_ordered[curr_x], "\tDistance:\t", distance)
            all_the_surrounding_points.append(x_ordered[curr_x])
        curr_x += 1
    return all_the_surrounding_points




if __name__ == "__main__":

    data = (calls, bases, demands, times) = read.populate_data()

    # re_x = util.reorder(calls, 0)
    # for x in range(len(bases)):
    #     surrounding = surrounding_points(calls[x], 0.2, bases, reordered_data=re_x)
    #     if surrounding:
    #         print("Result of search with the delta: " , surrounding)

    # Generate a list of calls, using the list of tuples of GPS coordinates of string. 

    converted_calls = []
    first = True
    for tup in calls:
        if first: 
            first = False
            continue

        x = tuple([float(tup[1]), float(tup[2])])
        print (x)
        converted_calls.append( x )

    #reorder_x_positions = util.reorder(converted_calls, 0)

    print(converted_calls)
    reorder_x_positions = converted_calls.sort(key=itemgetter(0))

    for c in converted_calls:
        print (c) 

    
    print("wow")

    for i in range(len(calls)):
        print(i)
        surrounding = surrounding_points(
            converted_calls[i], 
            0.3, 
            [], 
            reordered_data=converted_calls)

        if surrounding:
            print("Result of search with the delta: ", surrounding)


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