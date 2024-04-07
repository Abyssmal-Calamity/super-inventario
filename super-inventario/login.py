from PyQt6 import QtWidgets, uic


# inicia la aplacion
app=QtWidgets.QApplication([])

# carga archivos .ui
login =uic.loadUi("ventana1.ui")
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

login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(quit)


#ejecutable
login.show()
app.exec()