class Cliente:
  lista_clientes=[]

  def __init__(self, dni, nombre, apellido, domicilio):
    self._dni = dni
    self._nombre = nombre
    self._apellido = apellido
    self._domicilio = domicilio
    self.cuotas_pagadas = 0
  
  @property
  def dni(self):
    return self._dni
  
  @dni.setter
  def dni(self, nuevo_dni):
    self._dni = nuevo_dni

  @property
  def nombre(self):
    return self._nombre
  
  @nombre.setter
  def nombre(self, nuevo_nombre):
    self._nombre = nuevo_nombre

  @property
  def apellido(self):
    return self._apellido
  
  @apellido.setter
  def apellido(self, nuevo_apellido):
    self._apellido = nuevo_apellido
  
  @property
  def domicilio(self):
    return self._domicilio
  
  @domicilio.setter
  def domicilio(self, nuevo_domicilio):
    self._domicilio =nuevo_domicilio

  def agregar_cliente(self, nuevo_cliente):
    self.lista_clientes.append(nuevo_cliente)
    print("Cliente agregado con éxito.")

  def modificar_cliente(self, dni, atributo, nuevo_valor):
    for cliente in self.lista_clientes:
      if cliente.dni == dni:
        if atributo == 'dni':
          self.dni = nuevo_valor
        elif atributo == 'nombre':
          self.nombre = nuevo_valor
        elif atributo == 'apellido':
          self.apellido = nuevo_valor
        elif atributo == 'domicilio':
          self.domicilio = nuevo_valor
        else:
          print("Atributo no válido. Los atributos válidos son: dni, nombre, apellido y/o domicilio")
      else:
        print("Dni inexistente, intente nuevamente")

  def eliminar_cliente(self, dni_eliminar):
    cliente_encontrado = None
    for cliente in self.lista_clientes:
      if cliente.dni == dni_eliminar:
        cliente_encontrado = cliente
        break

    if cliente_encontrado:
      confirmacion = input(
          f"Está seguro de eliminar a {cliente_encontrado.nombre} {cliente_encontrado.apellido}? (s/n): "
      )
      if confirmacion.lower() == 's':
        self.lista_clientes.remove(cliente_encontrado)
        print(
            f"El cliente {cliente_encontrado.nombre} {cliente_encontrado.apellido} ha sido eliminado."
        )
      else:
        print("Operación cancelada.")
    else:
      print(f"No se encontró ningun cliente con DNI {dni_eliminar}.")
  
  def mostrar_clientes(self):
    for cliente in self.lista_clientes:
      print(f"Nombre: {cliente.nombre} Apellido: {cliente.apellido} - Dni: {cliente.dni} - Domicilio: {cliente.domicilio}")

