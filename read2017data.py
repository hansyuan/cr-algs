#!/usr/local/bin/python3
import time
import csv
from call_event import call_event
import operator

from dateutil import parser
from datetime import datetime
from IPython import embed

def diff_datetime(earlier, later):
	date_format = "%Y/%m/%d %H:%M:%S"
	time1 = datetime.strptime(earlier.datetime_to_string(), date_format)
	time2 = datetime.strptime(later.datetime_to_string(), date_format)
	diff = time2 - time1 
	# print (diff)
	return diff


def read2017():
	""" 
		This is a hardcoded function that reads the 2017 Cruz Roja data as 
		call_event objects
	"""

	newdata = "../data/tabladedatos.csv"

# "id","latitud","longitud","fecha","dia_semana","hora_llamada","vprioridad","no_unidad"

	with open(newdata, 'r') as csvfile:
		data = [list(line) for line in csv.reader(csvfile)]

	# For each event, create a representation for it:
	# year, month, date, hour, minute

	clean_data = []
	check_set = dict()

	for line in data[1:]:
		lat = line[1]
		lon = line[2]
		date = line[3].split('/')
		day = line [4]
		time = line [5].split(':')


		year = date[2] 

		if len(year) == 2:
			year = "20" + str(year)

		month = date[0]
		day = date[1]



		hour = time[0]
		minutes = time[1]
		seconds = time[2]

		point = (lat,lon)
		datetime = (year, month, day, hour, minutes, seconds)
		new_call_event = call_event(point, datetime)

		clean_data.append(new_call_event)

	# Calculate the wait time for the next ambulance
	clean_data.sort()

	for i in range(0, len(clean_data) - 1):
		wait = diff_datetime(clean_data[i], clean_data[i+1])
		# embed()
		clean_data[i].waittime = wait.seconds

	return clean_data


if __name__ == "__main__":
	read2017()
