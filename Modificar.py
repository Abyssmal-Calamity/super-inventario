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
        ModifyWindow.resize(1256, 546)
        self.centralwidget = QtWidgets.QWidget(parent=ModifyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1241, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagenes para TPA/Add_products_screen.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.producto1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto1.setGeometry(QtCore.QRect(50, 230, 231, 21))
        self.producto1.setText(self.mostrar_producto(0))
        self.producto1.setObjectName("producto1")

        self.producto2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto2.setGeometry(QtCore.QRect(50, 260, 231, 21))
        self.producto2.setText(self.mostrar_producto(1))
        self.producto2.setObjectName("producto2")

        self.producto3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto3.setGeometry(QtCore.QRect(50, 290, 231, 21))
        self.producto3.setText(self.mostrar_producto(2))
        self.producto3.setObjectName("producto3")

        self.boton_add_prod3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_add_prod3.setGeometry(QtCore.QRect(290, 290, 31, 28))
        self.boton_add_prod3.setObjectName("boton_add_prod3")
        self.boton_add_prod2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_add_prod2.setGeometry(QtCore.QRect(290, 260, 31, 28))
        self.boton_add_prod2.setObjectName("boton_add_prod2")
        self.boton_add_prod1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_add_prod1.setGeometry(QtCore.QRect(290, 230, 31, 28))
        self.boton_add_prod1.setObjectName("boton_add_prod1")
        self.cant_product1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cant_product1.setGeometry(QtCore.QRect(430, 230, 71, 21))
        self.cant_product1.setStyleSheet("h")
        self.cant_product1.setObjectName("cant_product1")
        self.producto_adquirdo2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto_adquirdo2.setGeometry(QtCore.QRect(770, 250, 241, 21))
        self.producto_adquirdo2.setObjectName("producto_adquirdo2")
        self.producto_adquirdo1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto_adquirdo1.setGeometry(QtCore.QRect(770, 220, 241, 21))
        self.producto_adquirdo1.setObjectName("producto_adquirdo1")
        self.producto_adquirdo3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.producto_adquirdo3.setGeometry(QtCore.QRect(770, 280, 241, 21))
        self.producto_adquirdo3.setObjectName("producto_adquirdo3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 190, 61, 41))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 200, 51, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.boton_remo_prod3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_remo_prod3.setGeometry(QtCore.QRect(360, 290, 31, 28))
        self.boton_remo_prod3.setObjectName("boton_remo_prod3")
        self.boton_remo_prod2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_remo_prod2.setGeometry(QtCore.QRect(360, 260, 31, 28))
        self.boton_remo_prod2.setObjectName("boton_remo_prod2")
        self.boton_remo_prod1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_remo_prod1.setGeometry(QtCore.QRect(360, 230, 31, 28))
        self.boton_remo_prod1.setObjectName("boton_remo_prod1")
        self.boton_aplicar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_aplicar.setGeometry(QtCore.QRect(310, 400, 131, 28))
        self.boton_aplicar.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.boton_aplicar.setObjectName("boton_aplicar")
        self.cant_product3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cant_product3.setGeometry(QtCore.QRect(430, 290, 71, 21))
        self.cant_product3.setStyleSheet("h")
        self.cant_product3.setObjectName("cant_product3")
        self.cant_product2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cant_product2.setGeometry(QtCore.QRect(430, 260, 71, 21))
        self.cant_product2.setStyleSheet("h")
        self.cant_product2.setObjectName("cant_product2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 190, 71, 31))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.thanos = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thanos.setGeometry(QtCore.QRect(910, 390, 131, 28))
        self.thanos.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.thanos.setObjectName("thanos")
        self.cantidad_final1 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cantidad_final1.setGeometry(QtCore.QRect(700, 220, 41, 21))
        self.cantidad_final1.setStyleSheet("h")
        self.cantidad_final1.setObjectName("cantidad_final1")
        self.cantidad_final3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cantidad_final3.setGeometry(QtCore.QRect(700, 280, 41, 21))
        self.cantidad_final3.setStyleSheet("h")
        self.cantidad_final3.setObjectName("cantidad_final3")
        self.cantidad_final2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.cantidad_final2.setGeometry(QtCore.QRect(700, 250, 41, 21))
        self.cantidad_final2.setStyleSheet("h")
        self.cantidad_final2.setObjectName("cantidad_final2")
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
    

    def mostrar_producto(self, i):
        with open("ArchivosCSV/Productos.csv", "r", encoding="utf-8") as F:
            datos = csv.reader(F, delimiter=',')
            next(datos)
            producto = list(datos)
        
        return (producto[i][1] + " " + producto[i][0])

    
    def retranslateUi(self, ModifyWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyWindow.setWindowTitle(_translate("ModifyWindow", "MainWindow"))
        self.boton_add_prod3.setText(_translate("ModifyWindow", "+1"))
        self.boton_add_prod2.setText(_translate("ModifyWindow", "+1"))
        self.boton_add_prod1.setText(_translate("ModifyWindow", "+1"))
        self.label_2.setText(_translate("ModifyWindow", "<html><head/><body><p>agregar</p></body></html>"))
        self.label_3.setText(_translate("ModifyWindow", "<html><head/><body><p>Quitar</p></body></html>"))
        self.boton_remo_prod3.setText(_translate("ModifyWindow", "+1"))
        self.boton_remo_prod2.setText(_translate("ModifyWindow", "+1"))
        self.boton_remo_prod1.setText(_translate("ModifyWindow", "+1"))
        self.boton_aplicar.setText(_translate("ModifyWindow", "Aplicar Cambiós"))
        self.label_4.setText(_translate("ModifyWindow", "<html><head/><body><p>cantidad</p></body></html>"))
        self.thanos.setText(_translate("ModifyWindow", "borrar todo"))
