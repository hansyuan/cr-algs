# To get a general sense of the data. Doesn't actually contribute anything.
import read
import util
import copy

"""
    bases = set of (x1,y1) of all the bases
    demands = set of (x2,y2) of all the bases
    times = based on indices of bases and demands, returns the times. 
"""


def print_lines(items: list) -> None:
    for i in items:
        print(i)


def reorder(input:list, position: int):
    """ Given a tuple and the position, reorder the list of tuple
    in numerical order based on the parameter. """

    tuples = []
    for each in input:
        t = copy.deepcopy(tuple(each))
        tuples.append(t)

    return_list = []

    # Find the lowest specific parameter value
    for i in tuples:
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


if __name__ == "__main__":

    data = (calls, bases, demands, times) = read.populate_data()

    p = util.borrow2(bases[0], bases[1])
    print(bases[0], bases[1])
    print(p)


    print("Reorder x")
    reordered_bases_x = reorder(bases, 0)
    with open("tmp_base_x.txt", 'w') as output:
        for each in reordered_bases_x:
            output.write(str(each).replace(" ", "\t") + "\n")
        output.write(str(len(reordered_bases_x)))

    print("Reorder y")
    reordered_bases_y = reorder(bases, 1)
    with open("tmp_base_y.txt", 'w') as output_y:
        for each in reordered_bases_y:
            output_y.write(str(each).replace(" ", "\t") + "\n")
        output_y.write(str(len(reordered_bases_y)))


    # x = util.diff_dist(data, 575, 54)
    # print(x)
    # x2 = util.diff_time(data, 575, 54)
    # print(x2)

    print("Done with main.")