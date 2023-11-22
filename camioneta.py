from vehiculo import Vehiculo

class Camioneta(Vehiculo):
  def _init_(self,id_vehiculo, marca, modelo, color, cant_puertas, ruedas, cant_pasajeros, tipo_caja):
    super()._init_(id_vehiculo, marca, modelo, color, cant_puertas, ruedas, cant_pasajeros)
    self.tipo_caja = tipo_caja