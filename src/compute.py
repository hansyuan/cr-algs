import copy
import time
import numpy as np

def choose_start_bases_greedy(allbases, demands, times, calls_latlong):
	# Pasted from yesterday: choose bases using greedy
	# Get the first base
	times_copy = copy.deepcopy(times)

	# Continually get the min cost row (most optimal base)
	# Delete the columns that are covered by this base by r1
	# Recalculate the total cost for each base
	# Repeat

	r1 = 600

	numbases = 8
	list_bases = []
	total_covered = []

	for x in range(numbases):
	    print(np.shape(times_copy))
	    covered = []
	    row_num = 0
	    for row in times_copy:
	        count = 0
	        for col in row:
	            if col < r1:
	                count += 1
	        covered.append((row_num, count))
	        row_num += 1
	    
	    d = [('index', int), ('covered', int)]
	    covered = np.array(covered, d)
	    
	    min_cost = (np.sort(covered, order='covered', kind='mergesort')[-1])

	    list_bases.append(min_cost[0])
	    
	    # Delete the columns (demands) that are covered by r1.
	    
	    primary_covered = [times_copy[min_cost[0]][i] < r1 for i in range(len(times_copy[min_cost[0]]))]
	    covered_indices = [i for i in range(len(primary_covered)) if primary_covered[i] ]
	    total_covered += covered_indices

	    times_copy = np.delete(times_copy, covered_indices, axis=1)

	ind = list_bases
	print("Total Covered: " , len(total_covered))
	return list_bases 




