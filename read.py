calls   = "input/calls.csv"
bases   = "input/bases.csv"
demands = "input/demand_points.csv"
times   = "input/times.csv"

# 969 Bases, 100 Demand Points.

# tuple (base, demandpoint) will have a corresponding time in times



def opendata(data = ""):
    all_data = []
    with open(data,'r') as file:
        lines = file.readlines()
        for line in lines:
            line_sets = line.split(",")
            all_data.append(line_sets)

    return all_data[1:]


# Opens files as list of lists (2D arrays)
# Perfect for CSV files
def openfile_as_listoflist(filename=""):
    rowsaslines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_sets = line.split(",")
            rowsaslines.append(line_sets)


    return rowsaslines


def strip_newline(s):
    if not isinstance(s, str):
        
        ("Not a string")
        exit(-1)
    """If string has a newline, return string without that char. """
    return float(s.rstrip("\n"))


def populate_data():
    global calls, bases, demands, times

    # Raw Data
    bases_d = openfile_as_listoflist(filename=bases)
    calls_d = openfile_as_listoflist(filename=calls)
    demands_d = openfile_as_listoflist(filename=demands)
    times_d = openfile_as_listoflist(filename=times)

    # Pick data wanted
    bases = []
    for each_base in bases_d:
        bases += tuple([each_base[4:6]])

    calls = calls_d

    # demands = demands_d
    demands = []
    for each_demand in demands_d:
        demands += tuple([each_demand])



    times = times_d

    lists = [bases, demands, times]
    for setofdata in lists:
        for i in range(len(setofdata)):
            for j in range(len(setofdata[i])):
                setofdata[i][j] = strip_newline(setofdata[i][j])

    # Translate strings into ints or floats


    for setofdata in (bases, demands):
        count = 0
        for i in range(len(setofdata)):
            setofdata[i].append(count)
            count += 1




    return (calls,bases,demands,times)

if __name__ == "__main__":
    populate_data()

