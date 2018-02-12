from IPython import embed 

# Class definition for events
class call_event:
	def __init__(self, location, datetime):

		# Check that point is a 2-tuple: lon, lat
		if len (location) != 2: 
			raise Exception("the call_event c-tor was called w/ malformed location point")

		# Check that datetime is a 6-tuple: year, mon, day, hour, min, sec
		if len (datetime) != 6: 
			raise Exception("the call_event c-tor was called w/ malformed datetime point")

		# I should also include checks based on the possible int/float values that 
		# these fields can take on 
		# for example, if year is not 2016 or 2017, then it's likely invalid.

		# TODO later

		self.lat = float(location[0])
		self.lon = float(location[1])
		self.year = int(datetime[0])
		self.month = int(datetime[1])
		self.day = int(datetime[2])
		self.hour = int(datetime[3])
		self.minute = int(datetime[4])
		self.second = int(datetime[5])

	def __str__(self):
		display = ""
		display += "Location in lat, lon: (%f, %f) \n" %(self.lat, self.lon)
		display += "Datetime: %04i/%02i/%02i %02i:%02i:%02i" %(self.year, 
			self.month, self.day, self.hour, self.minute, self.second)

		return (display)

	def __lt__(self, other):

		all_comparisons = [
			(self.year, other.year),
			(self.month, other.month),
			(self.day, other.day),
			(self.hour, other.hour),
			(self.minute, other.minute),
			(self.second, other.second)
		]

		for pairs in all_comparisons:
			lessthan = self.lessthan(pairs[0], pairs[1])
			if lessthan is not None: return lessthan 

		return False


	def lessthan(self, left, right):
		if left < right:
			return True
		if right < left: 
			return False
		else: 
			return None

def __main__():
	p = (1,2)
	q1 = (2,2,3,4,5,6)
	q2 = (2,2,3,4,5,7)

	event1 = call_event (p, q1)
	event2 = call_event (p, q2)
	print(event1 < event2)

if __name__ == "__main__":
	__main__()