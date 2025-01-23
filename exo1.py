# Demander le nom complet de l'utilisateur
nom = input("Veuillez entrer votre nom complet : ")

# Demander l'âge de l'utilisateur
âge = input("Veuillez entrer votre âge : ")

# Définir l'année actuelle
annee_actuelle = 2025
# Calculer l'année de naissance
annee_naissance = annee_actuelle - int(âge)
# Afficher un message de bienvenue avec le nom complet
print(f"Bonjour {nom}")
print(f"Vous êtes né(e) en {annee_naissance}")
# Afficher l'année de naissance
