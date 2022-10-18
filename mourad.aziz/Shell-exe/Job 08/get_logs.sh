#!/bin/bash

# Maintenant que vous connaissez les boucles, vous devez utiliser les Cron pour
# permettre d’exécuter ce script toutes les heures.
# Ce script aura pour but d’extraire de vos logs Linux le nombre de connexions à votre
# session qui ont eu lieu sur votre ordinateur. Ce nombre sera écrit dans un fichier qui se
# nommera number_connection-Date où Date sera remplacé par la date de création de
# votre fichier avec l’heure sous le format jj-mm-aaaa-HH:MM.
# Par la suite, ce fichier devra être archivé avec tar et déplacé dans un sous-dossier
# appelé Backup.
# Votre fichier script devra se nommer get_logs.sh
# Votre arborescence sera donc Job8 → Backup → number_connection-Date
PWD=pwd
[ ! -d "%PWD/Backup" ] && mkdir Backup

now=$(date +%d-%m-%Y-Hh%M)

for user in `ls /home`; do echo -ne "$user\t"; last $user | wc -l; done > number_connection-Date$now



tar -c number_connection-Date$now ./Backup/number_connection-Date$now.tar #verif synthaxe

#cron
#00 */1 * * * /$PWD/sh get_logs.sh