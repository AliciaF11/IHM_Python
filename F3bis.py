# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f3bis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import F2
import fcom
class View(object):
    def setupUi(self, MainWindow, model, ctrl, nomrouteur):
        self.nomrouteur= nomrouteur
        self.myModel = model
        self.myCtrl = ctrl
        self.MainWindow= MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 526)
        MainWindow.setStyleSheet("background-color: rgb(121, 115, 130);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_ip1 = QtWidgets.QLabel(self.centralwidget)
        self.label_ip1.setGeometry(QtCore.QRect(60, 120, 111, 21))
        self.label_ip1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_ip1.setObjectName("label_ip1")
        self.label_2_ip2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_ip2.setGeometry(QtCore.QRect(390, 120, 101, 20))
        self.label_2_ip2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2_ip2.setObjectName("label_2_ip2")
        self.lineEdit_ip1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ip1.setGeometry(QtCore.QRect(180, 120, 113, 20))
        self.lineEdit_ip1.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_ip1.setObjectName("lineEdit_ip1")
        self.lineEdit_2_pass1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2_pass1.setGeometry(QtCore.QRect(450, 220, 113, 20))
        self.lineEdit_2_pass1.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2_pass1.setObjectName("lineEdit_2_pass1")
        self.label_3_routeur = QtWidgets.QLabel(self.centralwidget)
        self.label_3_routeur.setGeometry(QtCore.QRect(210, 70, 91, 20))
        self.label_3_routeur.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3_routeur.setObjectName("label_3_routeur")
        self.lineEdit_4_routeur = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4_routeur.setGeometry(QtCore.QRect(320, 70, 113, 20))
        self.lineEdit_4_routeur.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_4_routeur.setObjectName("lineEdit_4_routeur")
        self.label_6_pass1 = QtWidgets.QLabel(self.centralwidget)
        self.label_6_pass1.setGeometry(QtCore.QRect(320, 220, 111, 21))
        self.label_6_pass1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6_pass1.setObjectName("label_6_pass1")
        self.label_8_titre_f3 = QtWidgets.QLabel(self.centralwidget)
        self.label_8_titre_f3.setGeometry(QtCore.QRect(170, 0, 411, 51))
        self.label_8_titre_f3.setStyleSheet("color: rgb(246, 225, 255);\n"
"font: italic 34pt \"Brush Script MT\";")
        self.label_8_titre_f3.setObjectName("label_8_titre_f3")
        self.lineEdit_7_ip2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7_ip2.setGeometry(QtCore.QRect(510, 120, 113, 20))
        self.lineEdit_7_ip2.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_7_ip2.setObjectName("lineEdit_7_ip2")
        self.pushButton_2_quitter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_quitter.setGeometry(QtCore.QRect(90, 420, 101, 21))
        self.pushButton_2_quitter.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton_2_quitter.setObjectName("pushButton_2_quitter")
        self.pushButton_supp_IP1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_supp_IP1.setGeometry(QtCore.QRect(130, 150, 61, 20))
        self.pushButton_supp_IP1.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_supp_IP1.setObjectName("pushButton_supp_IP1")
        self.pushButton_2_ok_pass1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_ok_pass1.setGeometry(QtCore.QRect(580, 220, 51, 21))
        self.pushButton_2_ok_pass1.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_2_ok_pass1.setObjectName("pushButton_2_ok_pass1")
        self.pushButton_3_ok_IP1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_ok_IP1.setGeometry(QtCore.QRect(60, 150, 61, 20))
        self.pushButton_3_ok_IP1.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_3_ok_IP1.setObjectName("pushButton_3_ok_IP1")
        self.pushButton_4_supp_AIP2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4_supp_AIP2.setGeometry(QtCore.QRect(480, 150, 61, 21))
        self.pushButton_4_supp_AIP2.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_4_supp_AIP2.setObjectName("pushButton_4_supp_AIP2")
        self.pushButton_5_ok_AIP2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5_ok_AIP2.setGeometry(QtCore.QRect(400, 150, 61, 21))
        self.pushButton_5_ok_AIP2.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_5_ok_AIP2.setObjectName("pushButton_5_ok_AIP2")
        self.pushButton_7_ok_nrouteur = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7_ok_nrouteur.setGeometry(QtCore.QRect(460, 70, 61, 20))
        self.pushButton_7_ok_nrouteur.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_7_ok_nrouteur.setObjectName("pushButton_7_ok_nrouteur")
        self.pushButton_sauvegarde = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sauvegarde.setGeometry(QtCore.QRect(90, 370, 101, 20))
        self.pushButton_sauvegarde.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton_sauvegarde.setObjectName("pushButton_sauvegarde")
        self.lineEditping = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditping.setEnabled(True)
        self.lineEditping.setGeometry(QtCore.QRect(180, 190, 113, 20))
        self.lineEditping.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.lineEditping.setReadOnly(True)
        self.lineEditping.setObjectName("lineEditping")
        self.label_titre_f4 = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_f4.setGeometry(QtCore.QRect(240, 250, 231, 51))
        self.label_titre_f4.setStyleSheet("color: rgb(246, 225, 255);\n"
"font: italic 40pt \"Brush Script MT\";")
        self.label_titre_f4.setObjectName("label_titre_f4")
        self.textEdit_tablederoutage = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_tablederoutage.setGeometry(QtCore.QRect(290, 310, 341, 171))
        self.textEdit_tablederoutage.setStyleSheet("font: 75 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_tablederoutage.setObjectName("textEdit_tablederoutage")
        self.pushButton_3_afficher = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_afficher.setGeometry(QtCore.QRect(90, 320, 101, 21))
        self.pushButton_3_afficher.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton_3_afficher.setObjectName("pushButton_3_afficher")
        self.pushButton_dsactiver = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dsactiver.setGeometry(QtCore.QRect(560, 150, 71, 21))
        self.pushButton_dsactiver.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.pushButton_dsactiver.setObjectName("pushButton_dsactiver")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 190, 31, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit_4_routeur.setText(self.nomrouteur.text()) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "config ip"))
        self.label_ip1.setText(_translate("MainWindow", "Adresse IP 1 / eth0"))
        self.label_2_ip2.setText(_translate("MainWindow", "Adresse IP 2 / eth1"))
        self.label_3_routeur.setText(_translate("MainWindow", "Nom du Routeur "))
        self.label_6_pass1.setText(_translate("MainWindow", "Passerelle par défaut"))
        self.label_8_titre_f3.setText(_translate("MainWindow", "Veuillez configurer ses informations"))
        self.pushButton_2_quitter.setText(_translate("MainWindow", "Quitter"))
        self.pushButton_supp_IP1.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_2_ok_pass1.setText(_translate("MainWindow", "OK"))
        self.pushButton_3_ok_IP1.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_4_supp_AIP2.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_5_ok_AIP2.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_7_ok_nrouteur.setText(_translate("MainWindow", "OK"))
        self.pushButton_sauvegarde.setText(_translate("MainWindow", "Sauvegarder"))
        self.label_titre_f4.setText(_translate("MainWindow", "Table de routage "))
        self.pushButton_3_afficher.setText(_translate("MainWindow", "Afficher"))
        self.pushButton_dsactiver.setText(_translate("MainWindow", "Désactiver"))
        self.label.setText(_translate("MainWindow", "Ping"))

        self.pushButton_7_ok_nrouteur.clicked.connect(self.namerouteur)
        #boutton ok du routeur connecter à la fonction namerouteur
        self.pushButton_3_ok_IP1.clicked.connect(self.config_eth0)
        #boutton ajouter de l'IP1 connecter à la fonction configuration du routeur1
        self.pushButton_5_ok_AIP2.clicked.connect(self.config_eth1)
        #boutton ajouter de l'IP2 connecter à la fonction configuration du routeur2
        self.pushButton_supp_IP1.clicked.connect(self.suppr_ip1)
        #boutton supprimer IP1 connecter la fonction supprimer IP1
        self.pushButton_2_quitter.clicked.connect(self.quitter)
        #boutton supprimer IP2 connecter la fonction supprimer IP2
        self.pushButton_sauvegarde.clicked.connect(self.sauvegarder)
        #boutton sauvegarder relié à la fonction sauvegarder
        self.pushButton_4_supp_AIP2.clicked.connect(self.suppr_ip2)
        #boutton supprimer IP2 connecté à la fonction suppr IP2
        self.pushButton_2_ok_pass1.clicked.connect(self.pdef_R1)
        #boutton ok de la passerelle par défaut connecté à la fonction pdef du routeur 1
        # self.pushButton_lire.clicked.connect(self.lire)
        # #configuration du routeur2
        self.pushButton_3_afficher.clicked.connect(self.table_routage)
        
        self.pushButton_dsactiver.clicked.connect(self.desact_eth1)
        
        # self.pushButton_lire.clicked.connect(self.lire)
        
        
        
    def namerouteur(self, lineEdit_4_routeur):
        self.myCtrl.namerouteur(self.nomrouteur, self.lineEdit_4_routeur) 
    def config_eth0(self, lineEdit_ip1):
        self.myCtrl.config_eth0(self.nomrouteur, self.lineEdit_ip1,self.lineEditping)       
    def config_eth1(self, lineEdit_7_ip2):
        self.myCtrl.config_eth1(self.lineEdit_7_ip2, self.nomrouteur)
    def suppr_ip1(self, lineEdit_ip1):
        self.myCtrl.suppr_ip1(self.nomrouteur, self.lineEdit_ip1)
    def suppr_ip2(self, lineEdit_7_ip2):
        self.myCtrl.suppr_ip2(self.lineEdit_7_ip2, self.nomrouteur)
    def pdef_R1(self, lineEdit_2_pass1):
        self.myCtrl.pdef_R1(self.lineEdit_2_pass1, self.nomrouteur)   
    def table_routage(self, textEdit_tablederoutage):
        self.myCtrl.table_routage(self.nomrouteur, self.textEdit_tablederoutage)
    def desact_eth1(self):
        self.myCtrl.desact_eth1(self.nomrouteur)
    def quitter(self):
        self.MainWindow.close()
    def sauvegarder(self):
        self.myCtrl.sauvegarder(self.nomrouteur, self.lineEdit_4_routeur, self.lineEdit_ip1, self.lineEdit_7_ip2, self.lineEdit_2_pass1)
      
    def lire(self):
        self.myCtrl.lire(self.nomrouteur, self.lineEdit_4_routeur, self.lineEdit_ip1, self.lineEdit_7_ip2, self.lineEdit_2_pass1)
