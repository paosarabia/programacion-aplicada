from vehiculo import Vehiculo

class Auto(Vehiculo):
  def __init__(self,id_vehiculo, marca, modelo, color, cant_puertas, ruedas, cant_pasajeros, tiene_baul):
    super().__init__(id_vehiculo, marca, modelo, color, cant_puertas, ruedas, cant_pasajeros)
    self.tiene_baul = tiene_baul