#!/bin/bash

# Créer un script nommé add.sh qui prendra cette fois-ci des paramètres en entrée de
# script. Ce script devra permettre d’additionner 2 nombres. Les nombres doivent être
# renseignés en argument du script comme ceci :


sum=$(($1 + $2)) ; echo $sum