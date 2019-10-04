#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import os
import fonctions
directory = os.getcwd()+"/stations"
os.chdir(directory)

list_stations = os.listdir()
list_stations[:] = [int(elt) for elt in list_stations]
list_stations = set(list_stations)

for station in list_stations:
	print("##################~~~"+str(station)+"~~~##################")
	os.chdir(directory+"/"+str(station))
	data = open("bikes_train.data","r")
	data = fonctions.fic_to_floatlist3(data)

	new_len = len(data[0]) - 1

	solutions = open("bikes_train.solution","r")
	solutions = fonctions.fic_to_floatlist2(solutions)

	saisons = [0,1,2,3]

	list_clusters = list()
	for saison in saisons:
		print(str(station)+"-------->"+str(saison))
		path = directory+"/"+str(station)+"/saison/"+str(saison)
		
		if not os.path.exists(path):
			os.makedirs(path)
		os.chdir(path)

		fic = open("bikes_train.data","w")
		sor = open("bikes_train.solution","w")
		
		for i, elt in enumerate(data):
			if elt[2] == saison and len(elt) != new_len:
				print("ici")
				del elt[2]
				fic.write(fonctions.vector_toString(elt))
				sor.write(str(solutions[i])+"\n")
