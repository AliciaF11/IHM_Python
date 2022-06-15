# Cisco Router Configuration Interface

## Objective of the project
Developed a graphical user interface (GUI) allowing the configuration of Cisco routers in a network.  
This project aims to avoid configurations via command line, by offering a more intuitive interface to the user.

## Technologies used
* Paramiko for SSH access
* MVC 
* QtDesigner + PyQT for graphics development

## Development of my GUI on QtDesigner
My interface consists of 2 pages
<p align="center">
  <img src="Image1.jpg"/>
</p>
<p align="center">
  <img src="Image2.jpg"/>
</p>

## Features
### Page 1
This window allows you to select a router and then enter its characteristics.
### Page 2
This window includes all the features that the user can modify:
* Changed router name
* Add IP address
* Deletion of an IP address
* Add default gateway
* Disable eth1 card
* Routing table display
* Backup file

#### Please find the codes associated with this project in the same place as the readme.md

