import csv

class Usuarios:
    def __init__(self, Usuario: str, Password: str, Cargo: str):
        self.__Usuario = Usuario
        self.__Password = Password
        self.__Cargo = Cargo
    
    # Getters
    def get_usuario(self):
        return self.__Usuario
    
    def get_password(self):
        return self.__Password

    def get_cargo(self):
        return self.__Cargo
    
    # Setters
    def set_marca(self, Usuario):
        self.__Usuario = Usuario
        
    def set_nombre(self, Password):
        self.__Password= Password

    def set_precio(self, Cargo):
        self.__Cargo = Cargo
    
    def cargar_usuarios_CSV():
        lista_usuarios = []
        with open('ArchivosCSV/Usuarios.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Usuario, Password, Cargo = row
                user = Usuarios(Usuario, Password, Cargo)
                lista_usuarios.append(user)
                
        return lista_usuarios
