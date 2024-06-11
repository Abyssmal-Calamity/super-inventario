# Form implementation generated from reading ui file 'ventana3.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import csv
from PyQt6 import QtCore, QtGui, QtWidgets

# Se importan las ventanas
from Ventana_principal import Ui_MainWindow
from Registro import Ui_Registrar
from Agregar_productos import Ui_AgregarP


class Ui_Login(object):
    """def __init__(self):
        self.comprobarlistaUsuarios()"""

    
    def setupUi(self, Login):
        self.log_in = Login
        self.log_in.setObjectName("Login")
        self.log_in.resize(1261, 532)         # Resolucion ventana
        self.log_in.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=self.log_in)
        self.centralwidget.setObjectName("centralwidget")


        # Imagenes
        self.background = QtWidgets.QLabel(parent=self.centralwidget)       # Imagen de fondo
        self.background.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/Start_Screen_JPG.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        
        
        # Etiquetas
        self.userEdit = QtWidgets.QLineEdit(parent=self.centralwidget)      # Cuadro para ingresar usuario
        self.userEdit.setGeometry(QtCore.QRect(666, 229, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userEdit.setFont(font)
        self.userEdit.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
        self.userEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.userEdit.setObjectName("userEdit")

        self.passwordEdit = QtWidgets.QLineEdit(parent=self.centralwidget)  # Cuadro para ingresar contraseña
        self.passwordEdit.setGeometry(QtCore.QRect(660, 306, 178, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordEdit.setStyleSheet("border-top-left-radius: 10px;\n" "border-bottom-left-radius: 10px;\n"
                                        "border: solid;\n" "border-width: 1px 0px 1px 1px;")
        self.passwordEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.passwordEdit.setObjectName("passwordEdit")

        self.textLabel = QtWidgets.QLabel(parent=self.centralwidget)        # Muestra texto informativo
        self.textLabel.setGeometry(QtCore.QRect(586, 350, 480, 43))
        self.textLabel.setStyleSheet("background: transparent;")
        self.textLabel.setText("")
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textLabel.setObjectName("textLabel")

        self.bienvenida = QtWidgets.QLabel(self.centralwidget)              # Muestra texto de bienvenida
        self.bienvenida.setGeometry(QtCore.QRect(490, 100, 270, 84))
        self.bienvenida.setStyleSheet("background: transparent;")
        self.bienvenida.setPixmap(QtGui.QPixmap("images/bembenido.png"))
        self.bienvenida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bienvenida.setObjectName("bienvenida")

        
        # Interfaz botones
        self.showKey = CustomButton(parent=self.centralwidget)
        self.showKey.setGeometry(QtCore.QRect(838, 306, 34, 32))
        self.showKey.setIconSize(QtCore.QSize(32, 32))
        self.showKey.setText("")
        self.showKey.setObjectName("showKey")

        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)     # Boton iniciar sesion
        self.loginButton.setGeometry(QtCore.QRect(810, 404, 131, 36))
        self.loginButton.setStyleSheet(self.btn_style_sheet())
        self.loginButton.setObjectName("loginButton")

        self.exitButton = QtWidgets.QPushButton(parent=self.centralwidget)      # Boton para cerrar programa
        self.exitButton.setGeometry(QtCore.QRect(1110, 442, 131, 36))
        self.exitButton.setStyleSheet(self.btn_style_sheet())
        self.exitButton.setObjectName("exitButton")

        self.btnRegistrar = QtWidgets.QPushButton(parent=self.centralwidget)    # Boton registrar usuario
        self.btnRegistrar.setGeometry(QtCore.QRect(620, 404, 131, 36))
        self.btnRegistrar.setStyleSheet(self.btn_style_sheet())
        self.btnRegistrar.setObjectName("btnRegistrar")
        
        self.btnAgregar= QtWidgets.QPushButton(parent=self.centralwidget)    # Boton registrar usuario
        self.btnAgregar.setGeometry(QtCore.QRect(620, 450, 131, 36))
        self.btnAgregar.setStyleSheet(self.btn_style_sheet())
        self.btnAgregar.setObjectName("btnRegisbtnAgregartrar")

        
        # Accion botones
        self.showKey.pressed.connect(lambda: self.showKey.setIcon(QtGui.QIcon("icono/mostrar2.png")))
        self.showKey.pressed.connect(lambda: self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal))
        self.showKey.released.connect(lambda: self.showKey.setIcon(QtGui.QIcon("icono/nomostrar2.png")))
        self.showKey.released.connect(lambda: self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password))
        
        self.exitButton.clicked.connect(self.log_in.close)

        self.loginButton.clicked.connect(self.acceder)
        
        self.btnRegistrar.clicked.connect(self.gui_registrar)
        self.btnAgregar.clicked.connect(self.gui_agregar)
        

        self.log_in.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.log_in)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        self.log_in.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.log_in)
        self.statusbar.setObjectName("statusbar")
        self.log_in.setStatusBar(self.statusbar)

        self.retranslateUi(self.log_in)
        QtCore.QMetaObject.connectSlotsByName(self.log_in)
    
    
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.loginButton.setText(_translate("Login", "Ingresar"))
        self.exitButton.setText(_translate("Login", "Salir"))
        self.btnRegistrar.setText(_translate("Login", "Registrar"))
        self.btnAgregar.setText(_translate("Login", "Agregar Productos"))
    
    
    def limpiarCampos(self):                    # Metodo para limpiar los campos de texto
        self.textLabel.setPixmap(QtGui.QPixmap(None))
        self.userEdit.setText(None)
        self.passwordEdit.setText(None)
    
    
    def gui_registrar(self):     # Metodo para abrir ventana de registro de nuevos usuarios
        self.limpiarCampos()        # Se borran los datos de los campos de texto
        self.ventanaRegistro = QtWidgets.QMainWindow()      # Se abre la ventana de registro
        self.ui = Ui_Registrar()
        self.ui.setupUi(self.ventanaRegistro, self.log_in)
        self.ventanaRegistro.setWindowTitle("ULAGOS Market")
        self.ventanaRegistro.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
        self.ventanaRegistro.show()

        self.log_in.close()
        
    def gui_agregar(self):     # Metodo para abrir ventana de agregado de nuevos productos
        self.limpiarCampos()        # Se borran los datos de los campos de texto
        self.ventanaAgregarP = QtWidgets.QMainWindow()      # Se abre la ventana de agregado
        self.ui = Ui_AgregarP()
        self.ui.setupUi(self.ventanaAgregarP, self.log_in)
        self.ventanaAgregarP.setWindowTitle("ULAGOS Market")
        self.ventanaAgregarP.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
        self.ventanaAgregarP.show()

        self.log_in.close()

    
    def acceder(self):                 # Metodo para iniciar sesion
        nickname = self.userEdit.text()
        password = self.passwordEdit.text()

        if self.comprobarlistaUsuarios():
            self.listaUsuariosVacia()
        
        elif self.verificarDatos(nickname, password):
            self.limpiarCampos()                                # Se borran los datos de los campos de texto
            self.ventanaPrincipal = QtWidgets.QMainWindow()     # Se abre la ventana principal
            self.Ui = Ui_MainWindow()
            self.Ui.setupUi(self.ventanaPrincipal, self.log_in)
            self.ventanaPrincipal.setWindowTitle("ULAGOS Market")
            self.ventanaPrincipal.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
            self.ventanaPrincipal.show()
            
            self.log_in.close()
        
        elif len(nickname) == 0 or len(password) == 0:
            self.textLabel.setGeometry(QtCore.QRect(586, 350, 529, 43))
            self.textLabel.setPixmap(QtGui.QPixmap("images/Informacion.png"))

        else:
            self.textLabel.setGeometry(QtCore.QRect(586, 350, 480, 43))
            self.textLabel.setPixmap(QtGui.QPixmap("images/Datos.png"))
    
    
    def verificarDatos(self, usuario, contrasena):               # Metodo para verificar credenciales de usuario
        with open("ArchivosCSV/Usuarios.csv", "r", encoding="utf-8", newline='') as f:
            lector = csv.reader(f, delimiter=',')
            next(lector)
            
            for row in lector:
                if row[0] == usuario:
                    if row[1] == contrasena:
                        return True
            
        return False
    

    def comprobarlistaUsuarios(self):
        datos = self.leerDatosCSV()

        if datos:
            return False
        else:
            return True
    
    
    def leerDatosCSV(self):
        with open("ArchivosCSV/Usuarios.csv", "r", encoding="utf-8", newline='') as file:
            lector = csv.reader(file, delimiter=',', quotechar='"')
            next(lector)
            return list(lector)
    

    def listaUsuariosVacia(self):
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setWindowTitle("Base de datos vacía")
        self.mensaje.setText("No existen usuarios en nuestra base de datos.\n¿Desea registrarse ahora?")
        self.mensaje.setIcon(QtWidgets.QMessageBox.Icon.Information)
        self.mensaje.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        btnSi = self.mensaje.button(QtWidgets.QMessageBox.StandardButton.Yes)
        btnSi.setText("Sí")
        btnSi.clicked.connect(self.gui_registrar)
        btnNo = self.mensaje.button(QtWidgets.QMessageBox.StandardButton.No)
        btnNo.setText("No")

        self.mensaje.exec()
    

    def btn_style_sheet(self):
        return ("QPushButton{\n"
                "   font: 600 12pt \"Segoe UI Semibold\";\n"
                "   background-color: rgb(255, 255, 255);\n"
                "   border-radius: 10px;\n"
                "   border: 1px solid;\n"
                "}\n"
                "QPushButton::hover{\n"
                "   background-color: rgb(255, 170, 255);\n"
                "   color: rgb(85, 85, 255);\n"
                "   border: 1px solid rgb(85, 0, 255);\n"
                "}\n"
                "QPushButton::pressed{\n"
                "   font: 700 12pt \"Segoe UI\";\n"
                "   background-color: rgb(255, 0, 255);\n"
                "   color: rgb(255, 255, 255);\n"
                "   border: 0px;\n"
                "}")




class CustomButton(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QtGui.QIcon("icono/nomostrar.png"))
        self.setStyleSheet("border-top-right-radius: 10px;\n" "border-bottom-right-radius: 10px;\n"
                           "border: solid;\n" "border-width: 1px 1px 1px 0px;")
    

    def enterEvent(self, event):
        self.setIcon(QtGui.QIcon("icono/nomostrar2.png"))
    

    def leaveEvent(self, event):
        self.setIcon(QtGui.QIcon("icono/nomostrar.png"))
