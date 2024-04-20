import sys
from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6.QtGui import QIcon

# Se importa las vistas
from Inicio_sesion import Ui_Login

class Main_Window(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.Ui = Ui_Login()
        self.Ui.setupUi(self)


if __name__ == "__main__":
    # inicia la aplicacion
    app = QApplication(sys.argv)
    ventana = Main_Window()
    ventana.setWindowTitle("ULAGOS Market")
    ventana.setWindowIcon(QIcon("icono\\xanxho.png"))

    #ejecutable
    ventana.show()
    sys.exit(app.exec())
