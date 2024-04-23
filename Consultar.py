# Form implementation generated from reading ui file 'ventana4.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ShowInventary(object):
    def cerrarVentana(self, main_w, consul_w):
        main_w.show()
        consul_w.close()
    
    def setupUi(self, ShowInventary, MainWindow):
        ShowInventary.setObjectName("ShowInventary")
        ShowInventary.resize(1261, 532)
        ShowInventary.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n" "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=ShowInventary)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/Screen_2_JPG.jpg"))
        self.background.setObjectName("background")

        # # Interfaz botones con operaciones lambda
        self.btnVolver = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.cerrarVentana(MainWindow, ShowInventary))    #lambda
        self.btnVolver.setGeometry(QtCore.QRect(190, 81, 131, 41))
        self.btnVolver.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.btnVolver.setObjectName("btnVolver")

        ShowInventary.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ShowInventary)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        ShowInventary.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ShowInventary)
        self.statusbar.setObjectName("statusbar")
        ShowInventary.setStatusBar(self.statusbar)

        self.retranslateUi(ShowInventary)
        QtCore.QMetaObject.connectSlotsByName(ShowInventary)

    def retranslateUi(self, ShowInventary):
        _translate = QtCore.QCoreApplication.translate
        ShowInventary.setWindowTitle(_translate("ShowInventary", "MainWindow"))
        self.btnVolver.setText(_translate("ShowInventary", "Volver"))
