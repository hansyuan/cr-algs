# To get a general sense of the data. Doesn't actually contribute anything.
import read
import util

"""
    bases = set of (x1,y1) of all the bases
    demands = set of (x2,y2) of all the bases
    times = based on indices of bases and demands, returns the times. 
"""


def print_lines(items: list) -> None:
    for i in items:
        print(i)


if __name__ == "__main__":

    data = (calls, bases, demands, times) = read.populate_data()

    print_lines(demands)


    x = util.diff_dist(data, 575, 54)
    print(x)
    x2 = util.diff_time(data, 575, 54)
    print(x2)