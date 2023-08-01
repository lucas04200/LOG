#python
# -*- coding: utf-8 -*-
#exercice numero 1 : parcourir le fichier et constituer un tableau qui compte le nombre d'occurence de chaque user


#importer les fonctions operator, collections, et la fonction pour trier les dictionnaires
import operator
import collections
from typing import OrderedDict
i = 0
#dictionnaire vide log
log = {} 
#ouverture du fichier auth.V1.log et lecture du fichier 
text = open('fichier\\auth.V1.log', 'r')


#mettre en ligne chaque 10ème mots du  premier fichier.txt
for line in text:
    mot = line.split(' ')
    login = mot [10]

#retourner à la ligne à chaque fois 

    if login in log.keys():
        log[login] = log[login] + 1  
    else:
        log[login] = 1 

cpt = 0

#trier les valeurs du dictionnaire pour les mettres dans l'ordre décroissant
VALEUR = sorted(log.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(VALEUR)

# tant que la variable i est inférieur à dix valeurs alors répéter dix fois i et écrire les clés et les valeurs des utilisateurs
while i < 10:

# écrire chaque nouvelles clés et valeurs jusqu'à ce que i soit à 10
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])
    print ('{} : ({} fois)'.format(cle,valeur))
    

#fermer le fichier 
text.close()