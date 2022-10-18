#!/bin/bash

# Vous allez maintenant voir les conditions, pour cela il vous faut réaliser un script qui
# affichera soit “Bonjour, je suis un script !” soit “Au revoir et bonne journée” selon
# l’argument passé.
# Le paramètre “Hello” devra afficher le message “Bonjour ......” et “Bye” devra afficher le
# message “Au revoir ......”
# Votre script devra se nommer hello_bye.sh et se lancera de cette façon :
# ./hello_bye.sh Bye


if [ $1 = "Hello" ]
then
echo "Bonjour, je suis un script !"

elif [ $1 = "Bye" ]
then
echo "Au revoir et bonne journée"

else
echo "l'argument doit être Hello ou Bye"
fi
