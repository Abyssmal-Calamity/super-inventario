# Form implementation generated from reading ui file 'registro.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import csv


class Ui_Registrar(object):
    
    def setupUi(self, Registrar, Login):
        self.Registrar = Registrar
        self.Registrar.setObjectName("Registrar")
        self.Registrar.resize(1261, 532)         # Resolucion ventana
        self.Registrar.setMinimumSize(1261, 532)
        self.Registrar.setMaximumSize(1261, 532)
        self.Registrar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=self.Registrar)
        self.centralwidget.setObjectName("centralwidget")

        
        # Etiquetas
        self.fondo = QtWidgets.QLabel(parent=self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.fondo.setText("")
        self.fondo.setPixmap(QtGui.QPixmap("images/Register_Screen_JPG.jpg"))
        self.fondo.setObjectName("fondo")

        self.texto1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.texto1.setGeometry(QtCore.QRect(210, 264, 300, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto1.setFont(font)
        self.texto1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.texto1.setStyleSheet("background: transparent;\n" "color: rgb(175,175,175);\n")
        self.texto1.setText("")
        self.texto1.setObjectName("texto1")

        self.texto2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.texto2.setGeometry(QtCore.QRect(210, 364, 300, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto2.setFont(font)
        self.texto2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.texto2.setStyleSheet("background: transparent;\n" "color: rgb(175,175,175);\n")
        self.texto2.setText("")
        self.texto2.setObjectName("texto2")

        self.texto3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.texto3.setGeometry(QtCore.QRect(210, 460, 300, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto3.setFont(font)
        self.texto3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.texto3.setStyleSheet("background: transparent;\n" "color: rgb(175,175,175);\n")
        self.texto3.setText("")
        self.texto3.setObjectName("texto3")

        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setGeometry(QtCore.QRect(210, 224, 300, 40))
        self.username.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;\n" "background-color: rgb(190,190,190);\n" "color: rgb(0,0,0);")
        self.username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username.setObjectName("username")

        self.contasena = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.contasena.setFont(font)
        self.contasena.setGeometry(QtCore.QRect(210, 324, 264, 40))
        self.contasena.setStyleSheet("color: rgb(0,0,0);\n" "border-top-left-radius: 10px;\n" "border-bottom-left-radius: 10px;\n" "background-color: rgb(190,190,190)\n;"
                                     "border: solid;\n" "border-width: 1px 0px 1px 1px;")
        self.contasena.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contasena.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.contasena.setObjectName("contasena")
        
        self.etiquetaCargo = QtWidgets.QLabel(parent=self.centralwidget)
        self.etiquetaCargo.setGeometry(QtCore.QRect(550, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.etiquetaCargo.setFont(font)
        self.etiquetaCargo.setStyleSheet("color: rgb(230, 29, 82);\n" "background-color: rgb(190,190,190);\n" "border-radius: 10px;\n" "border: solid;" "border-width: 1px;")
        self.etiquetaCargo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.etiquetaCargo.setObjectName("etiquetaCargo")
        self.nombreCargo = ""

        
        # Interfaz botones
        self.showKey = CustomButton(parent=self.centralwidget)
        self.showKey.setGeometry(QtCore.QRect(474, 324, 36, 40))
        self.showKey.setIconSize(QtCore.QSize(32, 32))
        self.showKey.setText("")
        self.showKey.setObjectName("showKey")

        self.btnAdmin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAdmin.setGeometry(QtCore.QRect(200, 422, 121, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAdmin.setFont(font)
        self.btnAdmin.setStyleSheet(self.btn_style_sheet_1())
        self.btnAdmin.setObjectName("btnAdmin")

        self.btnEmpleado = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnEmpleado.setGeometry(QtCore.QRect(390, 422, 121, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnEmpleado.setFont(font)
        self.btnEmpleado.setStyleSheet(self.btn_style_sheet_1())
        self.btnEmpleado.setObjectName("btnEmpleado")

        self.btnCrear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCrear.setGeometry(QtCore.QRect(570, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btnCrear.setFont(font)
        self.btnCrear.setStyleSheet(self.btn_style_sheet_1())
        self.btnCrear.setObjectName("btnCrear")
        
        self.btnCancelar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(570, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet(self.btn_style_sheet_1())
        self.btnCancelar.setObjectName("btnCancelar")


        # Accion botones
        self.showKey.pressed.connect(lambda: self.showKey.setIcon(QtGui.QIcon("icono/mostrar2.png")))
        self.showKey.pressed.connect(lambda: self.contasena.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal))
        self.showKey.released.connect(lambda: self.showKey.setIcon(QtGui.QIcon("icono/nomostrar2.png")))
        self.showKey.released.connect(lambda: self.contasena.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password))

        self.btnCrear.clicked.connect(self.validacionCampos)

        self.btnCancelar.clicked.connect(lambda: self.cancelar(Login))

        self.btnAdmin.clicked.connect(lambda: self.btnAdmin.setStyleSheet(self.btn_style_sheet_2()))
        self.btnAdmin.clicked.connect(lambda: self.btnEmpleado.setStyleSheet(self.btn_style_sheet_1()))
        self.btnAdmin.clicked.connect(self.set_admin)

        self.btnEmpleado.clicked.connect(lambda: self.btnEmpleado.setStyleSheet(self.btn_style_sheet_2()))
        self.btnEmpleado.clicked.connect(lambda: self.btnAdmin.setStyleSheet(self.btn_style_sheet_1()))
        self.btnEmpleado.clicked.connect(self.set_empleado)
        

        self.Registrar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.Registrar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        self.Registrar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.Registrar)
        self.statusbar.setObjectName("statusbar")
        self.Registrar.setStatusBar(self.statusbar)

        self.retranslateUi(self.Registrar)
        QtCore.QMetaObject.connectSlotsByName(self.Registrar)

    
    def retranslateUi(self, Registrar):
        _translate = QtCore.QCoreApplication.translate
        Registrar.setWindowTitle(_translate("Registrar", "MainWindow"))
        self.btnEmpleado.setText(_translate("Registrar", "EMPLEADO"))
        self.btnAdmin.setText(_translate("Registrar", "ADMINISTRADOR"))
        self.btnCancelar.setText(_translate("Registrar", "CANCELAR"))
        self.btnCrear.setText(_translate("Registrar", "CREAR"))
        self.etiquetaCargo.setText(_translate("Registrar", "Cargo deseado"))
    

    def set_admin(self):
        self.nombreCargo = "Administrador"
        self.etiquetaCargo.setText(self.nombreCargo)


    def set_empleado(self):
        self.nombreCargo = "Empleado"
        self.etiquetaCargo.setText(self.nombreCargo)
    

    def validacionCampos(self):
        camposValidados = True

        if self.username.text() == "":
            self.username.setStyleSheet("border-radius: 10px;\n" "border: 2px solid rgb(255, 0, 0);")
            self.texto1.setText("Este campo es obligatorio")
            camposValidados = False
        elif self.usuario_existente():
            self.username.setStyleSheet("border-radius: 10px;\n" "border: 2px solid rgb(255, 0, 0);")
            self.texto1.setText("Ya existe un usuario registrado con este nombre")
            camposValidados = False
        else:
            self.username.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
            self.texto1.setText("")
        
        if len(self.contasena.text()) == 0:
            self.contasena.setStyleSheet("border-top-left-radius: 10px;\n" "border-bottom-left-radius: 10px;\n"
                                         "border: solid rgb(255, 0, 0);\n" "border-width: 2px 0px 2px 2px;")
            self.showKey.setStyleSheet("border-top-right-radius: 10px;\n" "border-bottom-right-radius: 10px;\n"
                                       "border: solid rgb(255, 0, 0);\n" "border-width: 2px 2px 2px 0px;")
            self.texto2.setText("Este campo es obligatorio")
            camposValidados = False
        elif len(self.contasena.text()) < 8:
            self.contasena.setStyleSheet("border-top-left-radius: 10px;\n" "border-bottom-left-radius: 10px;\n"
                                         "border: solid rgb(255, 0, 0);\n" "border-width: 2px 0px 2px 2px;")
            self.showKey.setStyleSheet("border-top-right-radius: 10px;\n" "border-bottom-right-radius: 10px;\n"
                                       "border: solid rgb(255, 0, 0);\n" "border-width: 2px 2px 2px 0px;")
            self.texto2.setText("La contraseña debe tener mínimo 8 caracteres")
            camposValidados = False
        else:
            self.contasena.setStyleSheet("border-top-left-radius: 10px;\n" "border-bottom-left-radius: 10px;\n"
                                         "border: solid;\n" "border-width: 1px 0px 1px 1px;")
            self.showKey.setStyleSheet("border-top-right-radius: 10px;\n" "border-bottom-right-radius: 10px;\n"
                                       "border: solid;\n" "border-width: 1px 1px 1px 0px;")
            self.texto2.setText("")
        
        if self.nombreCargo != "Administrador" and self.nombreCargo != "Empleado":
            self.texto3.setText("Debe elegir una opción")
            camposValidados = False
        else:
            self.texto3.setText("")
        
        if camposValidados:
            self.crearUsuario()
            self.cuadroUsuarioCreado()


    def crearUsuario(self):                 # Metodo para almacenar datos del nuevo usuario
        usuario = self.username.text()
        password = self.contasena.text()
        ocupacion = str(self.nombreCargo)
        
        new_user = [usuario, password, ocupacion]

        with open('ArchivosCSV/Usuarios.csv', 'a', encoding='utf-8', newline='') as write:
            writer = csv.writer(write)
            writer.writerow(new_user)
    

    def usuario_existente(self):        # Metodo para comprobar si ya existe un usuario que se intento crear
        with open("ArchivosCSV/Usuarios.csv", "r", encoding="utf-8") as archivo:
            users = csv.reader(archivo, delimiter=',')
            next(users)
            
            for row in users:
                if row[0] == self.username.text():
                    return True
        
        return False

    

    def cuadroUsuarioCreado(self):       # Se muestra un mensaje de usuario creado
        self.notificacion = QtWidgets.QMessageBox()
        self.notificacion.setWindowTitle("Usuario creado")
        self.notificacion.setText("Se ha registrado con éxito")
        self.notificacion.setIcon(QtWidgets.QMessageBox.Icon.Information)
        self.notificacion.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        btnAceptar = self.notificacion.button(QtWidgets.QMessageBox.StandardButton.Ok)
        btnAceptar.setText("Aceptar")
        btnAceptar.clicked.connect(self.volver_A_VentanaLogin)

        self.notificacion.exec()

    
    def cancelar(self, login):                     # Metodo para cancelar registro de usuario
        login.show()
        self.Registrar.close()
    

    def volver_A_VentanaLogin(self):      # Metodo para mostrar ventana de inicio sesion
        from Inicio_sesion import Ui_Login
        self.ventanaLogin = QtWidgets.QMainWindow()
        self.Ui = Ui_Login()
        self.Ui.setupUi(self.ventanaLogin)
        self.ventanaLogin.setWindowTitle("ULAGOS Market")
        self.ventanaLogin.setWindowIcon(QtGui.QIcon("icono/martin.png"))
        self.ventanaLogin.show()

        self.Registrar.close()
    

    def btn_style_sheet_1(self):
        return ("QPushButton{\n"
                "   background-color: rgb(80, 80, 80);\n"
                "   color: rgb(175, 175, 175);\n"
                "   border-radius: 10px;\n"
                "   border: 1px solid;\n"
                "}\n"
                "QPushButton::hover{\n"
                "   background-color: rgb(100, 100, 100);\n"
                "   color: rgb(225, 225, 225);\n"
                "   border: 1px solid rgb(100, 100, 100);\n"
                "}\n"
                "QPushButton::pressed{\n"
                "   background-color: rgb(230, 29, 82);\n"
                "   color: rgb(255, 255, 255);\n"
                "   border: 0px;\n"
                "}")
    

    def btn_style_sheet_2(self):
        return ("background-color: rgba(230, 29, 82, 0.75);\n"
                "border-radius: 10px;\n"
                "color: rgb(255, 255, 255);")




class CustomButton(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QtGui.QIcon("icono/nomostrar.png"))
        self.setStyleSheet("border-top-right-radius: 10px;\n" "border-bottom-right-radius: 10px;\n"
                           "border: solid;\n" "border-width: 1px 1px 1px 0px;\n" "background-color: rgb(190,190,190);")
    

    def enterEvent(self, event):
        self.setIcon(QtGui.QIcon("icono/nomostrar2.png"))
    

    def leaveEvent(self, event):
        self.setIcon(QtGui.QIcon("icono/nomostrar.png"))
