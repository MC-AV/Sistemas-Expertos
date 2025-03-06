import numpy as np

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, id_vehiculo, marca, modelo, año, precio):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_informacion(self):
        print(f"ID: {self.id_vehiculo}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio}")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

# Herencia: Clase para autos eléctricos
class AutoElectrico(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año, precio, autonomia):
        super().__init__(id_vehiculo, marca, modelo, año, precio)
        self.autonomia = autonomia

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Autonomía: {self.autonomia} km")

# Herencia: Clase para autos deportivos
class AutoDeportivo(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, año, precio, velocidad_maxima):
        super().__init__(id_vehiculo, marca, modelo, año, precio)
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")

# Función para mostrar el menú
def mostrar_menu():
    print("\n----- Menú de Gestión de Agencia de Autos -----")
    opciones = (
        "1. Dar de alta un vehículo",
        "2. Modificar el precio de un vehículo",
        "3. Mostrar inventario",
        "4. Salir"
    )
    for opcion in opciones:
        print(opcion)

# Lista para almacenar vehículos
inventario = []

# Función para agregar un vehículo
def agregar_vehiculo():
    id_vehiculo = input("Ingrese el ID del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    año = int(input("Ingrese el año del vehículo: "))
    precio = float(input("Ingrese el precio del vehículo: "))
    
    tipo = input("Ingrese el tipo de vehículo (Electrico/Deportivo/Otro): ")
    if tipo.lower() == "electrico":
        autonomia = int(input("Ingrese la autonomía en km: "))
        vehiculo = AutoElectrico(id_vehiculo, marca, modelo, año, precio, autonomia)
    elif tipo.lower() == "deportivo":
        velocidad_maxima = int(input("Ingrese la velocidad máxima en km/h: "))
        vehiculo = AutoDeportivo(id_vehiculo, marca, modelo, año, precio, velocidad_maxima)
    else:
        vehiculo = Vehiculo(id_vehiculo, marca, modelo, año, precio)
    
    inventario.append(vehiculo)
    print("Vehículo agregado con éxito.")

# Función para modificar el precio de un vehículo
def modificar_precio_vehiculo():
    id_vehiculo = input("Ingrese el ID del vehículo a modificar: ")
    for vehiculo in inventario:
        if vehiculo.id_vehiculo == id_vehiculo:
            nuevo_precio = float(input(f"Ingrese el nuevo precio para {vehiculo.marca} {vehiculo.modelo}: "))
            vehiculo.actualizar_precio(nuevo_precio)
            print("Precio actualizado con éxito.")
            return
    print("Vehículo no encontrado.")

# Función para mostrar el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n----- Inventario de Vehículos -----")
        for vehiculo in inventario:
            vehiculo.mostrar_informacion()
            print("---------------------")

# Función principal para ejecutar la aplicación
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_vehiculo()
        elif opcion == '2':
            modificar_precio_vehiculo()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()

