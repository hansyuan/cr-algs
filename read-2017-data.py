#!/usr/local/bin/python3
import time
import csv
from call_event import call_event
import operator

from dateutil import parser
from IPython import embed

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

	return clean_data.sort()


if __name__ == "__main__":
	read2017()
