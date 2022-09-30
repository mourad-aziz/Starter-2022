#!/bin/bash

# Poussons un peu les boucles, pour cela, vous allez créer une minicalculatrice qui
# permettra de faire les opérations suivantes : “x + - ÷”.
# Votre script devra se nommer my_calculator.sh
# Les chiffres de l’opération seront passés en premier et troisième paramètre et le
# symbole de l’opération en deuxième position de telle sorte que votre script se lance de
# la manière suivante :
# ./my_calculator.sh 2 + 3


resultat=$(echo "$1 $2 $3" | bc)
echo $resultat