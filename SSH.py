# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 22:12:45 2021

@author: Alicia
"""
#fichier ssh pour connecter mon interface et le routeur
# contient uniquement le code ssh 
from paramiko import client 
#paramiko est une bibliothèque de python
# import getpass, sys


class ssh :
    client =None 
    
    def __init__(self, hostname, port, username, password):
        try:
            print("Connecting to server.")
            self.client=client.SSHClient() #Instance d'un client SSH
            self.client.set_missing_host_key_policy(client.AutoAddPolicy())  
            self.client.connect(hostname, port=port, username=username, password=password) 
            # établit la connexion avec le serveur SSH
            
        except:
            print("Exception raised !")
            
    def sendCommand(self, command):
        if(self.client):
            stdin,stdout,stderr= self.client.exec_command(command) 
            #j'execute une commande sur le terminal distant
            #stdin: permet de passer des configurations en plus
            #stdout: contient le resultat du terminal
            #stderr: contient les erreurs du terminal
            # print (stdout.read().decode())
            return stdout.read().decode()
            #on affiche le contenu du fichier stdout
        else:
            print("Connection not opened.")
        self.client.close()
        # ferme la connexion 

# hostname="192.168.43.2" etape pour vérifier que mon routeur se connecte bien avec mon interface
# username="etudiant"
# password="vitrygtr"
# port=22

# hostname = sys.argv 
# port = sys.argv
# username = sys.argv
# password = getpass.getpass("Mot de passe : ")


if __name__ == "__main__":
    user = ssh(hostname,port,username,password)
    # user.sendCommand("ip a") 
    resultat = user.sendCommand("ip route")
    print(resultat)
    


            
            