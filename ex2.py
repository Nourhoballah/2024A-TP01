# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

import math

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? " ) )
x = water_quantity

filtreNecessaire= math.ceil((x*1)/5)
lampeNecessaire= math.ceil((x*3)/5)
chloreNecessaire=(x*0.5)/5

print(f"Voici les éléments requis pour assainir {x:.1f}L d'eau:\n        ")
print(f"\t- Filtre(s) : {filtreNecessaire}" )
print(f"\t- Lampe(s) UV : {lampeNecessaire}")
print(f"\t- Chlore : {chloreNecessaire:.1f}kg")

