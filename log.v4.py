#python
# -*- coding: utf-8 -*-
#log.v4.py : afficher 

import operator
import collections
from typing import OrderedDict
import urllib.request
import json 

i = 0
valid_user = {}
invalid_user = {}
Ip = {}

text = open('fichier\\auth.V3.log', 'r')
localisation = open('localisations.js', 'w')

#erreur à gérer comme avant 

erreur = "Invalid user"
erreur_2 = "Failed password"
erreur_3 = "Failed password for invalid user"

# détecter si les différentes erreurs sont sur les lignes pour chaque ligne 

for line in text:
    mot = line.split(' ')
    
    if erreur in line:
        # Si le code remarque dans le fichier ou il y'a une ligne ou il y'a Invalid user alors l'adresse sera le 9eme mot 
        IPV4 = mot [9]

    elif erreur_3 in line:
        # Si le code remarque dans le fichier ou il y'a une ligne ou il y'a Failed password alors l'adresse sera le 12eme mot 
        IPV4 = mot [12] 
               
    elif erreur_2 in line:
        # Si le code remarque dans le fichier ou il y'a une ligne ou il y'a Failed password for invalid user alors l'adresse sera le 10eme mot 
        IPV4 = mot [10]
    
    
    
    else:
        continue
    
    if IPV4 in Ip.keys():
        Ip[IPV4] = Ip[IPV4] + 1
       
       
    else:
        Ip[IPV4] = 1
        

# Détécter si il y'a un type d'erreur en fonction de la ligne à chaque fois

    

i = 0
  
 # trier dictionnaire 
print("--------------------------------")
Ip = sorted(Ip.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(Ip)

localisation.write('var locations =[')

for key, valeur  in var.items():

#maintenant il faut récupérer la latitude et longitude, transférer ces valeurs dans le fichier localisation et les afficher sur une carte qu'on va générer
    
    
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])

    with urllib.request.urlopen("https://geolocation-db.com/json/" + cle) as url:
        data = json.loads(url.read().decode())
        
#gestion d'une erreur comme dans le numéro 2 et trois (Not Found) pour avoir tout les pays

    if data['latitude'] != 'Not found' or data['longitude'] != 'Not found':
        localisation.write('\n  ["{} ({} attaques)", {}, {}],'.format(cle, valeur, data['latitude'], data['longitude']))    


# on affiche alors l'adresse, avec la valeur de la latitude et de la longitude pour avoir sa position exacte sur notre superbe carte 
localisation.write('\n]')

print("--------------------------------")





#fermeture des deux fichier (fichier texte et fichier JavaScript)

text.close()
localisation.close()
