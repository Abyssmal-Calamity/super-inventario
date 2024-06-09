# Form implementation generated from reading ui file 'Consultar_inventario.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from clases.Productos import Productos

class Ui_ShowInventary(object):

    def setupUi(self, ShowInventary, MainWindow):
        ShowInventary.setObjectName("ShowInventary")
        ShowInventary.resize(1261, 532)
        ShowInventary.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=ShowInventary)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/Consultar_screen.jpg"))
        self.background.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.background.setObjectName("background")

        self.btnVolver = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.cerrarVentana(MainWindow, ShowInventary))
        self.btnVolver.setGeometry(QtCore.QRect(1120, 90, 100, 32))
        self.btnVolver.setStyleSheet("QPushButton{\n"
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
        self.btnVolver.setObjectName("btnVolver")
        
        self.userLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(130, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLabel.setFont(font)
        self.userLabel.setText("")
        self.userLabel.setObjectName("userLabel")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 140, 1160, 358))
        self.scrollArea.setStyleSheet("border-radius: 0px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1143, 478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Carga la lista de productos del archivo CSV
        lista_productos = Productos.cargar_productos_CSV()

        # Se crea un panel grid para cargar los productos del archivo csv y mostrarlos en este mismo
        panel_grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        panel_grid.setHorizontalSpacing(20)
        panel_grid.setVerticalSpacing(20)

        # Se inicializan las filas y columnas para organizar los productos en el panel grid
        fila = 0
        columna = 0

        for producto in lista_productos:
            # Carga la imagen respecto al nombre del producto
            nombre_producto = producto.get_nombre()
            ruta_imagen = "productos/" + nombre_producto + ".jpg"
            imagen_producto = QtGui.QPixmap(ruta_imagen)
            
            # Si no hay imagen carga una por defecto
            if imagen_producto.isNull():
                imagen_producto = QtGui.QPixmap("productos/No_Imagen.jpg") 
                imagen_producto = imagen_producto.scaled(250, 250, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

            # Cambia el tamaño de la imagen y lo hace de 250x250 manteniendo el aspect ratio
            imagen_producto = imagen_producto.scaled(250, 250, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

            # Crea un label para la imagen del producto
            label_imagen = QtWidgets.QLabel()
            label_imagen.setPixmap(imagen_producto)
            label_imagen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            # Crea un label para el nombre del producto
            nombre_producto = producto.get_nombre()
            producto_texto = "Producto: " + nombre_producto
            label_producto = QtWidgets.QLabel(producto_texto)
            label_producto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            # Crea un label para la cantidad del producto
            cantidad = producto.get_cantidad()
            cantidad_texto = "Cantidad: " + cantidad
            label_cantidad = QtWidgets.QLabel(cantidad_texto)
            label_cantidad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
            # Crea un label para la precio del producto
            precio = producto.get_precio()
            precio_texto = "Precio: " + precio
            label_precio = QtWidgets.QLabel(precio_texto)
            label_precio.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            # Se crea una verticalbox para organizar los productos por imagen, nombre y cantidad en vertical
            layout_producto = QtWidgets.QVBoxLayout()
            layout_producto.setSpacing(0)
            layout_producto.addWidget(label_imagen)
            layout_producto.addWidget(label_producto)
            layout_producto.addWidget(label_cantidad)
            layout_producto.addWidget(label_precio)

            # Se añade el verticalbox al panel grid
            panel_grid.addLayout(layout_producto, fila, columna)

            # Avanza una columna por cada producto, al pasar los 3 productos salta de linea
            columna += 1
            if columna >= 3:
                columna = 0
                fila += 1

        # Se hace que el panel grid sea scrolleable
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        ShowInventary.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ShowInventary)
        self.statusbar.setObjectName("statusbar")
        ShowInventary.setStatusBar(self.statusbar)

        self.retranslateUi(ShowInventary)
        QtCore.QMetaObject.connectSlotsByName(ShowInventary)

    def retranslateUi(self, ShowInventary):
        _translate = QtCore.QCoreApplication.translate
        ShowInventary.setWindowTitle(_translate("ShowInventary", "MainWindow"))
        self.btnVolver.setText(_translate("ShowInventary", "Volver"))

    def cerrarVentana(self, main_w, consul_w):
        main_w.show()
        consul_w.close()