class Controller:     
    def __init__(self, model):
        self.myModel = model
        
    def namerouteur(self, nomrouteur, lineEdit_4_routeur):
       self.myModel.namerouteur(nomrouteur, lineEdit_4_routeur) 
    def config_eth0(self, nomrouteur, lineEdit_ip1,lineEditping):
        self.myModel.config_eth0(nomrouteur, lineEdit_ip1,lineEditping)       
    def config_eth1(self, lineEdit_7_ip2, nomrouteur):
        self.myModel.config_eth1(lineEdit_7_ip2, nomrouteur)
    def suppr_ip1(self, nomrouteur, lineEdit_ip1):
        self.myModel.suppr_ip1(nomrouteur, lineEdit_ip1)
    def suppr_ip2(self, lineEdit_7_ip2, nomrouteur):
        self.myModel.suppr_ip2(lineEdit_7_ip2, nomrouteur)
    def pdef_R1(self, lineEdit_2_pass1, nomrouteur):
        self.myModel.pdef_R1(lineEdit_2_pass1, nomrouteur)    
    def table_routage(self, nomrouteur, textEdit_tablederoutage):
        self.myModel.table_routage(nomrouteur, textEdit_tablederoutage)
    def desact_eth1(self, nomrouteur):
        self.myModel.desact_eth1(nomrouteur)
    def quitter(self):
        self.myModel.quitter()
    def sauvegarder(self, nomrouteur, lineEdit_4_routeur, lineEdit_ip1, lineEdit_7_ip2, lineEdit_2_pass1):
        self.myModel.sauvegarder(nomrouteur, lineEdit_4_routeur, lineEdit_ip1, lineEdit_7_ip2, lineEdit_2_pass1)
    def lire(self, nomrouteur, lineEdit_4_routeur, lineEdit_ip1, lineEdit_7_ip2, lineEdit_2_pass1):   
        self.myModel.lire(nomrouteur, lineEdit_4_routeur, lineEdit_ip1, lineEdit_7_ip2, lineEdit_2_pass1)
