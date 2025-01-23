secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees = secondes // 31536000
# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
semaines = (secondes % 31536000) // 604800
# TODO: Assigner à la variable "jours" le nombre de jours restants
jours = (secondes % 31536000) % 604800 // 86400    
# TODO: Assigner à la variable "heures" le nombre d'heures restantes
heures = (secondes % 31536000) % 604800 % 86400 // 3600
# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
minutes = (secondes % 31536000) % 604800 % 86400 % 3600 // 60
# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
secondes = (secondes % 31536000) % 604800 % 86400 % 3600 % 60   
# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
# Exemple: print(annees, semaines, jours, heures, minutes, secondes)
print(annees, semaines, jours, heures, minutes, secondes)