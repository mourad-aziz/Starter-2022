# Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie du célèbre
# jeu le pendu dans le terminal.
# Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
# souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi (exemple
# débutant 10, intermédiaire 7, expert 4). Vous êtes libres de choisir le nombre de vies par
# niveau.
# Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible
# ici, et afficher :
# -
# Le nombre de vies restantes au joueur
# -
# Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
# En expert, la liste n’apparaîtra pas)
# -
# Des “_” pour remplacer les lettres non trouvées
# -
# Les lettres proposées qui se trouvent dans le mot
# La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.

from random import choice
#from unidecode import unidecode

#
option = 1 
while option ==1:
    niveau = int(input('Entre niveau (1)Débutant 10 essais, (2)Intermédiaire 7 essais, (3)Expert 4 essais : '))

    if niveau == 1: 
        vie = 10
        option = 0 
    elif niveau == 2:
        vie = 7
        option = 0 
    elif niveau == 3:
        vie = 4
        option = 0 
    else :
        print('option possible 1 pour debutant, 2 pour intermediaire, 3 pour expert : ')
        option = 1
    



# un mot au hasard

def word():
    f = open('C:\\Users\\Admin\\Documents\\GitHub\\Starter-2022\\mourad.aziz\\python-projects\\dico_france.txt', 'r')# , encoding = 'utf8')
    contenu = f.readlines()
    #return choice(contenu).Myuper().replace('\n','')
    print(choice(contenu))
    return choice(contenu).replace('\n','')

# remplacement par des underscores

def underscore(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]

# saisie d'une lettre

def saisie():
    lettre = input('Entrez une lettre : ')
    if len( lettre ) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    else:
        return lettre.upper()
    

# programme 

lettres_deja_proposees = []
mot_a_deviner = word()

fromChar = "ÀÁÂÃÄàáâãäªÈÉÊËèéêëÍÌÎÏíìîïÒÓÔÕÖòóôõöºÙÚÛÜùúûüÑñÇç§³²¹"
toChar   = "AAAAAaaaaaAEEEEeeeeIIIIiiiiOOOOOoooooOUUUUuuuuNnCcS321"

S = mot_a_deviner
R = ""                                 # start result with an empty string
for c in S:                            # go through characters
    p = fromChar.find(c)               # find position of accented character
    R += toChar[p] if p>=0 else c      # use replacement or original character

print( 'sans accent : ' ,R)

mot_a_deviner = S

print( 'mot a dev : ' ,S)





affichage = underscore( mot_a_deviner )
print(mot_a_deviner)
print( 'Mot à deviner : ' , affichage )
nb_erreurs = 0

while '_' in affichage and nb_erreurs < vie:
    lettre = saisie()
    if lettre not in lettres_deja_proposees:
        lettres_deja_proposees += [ lettre ]
        
    if lettre not in R:
        nb_erreurs += 1
    #if niveau != 3:        
        affichage = underscore( mot_a_deviner , lettres_deja_proposees )
    #else:
        #affichage = underscore( mot_a_deviner )
    print( '\nMot à deviner : ' , affichage , ' '*15 , 'Nombre d\'erreurs restantes :' , vie-nb_erreurs )

