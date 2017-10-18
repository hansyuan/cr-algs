from read import *
from analyze import *
from time import sleep
from threading import Thread

wait = 2

def do_calc(first, second):
    # Calculate every single point:
    if not isinstance(first, list):
        exit(-1)
    if not isinstance(first, list):
        exit(-1)

    calcs_so_far = 0

    for start in first:
        for end in second:
            calcs_so_far += 1
            try:
                difference = (end[0] - start[0])
                # print (difference)
            except:
                print("AN EXCEPTION WAS THROWN")

            if calcs_so_far % 10000 == 0:
                print(calcs_so_far)
                # sleep(0.3) # Reenable timer if want to timeshare.

def calculate_distances():
    """
    • Between each two points, calculate the distance.
    • Of course, this is a stupidly exponential problem.
    • What I really want is to build intuition of possible solution sets to build.
    """
    global wait
    coordinates = scatter_plot(show=False) # type dict/set
    num_coor = len(coordinates)
    total_calcs = num_coor * num_coor

    print("The number of calculations is %i" % total_calcs)

    # Get a list of coords.
    list_coords = [coord for coord in coordinates]
    print(len(list_coords))
    print (list_coords)

    # Break the list into n lists and run all n^2 multiplications
    # TODO Generalize this to x many threads.
    first = list_coords[0:int(num_coor/2)]
    second = list_coords[int(num_coor/2) + 1: ]

    # Allow the number of calcs to be done printed:
    while wait > 0:
        print ("Waiting %i seconds..." %wait)
        wait -= 1
        sleep(1)

    all_threads = []

    # TODO Generalize this to x many calculations being doing.

    all_threads.append(Thread(target=do_calc, args=(first, first)))
    all_threads.append(Thread(target=do_calc, args=(first, second)))
    all_threads.append(Thread(target=do_calc, args=(second, second)))
    all_threads.append(Thread(target=do_calc, args=(second, first)))

    for t in all_threads:
        t.start()

    return

if __name__ == "__main__":
    calculate_distances()