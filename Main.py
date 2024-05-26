import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

# Se importan las ventanas
from Inicio_sesion import Ui_Login


class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Ui = Ui_Login()
        self.Ui.setupUi(self)
        
        self.registro()

    def registro(self):
        try:
            with open('ArchivosCSV/Usuarios.csv', 'r', encoding='utf-8') as file:
                data = csv.reader(file, delimiter=',')

        except:
            print("Creando nuevo archivo de registro...")

            with open('ArchivosCSV/Usuarios.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                field = ["Usuario", "Contraseña", "Ocupación"]
                writer.writerow(field)



if __name__ == "__main__":
    # inicia la aplicacion
    app = QApplication(sys.argv)
    ventana = Main_Window()
    ventana.setWindowTitle("ULAGOS Market")
    ventana.setWindowIcon(QIcon("icono\\martin.png"))

    #ejecutable
    ventana.show()
    sys.exit(app.exec())
