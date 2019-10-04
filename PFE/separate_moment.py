#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import os
import fonctions

root = os.getcwd()+"/stations"
os.chdir(root)

list_stations = os.listdir()
list_stations[:] = [int(elt) for elt in list_stations]
list_stations = set(list_stations)

for station in list_stations:
	print("##################~~~"+str(station)+"~~~##################")
	path = root +"/"+str(station)
	os.chdir(path)

	saisons = [0,1,2,3]
	moments = [0,1,2,3]

	list_clusters = list()
	for saison in saisons:
		os.chdir(root+"/"+str(station)+"/saison/"+str(saison))
		if os.path.isfile(os.getcwd()+"/bikes_train.data"):
			data = open("bikes_train.data","r")
			data = fonctions.fic_to_floatlist(data)

			solutions = open("bikes_train.solution","r")
			solutions = fonctions.fic_to_floatlist2(solutions)

			new_len = len(data) - 1

			for moment in moments:
				print(str(station)+"-------->"+str(saison)+"------>"+str(moment))
				path = root+"/"+str(station)+"/saison/"+str(saison)+"/moment/"+str(moment)
				
				if not os.path.exists(path):
					os.makedirs(path)
				os.chdir(path)

				fic = open("bikes_train.data","w")
				sor = open("bikes_train.solution","w")
			
				for i, elt in enumerate(data):
					if elt[0] == moment:
						del elt[0]

						fic.write(fonctions.vector_toString(data[i]))
						sor.write(str(solutions[i])+"\n")