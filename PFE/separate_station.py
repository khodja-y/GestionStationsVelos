#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import os
import fonctions

os.chdir(os.getcwd())
print(os.getcwd())

data = open("n_bikes_train.data","r")
sol = open("bikes_train.solution","r")
data = fonctions.fic_to_floatlist(data)
sol = fonctions.fic_to_floatlist2(sol)

id_stations = fonctions.get_id_stations(data)

#print(id_stations)

new_len = len(data[0]) - 1

for station in id_stations:
	print(int(station))

	directory = "stations/"+str(int(station))

	if not os.path.exists(directory):
		os.makedirs(directory)

	sortie = open(directory+"/bikes_train.data","w")
	sortie_sol = open(directory+"/bikes_train.solution","w")
	str_fic = ""
	str_sol = ""

	for i, donnee in enumerate(data):
		if(donnee[1] == station) and len(donnee) != new_len:
			del donnee[1]
			str_fic += fonctions.vector_toString(donnee)
			str_sol += str(sol[i])+"\n"
			
	sortie.write(str_fic)
	sortie_sol.write(str_sol)
	sortie.close()

