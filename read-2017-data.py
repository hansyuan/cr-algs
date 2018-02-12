#!/usr/local/bin/python3
import time
import csv
from dateutil import parser

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

	point = (lat,lon)

	year = date[2] 
	if len(year) == 2:
		year = "20" + year
	month = date[0]
	day = date[1]

	hour = time[0]
	minute = time[1]
	seconds = time[2]

	ID = year+month+day+hour+minute+seconds+lat+lon
	if ID in check_set:
		print("duplicate found: ", ID )
		check_set[ID] += 1
	else:
		check_set[ID] = 1

# print (check_set.values())

	# print(year,month,day,hour,minute,seconds, point)
	# print(ID)






# my_data = genfromtxt(newdata, delimiter=',', dtype=None)
# print (my_data[2])
