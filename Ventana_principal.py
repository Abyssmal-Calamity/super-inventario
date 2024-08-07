# Form implementation generated from reading ui file 'ventana2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

# Se importa las vistas
from Modificar import Ui_ModifyWindow
from Consultar import Ui_ShowInventary
from Seleccionar_Productos import Ui_SelectProducts
from Agregar_productos import Ui_AgregarP
from ListaUsuarios import Ui_VentanaListaUsuarios


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, Login, Usuario, Cargo):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 532)        # Resolucion ventana
        MainWindow.setMinimumSize(1261, 532)
        MainWindow.setMaximumSize(1261, 532)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        # Imagenes
        self.backgroud = QtWidgets.QLabel(parent=self.centralwidget)    # Imagen de fondo
        self.backgroud.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.backgroud.setText("")
        self.backgroud.setPixmap(QtGui.QPixmap("images/Screen_2_JPG.jpg"))
        self.backgroud.setObjectName("backgroud")

        #self.thomas = QtWidgets.QLabel(parent=self.centralwidget)       # Imagen del Thomas puesto como meme
        #self.thomas.setGeometry(QtCore.QRect(995, 278, 256, 256))
        #self.thomas.setStyleSheet("background:transparent;")
        #self.thomas.setText("")
        #self.thomas.setPixmap(QtGui.QPixmap("images/thomas.png"))
        #self.thomas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #self.thomas.setObjectName("thomas")

        
        # Etiquetas
        self.userLabel = QtWidgets.QLabel(parent=self.centralwidget)        # Muestra el nombre de usuario
        self.userLabel.setGeometry(QtCore.QRect(150, 80, 171, 39))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("background: transparent;")
        self.userLabel.setText(Usuario)
        self.userLabel.setObjectName("userLabel")

        
        # Interfaz botones
        self.logoutButton = QtWidgets.QPushButton(parent=self.centralwidget)    # Boton cerrar sesion
        self.logoutButton.setGeometry(QtCore.QRect(18, 132, 90, 60))
        self.logoutButton.setStyleSheet(self.btn_style_sheet())
        self.logoutButton.setObjectName("logoutButton")

        self.modify_invBtn = QtWidgets.QPushButton(parent=self.centralwidget)   # Boton modificar inventario
        self.modify_invBtn.setGeometry(QtCore.QRect(826, 290, 171, 61))
        self.modify_invBtn.setStyleSheet(self.btn_style_sheet())
        self.modify_invBtn.setObjectName("modify_invBtn")
        
        self.select_invBtn = QtWidgets.QPushButton(parent=self.centralwidget)   # Boton seleccionar productos
        self.select_invBtn.setGeometry(QtCore.QRect(548, 290, 171, 61))
        self.select_invBtn.setStyleSheet(self.btn_style_sheet())
        self.select_invBtn.setObjectName("select_invBtn")

        self.show_invBtn = QtWidgets.QPushButton(parent=self.centralwidget)     # Boton consultar inventario
        self.show_invBtn.setGeometry(QtCore.QRect(266, 290, 171, 61))
        self.show_invBtn.setStyleSheet(self.btn_style_sheet())
        self.show_invBtn.setObjectName("show_invBtn")

        self.btnAdministrarUsers = QtWidgets.QPushButton(parent=self.centralwidget)    # Boton para despedir un empleado
        self.btnAdministrarUsers.setGeometry(QtCore.QRect(18, 420, 120, 60))
        self.btnAdministrarUsers.setStyleSheet(self.btn_style_sheet())
        self.btnAdministrarUsers.setObjectName("btnAdministrarUsers")

        self.btnAgregar= QtWidgets.QPushButton(parent=self.centralwidget)    # Boton agregar productos
        self.btnAgregar.setGeometry(QtCore.QRect(1090, 430, 143, 60))
        self.btnAgregar.setStyleSheet(self.btn_style_sheet())
        self.btnAgregar.setObjectName("btnAgregar")
        
        # Nueva restricción: Se deshabilitará la opción de modificar el inventario si un usuario es Empleado
        self.modify_invBtn.setVisible(self.RestriccionEmpleado(Cargo))
        self.btnAgregar.setVisible(self.RestriccionEmpleado(Cargo))

        # Opción exclusiva para administradores
        self.btnAdministrarUsers.setVisible(self.btnDespedirVisible(Cargo))

        
        # Accion botones
        self.logoutButton.clicked.connect(lambda: self.gui_Logoff(Login, MainWindow))

        self.modify_invBtn.clicked.connect(lambda: self.modificarInv(MainWindow))
        
        self.select_invBtn.clicked.connect(lambda: self.selectInv(MainWindow))

        self.show_invBtn.clicked.connect(lambda: self.consultarInv(MainWindow))

        self.btnAgregar.clicked.connect(lambda: self.gui_agregar(MainWindow))

        self.btnAdministrarUsers.clicked.connect(lambda: self.verListaUsuarios(MainWindow, Usuario))

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logoutButton.setText(_translate("MainWindow", "Cerrar\nsesión"))
        self.modify_invBtn.setText(_translate("MainWindow", "Modificar inventario"))
        self.show_invBtn.setText(_translate("MainWindow", "Consultar inventario"))
        self.select_invBtn.setText(_translate("MainWindow", "Caja para empleados"))
        self.btnAdministrarUsers.setText(_translate("MainWindow", "Administrar\nusuarios"))
        self.btnAgregar.setText(_translate("Login", "Agregar nuevos\nproductos"))
    

    def RestriccionEmpleado(self, ocupacion):   # Retorna valor booleano que restringe las acciones de un empleado
        if ocupacion == "Empleado":
            self.select_invBtn.setGeometry(QtCore.QRect(826, 290, 171, 61))
            return False
        else:
            return True
    
    def btnDespedirVisible(self, ocupacion):
        if ocupacion == "Administrador":
            return True
        else:
            return False
    
    
    def gui_Logoff(self, login, main_w):            # Metodo para cerrar sesion
        login.show()
        main_w.close()
    

    def gui_agregar(self, mainWindow):     # Metodo para abrir ventana de agregado de nuevos productos
        self.ventanaAgregarP = QtWidgets.QMainWindow()      # Se abre la ventana de agregado
        self.ui = Ui_AgregarP()
        self.ui.setupUi(self.ventanaAgregarP, mainWindow)
        self.ventanaAgregarP.setWindowTitle("ULAGOS Market")
        self.ventanaAgregarP.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
        self.ventanaAgregarP.show()

        mainWindow.close()
    
    
    def modificarInv(self, mainWindow):             # Metodo para modificar inventario
        # Se abre la ventana modificar inventario
        self.ventModif = QtWidgets.QMainWindow()
        self.Ui = Ui_ModifyWindow()
        self.Ui.setupUi(self.ventModif, mainWindow)
        self.ventModif.setWindowTitle("ULAGOS Market")
        self.ventModif.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
        self.ventModif.show()

        mainWindow.close()
        
    def selectInv(self, mainWindow):                # Metodo para seleccionar productos
        # Se abre la ventana seleccionar productos
        self.ventSelect = QtWidgets.QMainWindow()
        self.Ui = Ui_SelectProducts()
        self.Ui.setupUi(self.ventSelect, mainWindow)
        self.ventSelect.setWindowTitle("ULAGOS Market")
        self.ventSelect.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
        self.ventSelect.show()

        mainWindow.close()
    
    
    def consultarInv(self, mainWindow):             # Metodo para consultar inventario
        # Se abre la ventana consultar inventario
        self.ventCons = QtWidgets.QMainWindow()
        self.Ui = Ui_ShowInventary()
        self.Ui.setupUi(self.ventCons, mainWindow)
        self.ventCons.setWindowTitle("ULAGOS Market")
        self.ventCons.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
        self.ventCons.show()

        mainWindow.close()
    

    def verListaUsuarios(self, mainWindow, usuario):
        self.ventanaUsuarios = QtWidgets.QMainWindow()
        self.Ui = Ui_VentanaListaUsuarios()
        self.Ui.setupUi(self.ventanaUsuarios, mainWindow, usuario)
        self.ventanaUsuarios.setWindowTitle("ULAGOS Market")
        self.ventanaUsuarios.setWindowIcon(QtGui.QIcon("icono\\martin.png"))
        self.ventanaUsuarios.show()

        mainWindow.close()
    

    def btn_style_sheet(self):
        return ("QPushButton{\n"
                "   font: 600 12pt \"Segoe UI Semibold\";\n"
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
