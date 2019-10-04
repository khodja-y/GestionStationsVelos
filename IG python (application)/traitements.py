#!/usr/bin/python
# -*-coding:utf-8 -*

#!/usr/bin/python3

import os
from fonctions import *
from operator import itemgetter

##########################################~~functions~~###################################################################

def distances_init(data,vect, k):
	dist = list()
	size = len(data)
	if size >=k:
		for i in range(0,k):
			temp = list()
			temp.append(i)
			temp.append(distance(data[i], vect))
			dist.append(temp)
	else:
		for i in range(0,size):
			temp = list()
			temp.append(i)
			temp.append(distance(data[i], vect))
			dist.append(temp)
	dist = sorted(dist,key= itemgetter(1))
	return dist

def positionne_dist(dist, index_data, vect_dist):
	temp = [index_data, dist]
	for i, elt in enumerate(vect_dist):
		if dist < elt[1] and i == 0:
			vect_dist.insert(0,temp)
			vect_dist.pop()
			break
		elif dist < elt[1] and dist > vect_dist[i-1][1]:
			vect_dist.insert(i,temp)
			vect_dist.pop()
			break
		else:
			pass

	return vect_dist

def getSorties(vect_dist, solution):
	for elt in vect_dist:
		ind_sol = elt[0]
		elt[1] = solution[ind_sol]
	return vect_dist

def calcul_sortie(vect_sorties):
	sorties = list()
	for elt in vect_sorties:
		cpt = 0
		for ech in vect_sorties:
			if elt[1]  == ech[1]:
				cpt +=1
		sorties.append([elt[1], cpt])
	sorties = sorted(sorties,key= itemgetter(1))
	sortie = sorties.pop()
	sortie = sortie[0]

	return sortie

##########################################~~ workspace ~~##########################################################################""

def knn(vect):
	#############~~ init ~~#########################################################
	k=35

	root = os.getcwd()
	station = int(vect[0])
	saison 	= int(vect[1])
	moment 	= int(vect[2])

	del vect[2]
	del vect[1]
	del vect[0]

	evident = open("evident","r")
	evident = fic_to_floatlist(evident)

	path = root + "/stations/" +str(station)+"/saison/"+str(saison)+"/moment/"+str(moment)
	fic = path + "/bikes_train.data"

	#############~~si la sortie est constante (connue)~~#############################
	ev = -1
	for i, elt in enumerate(evident):
		if elt[0] == station and elt[1] == saison and elt[2] == moment:
			nbr_velos = int(elt[3])
			ev = i
			break

	if ev != -1:
		pass

	#############~~ la sortie est dynamique~~########################################
	elif os.path.exists(fic):
		os.chdir(path)
		data = open("bikes_train.data","r")
		data = fic_to_floatlist3(data)

		solution = open("bikes_train.solution","r")
		solution = fic_to_floatlist2(solution)

		size_data = len(data)
		###########~~ calcul ~~######################################################
		distances = distances_init(data, vect, k)

		for j in range(k,size_data):
			dist = distance(vect, data[j])
			distances = positionne_dist(dist, j, distances)

		sorties = getSorties(distances, solution)

		nbr_velos = calcul_sortie(sorties)

	############~~ sinon le moment demandé n'existe pas dans l'architecture ~~#######
	else:
		nbr_velos = -1

	return nbr_velos