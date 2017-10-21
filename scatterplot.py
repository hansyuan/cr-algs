from read import opendata
import numpy as np
import matplotlib.pyplot as plt


def coords_as_set():
    pass

def scatter_plot(show=False, print_stuff=False):
    coords = dict()
    data = opendata("input/calls.csv")
    x = []
    y = []
    for d in data:

        if not isinstance((d[1]), float) or not isinstance(d[2], float):

            d[1] = float(d[1])
            d[2] = float(d[2])
        point = (d[1], d[2])

        if point in coords:
            coords[point] += 1
        else:
            coords[point] = 1

    if print_stuff:
        for item in coords:
            print(item, coords[item])

    for coord in coords:
        x.append(coord[0])
        y.append(coord[1])

    if show:
        plt.scatter(x, y)
        plt.show()
    return coords

if __name__ == '__main__':
    scatter_plot(show=True)