import csv

class Productos:
    def __init__(self, Marca: str, Nombre: str, Precio: str, Cantidad: int):
        self.__Marca = Marca
        self.__Nombre = Nombre
        self.__Precio = Precio
        self.__Cantidad = Cantidad
    
    # Getters
    def get_marca(self):
        return self.__Marca
    
    def get_nombre(self):
        return self.__Nombre

    def get_precio(self):
        return self.__Precio

    def get_cantidad(self):
        return self.__Cantidad

    # Setters
    def set_marca(self, Marca):
        self.__Marca = Marca
        
    def set_nombre(self, Nombre):
        self.__Nombre= Nombre

    def set_precio(self, Precio):
        self.__Precio = Precio

    def set_cantidad(self, Cantidad):
        self.__Cantidad = Cantidad

    def guardar_productos_CSV(self, lista_productos):
        with open('ArchivosCSV/Productos.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Marca', 'Producto', 'Precio', 'Cantidad'])
            for producto in lista_productos:
                writer.writerow([producto.Marca, producto.Nombre, producto.Precio, producto.Precio])
                
    def cargar_productos_CSV():
        lista_productos = []
        with open('ArchivosCSV/Productos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Marca, Nombre, Precio, Cantidad = row
                producto = Productos(Marca, Nombre, Precio, Cantidad)
                lista_productos.append(producto)
                
        return lista_productos
    
    def agregar_producto(marca, nombre, precio, cantidad):
        lista_productos = Productos.cargar_productos_CSV()

        producto = Productos(marca, nombre, precio, cantidad)
        producto.Marca = marca
        producto.Nombre = nombre
        producto.Precio = precio
        producto.Cantidad = cantidad
        
        lista_productos.append(producto)

        # Guarda solo el Producto agregado en el archivo CSV
        with open('ArchivosCSV/Productos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([producto.get_marca(), producto.get_nombre(), producto.get_precio(), producto.get_cantidad()])

# Inicializar la lista de productos
lista_productos = Productos.cargar_productos_CSV()

# Ejemplo de cómo agregar un producto al archivo CSV
# Productos.agregar_producto('Toshiba', 'Disco Duro', '$50000', 5)
