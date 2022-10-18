# Job 10 : Ecriture et lecture de fichier
# Écrire un programme job10.py qui demande à l’utilisateur d’entrer un texte. Le
# programme devra récupérer ce texte, et l’écrire dans un fichier “output.txt”.
# Écrire un programme qui lit le contenu de fichier “output.txt”, et qui l’écrit dans le
# terminal.

user_input = input("Entrer un texte ? : ")

f = open('C:\\Users\\Admin\\Documents\\GitHub\\Starter-2022\\mourad.aziz\\python\\output.txt', 'w')
f.write(user_input)
f.close()


