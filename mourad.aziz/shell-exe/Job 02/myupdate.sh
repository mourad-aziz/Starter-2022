#!/bin/bash

# Votre gestionnaire de paquet préféré a besoin d’être mis à jour de manière récurrente,
# une tâche avec 2 lignes de commandes qui pourrait être simplifié en une seule !
# - Réalisez un script nommé myupdate.sh qui met à jour votre gestionnaire de
# paquet

if [ "$UID" -ne 0 ]
then
echo "il faut être root pour utiliser ce script."
exit 87
fi

apt update && apt upgrade