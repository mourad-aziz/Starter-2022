#! /bin/bash

# Créer un script nommé accessrights.sh qui depuis ce fichier CSV, récupère les
# informations des utilisateurs et les crée sur votre système.
# Si l’utilisateur est un admin., donnez-lui le rôle de super utilisateur de votre système
# Pour la suite, utilisez les cron pour permettre au script de se relancer automatiquement
# s'il y a un changement dans le fichier CSV. (Pour tester, je vous invite à modifier le fichier
# à la main).



while IFS="," read -r id firstname lastname Mdp "Rôle"
do
  echo "Record ID: $id"
  echo "Firstname: $firstname"
  echo " Lastname: $lastname"
  echo "Password: $Mdp"
  echo "Rôle: $role"
  echo ""
  if [ $role != admin ]
  then #utilisateur normal adduser -u $username - :kk:mm
  else #droit root moduser add group root
  fi
  
done < <(tail -n +2 sample.csv)

cat sample.csv > sample.csv.backup
 

# cron @minutly if [sample.csv != sample.csv.backup] diff sample.csv sample.csv.backup | sudo ./accessrights.sh 