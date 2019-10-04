#!/usr/bin/python3

import os
from shutil import rmtree
#os.stat(fic).st_size == 0

root = os.getcwd()+"/stations"
os.chdir(root)

list_stations = os.listdir()
list_stations[:] = [int(elt) for elt in list_stations]
list_stations = set(list_stations)

saisons = [0,1,2,3]
moments = [0,1,2,3]

for station in list_stations:
	path = root+"/"+ str(station)
	fic = path + "/bikes_train.solution"
	if os.stat(fic).st_size == 0:
		rmtree(path)
		continue

	for saison in saisons:
		path = root+"/"+ str(station) +"/saison/"+ str(saison)
		fic = path + "/bikes_train.solution"
		if os.stat(fic).st_size == 0:
			rmtree(path)
			continue

		for moment in moments:
			path = root+"/"+ str(station) +"/saison/"+ str(saison) +"/moment/"+ str(moment)
			fic = path + "/bikes_train.solution"
			if os.stat(fic).st_size == 0:
				rmtree(path)
				continue