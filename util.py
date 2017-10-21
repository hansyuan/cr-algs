# This file contains utilities to work with the data.


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