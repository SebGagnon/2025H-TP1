import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
# Demander la vitesse initiale de la boule
v0 = input("Vitesse initiale (en m/s): ")
# Demander l'angle de lancement
Theta = input("Angle de lancer (en degrés): ")  
# Convertir l'angle en radians
theta = math.radians(float(Theta))  
# Calculer la distance maximale en x
distance = (float(v0)**2)*math.sin(2*theta)/g   
# Afficher la distance maximale arrondie à 2 chiffres après la virgule
print(f"Distance parcourue: {distance:.2f}m")
# Exemple:
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m
