import os
import textwrap

def createvhost(filename):
	print("Enter site name(name of folder where website files are located): ")
	sitename = input()

	print("Enter new domain name(example.com): ")
	domainname = input()

	print("Enter server alias(www.example.com)")
	domainalias = input()


	print("Sitename = "+sitename+"\n")
	#os.mkdir("/var/www/"+sitename)

	contentsList = ["ServerAdmin admin@example.com","DocumentRoot /var/www/"+sitename,
	"ServerName "+domainname,"ServerAlias "+domainalias,"<Directory /var/www/"+sitename+">","Options +FollowSymlinks",
	"AllowOverride All","Require all granted","</Directory>","ErrorLog ${APACHE_LOG_DIR}/error.log","CustomLog ${APACHE_LOG_DIR}/access.log combined"]

	f = open(filename,"w+")
	f.write("<VirtualHost *:80>")
	f.write("\n")
	f.close()

	with open(filename,"a+") as f:
		for word in contentsList:
			f.write(textwrap.indent(text=word, prefix='    '))
			f.write("\n")

	f = open(filename,"a+")
	f.write("</VirtualHost>")
	f.close()

	print("Place your files in /var/www/"+sitename)

print("Enter name of site(name of configuration file - Do NOT include .conf)")
namefile = input()
confname = open("/etc/apache2/sites-available/"+namefile+".conf","w")
confname.close()
createvhost("/etc/apache2/sites-available/"+namefile+".conf")
	
