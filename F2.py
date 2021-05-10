# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import F3bis
import SSH


#code design fenêtre 2
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 364)
        MainWindow.setStyleSheet("background-color: rgb(121, 115, 130);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titref2 = QtWidgets.QLabel(self.centralwidget)
        self.label_titref2.setGeometry(QtCore.QRect(120, 40, 391, 51))
        self.label_titref2.setStyleSheet("color: rgb(246, 225, 255);\n"
"font: italic 40pt \"Brush Script MT\";")
        self.label_titref2.setObjectName("label_titref2")
        self.pushButton_R1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_R1.setGeometry(QtCore.QRect(200, 140, 111, 21))
        self.pushButton_R1.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton_R1.setObjectName("pushButton_R1")
        self.pushButton_2_R2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_R2.setGeometry(QtCore.QRect(200, 210, 111, 20))
        self.pushButton_2_R2.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton_2_R2.setObjectName("pushButton_2_R2")
        self.pushButton_2_quitter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_quitter.setGeometry(QtCore.QRect(430, 300, 71, 20))
        self.pushButton_2_quitter.setStyleSheet("color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton_2_quitter.setObjectName("pushButton_2_quitter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choix Routeurs"))
        self.label_titref2.setText(_translate("MainWindow", "Selectionner un routeur "))
        self.pushButton_R1.setText(_translate("MainWindow", "Routeur 1"))
        self.pushButton_2_R2.setText(_translate("MainWindow", "Routeur 2"))
        self.pushButton_2_quitter.setText(_translate("MainWindow", "Quitter"))
        
        self.pushButton_R1.clicked.connect(self.suivant1)
        #connexion du boutton R1 à la fonction suivant1 pour passer à la fenêtre 2
        self.pushButton_2_R2.clicked.connect(self.suivant2)
        #appel de la fonction suivant2 via le pushbutton du routeur2 pour passer à la fenêtre 2 
        self.pushButton_2_quitter.clicked.connect(self.quitter)
        # on connecte le bouton quitter à la fonction quitter pour fermer la fenêtre actuelle 
        
    def suivant1(self): #fonction permettant de passer de la fenêtre  1 à la 2
        self.MainWindow3 = QtWidgets.QMainWindow()
        self.View= F3bis.View() 
        self.Model= F3bis.Model()
        self.Controller= F3bis.Controller(self.Model)
        self.View.setupUi(self.MainWindow3, self.Model, self.Controller, self.pushButton_R1)
        self.MainWindow3.show() #ouverture de la deuxième fenêtre
        MainWindow.hide() #fermeture de la fenêtre actuelle 
        
        
    def suivant2(self): #fonction pour passer de la fenêtre 1 à la 2 à partir du routeur2
        self.MainWindow3 = QtWidgets.QMainWindow()
        self.View= F3bis.View() 
        self.Model= F3bis.Model()
        self.Controller= F3bis.Controller(self.Model)
        self.View.setupUi(self.MainWindow3, self.Model, self.Controller, self.pushButton_2_R2)
        self.MainWindow3.show() #ouverture de la fenêtre 2
        MainWindow.hide() #fermeture de la fenêtre actuelle
        
    def connexion_R1(self): #fonction pour établir la connexion 
    #entre le routeur 1 de la VM à nos interfaces
        # hostname="192.168.43.2"
        hostname="10.10.25.2"
        print(hostname)
        username="etudiant"
        password="vitrygtr"
        port=22

        return hostname , port , username ,password
    
    def connexion_R2(self): #on connecte le routeur2 à notre interface
        # hostname="192.168.43.4"
        hostname="10.10.25.1"
        print(hostname)
        username="etudiant"
        password="vitrygtr"
        port=22

        return hostname , port , username ,password
    
    def quitter(self): #fonction pour fermer la fenêtre actuelle 
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

