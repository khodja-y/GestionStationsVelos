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

root = os.getcwd()
evident = open("evident","r")
evident = fic_to_floatlist(evident)

estime = open("estime2","w")

taux_file = open("taux","w")

#for k in range(1,101):
	#print("###################################################################")
	#print("k = "+str(k))

os.chdir(root+"/stations")

list_stations = os.listdir()
list_stations[:] = [int(elt) for elt in list_stations]
list_stations = set(list_stations)

list_saisons = [0,1,2,3]
list_moments = [0,1,2,3]

cpt_corrects = 0 #compteur de résultats corrects en k-means
erreur_deficit = list()
erreur_surestime = list()
sup5 = 0

nbr_test = 0


k = int(input("donnez k: "))
for station in list_stations:
	for saison in list_saisons:
		for moment in list_moments:
			path = root + "/stations/" +str(station)+"/saison/"+str(saison)+"/moment/"+str(moment)
			fic = path + "/bikes_train.data"


			#############~~si la sortie est constante (connue)~~##########################
			ev = -1
			for i, elt in enumerate(evident):
				if elt[0] == station and elt[1] == saison and elt[2] == moment:
					nbr_velos = elt[3]
					ev = i
					break

			#############~~sinon la sortie est dynamique~~################################
			if os.path.isfile(fic) and ev ==-1:

				os.chdir(path)
				data = open("bikes_train.data","r")
				data = fic_to_floatlist3(data)

				solution = open("bikes_train.solution","r")
				solution = fic_to_floatlist2(solution)
				size = len(data)

				test_data = list()
				test_solution = list() 
				start = int(size/2 + 1)
				
				###########~~separation de train(data) et test ~~#########################
				for i in range(start,size): 
						test_data.append(data[i])
						test_solution.append(solution[i])
				
				nbr_test += len(test_data)
				
				for i in range(start,size): 
						del data[start]
						del solution[start]
				
				###########~~test ~~######################################################
				for i, elt in enumerate(test_data):
					distances = distances_init(data, elt, k)
					size_test = len(test_data)
					size_train = len(data)

					for j in range(k,size_train):
						dist = distance(elt, data[j])
						distances = positionne_dist(dist, j, distances)

					sorties = getSorties(distances, solution)

					nbr_velos = calcul_sortie(sorties)
					#print(nbr_velos)
					erreur = nbr_velos - test_solution[i]
					
					#estime.write(str(nbr_velos)+" "+str(test_solution[i])+"\n")

					if test_solution[i] > 20:
						accepte_erreur = int(test_solution[i] / 10) + 1
					else:
						accepte_erreur = 3

					if abs(erreur) <= accepte_erreur:
						cpt_corrects += 1
					elif erreur < 0:
						erreur_deficit.append(abs(erreur))
					else:
						erreur_surestime.append(erreur)

taux = cpt_corrects/ nbr_test * 100

print ("\néchantillons corrects: "+str(cpt_corrects))
print ("\tdéficit\t\tmax déficite\tmin déficite")
print ("\t"+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if len(erreur_deficit) != 0 :
	print ("\t"+str(len(erreur_deficit))+"\t\t"+str(max(erreur_deficit))+"\t\t"+str(min(erreur_deficit)))
else :
	print ("\t"+str(len(erreur_deficit))+"\t")
print ("\tdéficit moyen: "+str(sum(erreur_deficit)/len(erreur_deficit)) )

print ("\n\tsurestimé\tmax surestimé\tmin surestimé")
print ("\t"+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if len(erreur_surestime) != 0:
	print("\t"+str(len(erreur_surestime))+"\t\t"+str(max(erreur_surestime))+"\t\t"+str(min(erreur_surestime)))
else :
	print("\t"+str(len(erreur_surestime))+"\t")
print("\tsurestimation moyenne: "+str(sum(erreur_surestime)/len(erreur_surestime)) )

print("\nle taux de bonnes prédictions est de: "+str(taux))

#taux_file.write(str(k)+" "+str(taux)+"\n")