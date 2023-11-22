import os

# Definición de la clase Persona
class Persona:
  def __init__(self, dni=None, nombre=None, apellido=None, domicilio=None):
    if dni is None and nombre is not None and apellido is not None and domicilio is not None:
      self._dni = dni
      self._nombre = nombre
      self._apellido = apellido
      self._domicilio = domicilio
  
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

  def agregar_persona(self, lista_personas):
    lista_personas.append(self)

  def modificar_persona(self, atributo, nuevo_valor):
    if atributo == 'dni':
      self.dni = nuevo_valor
    elif atributo == 'nombre':
      self.nombre = nuevo_valor
    elif atributo == 'apellido':
      self.apellido = nuevo_valor
    elif atributo == 'domicilio':
      self.domicilio = nuevo_valor
    else:
      print(
        "Atributo no válido. Los atributos válidos son: dni, nombre, apellido, domicilio"
      )

  def eliminar_persona(self, lista_personas):
    dni_eliminar = input("Ingrese el DNI de la persona que desea eliminar: ")

    # Buscar la persona por su DNI en la lista
    persona_encontrada = None
    for persona in lista_personas:
      if persona.dni == dni_eliminar:
        persona_encontrada = persona
        break

    if persona_encontrada:
      confirmacion = input(
          f"¿Está seguro de eliminar a {persona_encontrada.nombre} {persona_encontrada.apellido}? (s/n): "
      )
      if confirmacion.lower() == 's':
        lista_personas.remove(persona_encontrada)
        print(
            f"La persona {persona_encontrada.nombre} {persona_encontrada.apellido} ha sido eliminada."
        )
      else:
        print("Operación cancelada.")
    else:
      print(f"No se encontró ninguna persona con DNI {dni_eliminar}.")
  
  def mostrarPersonas(self):
    for persona in lista_personas:
      print(f"nombre: {persona.nombre} apellido: {persona.apellido} dni: {persona.dni}")

# Definición de la clase Cliente que hereda de Persona

class Cliente(Persona):

  def __init__(self, dni=None, nombre=None, apellido=None, domicilio=None, nro_cliente=None):
    if dni is not None and nombre is not None and apellido is not None and domicilio is not None and apellido is not None and nro_cliente is not None:
      super().__init__(dni, nombre, apellido, domicilio)
      self.nro_cliente = nro_cliente
      self.cuotas_pagadas = 0  # Nuevo atributo para llevar registro de cuotas pagadas

  def agregar_grupo(self, grupo):
    if grupo.cantidad_clientes < 5:  # Verificar si el grupo tiene menos de 5 clientes
      grupo.agregar_cliente(self)
      grupo.cantidad_clientes += 1  # Incrementar contador de clientes en el grupo
    else:
      print(
        "No se puede agregar más clientes a este grupo. Límite alcanzado."
      )

  def registrar_pago_cuota(self):
    if self.cuotas_pagadas < 8:  # Verificar que el cliente no haya pagado todas las cuotas
      self.cuotas_pagadas += 1
      print(f"Se registró el pago de la cuota {self.cuotas_pagadas}.")
    if self.cuotas_pagadas == 8:  # Si se completan las 8 cuotas, gestionar adjudicación
      self.gestionar_adjudicacion()

  def gestionar_adjudicacion(self):
    print("¡Felicidades! Usted ha completado el pago de todas las cuotas.")
    print("Seleccione el método de adjudicación:")
    print("1. Sorteo mensual")
    print("2. Pago completo de cuotas")
    print("3. Licitación")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
      if self.sorteo_mensual():
        print("¡Felicidades! Usted ha sido adjudicado por sorteo.")
        self.registrar_pago_cuota()  # Registrar el pago de una cuota
      else:
        print("Lo sentimos, no fue seleccionado en el sorteo.")
    elif opcion == '2':
      self.pago_completo_cuotas()
    elif opcion == '3':
      self.licitacion()
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")


# Definición de la clase Grupo
class Grupo:

  def __init__(self, nro_grupo=None, fecha_inicio=None, fecha_cierre=None):
    if nro_grupo is not None and fecha_inicio is not None and fecha_cierre is not None:
      self.nro_grupo = nro_grupo
      self.fecha_inicio = fecha_inicio
      self.fecha_cierre = fecha_cierre
      self.cantidad_clientes = 0
      self.clientes = []
      self.vehiculos = []

  def agregar_cliente(self, cliente):
    self.clientes.append(cliente)
    self.cantidad_clientes += 1

  def agregar_vehiculo(self, vehiculo):
    self.vehiculos.append(vehiculo)

  def modificar_grupo(self):
    # Implementar la lógica para modificar un grupo
    pass

  def cerrar_grupo(self):
    # Implementar la lógica para cerrar un grupo
    pass


