# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
charge = int(input("Entrez le niveau de charge actuel de la batterie : "))
# Vérifiez si le niveau de charge est valide
if charge>100 or charge<0:
    print("Erreur : niveau de charge invalide.")
else:
    # Arrondir le pourcentage à la dizaine la plus proche
    charge_arrondi=(round(charge/10))*10
    # Calculer le nombre de barres
    nb_barres=charge_arrondi//10
    # Afficher la représentation graphique de la charge de la batterie
    print("["+ "❚"*int(nb_barres)+" "*int(10-nb_barres)+"]")
    print(str(charge)+"%")

