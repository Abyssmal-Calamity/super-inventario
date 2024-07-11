from PyQt6 import QtCore, QtGui, QtWidgets
import csv

class Ui_VentanaListaUsuarios(object):

    def setupUi(self, ListaEmp, MainWindow, Usuario):
        ListaEmp.setObjectName("ListaEmp")
        ListaEmp.resize(1261, 532)        # Resolucion ventana
        ListaEmp.setMinimumSize(1261, 532)
        ListaEmp.setMaximumSize(1261, 532)
        ListaEmp.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=ListaEmp)
        self.centralwidget.setObjectName("centralwidget")
        self.Usuario = Usuario

        
        # Imagenes
        self.backgroud = QtWidgets.QLabel(parent=self.centralwidget)    # Imagen de fondo
        self.backgroud.setGeometry(QtCore.QRect(10, 0, 1241, 511))
        self.backgroud.setText("")
        self.backgroud.setPixmap(QtGui.QPixmap("images/admin_user_screen.jpg"))
        self.backgroud.setObjectName("backgroud")

        
        # Interfaz botones
        self.BtnDespedir = QtWidgets.QPushButton(parent=self.centralwidget)    # Boton para despedir un empleado
        self.BtnDespedir.setGeometry(QtCore.QRect(610, 440, 180, 44))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.BtnDespedir.setFont(font)
        self.BtnDespedir.setStyleSheet("QPushButton{\n"
                                        "   background-color: rgba(80, 80, 80, 0.6);\n"
                                        "   color: rgb(175, 175, 175);\n"
                                        "   border-radius: 10px;\n"
                                        "   border: 1px solid;\n"
                                        "}")
        self.BtnDespedir.setObjectName("BtnDespedir")
        self.BtnDespedir.setEnabled(False)

        self.btnVolver = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnVolver.setGeometry(QtCore.QRect(30, 440, 100, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.btnVolver.setFont(font)
        self.btnVolver.setStyleSheet("QPushButton{\n"
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
        self.btnVolver.setObjectName("btnVolver")
        
        
        # Accion botones
        #self.BtnDespedir.clicked.connect(lambda: self.eliminarUsuario(self.obtenerUsuarioSeleccionado()))
        self.BtnDespedir.clicked.connect(self.confirmacion)

        self.btnVolver.clicked.connect(lambda: self.cerrarVentana(MainWindow, ListaEmp))


        self.tablaListaUsuarios = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tablaListaUsuarios.setGeometry(QtCore.QRect(30, 160, 761, 261))
        self.tablaListaUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaListaUsuarios.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaListaUsuarios.setObjectName("tablaListaUsuarios")
        self.tablaListaUsuarios.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tablaListaUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tablaListaUsuarios.setHorizontalHeaderItem(1, item)
        self.tablaListaUsuarios.horizontalHeader().setCascadingSectionResizes(True)
        self.tablaListaUsuarios.horizontalHeader().setDefaultSectionSize(115)
        self.tablaListaUsuarios.horizontalHeader().setHighlightSections(True)
        self.tablaListaUsuarios.horizontalHeader().setMinimumSectionSize(58)
        self.tablaListaUsuarios.horizontalHeader().setSortIndicatorShown(False)
        self.tablaListaUsuarios.horizontalHeader().setStretchLastSection(True)
        self.tablaListaUsuarios.verticalHeader().setCascadingSectionResizes(True)
        self.tablaListaUsuarios.verticalHeader().setHighlightSections(True)
        self.tablaListaUsuarios.verticalHeader().setSortIndicatorShown(False)
        self.tablaListaUsuarios.verticalHeader().setVisible(False)


        # Cargar Usuarios del CSV
        self.cargarUsuariosCSV()

        self.tablaListaUsuarios.itemSelectionChanged.connect(self.actualizarBotones)

        
        ListaEmp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ListaEmp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        ListaEmp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ListaEmp)
        self.statusbar.setObjectName("statusbar")
        ListaEmp.setStatusBar(self.statusbar)

        self.retranslateUi(ListaEmp)
        QtCore.QMetaObject.connectSlotsByName(ListaEmp)

    
    def retranslateUi(self, ListaEmp):
        _translate = QtCore.QCoreApplication.translate
        ListaEmp.setWindowTitle(_translate("ListaEmp", "ListaEmp"))
        self.BtnDespedir.setText(_translate("ListaEmp", "Despedir usuario"))
        item = self.tablaListaUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("ListaEmp", "Cargo"))
        item = self.tablaListaUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("ListaEmp", "Nombre de usuario"))
        self.btnVolver.setText(_translate("ListaEmp", "Volver"))
    

    def cerrarVentana(self, main_w, listausuarios):
        main_w.show()
        listausuarios.close()
    

    # Abre el archivo CSV y devuelve los datos como una lista de filas
    def leerDatosDesdeCSV(self):
        with open('ArchivosCSV/Usuarios.csv', encoding="utf-8", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            return list(reader)


    # Inserta los datos en el widget de la tabla
    def insertarDatosEnTabla(self, datos):
        for fila in datos:
            posicionFila = self.tablaListaUsuarios.rowCount()
            self.tablaListaUsuarios.insertRow(posicionFila)

            for columna, value in enumerate(fila):
                item = QtWidgets.QTableWidgetItem(value)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tablaListaUsuarios.setItem(posicionFila, columna, item)

 
        # Carga los datos del archivo CSV en el tableWidget
    def cargarUsuariosCSV(self):
        datos = self.leerDatosDesdeCSV()

        if datos:
            # Selecciona las columnas "Ocupación", "Usuario" (columnas 2, 0 ) de todos los usuarios
            # excepto las del administrador en uso
            datos_seleccionados = [[fila[2],fila[0]] for fila in datos if fila[0] != self.Usuario]
            encabezados = datos_seleccionados.pop(0)  
            self.tablaListaUsuarios.setColumnCount(len(encabezados))
            self.tablaListaUsuarios.setHorizontalHeaderLabels(encabezados)

            self.insertarDatosEnTabla(datos_seleccionados)
        else:
            print("La lista de datos está vacía")
    

    def actualizarBotones(self):
        filasSeleccionada = self.tablaListaUsuarios.selectedIndexes()

        if filasSeleccionada:
            # Se seleccionó al menos una fila
            self.BtnDespedir.setEnabled(True)
            self.BtnDespedir.setStyleSheet("QPushButton{\n"
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
        else:
            # No se seleccionó ninguna fila
            self.BtnDespedir.setEnabled(False)
            self.BtnDespedir.setStyleSheet("QPushButton{\n"
                                            "   background-color: rgba(80, 80, 80, 0.6);\n"
                                            "   color: rgb(175, 175, 175);\n"
                                            "   border-radius: 10px;\n"
                                            "   border: 1px solid;\n"
                                            "}")


    def obtenerUsuarioSeleccionado(self):
        fila_seleccionada = self.tablaListaUsuarios.currentRow()
        if fila_seleccionada != -1:
            id_usuario = self.tablaListaUsuarios.item(fila_seleccionada, 1).text()
            self.usuario_seleccionado = id_usuario
            return id_usuario

    
    def eliminarUsuario(self, usuario_id):
        # Obtener el índice de la fila seleccionada
        fila_seleccionada = self.tablaListaUsuarios.currentRow()

        # Eliminar la fila de la tabla
        self.tablaListaUsuarios.removeRow(fila_seleccionada)

        # Eliminar el usuario del archivo CSV
        datos = self.leerDatosDesdeCSV()
        if datos:
            usuarios_actualizados = [fila for fila in datos if fila[0] != usuario_id]
        with open('ArchivosCSV/Usuarios.csv', 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(usuarios_actualizados)

        # Actualizar los botones
        self.actualizarBotones()
    

    def confirmacion(self):       # Se muestra un mensaje para confirmar eliminación de usuario
        self.notificacion = QtWidgets.QMessageBox()
        self.notificacion.setWindowTitle("Eliminar usuario")
        self.notificacion.setText("Esta acción no se podrá deshacer. ¿Desea continuar?")
        self.notificacion.setIcon(QtWidgets.QMessageBox.Icon.Information)
        self.notificacion.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)

        btnAceptar = self.notificacion.button(QtWidgets.QMessageBox.StandardButton.Ok)
        btnAceptar.setText("Aceptar")
        btnAceptar.clicked.connect(lambda: self.eliminarUsuario(self.obtenerUsuarioSeleccionado()))

        btnCancelar = self.notificacion.button(QtWidgets.QMessageBox.StandardButton.Cancel)
        btnCancelar.setText("Cancelar")

        self.notificacion.exec()

