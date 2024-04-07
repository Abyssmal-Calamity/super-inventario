from PyQt6 import QtWidgets, uic


# inicia la aplacion
app=QtWidgets.QApplication([])

# carga archivos .ui
login =uic.loadUi("ventana3.ui")
entrar =uic.loadUi("ventana2.ui")

def gui_login():
    name = login.lineEdit.text()
    password=login.lineEdit_2.text()
    if len(name)==0 or len(password)==0:
        login.label_2.setText("se requiere que complete con informacion")
    
    elif name=="profe" and password=="1234":
        gui_entrar()
    else:
        login.label_2.setText("los datos ingresados son incorrectos")

# agregar funcion de boton de salir

def gui_entrar():
    login.hide()
    entrar.show()

    

#botones
#primera ventana
login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(quit)
#segundo ventana
entrar.pushButton.clicked.connect(quit)
entrar.pushButton_2.clicked.connect(quit) # abrir ventana 1 ,modificar inventario
entrar.pushButton_3.clicked.connect(quit) #abrir ventana 4 ,  mostrar inventario

#ejecutable
login.show()
app.exec()