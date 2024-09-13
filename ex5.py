#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

"""
Afin de faciliter le suivi et le calcul des médailles gagnées par pays, le comité vous demande de créer un script permettant de traiter la chaîne de caractères suivante: `GBBSBG`.  
- `G` signifie une médaille d'or
- `S` signifie une médaille d'argent
- `B` signifie une médaille de bronze

Consignes: 
- Demander la chaîne de caractères représentant le résultat d'un pays
- Afficher le nombre de médailles de ce pays
- Si un caractère inattendu se glisse dans la chaîne, veuillez afficher une erreur
#.1

Exemple: 

![Exemple gif ex5](./assets/ex5.gif)

| Sorties | Entrées |
|:-|:-|
| Résultat du pays: | GBBSBG |
| Médailles:<br>- Or: 2<br>- Argent: 1<br>- Bronze: 2 |


| Sorties | Entrées |
|:-|:-|
| Résultat du pays: | Ceci est une chaîne invalide |
| Veuillez entrer une chaîne valide. |

AGSB        GSB
"""
Pays=input("Quel est votre pays?")
codeMedaille=input("Quel est le résultat de votre pays? ")
MEDAL_TYPE = {"G","B","S"}

Gold=0
Silver = 0
Bronze = 0
for x in codeMedaille:
     if x not in MEDAL_TYPE:
           print("Ceci est une chaîne invalide | Veuillez entrer une chaîne valide.") 
           break 
else:  
     for x in codeMedaille:
          if x=="G":
             Gold+=1
          elif x=="S":
                 Silver+=1
          elif x == "B":
                      Bronze+=1
     print(f"Results: {Gold}gold medals, {Silver}silver medals, {Bronze}bronze medals")
     

                  
                
