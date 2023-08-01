#python
# -*- coding: utf-8 -*-
#log.v4.py : afficher 

import operator
import collections
from typing import OrderedDict
import urllib.request
import json 

#dictionnaire 

i = 0
valid_user = {}
invalid_user = {}
Ip = {}

# ouverture du fichier big.log, localisation et serie1.js on va ouvrir le serie2.js plus tard.
text = open('fichier\\auth.big.log', 'r')
localisation = open('highcharts\\localisations2.js', 'w')
serie1 = open('highcharts\\serie1.js', 'w')



erreur = "Invalid user"
erreur_2 = "Failed password"
erreur_3 = "Failed password for invalid user"

#si il y'a des erreurs alors prendre la bonne valeurs de position du mot 

for line in text:
    mot = line.split(' ')
     
    if erreur in line:
        IPV4 = mot [9]
        utilisateur = mot [7]
        # si l'erreur invalid user est detectée alors l'utilisateur et le 7eme mot et l'IPV4 est le 9 mot
        if utilisateur in invalid_user.keys():
            invalid_user[utilisateur] = invalid_user[utilisateur] + 1
        else:
            invalid_user[utilisateur] = 1
        # si l'utilisateur est un utilisateur invalid alors on rajoute un et si on l'a jamais eu avant, le rajouter.
    elif erreur_3 in line:
        IPV4 = mot [12] 
        # si l'erreur trois est détecté l'Ipv4 sera le 12eme mots            
    elif erreur_2 in line:
        IPV4 = mot [10]
        utilisateur = mot[8]
        # si l'erreur deux est détectée l'ipv4 sera le 10eme mot et l'utilisateur est le 8eme mot   
    
    else:
        continue # sinon continuer 
    
    if IPV4 in Ip.keys():
        Ip[IPV4] = Ip[IPV4] + 1
       # si l'ipv4 est déjà dans notre liste alors on l'ajoute à la au même utilisateur 
       
    else:
        Ip[IPV4] = 1
        # si on a jamais eu l'adresse IPV4 alors on l'ajoute à notre liste

    # nous voulons sortir tout d'abord les invalid_users 

print ('invalid_users') # j'écris des print pour vérifier les étapes pendant l'execution de notre script 

    # permet de faire le tri des 'invalid_users' 

invalid_user = sorted(invalid_user.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(invalid_user)


    # nous devons écrire le début du texte pour que le diagramme marche correctement


serie1.write("""Highcharts.chart('serie1',
{
        chart: {
            type: 'pie'
        },
		title: {
			text: 'Analyse de auth.log'
		},
		subtitle: {
			text: 'Users inconnu utilise pour des attaques SSH'
		},
        series: [{
            data: [ """)

j = 0 
    # nous voulons écrire les 13 premiers utilisateurs et après écrire les autres 
while j <= 13:
    j += 1 
    # écrire chaque clés et chaque valeurs pour les invalid_user
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])

  
    serie1.write('\n [ \'{}\' , {}], \n'.format(cle,valeur))

    
    #sortir les invalid user 
serie1.write("""\n]
\n }]
\n });
""")

    # fermeture du fichier 1
serie1.close()


print("End (invalid_users)")

    #trouver dans les lignes du big_log les utilisateurs valid avec les Ip correspondante


    
    # il faut maintenant s'occuper des valid_user 
print('valid_users')

    #ouverture du fichier series2.js
serie2 = open('highcharts\\serie2.js', 'w')

    #l'utilisateur se retrouve sur le 6 mot
for line in text:
    mot = line.split(' ')
    utilisateur = mot [6]

    #triage du dictionnaire valid_user 
valid_user = sorted(valid_user.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(valid_user)

    #écrire dans le fichier serie2.js pour avoir le resultat sous forme de diagramme 
serie2.write("""Highcharts.chart('serie2',
{
        chart: {
            type: 'pie'
        },
		title: {
			text: 'Analyse de auth.log'
		},
		subtitle: {
			text: 'Users connu utilise pour des attaques SSH'
		},
        series: [{
            data: [ """)


for key, valeur  in var.items():
    #sortir les valid user 
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])

    
serie2.write('[ \'{}\' , {}], \n'.format(cle,valeur)) # écrire la clé et la valeur 

    # écrire dans la fin du fichier pour pouvoir écrire correctement dans le diagramme 
serie2.write("""\n]  
\n }]
\n });
""")

i = 0
 
print("end (valid_users)")


    # fermeture du fichier2.py 

serie2.close()

print('ip')

    # trier les Ip ordre décroissant
Ip = sorted(Ip.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(Ip)

    # écriture du début du fichier 

localisation.write('var locations =[') # début d'écriture sur notre fichier localisation2.js
API = '3a2b5be0-75a0-11ec-acd1-89ce18e6dbfe' # ma clé API 
URL = "https://geolocation-db.com/json/" # URL de notre site de géolocalisation d'ip qu'on a exploser XD
ruz = 0
for key, valeur  in var.items():
    
    
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])
    # refaire comme dans le log.v4.py, afficher l'ip et enfin la latitude et longtitude pour l'afficher encore sur notre superbe carte 
    with urllib.request.urlopen("{}/{}/{}".format(URL,API,cle)) as url:
        data = json.loads(url.read().decode())
        

    # prendre l'ip la latitude et la longitude 

    if data['latitude'] != 'Not found' or data['longitude'] != 'Not found': # on traite ce fichier avec une erreur not found pour éviter de faire planter le python
        localisation.write('\n  ["{} ({} attaques)", {}, {}],'.format(cle, valeur, data['latitude'], data['longitude']))     # on affiche l'ip et le reste pour la carte 


# j'écris une ] à la fin pour pouvoir avoir le fichier localisation deux qui marche correctement 
   
localisation.write('\n]')


# je print end (ip) pour vérifier ou en est l'execution du fichier car c'est long :)

print("end (ip)")




# fermeture du fichier Big.log et du fichier localisation.js
text.close()
localisation.close()

