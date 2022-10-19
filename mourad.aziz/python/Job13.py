# Job 13  Traitement d’un fichier 3.0
# Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre
# entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
# nombre de mots de la taille renseignée qui s’y trouvent.


user_input = input("Taille des mots recherché ? : ")
#msg = "Bonjour"
#print(msg , user_input)

words = open('C:\\Users\\Admin\\Documents\\GitHub\\Starter-2022\\mourad.aziz\\python\\data.txt', 'r').read().split()
# data = file.read()
# words = data.split()

print('Nombre de mots total :', len(words))


count = 0
for word in words:
    if len(word) == user_input:
        count += 1

print('Nombre de mots de taille :', count)    