# Definición de la clase Plan
class Plan:
  def __init__(self, nombre_plan, fecha_apertura, fecha_cierre):
    self.nombre_plan = nombre_plan
    self.fecha_apertura = fecha_apertura
    self.fecha_cierre = fecha_cierre
    self.grupos = []

  def agregar_grupo(self, grupo):
    self.grupos.append(grupo)


# Definición de la clase Vehiculo
class Vehiculo:
  def __init__(self, marca, modelo, color, cantidad_puertas, cant_pasajeros, precio):
    # self.marca = marca
    # self.modelo = modelo
    # self.color = color
    # self.cantidad_puertas = cantidad_puertas
    # self.cant_pasajeros = cant_pasajeros
    # self.precio = precio
    lista_vehiculos.append(marca, modelo, color, cantidad_puertas, cant_pasajeros, precio)

  def agregar_vehiculo(self):
    lista_vehiculos.append()


class Camioneta(Vehiculo):

  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
    cant_pasajeros, carga, tolva):
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas, cant_pasajeros)
    self.carga = carga
    self.tolva = tolva

  def cargar(self, carga):
    # Implementar la lógica para cargar la camioneta
    pass


class Auto(Vehiculo):

  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas, cant_pasajeros, tipo):
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas, cant_pasajeros)
    self.tipo = tipo


def mostrar_menu():
  print("¡Bienvenido al Plan de Ahorro de Autos!")
  print("Por favor, seleccione una opción:")
  print("a. Gestionar Clientes")
  print("b. Gestionar Grupos de Clientes")
  print("c. Agregar pago de cuotas de los clientes")
  print("d. Registrar una adjudicación")
  print("e. Gestionar vehículos")
  print("q. Salir")


def limpiar_pantalla():
  os.system('clear' if os.name == 'posix' else 'cls')


def gestionar_clientes(lista_personas):
  print("Gestionando Clientes...")
  dni = input("Ingrese DNI del cliente: ")
  nombre = input("Ingrese nombre del cliente: ")
  apellido = input("Ingrese apellido del cliente: ")
  domicilio = input("Ingrese domicilio del cliente: ")
  nro_cliente = input("Ingrese número de cliente: ")

  cliente = Cliente(dni, nombre, apellido, domicilio, nro_cliente)
  cliente.agregar_persona(lista_personas)

  print("Cliente agregado con éxito.")


def gestionar_grupos():
  print("Gestionando Grupos de Clientes...")
  # Implementar lógica para gestionar grupos
  pass


def agregar_pago_cuotas():
  print("Agregando pago de cuotas de los clientes...")
  # Implementar lógica para agregar pagos de cuotas
  pass


def registrar_adjudicacion():
  print("Registrando una adjudicación...")
  # Implementar lógica para registrar una adjudicación
  pass


def gestionar_vehiculos():
  print("Gestionando vehículos...")
  # Implementar lógica para gestionar vehículos
  pass




while True:
  #limpiar_pantalla()
  mostrar_menu()
  opcion = input("Seleccione una opción: ").lower()

  if opcion == 'a':
    gestionar_clientes(lista_personas)
  elif opcion == 'b':
    gestionar_grupos()
  elif opcion == 'c':
    agregar_pago_cuotas()
  elif opcion == 'd':
    registrar_adjudicacion()
  elif opcion == 'e':
    gestionar_vehiculos()
  elif opcion == 'q':
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")





