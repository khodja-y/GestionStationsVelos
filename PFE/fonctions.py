#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import os

#this function checks if the station exists
def station_existe(station): 
	os.chdir(os.getcwd()+"/stations")
	
	existe = False
	for dirname, dirnames, filenames in os.walk('.'):
		for filename in filenames:
			if(filename == (station+'.data')):
				existe = True

	
	return existe


#this function returns a float list by entering a file
def fic_to_floatlist(fic):
	fic1 = fic.read().split("\n")
	doc = [line.split(' ') for line in fic1]
	
	doc.pop() #removes the last element of the list which is EOF	
	for i, line in enumerate(doc):
		line[:] = [float(elt) for elt in line]
		line[0] = int(line[0])
		line[1] = int(line[1])
	
	return doc

#this function returns a float list by entering a file
def fic_to_floatlist2(fic):
	doc = fic.read().split("\n")
	
	doc.pop() #removes the last element of the list which is EOF	
	doc[:] = [int(elt) for elt in doc]
	
	return doc

#this function returns a float list by entering a file
def fic_to_floatlist3(fic):
	fic1 = fic.read().split("\n")
	doc = [line.split(' ') for line in fic1]
	
	doc.pop() #removes the last element of the list which is EOF	
	for i, line in enumerate(doc):
		line[:] = [float(elt) for elt in line]
	
	return doc

#count list id station
def get_id_stations(docu_list):
	#doc = fic_to_floatlist(fic)
	doc = docu_list

	x = list()

	for line in doc:
		x.append(line[1])

	x = set(x)

	return x

#counts the distance between two vectors
def distance(a,b):
	import math
	result = 0
	for i, elt_a in enumerate(a):
		result += ((b[i] - elt_a) ** 2)

	result = math.sqrt(result)
	return result


#cette fonction recupere l'indice du premier echantillon de chaque classe 
def echantillons(float_file):
	data = float_file
	
	found1 = False
	found2 = False
	found3 = False

	
	for i, line in enumerate(data):
		if line[0] < 11 and not found1 :
			ech1 = get_vector_by_pos(i)
			i1 = i
			found1 = True
		if 10 < line[0] < 31 and (not found2):
			ech2 = get_vector_by_pos(i)
			i2 = i
			found2 = True
		if line[0] > 30 and (not found3):
			ech3 = get_vector_by_pos(i)
			i3 = i
			found3 = True

		if found1 and  found2 and  found3:
			break


#	print (str(ech1))
#	print (str(ech2))
#	print (str(ech3))

	return (ech1,i1,ech2,i2,ech3,i3)

def vector_toString(vect):
	string = ""
	length = len(vect) - 1
	for i, elt in enumerate(vect):
		if i == length:
			string += str(elt)
		else:
			string += str(elt)+" "

	string += "\n"
	return string

def get_vector_by_pos(pos):
	data = open("n_bikes_train.data","r")
	data = fic_to_floatlist(data)

	for i, line in enumerate(data):
		if i == pos:
			break

#	line = [line.append(elt) for let in line]
#	line[:] = [float(elt) for elt in line]
	
#	print(str(line))
	return line

def calcul_centre_de_classe(file):
	data = file

	nbr_line = len(data)
	nbr_col = len(data[0])

	vect_sum = list()

	j = 0
	while j < nbr_col :
		i = 0
		somme = 0
		while i < nbr_line :
			somme += data[i][j]
			i += 1
		vect_sum.append(somme)
		j += 1

	vect_moy = [(elt/nbr_line) for elt in vect_sum]
	vect_moy[0] = int(vect_moy[0]) 
	vect_moy[1] = int(vect_moy[1]) 
	print(vect_moy)
	return vect_moy


#this is just here to test if the functions work well
if(__name__ == "__main__"):
#	x = input("num de please:\t")
#	if(station_existe(x)):
#		print("existe")
#	else:
#		print("existe ap")
#	print()

#	os.chdir()

#	data = open('bikes_train.data','r')
#	doc = fic_to_floatlist(data)
#	print(doc[1][1])
#	get_id_stations(data)

	a, b = [1,2,3], [4,5,6]

	print(distance(a,b))