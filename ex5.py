#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.


Pays=input("Pays concerné ? ")
codeMedaille=input("Chaine représentant les médailles ? ")
MEDAL_TYPE = {"G","B","S"}

Gold=0
Silver = 0
Bronze = 0
for x in codeMedaille:
     if x not in MEDAL_TYPE:
           print("Ceci est une chaine invalide.") 
           break 
else:  
     for x in codeMedaille:
          if x=="G":
             Gold+=1
          elif x=="S":
                 Silver+=1
          elif x == "B":
                      Bronze+=1
     print(f"{Pays}:\n- {Gold} Or\n- {Silver} Argent\n- {Bronze} Bronze")
     

                  
                
