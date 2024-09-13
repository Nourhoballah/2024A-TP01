# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

import math

water_quantity = int(input("Quelle quantité d'eau faut-il assainir ? ") )
x=water_quantity

filtreNecessaire= (x*1)/5
lampeNecessaire= (x*3)/5
chloreNecessaire=(x*0.5)/5

print("Voici les matériaux requis pour l'assainissement de", x,   "L d'eau :" ,filtreNecessaire ,"filtres, ",lampeNecessaire, "lampes UV ""et" ,chloreNecessaire, "kg de chlore" )
#print("la quantité nécessaire de filtre est de " filtreNecessaire)
#print("la quantité nécessaire de filtre est de " lampeNecessaire)
#print("la quantité nécessaire de filtre est de " chloreNecessaire)


