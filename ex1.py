# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ? ")
date = input("Date du record ? ")
discipline= input("Dans quelle discipline ? ")
Categorie = input("Dans une catégorie spécifique ? ")
Record = input("Quel est le record ? ")
espace= "  "

print("\nNouveau Record:")
print("--------------------")
print(f"{date} - {discipline} - {Categorie}:" )
print(f"\t{athlete} ({country}) - {Record}")
