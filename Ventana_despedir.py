from PyQt6 import QtCore, QtGui, QtWidgets
import csv

class Ui_DespedirEmpleados(object):

    def setupUi(self, DespedirEmp, MainWindow):
        DespedirEmp.setObjectName("DespedirEmp")
        DespedirEmp.resize(1261, 532)        # Resolucion ventana
        DespedirEmp.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=DespedirEmp)
        self.centralwidget.setObjectName("centralwidget")

        
        # Imagenes
        self.backgroud = QtWidgets.QLabel(parent=self.centralwidget)    # Imagen de fondo
        self.backgroud.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.backgroud.setText("")
        self.backgroud.setPixmap(QtGui.QPixmap("images/Screen_2_JPG.jpg"))
        self.backgroud.setObjectName("backgroud")

        
        # Etiquetas

        
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

        self.despedirEmp = QtWidgets.QPushButton(parent=self.centralwidget)    # Boton para despedir un empleado
        self.despedirEmp.setGeometry(QtCore.QRect(18, 220, 90, 60))
        self.despedirEmp.setStyleSheet(self.btn_style_sheet())
        self.despedirEmp.setObjectName("despedirEmp")
        
        
        # Accion botones
        #self.logoutButton.clicked.connect(lambda: self.gui_Logoff(Login, MainWindow))

        #self.modify_invBtn.clicked.connect(lambda: self.modificarInv(MainWindow))
        
        #self.select_invBtn.clicked.connect(lambda: self.selectInv(MainWindow))

        #self.show_invBtn.clicked.connect(lambda: self.consultarInv(MainWindow))

        
        DespedirEmp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=DespedirEmp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        DespedirEmp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=DespedirEmp)
        self.statusbar.setObjectName("statusbar")
        DespedirEmp.setStatusBar(self.statusbar)

        self.retranslateUi(DespedirEmp)
        QtCore.QMetaObject.connectSlotsByName(DespedirEmp)

    
    def retranslateUi(self, DespedirEmp):
        _translate = QtCore.QCoreApplication.translate
        DespedirEmp.setWindowTitle(_translate("DespedirEmp", "DespedirEmp"))
        self.logoutButton.setText(_translate("DespedirEmp", "Cerrar\nsesión"))
        self.modify_invBtn.setText(_translate("DespedirEmp", "Modificar inventario"))
        self.show_invBtn.setText(_translate("DespedirEmp", "Consultar inventario"))
        self.select_invBtn.setText(_translate("DespedirEmp", "Seleccionar productos"))
        self.despedirEmp.setText(_translate("DespedirEmp", "Despedir\nempleado"))
