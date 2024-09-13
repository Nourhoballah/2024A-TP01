# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Quelle est le Pourcentage de la batterie : "))

if battery_level > 100 or battery_level < 0:
    print("Le pourcentage de la batterie doit être compris entre 0 et 100.")
else:
    if battery_level >= 50:
        distance = battery_level * 2
    elif battery_level >= 25:
        distance = battery_level * 1.5
    elif battery_level >= 10:
        distance = battery_level * 1.2
    elif battery_level >= 5:
        distance = battery_level * 0.8
    else:
        distance = battery_level * 0.5

    print(f"L'autonomie estimée est de {distance} Km.")
          
