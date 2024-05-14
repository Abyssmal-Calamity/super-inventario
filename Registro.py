# Form implementation generated from reading ui file 'registro.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import csv

class Ui_Registrar(object):
    def registro(self, usuario, contrasena):
        with open('ArchivosCSV/Usuarios.csv', 'w', encoding='utf-8', newline='') as write:
            writer = csv.writer(write)
        
        with open('ArchivosCSV/Usuarios.csv', encoding='utf-8', newline='') as read:
            reader = csv.reader(read, delimiter=',')

    def cerrar(self, login, reg):
        login.show()
        reg.close()

    def setupUi(self, Registrar, Login):
        Registrar.setObjectName("Registrar")
        Registrar.resize(1261, 532)
        Registrar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=Registrar)
        self.centralwidget.setObjectName("centralwidget")

        # Etiquetas
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Register_Screen_JPG.jpg"))
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setGeometry(QtCore.QRect(210, 210, 301, 41))
        self.username.setStyleSheet("border-radius:10px")
        self.username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username.setObjectName("username")
        self.contasena = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contasena.setFont(font)
        self.contasena.setGeometry(QtCore.QRect(210, 310, 301, 41))
        self.contasena.setStyleSheet("border-radius: 10px;")
        self.contasena.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.contasena.setObjectName("contasena")
        self.etiquetaCargo = QtWidgets.QLabel(parent=self.centralwidget)
        self.etiquetaCargo.setGeometry(QtCore.QRect(550, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.etiquetaCargo.setFont(font)
        self.etiquetaCargo.setStyleSheet("background-color: rgb(255, 255, 255);\n" "border-radius: 10px;")
        self.etiquetaCargo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.etiquetaCargo.setObjectName("etiquetaCargo")

        # Interfaz botones
        self.btnEmpleado = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnEmpleado.setGeometry(QtCore.QRect(390, 420, 121, 41))
        self.btnEmpleado.setStyleSheet("QPushButton{\n"
                                    "   font: 10pt \"Segoe UI\";\n"
                                    "   background-color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::hover{\n"
                                    "   background-color: rgb(255, 170, 255);\n"
                                    "   color: rgb(85, 85, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::pressed{\n"
                                    "   background-color: rgb(255, 85, 255);\n"
                                    "   color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}")
        self.btnEmpleado.setObjectName("btnEmpleado")
        self.btnAdmin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAdmin.setGeometry(QtCore.QRect(200, 420, 121, 41))
        self.btnAdmin.setStyleSheet("QPushButton{\n"
                                    "   font: 10pt \"Segoe UI\";\n"
                                    "   background-color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::hover{\n"
                                    "   background-color: rgb(255, 170, 255);\n"
                                    "   color: rgb(85, 85, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::pressed{\n"
                                    "   background-color: rgb(255, 85, 255);\n"
                                    "   color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}")
        self.btnAdmin.setObjectName("btnAdmin")
        self.btnCancelar = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.cerrar(Login, Registrar))    #lambda
        self.btnCancelar.setGeometry(QtCore.QRect(570, 320, 121, 41))
        self.btnCancelar.setStyleSheet("QPushButton{\n"
                                    "   font: 700 12pt \"Segoe UI\";\n"
                                    "   background-color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::hover{\n"
                                    "   background-color: rgb(255, 170, 255);\n"
                                    "   color: rgb(85, 85, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::pressed{\n"
                                    "   background-color: rgb(255, 85, 255);\n"
                                    "   color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}")
        self.btnCancelar.setObjectName("btnCancelar")
        usuario = str(self.username)
        contrasena = str(self.contasena)
        self.btnCrear = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.registro(usuario, contrasena))
        self.btnCrear.setGeometry(QtCore.QRect(570, 240, 121, 41))
        self.btnCrear.setStyleSheet("QPushButton{\n"
                                    "   font: 700 12pt \"Segoe UI\";\n"
                                    "   background-color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::hover{\n"
                                    "   background-color: rgb(255, 170, 255);\n"
                                    "   color: rgb(85, 85, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton::pressed{\n"
                                    "   background-color: rgb(255, 85, 255);\n"
                                    "   color: rgb(255, 255, 255);\n"
                                    "   border-radius: 10px;\n"
                                    "}")
        self.btnCrear.setObjectName("btnCrear")
        
        Registrar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Registrar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        Registrar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Registrar)
        self.statusbar.setObjectName("statusbar")
        Registrar.setStatusBar(self.statusbar)

        self.retranslateUi(Registrar)
        QtCore.QMetaObject.connectSlotsByName(Registrar)

    def retranslateUi(self, Registrar):
        _translate = QtCore.QCoreApplication.translate
        Registrar.setWindowTitle(_translate("Registrar", "MainWindow"))
        self.btnEmpleado.setText(_translate("Registrar", "EMPLEADO"))
        self.btnAdmin.setText(_translate("Registrar", "ADMINISTRADOR"))
        self.btnCancelar.setText(_translate("Registrar", "CANCELAR"))
        self.btnCrear.setText(_translate("Registrar", "CREAR"))
        self.etiquetaCargo.setText(_translate("Registrar", "Cargo elegido"))
