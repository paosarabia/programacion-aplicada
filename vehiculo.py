class Vehiculo:
    lista_vehiculos = []
    
    def __init__(self,id_vehiculo, marca, modelo, color, cant_puertas, cant_pasajeros, precio):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cant_puertas = cant_puertas
        self.cant_pasajeros = cant_pasajeros
        self.precio = precio

    
    def agregar_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)
        print("Vehiculo agregado con éxito.")
    
    def eliminar_vehiculo(self, modelo):
        vehiculo_encontrado = None
        for vehiculo in self.lista_vehiculos:
            if vehiculo.modelo == modelo:
                vehiculo_encontrado = vehiculo
                break

        if vehiculo_encontrado:
            confirmacion = input(f"Está seguro de eliminar {vehiculo_encontrado.modelo}? (s/n): ")
            if confirmacion.lower() == 's':
                self.lista_vehiculos.remove(vehiculo_encontrado)
                print(f"El vehículo {vehiculo_encontrado.modelo} ha sido eliminado")
            else:
                print("Operación cancelada.")
        else:
            print(f"No se encontró el modelo proporcionado entre los vehículos guardados")
            
    def listar_vehiculos(self):
        for vehiculo in self.lista_vehiculos:
            print(f'{vehiculo.id_vehiculo} {vehiculo.marca} {vehiculo.modelo} {vehiculo.color}, {vehiculo.cant_puertas} puertas, para {vehiculo.cant_pasajeros} personas. Precio: ${vehiculo.precio}.-')

