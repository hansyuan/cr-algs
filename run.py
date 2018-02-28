#!/Users/vectflux/miniconda3/bin/python3
import compute 
import execute

def main():
	retvar = None

	# retvar = execute.get_starting_set(8, 600, display = False) # Is this old?
	 
	compute.choose_start_bases_greedy(allbases, demands, times, calls_latlong)
	retvar = execute.check_coverage(retvar)
	return retvar

if __name__ == "__main__":
	print(main())