def menu_gestionar_clientes():
    print("\n--- Menú Gestionar Clientes ---")
    print("a. Agregar Cliente")
    print("b. Modificar Cliente")
    print("c. Eliminar Cliente")
    print("d. Mostrar Clientes")
    print("e. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion

def menu_gestionar_grupos():
    print("\n--- Menú Gestionar Grupos de Clientes ---")
    print("a. Agregar Grupo")
    print("b. Modificar Grupo")
    print("c. Eliminar Grupo")
    print("d. Agregar Cliente a Grupo")
    print("e. Listar Grupos")
    print("f. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion

def menu_gestionar_autos():
    print("\n--- Menú Gestionar Autos ---")
    print("a. Agregar Auto")
    print("b. Eliminar Auto")
    print("c. Listar Autos")
    print("d. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion


#menu principal
def main():
  gestion_clientes = Cliente()
  gestion_grupos = Grupo()
  gestion_autos = Vehiculo()

  while True:
    print("\n--- Menú Principal ---")
    print("1. Gestionar Clientes")
    print("2. Gestionar Grupos de Clientes")
    print("3. Gestionar Autos")
    print("4. Salir")

    opcion_principal = input("Seleccione una opción: ")

    if opcion_principal == '1':
      while True:
        opcion_gestion_clientes = menu_gestionar_clientes()

        if opcion_gestion_clientes == 'a':
          # Agregar Cliente
          dni = input("Ingrese DNI del cliente: ")
          nombre = input("Ingrese el nombre del cliente: ")
          apellido = input("Ingrese el apellido del cliente: ")
          domicilio = input("Ingrese domicilio del cliente: ")
          nro_cliente = input("Ingrese número de cliente: ")
          gestion_clientes.agregarCliente(dni, nombre, apellido, dni, domicilio, nro_cliente)

        elif opcion_gestion_clientes == 'b':
          # Modificar Cliente
          dni = input("Ingrese el DNI del cliente a modificar: ")
          nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
          nuevo_apellido = input("Ingrese el nuevo apellido del cliente: ")
          cliente = gestion_clientes.encontrar_cliente_por_dni(dni)
          if cliente:
            cliente.modificarCliente(nuevo_nombre, nuevo_apellido)
          else:
            print("Cliente no encontrado.")

        elif opcion_gestion_clientes == 'c':
          # Eliminar Cliente
          dni = input("Ingrese el DNI del cliente a eliminar: ")
          gestion_clientes.eliminarCliente(dni)

        elif opcion_gestion_clientes == 'd':
          # Mostrar Clientes
          gestion_clientes.mostrarClientes()

        elif opcion_gestion_clientes == 'e':
          # Volver al Menú Principal
          break

        else:
          print("Opción inválida. Intente nuevamente.")

    elif opcion_principal == '2':
      while True:
        opcion_gestion_grupos = menu_gestionar_grupos()

        if opcion_gestion_grupos == 'a':
          # Agregar Grupo
          id_grupo = input("Ingrese el ID del grupo: ")
          nombre_grupo = input("Ingrese el nombre del grupo: ")
          id_auto_grupo = input("Ingrese el id del auto que será del grupo: ")
          auto_grupo = gestion_autos.agregarAuto(marca_auto, modelo_auto, anio_auto, precio_auto)
          gestion_grupos.agregar_grupo(auto_grupo)

        elif opcion_gestion_grupos == 'b':
          # Modificar Grupo
          id_grupo = input("Ingrese el ID del grupo a modificar: ")
          marca_auto = input("Ingrese la nueva marca del auto del grupo: ")
          auto_grupo = gestion_autos.agregarAuto(marca_auto, modelo_auto, anio_auto, precio_auto)
          gestion_grupos.modificar_grupo(id_grupo, auto_grupo)

        elif opcion_gestion_grupos == 'c':
          # Eliminar Grupo
          id_grupo = input("Ingrese el ID del grupo a eliminar: ")
          gestion_grupos.eliminar_grupo(id_grupo)

        elif opcion_gestion_grupos == 'd':
          # Agregar Cliente a Grupo
          id_grupo = input("Ingrese el ID del grupo al que desea agregar un cliente: ")
          dni_cliente = input("Ingrese el DNI del cliente a agregar: ")
          cliente_a_agregar = gestion_clientes.encontrar_cliente_por_dni(dni_cliente)
          if cliente_a_agregar:
            gestion_grupos.agregarCliente_a_grupo(id_grupo, cliente_a_agregar)
          else:
            print("Cliente no encontrado.")

        elif opcion_gestion_grupos == 'e':
          # Listar Grupos
          gestion_grupos.listar_grupos()

        elif opcion_gestion_grupos == 'f':
          # Volver al Menú Principal
          break

        else:
          print("Opción inválida. Intente nuevamente.")

    elif opcion_principal == '3':
      while True:
        opcion_gestion_autos = menu_gestionar_autos()

        if opcion_gestion_autos == 'a':
          # Agregar Auto
          marca = input("Ingrese la marca del vehículo: ")
          modelo = input("Ingrese el modelo del vehículo: ")
          color = input("Ingrese el color del vehículo: ")
          cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
          cant_pasajeros = int(input("Ingrese la cantidad de pasajeros del vehículo: "))
          precio = int(input("Ingrese el precio del vehículo: "))
          gestion_autos.agregar_vehiculo()

        elif opcion_gestion_autos == 'b':
          # Eliminar Auto
          marca_auto = input("Ingrese la marca del auto a eliminar: ")
          modelo_auto = input("Ingrese el modelo del auto a eliminar: ")
          gestion_autos.eliminarAuto(marca_auto, modelo_auto)

        elif opcion_gestion_autos == 'c':
          # Listar Autos
          gestion_autos.listarAutos()

        elif opcion_gestion_autos == 'd':
          # Volver al Menú Principal
          break

        else:
          print("Opción inválida. Intente nuevamente.")

    elif opcion_principal == '4':
      # Salir
      print("¡Hasta luego!")
      break

    else:
      print("Opción inválida. Intente nuevamente.")