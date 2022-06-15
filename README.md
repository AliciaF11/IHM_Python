# Interface de configurations des routeurs Cisco

## But du projet
Développer une interface graphique d'utilisateur (GUI) permettant la configuration des routeurs Cisco dans un réseau.  
Ce projet a pour but d'éviter les configurations via ligne de commande, en offrant une interface plus intuitive à l'utilisateur.

## Technologies utilisées
* Paramiko pour l'accès SSH
* MVC 
* QtDeisgner + PyQT pour le développement graphique

## Développement de mon interface graphique sur QtDesigner
Mon interface se compose de 2 pages  
<p align="center">
  <img src="Image1.jpg"/>
</p>
<p align="center">
  <img src="Image2.jpg"/>
</p>

## Fonctionnalités
### Page 1
Cette fenêtre permet de sélectionner un router pour ensuite y entrer ses caractéristiques. 
### Page 2
Cette fenêtre comprend toutes les fonctionnalités que l'utilisateur peut modifier:
* Changement du nom du routeur
* Ajout d'une adresse IP
* Suppression d'une adresse IP
* Ajout de la passerelle par défaut
* Désactivation de la carte eth1
* Affichage de la table de routage
* Fichier sauvegarde
