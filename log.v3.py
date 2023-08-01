#python
# -*- coding: utf-8 -*-
#exercice log.v3.py : afficher les adresses IPV4 avec leurs localisations 

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
#cette fois il est question de trois erreurs donc je définis trois nouvelles variables pour pouvoir faire mes boucles tranquillement 
erreur = "Invalid user"
erreur_2 = "Failed password"
erreur_3 = "Failed password for invalid user"

#Boucle pour définir la position de notre valeur en fonction de l'erreur ou s'il y'en a pas tout simplement 
for line in text:
    mot = line.split(' ')
    
    if erreur in line:
        IPV4 = mot [9]

    elif erreur_3 in line:
        IPV4 = mot [12] 
               
    elif erreur_2 in line:
        IPV4 = mot [10]
   
# si une erreur des trois est détéctées alors trouver dans la ligne la bonne place de notre Ip         
    
    else:
        continue

   #addition ou nouvelle valeur  
    if IPV4 in Ip.keys():
        Ip[IPV4] = Ip[IPV4] + 1
       
       
    else:
        Ip[IPV4] = 1
        



    

i = 0
  
 
print("--------------------------------")
Ip = sorted(Ip.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(Ip)

#trier le dictionnaire par ordre décroissant 

for ip in Ip: 
    
    
    
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])
# cette fois il faut récupérer le nombre d'attaque qu'une Ip nous a infliger sur le site en dessous et afficher les lieux des attaquants
    with urllib.request.urlopen("https://geolocation-db.com/json/" + cle) as url:
        data = json.loads(url.read().decode())
        a= data['country_name']
# afficher les Ip, la localisation et enfin le nombre de fois ou cette Ip est ressortie

    print ('{} : from {}     ({} fois) '.format(cle,a,valeur))

print("--------------------------------")





#end 

text.close()