#!/usr/bin/python3.4
# -*-coding:utf-8 -*

from math import fabs
import os
import fonctions

root = os.getcwd()

ev = open("evident","r")
ev = fonctions.fic_to_floatlist(ev)
for line in ev:
	line[:] = [int(elt) for elt in line]

data = open("bikes_train.data","r")
data = fonctions.fic_to_floatlist(data)

solution = open("bikes_train.solution","r")
solution = fonctions.fic_to_floatlist2(solution)

estime = open("estime","w")


cpt_correct = 0 #compteur de resultats corrects
cpt_kmeans = 0#compteur de valeurs calculées avec les k-means
erreur_deficit = list()
erreur_surestime = list()

###########################################~~recuperation du vecteur a traiter~~############################################

#vect = input("Entrez un vecteur:\n").split(" ")
#vect[:] = [float(elt) for elt in vect]
#print(vect)

for i, line in enumerate(data):
	vect = line

	mo = int(vect[0])
	stat = int(vect[1])
	sais = int(vect[4])

	######################################~~suppression des donnees superflues~~######################################

	del vect[9] #nuage
	del vect[7] #visibilité
	del vect[4] #saison
	del vect[2] #date
	del vect[1] #station
	del vect[0] #moment

	######################################~~verifier si la sortie est évidente~~######################################
	
	pos_ev = -1
	for j, line1 in enumerate(ev):
		if stat == line1[0] and sais == line1[1] and mo == line1[2]:
			pos_ev = j
			sortie = line1[3]
			break

	if pos_ev != -1:
		pass
	
	#####################################~~recherche de la valeur en k-means~~#######################################
	
	else:
		path = root+"/stations/"+ str(stat) +"/saison/"+str(sais)+"/moment/"+str(mo)
		fic = path + "/vect_desc.data"
		if os.path.exists(path) and os.path.isfile(fic):
			os.chdir(path)

			vect_desc_list = open("vect_desc.data","r")
			vect_desc_list = fonctions.fic_to_floatlist3(vect_desc_list)

			Min = fonctions.distance(vect, vect_desc_list[0])
			i_min = 0

			for j, vect_desc in enumerate(vect_desc_list):

				dist = fonctions.distance(vect, vect_desc)

				if dist < Min:
					Min = dist
					i_min = j

			sortie = int(vect_desc_list[i_min][5])
			
	#estime.write(str(sortie)+" "+str(solution[i])+"\n")

	if solution[i] > 20:
		accepte_erreur = int(solution[i] / 10) + 1
	else:
		accepte_erreur = 3

	erreur = sortie - solution[i]

	if abs(erreur) <= accepte_erreur:
		cpt_correct += 1
	elif erreur < 0:
		erreur_deficit.append(abs(erreur))
	else:
		erreur_surestime.append(erreur)

	cpt_kmeans += 1

taux = cpt_correct / cpt_kmeans * 100

##################################~~ Affichage ~~#################################################################

print ("échantillons corrects: "+str(cpt_correct))
print ("\tdéficit\tmax déficite\tmin déficite")
print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if len(erreur_deficit) != 0 :
	print("\t"+str(len(erreur_deficit))+"\t\t"+str(max(erreur_deficit))+"\t\t"+str(min(erreur_deficit)))
else :
	print("\t"+str(len(erreur_deficit))+"\t")
print ("\tdéficit moyen: "+str(sum(erreur_deficit)/len(erreur_deficit)) )

print ("\n\tsurestimé\tmax surestimé\tmin surestimé")
print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if len(erreur_surestime) != 0:
	print("\t"+str(len(erreur_surestime))+"\t\t"+str(max(erreur_surestime))+"\t\t"+str(min(erreur_surestime)))
else :
	print("\t"+str(len(erreur_surestime))+"\t")
print("\tsurestimation moyenne: "+str(sum(erreur_surestime)/len(erreur_surestime)) )

print("\nle taux de bonnes prédictions est de: "+str(taux)+"%")


#	error.write(str(stat)+"-"+str(sais)+"-"+str(mo)+": " + str(sortie)+"---<+>---"+str(solution[i])+"---<+>---"+str(erreur) + "\n")
#	print("L'erreur est de:\t" + str(erreur))
#	if erreur <= 3:
#		print("###############################################")
#		fic_propre.write(fonctions.vector_toString(vect_propre))
#		cpt += 1