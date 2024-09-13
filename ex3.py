# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

Vitesse = float(input("Vitesse initiale (en m/s):"))
angle = float(input("Angle de lancement (en degrés):"))
import math
g= 9.8
Distance = ((Vitesse**2) * (math.sin(2*math.radians(angle))))/g
print(f"La distance maximale en x est de {Distance:.2f}m")

