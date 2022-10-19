# Job 22 : Chaîne de caractères
# Créer un programme job22.py. Il devra prendre un premier input qui sera une chaine de
# caractère, puis un deuxième. Si le deuxième input est :
# -
# “upper” : une fonction “myUper” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en majuscule.
# -
# “lower” : une fonction “myLower” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en minuscule.
# -
# “title” : une fonction “myTitle” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne avec une majuscule
# au début de chaque mot.
# -
# “clean” : une fonction “myClean” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en enlevant tous les
# espaces inutiles (en début et en fin de chaine de caractère, et les doubles
# espaces).
# Aucune fonction system n’est autorisée. Vous pouvez cependant les tester afin d’étudier
# leur fonctionnement.
# A la fin de votre programme, la chaine de caractère retournée par la fonction devra être
# affichée sur le terminal.


# chaine_caractere= input ("saisissez une chaine de caractere")



def myUper(str_data):
    result = ''
    for char in str_data:
        if ord(char) >= 97 and ord(char) <= 122 :
            result += chr(ord(char) - 32)
        else:
            result += chr(ord(char))
    print(result)            
    return result

    
#print(myUper('abcdefggijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ'))

def myLower(str_data):
    result = ''
    for char in str_data:
        if ord(char) >= 65 and ord(char) <= 90 :
            result += chr(ord(char) + 32)
        else:
            result += chr(ord(char)) 
    print(result)            
    return result
#print(myLower('abcdefggijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ'))

# def myTitle(str_data):

# print(myTitle('abcdef ABCDEF abCDef'))


# def myClean()

str_data= input ("saisir une chaine de caractere: ")
option= input ("saisir une fonction: upper, lower, title, clean: ")

if option == 'upper':
    print(myUper(str_data))
elif option == 'lower':
    print(myLower(str_data))
elif option == 'title':
    print(myTitle(str_data))
elif option == 'clean':
    print(myClean(str_data))
else: 
    print("option possible upper, lower, title, ou clean: ")
