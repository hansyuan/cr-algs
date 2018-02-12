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

		self.lat = location[0]
		self.lon = location[1]
		self.year = datetime[0]
		self.month = datetime[1]
		self.day = datetime[2]
		self.hour = datetime[3]
		self.minute = datetime[4]
		self.second = datetime[5]

	def __str__(self):
		display = ""
		display += "Location in lat, lon: (%f, %f) \n" %(self.lat, self.lon)
		display += "Datetime: %04i/%02i/%02i %02i:%02i:%02i" %(self.year, 
			self.month, self.day, self.hour, self.minute, self.second)

		return (display)


p = (1,2)
q = (1,2,3,4,5,6)

event1 = call_event (p, q)
print(event1)