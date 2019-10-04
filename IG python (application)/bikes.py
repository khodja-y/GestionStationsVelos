#!/usr/bin/python
# -*-coding:utf-8 -*

from tkinter import *
from tkinter import ttk
import tkinter as tk

from traitements import *

#########################~~fonctions~~##################################################################################
def switch_saisons(saison):
	saisons = {
		"Printemps":0,
		"Eté":1,
		"Automne":2,
		"Hiver":3
	}
	return saisons.get(saison,saison)

def switch_moments(moment):
	moments = {
		"Début de journée":0,
		"Matin":1,
		"Aprés midi":2,
		"Soir":3
	}
	return moments.get(moment,moment)


def toVect(*param):
	liste = list()
	for i, elt in enumerate(param):
		if elt == "":
			elt = 0

		if i == 1:
			elt = switch_saisons(elt)
		elif i == 2:
			elt = switch_moments(elt)
		
		liste.append(elt)

	liste[:] = [float(elt) for elt in liste]
	traitement(liste)


def traitement(vect):
	frame = tk.Toplevel()
	frame.title("Résultat")
	frame.geometry("250x100")
	frame.configure(background = "white")
	#frame.geometry("250x200")
	nbr_velos = knn(vect) + 3
	if nbr_velos != -1:
		tk.Label(frame, bg="white",text="Veuillez prévoir: \n"+str(nbr_velos)+" vélo(s)").pack()
	else:
		tk.Label(frame, bg="white", text="Le moment que vous demandez \nn'est pas indexé dans notre \nbase de données.\n").pack()




##########################~~fenêtre principale~~#########################################################################

main = Tk()
main.title("Gestion de stations de vélos")
main.configure(background = "white")

hello = Label(main, bg="white", text="Bienvenue,\nVeuillez Compléter les informations demandées\n", justify="center").grid(columnspan = "3")


#création des labels
id_label 	 	= Label(main, bg="white", text="ID Station:",justify="center").grid(row = 1, sticky=N+S+E+W)

saison_label 	= Label(main, bg="white", text="Saison",justify="center").grid(row = 2, sticky=N+S+E+W)

moment_label 	= Label(main, bg="white", text="Moment de la journée:",justify="center").grid(row = 3, sticky=N+S+E+W)

temp_label 	 	= Label(main, bg="white", text="Temperature en Fahrenheit:",justify="center").grid(row = 4, sticky=N+S+E+W)

hum_label 	 	= Label(main, bg="white", text="Taux d'humidité(%):",justify="center").grid(row = 5, sticky=N+S+E+W)

vent_label 	 	= Label(main, bg="white", text="Vitesse du Vent(km/h):",justify="center").grid(row = 6, sticky=N+S+E+W)

prec_label 	 	= Label(main, bg="white", text="Précipitations(%):",justify="center").grid(row = 7, sticky=N+S+E+W)

duration_label 	= Label(main, bg="white", text="Duration:",justify="center").grid(row = 8, sticky=N+S+E+W)


###########~~création des entrées
id_str 	 = StringVar()
id_entry = Entry(main, textvariable = id_str).grid(row=1,column=2, sticky=N+S+E+W)

saison_str = StringVar()
sais_combo = ttk.Combobox(main, textvariable = saison_str)
sais_combo['values']= ('Printemps','Eté','Automne','Hiver')
sais_combo.grid(row = 2, column=2, sticky=N+S+E+W)

moment_str = StringVar()
moment_combo = ttk.Combobox(main, textvariable = moment_str)
moment_combo['values']= ('Début de journée','Matin','Aprés midi','Soir')
moment_combo.grid(row = 3, column=2, sticky=N+S+E+W)

temp_str = StringVar()
temp_entry = Entry(main, textvariable = temp_str).grid(row=4,column=2, sticky=N+S+E+W)

hum_str = StringVar()
hum_entry = Entry(main, textvariable = hum_str).grid(row=5,column=2, sticky=N+S+E+W)

vent_str = StringVar()
vent_entry = Entry(main, textvariable = vent_str).grid(row=6,column=2, sticky=N+S+E+W)

prec_str = StringVar()
prec_entry = Entry(main, textvariable = prec_str).grid(row=7,column=2, sticky=N+S+E+W)

duration_str = StringVar()
duration_entry = Entry(main, textvariable = duration_str).grid(row=8,column=2, sticky=N+E+W)

#bouton de validation des entrées	
validate = Button(main, text="Valider", command = lambda:toVect(id_str.get() ,saison_str.get(),moment_str.get(),duration_str.get(),temp_str.get(),hum_str.get(),vent_str.get(),prec_str.get()) ).grid(column=1)


main.mainloop()