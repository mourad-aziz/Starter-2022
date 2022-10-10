#!/bin/bash
# installer ftp
# Last updated 06/10/2022 - mourad.aziz@laplateforme.io


f_proftpdinstall(){

apt install -y proftpd* &>/dev/null
echo -e "\n\e[1;32m[+]\e[0m proftpd* has been installed..."
f_mainmenu
}		
f_proftpdconfig(){
#useradd nobody group nogroup
echo " "> /etc/proftpd/proftpd.conf
echo "
ServerName			ProFTPD/n
ServerType			standalone/n
DefaultServer		on/n
Port				21/n
Umask				022/n
MaxInstances		30/n
User				nobody/n
Group				nogroup/n
DefaultRoot ~/n
<Directory />/n
  AllowOverwrite	on/n
</Directory>/n
 " >> /etc/proftpd/proftpd.conf
}

f_proftpduninstall(){

systemctl stop proftpd
apt purge --auto-remove proftpd*
rm /etc/ssl/private/proftpd.key
rm /etc/ssl/certs/proftpd.crt
rm /var/log/proftpd/tls.log
rm -rf /etc/proftpd/
rm -rf /srv/ftp/
#echo -e "\n\e[1;32m[+]\e[0m proftpd* has been uninstalled... reboot "
#sleep 5
reboot now

}		
f_autoinstall(){
f_proftpdinstall
f_proftpdconfig
f_enableanonyme
f_proftpdgenkey
f_enabletls
}
f_proftpdgenkey() {
openssl req -x509 -newkey rsa:1024 -keyout /etc/ssl/private/proftpd.key -out /etc/ssl/certs/proftpd.crt -nodes -days 365
chmod 0640 /etc/ssl/private/proftpd.key
}
f_addvirtuserfromcsv(){
while IFS="," read -r id firstname lastname Mdp "Rôle"
do
  echo "Record ID: $id"
  echo "Firstname: $firstname"
  echo " Lastname: $lastname"
  echo "Password: $Mdp"
  echo "Rôle: $role"
  echo ""
  if [ $role != admin ]
  then ftpasswd --passwd --file=/etc/proftpd/ftpd.passwd --name=$firstname --uid=$id --gid=$id / --home=/srv/ftp/$firstname/ --shell=/bin/false
  else #then ftpasswd --passwd --file=/etc/proftpd/ftpd.passwd --name=$firstname --uid=$id --gid=$id / --home=/srv/ftp/$firstname/ --shell=/bin/bash
  ftpasswd --group --name=nogroup --file=/etc/proftpd/ftpd.group --gid=0 --member $firstname
  fi
done < <(tail -n +2 userlist.csv)
f_mainmenu
}
f_enableanonyme() {
f_proftpdconfig
echo "
<Anonymous ~ftp>/n
User				ftp/n
Group				ftp/n

UserAlias			anonymous ftp/n

MaxClients			10/n
DisplayLogin			welcome.msg/n
DisplayFirstChdir		.message/n

<Limit WRITE>/n
DenyAll/n
 </Limit>/n
</Anonymous>/n
" >> /etc/proftpd/proftpd.conf
}
f_enabletls() {
# edit tls confg file echo ou fichier
echo "
<IfModule mod_tls.c>/n
TLSEngine                     on/n
TLSLog                         /var/log/proftpd/tls.log/n
TLSProtocol                    SSLv23/n
TLSRSACertificateFile          /etc/ssl/certs/proftpd.crt/n
TLSRSACertificateKeyFile       /etc/ssl/private/proftpd.key/n
TLSCACertificateFile 		   /etc/ssl/certs/CA.pem/n
TLSRequired                   on/n
TLSVerifyClient               off/n
" > etc/proftpd/tls.conf
echo "Include /etc/proftpd/tls.conf" >> /etc/proftpd/proftpd.conf
f_mainmenu
}
f_backup() {
BACKUPFILE=backup_$(date +%d-%m-%Y_%H:%M)
tar cvzf proftpdetc$BACKUPFILE.tar.gz /etc/proftpd/
tar cvzf ftpsrv$BACKUPFILE.tar.gz /srv/ftp/
scp jdoe@host1:proftpdetc$BACKUPFILE.tar.gz root@host2:/root/myfile2
scp jdoe@host1:ftpsrv$BACKUPFILE.tar.gz root@host2:/root/myfile2
f_mainmenu
}
f_addvirtuser(){
ftpasswd --passwd --file=/etc/proftpd/ftpd.passwd --name=merry --home=/srv/ftp/merry/
ftpasswd --passwd --file=/etc/proftpd/ftpd.passwd --name=pippin --home=/srv/ftp/pippin/
}

f_mainmenu(){

clear

	echo "install debian text mode uncheck all but ssh and outils"
 
	echo "1.  Install proftpd"
	echo "2.  Add users Merry and Pippin"
	echo "3.  Enable anonymous access"
	echo "4.  Enable TLS"
	echo "5.  Automatic install"
	echo "6.  Uninstall proftpd"
	echo "7.  Add users from csv file"
	echo "8.  Backup install"
	echo "9.  Exit"
	echo
	read -p "Choice: " mainchoice

	case $mainchoice in
	1) f_proftpdinstall ;;
	2) f_addvirtuser ;;
	3) f_enableanonyme ;;
	4) f_enabletls ;;
	5) f_autoinstall ;;
	6) f_proftpduninstall ;;
	7) f_addvirtuserfromcsv ;;
	8) f_backup ;;
	9) exit ;;
	*) clear;exit ;;
	esac

}
# run as root
if [ "$(id -u)" != "0" ]; then
	echo -e "\e[1;31m[!]\e[0m This script must be run as root" 1>&2
	exit 1
else
	f_mainmenu
fi