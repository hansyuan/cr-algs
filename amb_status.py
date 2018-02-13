from IPython import embed

class amb_status:
	next_id = 0

	def __init__(self):
		self.id = amb_status.next_id
		amb_status.next_id += 1

		self.deployed = False
		self.lat = -1
		self.lon = -1
		self.time_deployed = -1


	def deploy(self, time, lat, lon):
		self.time_deployed = time
		self.lat = lat
		self.lon = lon

	def finish(self):
		self.time_deployed = self.lat = self.lon = -1


def main():
	ambulances = []
	for x in range(10):
		ambulances.append(amb_status())


	for y in ambulances:
		print(y.id)

if __name__ == "__main__": main()