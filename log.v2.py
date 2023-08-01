#python
# -*- coding: utf-8 -*-
#exercice numero 2 : afficher les faux comptes et les vrais 

#importer les différentes fonctions que nous voulons utiliser
import operator
import collections
from typing import OrderedDict

i = 0
#définir des dictionnaires vide 
valid_user = {}
invalid_user = {}
Ip = {}
#ouverture et lecture du fichier auth.V2.log 
text = open('fichier\\auth.V2.log', 'r')

#création d'une erreur de type Invalid qui est présente dans notre fichier 
erreur = "invalid"


for line in text:
    mot = line.split(' ')
    #si la boucle trouve une erreur alors il va vouloir afficher notre valeur en comptant les cases, Invalid ++ 
    if erreur in line:
        utilisateur = mot [10]
        IPV4 = mot [12]
        if utilisateur in invalid_user.keys():
            invalid_user[utilisateur] = invalid_user[utilisateur] + 1
        else:
            invalid_user[utilisateur] = 1
    #Sinon faire le comptage normalement 
    else:
        utilisateur = mot [8]
        IPV4  = mot [10]
     
        if utilisateur in valid_user.keys():
            valid_user[utilisateur] = valid_user[utilisateur] + 1
        else:
            valid_user[utilisateur] = 1
    
    #retour a la ligne si il y'a la même adresses sinon l'ajouter 
    if IPV4 in Ip.keys():
        Ip[IPV4] = Ip[IPV4] + 1
       
    else:
        Ip[IPV4] = 1
        

    

    
    
#trier le dictionnaire 

invalid_user = sorted(invalid_user.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(invalid_user)


while i < 10:

#sortir les invalid user 
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])
    print ('{} : ({} fois)'.format(cle,valeur))



print("--------------------------------")

i = 0


# trier les utilisateurs qui sont valid 

valid_user = sorted(valid_user.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(valid_user)

while i < 10:

#sortir les valid users 
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])
    print ('{} : ({} fois)'.format(cle,valeur))



print("--------------------------------")

i = 0


#sortir les Ip que nous trouvons 

Ip = sorted(Ip.items(), key=operator.itemgetter(1),reverse=True)
var = collections.OrderedDict(Ip)

while i < 10:

#afficher à chaque fois les nouvelles clés et les nouvelles valeurs 
    i += 1 
    cle = (list(var.keys())[i-1])
    valeur = (list(var.values())[i-1])
    print ('{} : ({} fois)'.format(cle,valeur))

print("--------------------------------")

#fin (fermeture du fichier texte)

text.close()