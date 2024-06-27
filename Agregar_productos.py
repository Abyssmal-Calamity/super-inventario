# Form implementation generated from reading ui file 'registro.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator
import csv
from clases.Productos import Productos


class Ui_AgregarP(object):
    
    def setupUi(self, AgregarP, MainWindow):
        self.AgregarP = AgregarP
        self.AgregarP.setObjectName("AgregarP")
        self.AgregarP.resize(1261, 532)         # Resolucion ventana
        self.AgregarP.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=self.AgregarP)
        self.centralwidget.setObjectName("centralwidget")

        # Etiquetas
        self.fondo = QtWidgets.QLabel(parent=self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.fondo.setText("")
        self.fondo.setPixmap(QtGui.QPixmap("images/NewProducts_screen.jpg"))
        self.fondo.setObjectName("fondo")

        self.texto1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.texto1.setGeometry(QtCore.QRect(100, 250, 300, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto1.setFont(font)
        self.texto1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.texto1.setStyleSheet("background: transparent;\n" "color: rgb(225,0,0);\n")
        self.texto1.setText("")
        self.texto1.setObjectName("texto1")

        self.texto2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.texto2.setGeometry(QtCore.QRect(470, 250, 300, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto2.setFont(font)
        self.texto2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.texto2.setStyleSheet("background: transparent;\n" "color: rgb(225,0,0);\n")
        self.texto2.setText("")
        self.texto2.setObjectName("texto2")
        
        self.texto3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.texto3.setGeometry(QtCore.QRect(100, 350, 300, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto3.setFont(font)
        self.texto3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.texto3.setStyleSheet("background: transparent;\n" "color: rgb(225,0,0);\n")
        self.texto3.setText("")
        self.texto3.setObjectName("texto3")

        self.texto4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.texto4.setGeometry(QtCore.QRect(470, 350, 300, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto4.setFont(font)
        self.texto4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.texto4.setStyleSheet("background: transparent;\n" "color: rgb(225,0,0);\n")
        self.texto4.setText("")
        self.texto4.setObjectName("texto4")

        self.marca = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.marca.setFont(font)
        self.marca.setGeometry(QtCore.QRect(95, 220, 300, 40))
        self.marca.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
        self.marca.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.marca.setObjectName("marca")
        
        self.nombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nombre.setFont(font)
        self.nombre.setGeometry(QtCore.QRect(465, 220, 300, 40))
        self.nombre.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
        self.nombre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre.setObjectName("nombre")

        self.precio = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.precio.setFont(font)
        self.precio.setGeometry(QtCore.QRect(95, 340, 300, 40))
        self.precio.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
        self.precio.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.precio.setValidator(QIntValidator(1,9999999))
        self.precio.setObjectName("precio")
        
        self.cantidad = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cantidad.setFont(font)
        self.cantidad.setGeometry(QtCore.QRect(465, 340, 300, 40))
        self.cantidad.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
        self.cantidad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cantidad.setValidator(QIntValidator(1,9999))
        self.cantidad.setObjectName("cantidad")
    
        # Interfaz botones
        self.btnCrear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCrear.setGeometry(QtCore.QRect(900, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btnCrear.setFont(font)
        self.btnCrear.setStyleSheet(self.btn_style_sheet_1())
        self.btnCrear.setObjectName("btnCrear")
        
        self.btnCancelar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(900, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet(self.btn_style_sheet_1())
        self.btnCancelar.setObjectName("btnCancelar")


        # Accion botones
        self.btnCrear.clicked.connect(lambda: self.validacionCampos(MainWindow))

        self.btnCancelar.clicked.connect(lambda: self.cancelar(MainWindow))
        

        self.AgregarP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.AgregarP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        self.AgregarP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.AgregarP)
        self.statusbar.setObjectName("statusbar")
        self.AgregarP.setStatusBar(self.statusbar)

        self.retranslateUi(self.AgregarP)
        QtCore.QMetaObject.connectSlotsByName(self.AgregarP)

    
    def retranslateUi(self, AgregarP):
        _translate = QtCore.QCoreApplication.translate
        AgregarP.setWindowTitle(_translate("AgregarP", "MainWindow"))
        self.btnCancelar.setText(_translate("AgregarP", "CANCELAR"))
        self.btnCrear.setText(_translate("AgregarP", "CREAR"))

    

    def validacionCampos(self, mainWindow):
        camposValidados = True

        if self.marca.text() == "":
            self.marca.setStyleSheet("border-radius: 10px;\n" "border: 2px solid rgb(255, 0, 0);")
            self.texto1.setText("Este campo es obligatorio")
            camposValidados = False
        else:
            self.marca.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
            self.texto1.setText("")
            
        if self.nombre.text() == "":
            self.nombre.setStyleSheet("border-radius: 10px;\n" "border: 2px solid rgb(255, 0, 0);")
            self.texto2.setText("Este campo es obligatorio")
            camposValidados = False
        elif self.producto_existente():
            self.nombre.setStyleSheet("border-radius: 10px;\n" "border: 2px solid rgb(255, 0, 0);")
            self.texto2.setText("Ya existe un producto registrado con este nombre")
            camposValidados = False
        else:
            self.nombre.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
            self.texto2.setText("")
        
        if self.precio.text() == "":
            self.precio.setStyleSheet("border-radius: 10px;\n" "border: 2px solid rgb(255, 0, 0);")
            self.texto3.setText("Este campo es obligatorio")
            camposValidados = False
        else:
            self.precio.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
            self.texto3.setText("")
            
        if self.cantidad.text() == "":
            self.cantidad.setStyleSheet("border-radius: 10px;\n" "border: 2px solid rgb(255, 0, 0);")
            self.texto4.setText("Este campo es obligatorio")
            camposValidados = False
        else:
            self.cantidad.setStyleSheet("border-radius: 10px;\n" "border: 1px solid;")
            self.texto4.setText("")
        
        if camposValidados:
            self.crearProducto()
            self.cuadroProductoCreado(mainWindow)


    def crearProducto(self):                 # Metodo para almacenar datos del nuevo producto
        marca = self.marca.text()
        nombre = self.nombre.text()
        precio = self.precio.text()
        cantidad = self.cantidad.text()
        
        Productos.agregar_producto(marca, nombre, precio, cantidad)        
    
    def producto_existente(self):        # Metodo para comprobar si ya existe un producto que se intento crear
        with open("ArchivosCSV/Productos.csv", "r", encoding="utf-8") as archivo:
            users = csv.reader(archivo, delimiter=',')
            next(users)
            
            for row in users:
                if row[1] == self.nombre.text():
                    return True
        
        return False

    

    def cuadroProductoCreado(self, mainWindow):       # Se muestra un mensaje de usuario creado
        self.notificacion = QtWidgets.QMessageBox()
        self.notificacion.setWindowTitle("Producto creado")
        self.notificacion.setText("Se ha creado con éxito")
        self.notificacion.setIcon(QtWidgets.QMessageBox.Icon.Information)
        self.notificacion.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        btnAceptar = self.notificacion.button(QtWidgets.QMessageBox.StandardButton.Ok)
        btnAceptar.setText("Aceptar")
        btnAceptar.clicked.connect(lambda: self.volver_A_VentanaPrincipal(mainWindow))

        self.notificacion.exec()

    
    def cancelar(self, main_w):                     # Metodo para cancelar registro de usuario
        main_w.show()
        self.AgregarP.close()
    

    def volver_A_VentanaPrincipal(self, main_w):      # Metodo para mostrar ventana principal
        main_w.show()
        self.AgregarP.close()
    

    def btn_style_sheet_1(self):
        return ("QPushButton{\n"
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
                "   background-color: rgb(255, 0, 255);\n"
                "   color: rgb(255, 255, 255);\n"
                "   border: 0px;\n"
                "}")
    

    def btn_style_sheet_2(self):
        return ("background-color: rgba(255, 85, 255, 0.75);\n"
                "border-radius: 10px;\n"
                "color: rgb(255, 255, 255);")




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