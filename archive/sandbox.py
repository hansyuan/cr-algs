from read import openfile_as_listoflist
import scipy



if __name__ == "__main__":

    arr = openfile_as_listoflist("input/times.csv")
    for line in arr:
        print (line)

    stuff = set()
    count = 0

    # I was trying to figure out how many repeated lines in time.
    for line in arr:
        hashTHIS = " ".join(line)
        if hashTHIS not in stuff:
            stuff.add(hashTHIS)
        else:
            count += 1
            print (count)