#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import os
import fonctions
from statistics import median

kein_means = open("evident","w")

root = os.getcwd()+"/stations"
os.chdir(root)

list_stations = os.listdir()
list_stations[:] = [int(elt) for elt in list_stations]
list_stations = set(list_stations)

for station in list_stations:
	path = root+"/"+ str(station) +"/saison/"
	saisons = os.listdir(path)
	saisons[:] =  [int(elt) for elt in saisons]
	saisons = set(saisons)

	for saison in saisons:
		path = root+"/"+ str(station) +"/saison/"+ str(saison) +"/moment/"
		moments = os.listdir(path)
		moments[:] =  [int(elt) for elt in moments]
		moments = set(moments)
	

		for moment in moments:
			path = root+"/"+ str(station) +"/saison/"+ str(saison) +"/moment/"+ str(moment)

			os.chdir(path)

			solution = open("bikes_train.solution","r")
			solution = fonctions.fic_to_floatlist2(solution)

			Max = max(solution)
			Min = min(solution)
			mediane = median(solution)

			dynamique = Max - Min + 1
			
			print(str(station)+" "+str(saison)+" "+str(moment)+" "+str(dynamique)+" "+str(mediane))
			if mediane == dynamique:
				kein_means.write(str(station)+" "+str(saison)+" "+str(moment)+" "+str(Max)+"\n")