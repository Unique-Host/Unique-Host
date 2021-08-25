import os

print("\n Apt Updating ...")
os.system("apt update")

print("\n Apt Upgrading ...")
os.system("apt upgrade")

print("\n Installing Wget Package ...")
os.system("pkg install wget")

print("\n Installing Curl Package ...")
os.system("pkg install curl")

print("\n Installing Openssh Package ...")
os.system("pkg install openssh")

print("\n Installing Git Package ...")
os.system("pkg install git")

print("\n Installing Python ...")
os.system("pkg install python")

print("\n Installing Python2 ...")
os.system("pkg install python2")

print("\n Installing Ncurses-Utils ...")
os.system("apt install ncurses-utils")

print("\n Downloading ...")
os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")

print("\n Giving Executing Permission ...")
os.system("chmod +x metasploit.sh")

print ("\n Downloading Metasploit ...")
os.system("./metasploit.sh || bash metasploit.sh")

print("\n Done , Type msfconsole For Opening Metasploit Framework")
