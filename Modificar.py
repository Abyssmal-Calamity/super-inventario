# Form implementation generated from reading ui file 'ventana4.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import csv


class Ui_ModifyWindow(object):
    def setupUi(self, ModifyWindow, MainWindow):
        ModifyWindow.setObjectName("ModifyWindow")
        ModifyWindow.resize(1261, 532)          # Resolucion ventana
        ModifyWindow.setMinimumSize(1261, 532)
        ModifyWindow.setMaximumSize(1261, 532)
        ModifyWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=ModifyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Add_products_screen.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Contadores de productos
        self.agregado1 = 0
        self.agregado2 = 0
        self.agregado3 = 0
        
        self.producto1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto1.setGeometry(QtCore.QRect(60, 230, 231, 21))
        self.producto1.setText(self.mostrar_producto(0))
        self.producto1.setObjectName("producto1")

        self.producto2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto2.setGeometry(QtCore.QRect(60, 260, 231, 21))
        self.producto2.setText(self.mostrar_producto(1))
        self.producto2.setObjectName("producto2")

        self.producto3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto3.setGeometry(QtCore.QRect(60, 290, 231, 21))
        self.producto3.setText(self.mostrar_producto(2))
        self.producto3.setObjectName("producto3")

        self.btnVolver = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnVolver.setGeometry(QtCore.QRect(40, 90, 100, 32))
        self.btnVolver.setStyleSheet(self.btn_style_sheet_1())
        self.btnVolver.setObjectName("BtnVolver")

        self.btnGuardar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(1090, 90, 100, 32))
        self.btnGuardar.setStyleSheet(self.btn_style_sheet_1())
        self.btnGuardar.setObjectName("btnGuardar")

        self.boton_add_prod3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_add_prod3.setGeometry(QtCore.QRect(300, 290, 31, 28))
        self.boton_add_prod3.setStyleSheet(self.btn_style_sheet_2())
        self.boton_add_prod3.setObjectName("boton_add_prod3")

        self.boton_add_prod2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_add_prod2.setGeometry(QtCore.QRect(300, 260, 31, 28))
        self.boton_add_prod2.setStyleSheet(self.btn_style_sheet_2())
        self.boton_add_prod2.setObjectName("boton_add_prod2")

        self.boton_add_prod1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_add_prod1.setGeometry(QtCore.QRect(300, 230, 31, 28))
        self.boton_add_prod1.setStyleSheet(self.btn_style_sheet_2())
        self.boton_add_prod1.setObjectName("boton_add_prod1")

        self.boton_remo_prod3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_remo_prod3.setGeometry(QtCore.QRect(370, 290, 31, 28))
        self.boton_remo_prod3.setStyleSheet(self.btn_style_sheet_2())
        self.boton_remo_prod3.setObjectName("boton_remo_prod3")

        self.boton_remo_prod2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_remo_prod2.setGeometry(QtCore.QRect(370, 260, 31, 28))
        self.boton_remo_prod2.setStyleSheet(self.btn_style_sheet_2())
        self.boton_remo_prod2.setObjectName("boton_remo_prod2")

        self.boton_remo_prod1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_remo_prod1.setGeometry(QtCore.QRect(370, 230, 31, 28))
        self.boton_remo_prod1.setStyleSheet(self.btn_style_sheet_2())
        self.boton_remo_prod1.setObjectName("boton_remo_prod1")

        self.disponible1 = 100 - self.agregado1
        self.cant_product1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cant_product1.setGeometry(QtCore.QRect(440, 230, 71, 21))
        self.cant_product1.setStyleSheet("h")
        self.cant_product1.setText(str(self.disponible1))
        self.cant_product1.setObjectName("cant_product1")

        self.disponible2 = 100 - self.agregado2
        self.cant_product2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cant_product2.setGeometry(QtCore.QRect(440, 260, 71, 21))
        self.cant_product2.setStyleSheet("h")
        self.cant_product2.setText(str(self.disponible2))
        self.cant_product2.setObjectName("cant_product2")

        self.disponible3 = 100 - self.agregado3
        self.cant_product3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cant_product3.setGeometry(QtCore.QRect(440, 290, 71, 21))
        self.cant_product3.setStyleSheet("h")
        self.cant_product3.setText(str(self.disponible3))
        self.cant_product3.setObjectName("cant_product3")

        self.prod1 = ""
        self.producto_adquirdo1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto_adquirdo1.setGeometry(QtCore.QRect(780, 220, 241, 21))
        self.producto_adquirdo1.setText(self.mostrar_agregados(0))
        self.producto_adquirdo1.setObjectName("producto_adquirdo1")
        self.producto_adquirdo1.setVisible(self.producto1_no_Agregado())

        self.prod2 = ""
        self.producto_adquirdo2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto_adquirdo2.setGeometry(QtCore.QRect(780, 250, 241, 21))
        self.producto_adquirdo2.setText(self.mostrar_agregados(1))
        self.producto_adquirdo2.setObjectName("producto_adquirdo2")
        self.producto_adquirdo2.setVisible(self.producto2_no_Agregado())

        self.prod3 = ""
        self.producto_adquirdo3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto_adquirdo3.setGeometry(QtCore.QRect(780, 280, 241, 21))
        self.producto_adquirdo3.setText(self.mostrar_agregados(2))
        self.producto_adquirdo3.setObjectName("producto_adquirdo3")
        self.producto_adquirdo3.setVisible(self.producto3_no_Agregado())

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 190, 61, 31))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(366, 190, 51, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 190, 71, 31))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")

        self.boton_aplicar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_aplicar.setGeometry(QtCore.QRect(444, 440, 130, 68))
        self.boton_aplicar.setStyleSheet(self.btn_style_sheet_1())
        self.boton_aplicar.setIcon(QtGui.QIcon("icono/icono-agregar.png"))
        self.boton_aplicar.setIconSize(QtCore.QSize(64, 64))
        self.boton_aplicar.setObjectName("boton_aplicar")

        self.thanos = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thanos.setGeometry(QtCore.QRect(1104, 440, 130, 68))
        self.thanos.setStyleSheet(self.btn_style_sheet_1())
        self.thanos.setIcon(QtGui.QIcon("icono/icono-quitar.png"))
        self.thanos.setIconSize(QtCore.QSize(64, 64))
        self.thanos.setObjectName("thanos")

        self.cantidad_final1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cantidad_final1.setGeometry(QtCore.QRect(710, 220, 51, 21))
        self.cantidad_final1.setStyleSheet("h")
        self.cantidad_final1.setText(str(self.agregado1))
        self.cantidad_final1.setObjectName("cantidad_final1")
        self.cantidad_final1.setVisible(self.producto1_no_Agregado())

        self.cantidad_final2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cantidad_final2.setGeometry(QtCore.QRect(710, 250, 51, 21))
        self.cantidad_final2.setStyleSheet("h")
        self.cantidad_final2.setText(str(self.agregado2))
        self.cantidad_final2.setObjectName("cantidad_final2")
        self.cantidad_final2.setVisible(self.producto2_no_Agregado())

        self.cantidad_final3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cantidad_final3.setGeometry(QtCore.QRect(710, 280, 51, 21))
        self.cantidad_final3.setStyleSheet("h")
        self.cantidad_final3.setText(str(self.agregado3))
        self.cantidad_final3.setObjectName("cantidad_final3")
        self.cantidad_final3.setVisible(self.producto3_no_Agregado())
        

        # Accion botones
        self.btnVolver.clicked.connect(lambda: self.volver_a_ventana_principal(ModifyWindow, MainWindow))
        
        self.boton_add_prod1.clicked.connect(self.addProd1)
        self.boton_add_prod1.clicked.connect(self.prod1Visible)
        self.boton_add_prod2.clicked.connect(self.addProd2)
        self.boton_add_prod2.clicked.connect(self.prod2Visible)
        self.boton_add_prod3.clicked.connect(self.addProd3)
        self.boton_add_prod3.clicked.connect(self.prod3Visible)

        self.boton_remo_prod1.clicked.connect(self.remoProd1)
        self.boton_remo_prod2.clicked.connect(self.remoProd2)
        self.boton_remo_prod3.clicked.connect(self.remoProd3)

        self.boton_aplicar.clicked.connect(self.guardar_cambios)
        self.thanos.clicked.connect(self.eliminarTodo)


        ModifyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ModifyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 22))
        self.menubar.setObjectName("menubar")
        ModifyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ModifyWindow)
        self.statusbar.setObjectName("statusbar")
        ModifyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyWindow)
        QtCore.QMetaObject.connectSlotsByName(ModifyWindow)
    

    def volver_a_ventana_principal(self, modifyW, mainW):
        mainW.show()
        modifyW.close()
    

    def mostrar_producto(self, i):
        with open("ArchivosCSV/Productos.csv", "r", encoding="utf-8") as F:
            datos = csv.reader(F, delimiter=',')
            next(datos)
            producto = list(datos)

            if i == 0:
                self.agregado1 = int(producto[i][3])
            elif i == 1:
                self.agregado2 = int(producto[i][3])
            elif i == 2:
                self.agregado3 = int(producto[i][3])
        
        return (producto[i][1] + " " + producto[i][0])
    

    def mostrar_agregados(self, i):
        with open("ArchivosCSV/Productos.csv", "r", encoding="utf-8") as F:
            datos = csv.reader(F, delimiter=',')
            next(datos)
            producto = list(datos)

        if i == 0:
            self.prod1 = producto[i][1]
        elif i == 1:
            self.prod2 = producto[i][1]
        elif i == 2:
            self.prod3 = producto[i][1]
        
        return (producto[i][1] + " " + producto[i][0])
    

    def producto1_no_Agregado(self):
        if self.agregado1 == 0:
            return False
        else:
            return True
    

    def producto2_no_Agregado(self):
        if self.agregado2 == 0:
            return False
        else:
            return True
    

    def producto3_no_Agregado(self):
        if self.agregado3 == 0:
            return False
        else:
            return True
    
    
    def prod1Visible(self):
        if self.agregado1 > 0:
            self.producto_adquirdo1.setVisible(True)
            self.cantidad_final1.setVisible(True)
    

    def prod2Visible(self):
        if self.agregado2 > 0:
            self.producto_adquirdo2.setVisible(True)
            self.cantidad_final2.setVisible(True)
    

    def prod3Visible(self):
        if self.agregado3 > 0:
            self.producto_adquirdo3.setVisible(True)
            self.cantidad_final3.setVisible(True)
    

    def addProd1(self):
        if self.disponible1 > 0:
            self.agregado1 += 1
            self.disponible1 -= 1
            self.cantidad_final1.setText(str(self.agregado1))
            self.cant_product1.setText(str(self.disponible1))
    

    def addProd2(self):
        if self.disponible2 > 0:
            self.agregado2 += 1
            self.disponible2 -= 1
            self.cantidad_final2.setText(str(self.agregado2))
            self.cant_product2.setText(str(self.disponible2))
    

    def addProd3(self):
        if self.disponible3 > 0:
            self.agregado3 += 1
            self.disponible3 -= 1
            self.cantidad_final3.setText(str(self.agregado3))
            self.cant_product3.setText(str(self.disponible3))
    

    def remoProd1(self):
        if self.agregado1 > 0:
            self.agregado1 -= 1
            self.disponible1 += 1
            self.cantidad_final1.setText(str(self.agregado1))
            self.cant_product1.setText(str(self.disponible1))
    

    def remoProd2(self):
        if self.agregado2 > 0:
            self.agregado2 -= 1
            self.disponible2 += 1
            self.cantidad_final2.setText(str(self.agregado2))
            self.cant_product2.setText(str(self.disponible2))
    

    def remoProd3(self):
        if self.agregado3 > 0:
            self.agregado3 -= 1
            self.disponible3 += 1
            self.cantidad_final3.setText(str(self.agregado3))
            self.cant_product3.setText(str(self.disponible3))
    

    def guardar_cambios(self):
        producto1 = self.prod1
        producto2 = self.prod2
        producto3 = self.prod3

        with open("ArchivosCSV/Productos.csv", "r", encoding="utf-8") as file:
            products = csv.reader(file)
            lista = list(products)

            lista[1][3] = self.agregado1
            lista[2][3] = self.agregado2
            lista[3][3] = self.agregado3
        
        with open("ArchivosCSV/Productos.csv", "w", encoding="utf-8", newline='') as f:
            guardar = csv.writer(f)
            guardar.writerows(lista)
        
        print("Cambios guardados con éxito")
    

    def eliminarTodo(self):
        self.agregado1 = 0
        self.cantidad_final1.setText(str(self.agregado1))
        self.cantidad_final1.setVisible(self.producto1_no_Agregado())
        self.producto_adquirdo1.setVisible(self.producto1_no_Agregado())
        self.agregado2 = 0
        self.cantidad_final2.setText(str(self.agregado2))
        self.cantidad_final2.setVisible(self.producto2_no_Agregado())
        self.producto_adquirdo2.setVisible(self.producto2_no_Agregado())
        self.agregado3 = 0
        self.cantidad_final3.setText(str(self.agregado3))
        self.cantidad_final3.setVisible(self.producto3_no_Agregado())
        self.producto_adquirdo3.setVisible(self.producto3_no_Agregado())

        self.disponible1 = 100 - self.agregado1
        self.cant_product1.setText(str(self.disponible1))
        self.disponible2 = 100 - self.agregado2
        self.cant_product2.setText(str(self.disponible2))
        self.disponible3 = 100 - self.agregado3
        self.cant_product3.setText(str(self.disponible3))
        
        self.guardar_cambios()
    

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
        return ("QPushButton{\n"
                "   background-color: rgb(235, 235, 235);\n"
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

    
    def retranslateUi(self, ModifyWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyWindow.setWindowTitle(_translate("ModifyWindow", "MainWindow"))
        self.btnVolver.setText(_translate("ModifyWindow", "Volver"))
        self.btnGuardar.setText(_translate("ModifyWindow", "Guardar"))
        self.boton_add_prod3.setText(_translate("ModifyWindow", "+1"))
        self.boton_add_prod2.setText(_translate("ModifyWindow", "+1"))
        self.boton_add_prod1.setText(_translate("ModifyWindow", "+1"))
        self.label_2.setText(_translate("ModifyWindow", "<html><head/><body><p>Agregar</p></body></html>"))
        self.label_3.setText(_translate("ModifyWindow", "<html><head/><body><p>Quitar</p></body></html>"))
        self.boton_remo_prod3.setText(_translate("ModifyWindow", "-1"))
        self.boton_remo_prod2.setText(_translate("ModifyWindow", "-1"))
        self.boton_remo_prod1.setText(_translate("ModifyWindow", "-1"))
        self.label_4.setText(_translate("ModifyWindow", "<html><head/><body><p>Cantidad</p></body></html>"))
