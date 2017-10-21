

def difference(data, base_index, demand_index):
    ((calls, bases, demands, times)) = data
    # Distance:
    demand_point = demands[demand_index]
    base_point = bases[base_index]
    (x,y) = (demand_point[0]- base_point[0], demand_point[1] - base_point[1])
    print("Distance: ", (x,y))
    print("Time: ", times[base_index][demand_index]/60.0)