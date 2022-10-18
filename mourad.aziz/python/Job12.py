# Job 12 : Traitement d’un fichier 2.0
# Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
# le nombre de mots (sans caractère spéciaux) qui s’y trouvent.

file = open('C:\\Users\\Admin\\Documents\\GitHub\\Starter-2022\\mourad.aziz\\python\\data.txt', 'r')
data = file.read()
words = data.split()

print('Nombre de mots dans le fichier :', len(words))