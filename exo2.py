# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
charge = int(input("Entrez le niveau de charge de la batterie: "))
# Vérifiez si le niveau de charge est valide
if charge>100 or charge<0:
    print("Niveau de charge invalide")
    exit()
# Arrondir le pourcentage à la dizaine la plus proche
charge_arrondi=(round(charge/10))*10
# Calculer le nombre de barres
nb_barres=charge_arrondi//10
print(nb_barres)
# Afficher la représentation graphique de la charge de la batterie
print("["+ "❚"*int(nb_barres)+" "*int(10-nb_barres)+"]")
print(charge,"%")
# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%