class Model: 
    
    def namerouteur(self, nomrouteur, lineEdit_4_routeur):
        #fonction callback quand on clique dans bouton 
        #il accède au fichier fcom et il va utiliser la commande changement_NR1
        if nomrouteur.text() == "Routeur 1"  :  #cas du routeur 1
            s0= lineEdit_4_routeur.text()
            R1 = F2.Ui_MainWindow()
            hostname, port, username, password = R1.connexion_R1()
            fcom.changement_NR1(s0, hostname, port , username, password)
        elif nomrouteur.text() == "Routeur 2": #cas du routeur 2
            p0 =lineEdit_4_routeur.text()   
            R2 = F2.Ui_MainWindow()
            hostname, port , username,password = R2.connexion_R2()
            fcom.changement_NR2(p0, hostname,port, username,password)
        
  #fonction qui permet de changer les noms des routeurs sur la VM Routeur1


    def config_eth0(self, nomrouteur, lineEdit_ip1,lineEditping):
        if nomrouteur.text() == "Routeur 1"  :  
            s1 = lineEdit_ip1.text()
            R1 = F2.Ui_MainWindow()
            hostname, port, username, password = R1.connexion_R1()   
            # on se connecte sur le routeur 1 et apres appelle la fonction pour l'executer 
            res= fcom.add_ip_eth0_R1(s1, hostname, port, username, password)
            if res != "erreur":
                lineEditping.setText("connecté")
            
            else: 
                lineEditping.setText(res)
        
        elif nomrouteur.text() == "Routeur 2":
            p1 = lineEdit_ip1.text()
            R2 = F2.Ui_MainWindow()
            hostname, port , username,password = R2.connexion_R2()   
            # on se connecte sur le routeur 2 et apres appelle la fonction pour l'executer 
            fcom.add_ip_eth0_R2(p1,hostname, port, username, password)
            res= fcom.add_ip_eth0_R2(p1, hostname, port, username, password)
            if res != "erreur":
                  lineEditping.setText("connecté")
            
            else: 
                  lineEditping.setText(res)
            #fonction qui permet d'ajouter une adresse ip sur la carte eth0 du routeur 1 ou 2
        
    def config_eth1(self, lineEdit_7_ip2, nomrouteur):
        if nomrouteur.text() == "Routeur 1"  :  
            s2 = lineEdit_7_ip2.text()
            R1 = F2.Ui_MainWindow()
            hostname, port, username, password = R1.connexion_R1()
            # on se connecte sur le routeur 1 et apres apelle la fonction pour l'executer
            fcom.activ_eth1(hostname, port, username, password) 
            fcom.add_ip_eth1_R1(s2, hostname, port, username, password)
           
            
        elif nomrouteur.text() == "Routeur 2":
            p2= lineEdit_7_ip2.text()
            R2 = F2.Ui_MainWindow()
            hostname, port, username, password = R2.connexion_R2()
            # on se connecte sur le routeur 2 et apres apelle la fonction pour l'executer 
            fcom.activ_eth1(hostname, port, username, password) 
            fcom.add_ip_eth1_R2(p2, hostname, port , username, password)
        
    #fonction qui permet d'ajouter une adresse ip sur la carte eth1 du routeur 1 et 2
        
    def suppr_ip1(self, nomrouteur, lineEdit_ip1):
        if nomrouteur.text() == "Routeur 1"  : 
            s3 = lineEdit_ip1.text()
            R1 = F2.Ui_MainWindow()
            hostname, port, username, password = R1.connexion_R1()   
            # on se connecte sur le routeur 1 et apres appelle la fonction pour l'executer 
            fcom.delete_ip_eth0_R1(s3, hostname, port, username, password)
            
        elif nomrouteur.text() == "Routeur 2":
            p3 = lineEdit_ip1.text()
            R2 = F2.Ui_MainWindow()
            hostname, port, username, password = R2.connexion_R2()   
            # on se connecte sur le routeur 2 et apres appelle la fonction pour l'executer 
            fcom.delete_ip_eth0_R2(p3, hostname, port, username, password) 
        
    #fonction qui permet de supprimer l'adresse ip1 de la carte eth0 routeur1 et 2
    def suppr_ip2(self, lineEdit_7_ip2, nomrouteur):
        if nomrouteur.text() == "Routeur 1"  :
            s4 = lineEdit_7_ip2.text()
            R1 = F2.Ui_MainWindow()
            hostname, port, username, password = R1.connexion_R1()   # connecter sur le VM et apres apelle la fonction pour l'executer 
            fcom.delete_ip_eth1_R1(s4, hostname, port, username, password)
     #fonction qui permet de supprimer l'adresse ip2 de la carte eth1 du routeur1  
        elif nomrouteur.text() == "Routeur 2":
            p4 = lineEdit_7_ip2.text()
            R2 = F2.Ui_MainWindow()
            hostname, port, username, password = R2.connexion_R2()   # connecter sur le VM et apres apelle la fonction pour l'executer 
            fcom.delete_ip_eth1_R2(p4, hostname, port, username, password)
            
            
    def pdef_R1(self, lineEdit_2_pass1, nomrouteur):
        if nomrouteur.text() == "Routeur 1"  :
            s5 = lineEdit_2_pass1.text()
            R1 = F2.Ui_MainWindow()
            hostname, port, username, password = R1.connexion_R1()  
            fcom.add_pdef_R1(s5, hostname, port, username, password)
        
        elif nomrouteur.text() == "Routeur 2":
            p5 = lineEdit_2_pass1.text()
            R2 = F2.Ui_MainWindow()
            hostname, port, username, password = R2.connexion_R2()
            fcom.add_pdef_R2(p5, hostname, port, username, password)
    #fonction qui permet d'ajouter une passerelle par défaut au routeur1 et 2
    
        
    def table_routage(self,nomrouteur, textEdit_tablederoutage):
        if nomrouteur.text() == "Routeur 1"  : 
            R1 = F2.Ui_MainWindow()
            hostname, port, username, password = R1.connexion_R1()   
            # on se connecte sur le routeur 1 et apres apelle la fonction pour l'executer 
            resultat = fcom.table( hostname, port, username, password)
            # print(resultat)
            textEdit_tablederoutage.setText(resultat)
            # a = print(resultat)
            
            
        elif nomrouteur.text() == "Routeur 2":
            R2 = F2.Ui_MainWindow()
            hostname, port, username, password = R2.connexion_R2()
            # on se connecter sur le routeur 2 et apres apelle la fonction pour l'executer 
            resultat = fcom.table(hostname, port, username, password)
            #on retourne le resultat de la commande de sudo add ip route 
            #dans une variable resultat qui sera appelé dans l'emplacement de l'affichage de la 
            #table de routage
            # print (resultat)
            textEdit_tablederoutage.setText(resultat)
            # b = print(resultat)
          #affiche table routage routeur 1 et 2  
    def desact_eth1(self, nomrouteur):
        if nomrouteur.text() == "Routeur 1"  : 
            R1 = F2.Ui_MainWindow()
            hostname, port , username,password = R1.connexion_R1()   
            # on se connecte sur le routeur1 et apres appelle la fonction pour l'executer 
            fcom.desact_eth1(hostname, port, username, password)
    # fonction pour désactiver eth1 cad pour désactiver l'adresse ip2 du routeur 1
        elif nomrouteur.text() == "Routeur 2":
            R2 = F2.Ui_MainWindow()
            hostname, port , username,password = R2.connexion_R2()   
            # on se connecte sur le routeur2 et apres appelle la fonction pour l'executer 
            fcom.desact_eth1(hostname, port, username, password)
    # fonction pour désactiver eth1 cad pour désactiver l'adresse ip2 du routeur 2
        
    def sauvegarder(self, nomrouteur, lineEdit_4_routeur, 
                    lineEdit_ip1, lineEdit_7_ip2, lineEdit_2_pass1):
        #1ere méthode
        if nomrouteur.text() == "Routeur 1"  :
            f = open('sauvegarde.txt', 'w')
            s0 = lineEdit_4_routeur.text()  
            s1 = lineEdit_ip1.text()
            s2 = lineEdit_7_ip2.text()
            s5 = lineEdit_2_pass1.text()
            # a= print(resultat)
            f.write('\nNom du routeur : ' + s0 +
                    '\nAdresse IP1 eth0: ' + s1 +
                    '\nAdresse IP2 eth1 : ' + s2 + 
                    '\nPasserelle par défaut : ' + s5)  
            f.close()
        elif nomrouteur.text() == "Routeur 2":
            f = open('sauvegarde.txt', 'w')
            p0 = lineEdit_4_routeur.text()  
            p1 = lineEdit_ip1.text()
            p2 = lineEdit_7_ip2.text()
            p5 = lineEdit_2_pass1.text()
            # b= print(resultat)
            f.write('\nNom du routeur : ' + p0 + 
                    '\nAdresse IP1 eth0: ' + p1 + 
                    '\nAdresse IP2 eth1 : ' + p2 + 
                    '\nPasserelle par défaut : ' + p5)  
            f.close()
      #fichier de sauvegarde utilise à l'utilisateur      
        #2eme méthode
        # with open('sauvegarde.txt','w') as f:
        #    if nomrouteur.text() == "Routeur 1"  :
        #        s0 = lineEdit_4_routeur.text()  
        #        s1 = lineEdit_ip1.text()
        #        s2 = lineEdit_7_ip2.text()
        #        s5 = lineEdit_2_pass1.text()
        #        f.write('\nNom du routeur : ' + s0 + '\nAdresse IP eth0: ' + s1 + '\nAdresse IP eth1 : ' + s2 + '\nPasserelle par défaut : ' + s5)  
        #  # on sauvegarde dans un fichier txt les adresses ip, le nom de routeur et la passerelle par défaut que l'utilisateur à entrer  
        #    elif nomrouteur.text() == "Routeur 2":
        #        p0 = lineEdit_4_routeur.text()  
        #        p1 = lineEdit_ip1.text()
        #        p2 = lineEdit_7_ip2.text()
        #        p5 = lineEdit_2_pass1.text()
        #        f.write('\nNom du routeur : ' + p0 + '\nAdresse IP eth0: ' + p1 + '\nAdresse IP eth1 : ' + p2 + '\nPasserelle par défaut : ' + p5)  
    
    
    # def lire(self, nomrouteur, lineEdit_4_routeur, lineEdit_ip1, lineEdit_7_ip2, lineEdit_2_pass1):
    #     #1ere méthode
    #     if nomrouteur.text() == "Routeur 1"  :
    #         f = open('lire.txt', 'r')
    #         s0 = lineEdit_4_routeur.text()  
    #         s1 = lineEdit_ip1.text()
    #         s2 = lineEdit_7_ip2.text()
    #         s5 = lineEdit_2_pass1.text()
    #         f.read
    #         f.write (lineEdit_4_routeur.text(),lineEdit_ip1.text(),  lineEdit_7_ip2.text(), lineEdit_2_pass1.text())
    #     elif nomrouteur.text() == "Routeur 2":
    #         f = open('lire.txt', 'r')
    #         # p0 = lineEdit_4_routeur.text()  
    #         # p1 = lineEdit_ip1.text()
    #         # p2 = lineEdit_7_ip2.text()
    #         # p5 = lineEdit_2_pass1.text()
    #         f.read
    #         f.read(lineEdit_4_routeur.text(),lineEdit_ip1.text(),  lineEdit_7_ip2.text(), lineEdit_2_pass1.text())
   

        
 
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow3 = QtWidgets.QMainWindow()
    View= View() 
    Model= Model()
    Controller= Controller(Model)
    pushButton_3_afficher = QtWidgets.QPushButton()
    View.setupUi(MainWindow3, Model, Controller,pushButton_3_afficher)
    MainWindow3.show()
    sys.exit(app.exec_())
    

