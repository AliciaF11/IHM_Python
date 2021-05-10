# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 22:31:10 2021

@author: Alicia
"""

#fichier où on met les commandes : solution pour écrire sur la VM
from SSH import ssh

user = 'etudiant'


#changement nom de routeur 
def changement_NR1(s0, hostname, port, username, password):
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo hostnamectl set-hostname " + s0) 
    #changer le nom du routeur grâce à la commande linux

def changement_NR2(p0,hostname, port , username,password):
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo hostnamectl set-hostname " +p0) 
    #changer le nom du routeur
   
#ajout d'une adresse IP sur eth0
def add_ip_eth0_R1(s1, hostname, port, username, password): # on configure  l'adresse ip1 de eth0
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr add "+ s1 + " dev eth0 ")
    res= connect.sendCommand("ping -c 1" + s1 + ">/dev/null/ || echo erreur")
    return res

def add_ip_eth0_R2(p1,hostname, port , username,password): #configurer @ip
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr add "+ p1 + " dev eth0 ")
    res= connect.sendCommand("ping -c 1" + p1 + ">/dev/null/ || echo erreur")
    return res
#ajout d'une adresse IP sur eth1
def add_ip_eth1_R1(s2, hostname, port, username, password): #on configure l'adresse ip2 de eth1
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr add "+ s2 + " dev eth1 ")
    
def add_ip_eth1_R2(p2, hostname, port, username, password): #on configure l'adresse ip2 de eth1
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr add "+ p2 + " dev eth1 ")

#suppression d'une adresse IP sur eth0
def delete_ip_eth0_R1(s3, hostname, port, username, password): 
    #on supprime l'adresse ip1 de eth0
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr del "+ s3 + " dev eth0 ") 
def delete_ip_eth0_R2(p3, hostname, port, username, password): 
    #on supprime l'adresse ip1 de eth0
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr del "+ p3 + " dev eth0 ") 
    
#suppression d'une adresse IP sur eth1
def delete_ip_eth1_R1(s4, hostname, port, username, password): #on supprime l'adresse ip2 de eth1
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr del "+ s4 + " dev eth1 ") 
def delete_ip_eth1_R2(p4, hostname, port, username, password): #on supprime l'adresse ip2 de eth1
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip addr del "+ p4 + " dev eth1 ") 
    
    
#configuration d'une passerelle par défaut    
def add_pdef_R1(s5, hostname, port, username, password): #on change la passerelle par défaut
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip route add default via "+ s5)
    
def add_pdef_R2(p5, hostname, port, username, password): #on change la passerelle par défaut
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand("sudo ip route add default via "+ p5)
    
#affichage table de routage   
def table(hostname, port, username, password): 
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    res = connect.sendCommand("sudo ip route" )
    return res 



#BONUS     
# def desact_eth0(s1,hostname, port, username, password):
#     connect=ssh(hostname=hostname, port=port, username=username, password=password)
#     connect.sendCommand(" sudo ifdown eth0")

# def activ_eth0(hostname, port, username, password):
#     connect=ssh(hostname=hostname, port=port, username=username, password=password)
#     connect.sendCommand(" sudo ifup eth0")
    
def desact_eth1(hostname, port, username, password): #on désactive eth1
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand(" sudo ifdown eth1")
    
def activ_eth1(hostname, port, username, password): #on désactive eth1
    connect=ssh(hostname=hostname, port=port, username=username, password=password)
    connect.sendCommand(" sudo ifup eth1")



