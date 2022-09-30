#!/bin/bash

# Pour ce job, votre script devra créer un fichier dans le répertoire courant qui prendra le
# nom passé en premier argument. Il devra prendre en deuxième argument le nom d’un
# fichier dont il se servira pour remplir celui que vous venez de créer.
# Pour réaliser ce job, vous devrez utiliser obligatoirement les redirections.
# Votre script se nommera argument.sh et se lancera de la manière suivante :
# ./argument.sh myfile.txt copyfile.txt

touch $1
cat $2 > $1