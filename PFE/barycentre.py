#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import os
import fonctions

root = os.getcwd()+"/stations"
os.chdir(root)

stations = os.listdir()
stations[:] = [int(elt) for elt in stations]
stations = set(stations)

saisons = [0,1,2,3]
moments = [0,1,2,3]

for station in stations:
	for saison in saisons:
		for moment in moments:
			path = root+"/"+ str(station) +"/saison/"+ str(saison) +"/moment/"+ str(moment)
			fic = path + "/bikes_train.solution"
			if os.path.exists(path) and os.path.exists(fic):
				os.chdir(path)

				data = open("bikes_train.data","r")
				data = fonctions.fic_to_floatlist3(data)

				solution = open("bikes_train.solution","r")
				solution = fonctions.fic_to_floatlist2(solution)

				vect_desc = open("vect_desc.data","w")

				list_solutions = set(solution)
				for elt in list_solutions:
					list_vect = list()
					for i, sol in enumerate(solution):
						if sol == elt:
							data[i].append(elt)
							list_vect.append(data[i])
					cc = fonctions.calcul_centre_de_classe(list_vect)
					vect_desc.write(fonctions.vector_toString(cc))