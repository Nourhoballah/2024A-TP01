# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input('Pourcentage de batterie ?'))

if battery_level > 100 or battery_level <= 0:
    print("Pourcentage de batterie ?")
else:
    distance = 0

    print(f"{distance} km.")
          
