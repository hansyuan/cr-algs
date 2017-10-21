# To get a general sense of the data. Doesn't actually contribute anything.
import read
import util

#((calls,bases,demands,times)) = ([],[],[],[])

if __name__ == "__main__":

    ((calls, bases, demands, times)) = read.populate_data()
    data = (calls, bases, demands, times)
    x = util.difference(data, 575, 54);