#!/usr/bin/python3

from fonctions import fic_to_floatlist
from fonctions import fic_to_floatlist3
from os import chdir
from os import getcwd
root = getcwd()+"/stations/"

evident = open("evident","r")
evident = fic_to_floatlist(evident)

cpt = 0

for elt in evident:
	chdir(root + str(elt[0]) + "/saison/" + str(elt[1]) + "/moment/" + str( int(elt[2])) )
	data = open("bikes_train.data","r")
	data = fic_to_floatlist3(data)
	print(str(elt[0])+" "+str(elt[1])+" "+ str(elt[2]) + " " +  str(len(data)) + " "+str(elt[3]))

	cpt += len(data)

print(cpt)