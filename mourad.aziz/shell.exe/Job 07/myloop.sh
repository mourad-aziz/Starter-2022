#!/bin/bash

# Il est désormais temps d’entrevoir le monde des boucles. Pour cela, vous allez créer un
# script nommé myloop.sh qui va afficher 10 fois la phrase suivante et afficher en fin de
# phrase un chiffre qui s’incrémente à chaque fois :
# “Je suis un script qui arrive à faire une boucle 1”
# “Je suis un script qui arrive à faire une boucle 2”
# “Je suis un script qui arrive à faire une boucle 3”
# “Je suis un script qui arrive à faire une boucle 4”
# ……..
# “Je suis un script qui arrive à faire une boucle 10”
# Vous devez obligatoirement utiliser les boucles pour réaliser ce script.


for n in (1..10)
{ echo -n "Je suis un script qui arrive à faire une boucle $n ";echo "" ; }