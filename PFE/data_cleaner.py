#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import os
import fonctions

print(os.getcwd())
new = open("n_bikes_train.data","w")
data = open("bikes_train.data","r")
sor = open("bikes_train.solution","r")

sor = fonctions.fic_to_floatlist2(sor)

data = fonctions.fic_to_floatlist(data)

str_fic = ""
for i, line in enumerate(data):
	line[0] = int(line[0])
	line[1] = int(line[1])
	
	del line[9] #vent
	del line[7] #visibilité
	del line[2] #date
	str_fic += fonctions.vector_toString(line) 

print(str_fic)
new.write(str_fic)
new.close()