# Job 11 : Traitement d’un fichier 1.0
# Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
# compte le nombre de noms de domaine.

file = open('C:\\Users\\Admin\\Documents\\GitHub\\Starter-2022\\mourad.aziz\\python\\domains.xml', 'r')
data = file.read()
occurrences = data.count("column name=\"domain\"")

print("Nombre d'occurrences de nom de domaine :", occurrences)