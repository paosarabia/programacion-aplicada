import os
from cliente import Cliente
from grupo import Grupo
from auto import Auto
from camioneta import Camioneta

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

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
    print("e. Eliminar Cliente de Grupo")
    print("f. Listar Grupos")
    print("g. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion

def menu_gestionar_vehiculos():
    print("\n--- Menú Gestionar Vehículos ---")
    print("a. Agregar vehículo")
    print("b. Eliminar vehículo")
    print("c. Listar vehículos")
    print("d. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    #lista_grupos=[]

    while True:
        #limpiar_pantalla
        print("\n--- Menú Principal ---")
        print("1. Gestionar Clientes")
        print("2. Gestionar Vehiculos")
        print("3. Gestionar Grupos de Clientes")
        print("4. Cuotas")
        print("5. Adjudicación")
        print("6. Salir")

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
                    cliente = Cliente(dni, nombre, apellido, domicilio)
                    cliente.agregar_cliente(cliente)

                elif opcion_gestion_clientes == 'b':
                    # Modificar Cliente
                    dni = input("Ingrese el DNI del cliente a modificar: ")
                    atributo = input("Ingrese el atributo del cliente que desea modificar (dni, nombre, apellido o domicilio): ")
                    nuevo_valor = input("Ingrese el nuevo valor: ")
                    cliente.modificar_cliente(dni, atributo, nuevo_valor)

                elif opcion_gestion_clientes == 'c':
                    # Eliminar Cliente
                    dni_eliminar = input("Ingrese el DNI del cliente a eliminar: ")
                    cliente.eliminar_cliente(dni_eliminar)

                elif opcion_gestion_clientes == 'd':
                    # Mostrar Clientes
                    cliente.mostrar_clientes()

                elif opcion_gestion_clientes == 'e':
                    # Volver al Menú Principal
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")


        elif opcion_principal == '2':
            while True:
                opcion_gestion_vehiculos = menu_gestionar_vehiculos()

                if opcion_gestion_vehiculos == 'a':
                    # Agregar vehículo
                    tipo_vehiculo = input("Ingrese el tipo de vehículo a gestionar(auto o camioneta): ")
                    
                    if tipo_vehiculo == "auto":
                        id_vehiculo = input("Ingrese el ID del Auto: ")
                        marca = input("Ingrese la marca del Auto: ")
                        modelo = input("Ingrese el modelo del auto: ")
                        color = input("Ingrese el color del auto: ")
                        cant_puertas = int(input("Ingrese la cantidad de puertas del auto: "))
                        cant_pasajeros = int(input("Ingrese la cantidad de pasajeros del auto: "))
                        precio = int(input("Ingrese el precio del auto: "))
                        tiene_baul = input("Tiene baul? (s/n): ")
                        auto = Auto(id_vehiculo, marca, modelo, color, cant_puertas, cant_pasajeros, precio, tiene_baul)
                        auto.agregar_vehiculo(auto)
                    elif tipo_vehiculo == "camioneta":
                        id_vehiculo = input("Ingrese el ID de la camioneta: ")
                        marca = input("Ingrese la marca de la camioneta: ")
                        modelo = input("Ingrese el modelo de la camioneta: ")
                        color = input("Ingrese el color de la camioneta: ")
                        cant_puertas = int(input("Ingrese la cantidad de puertas de la camioneta: "))
                        cant_pasajeros = int(input("Ingrese la cantidad de pasajeros de la camioneta: "))
                        precio = int(input("Ingrese el precio de la camioneta: "))
                        tipo_caja = input("Qué tipo de caja tiene? (abierta/cerrada): ")
                        camioneta = Camioneta(id_vehiculo, marca, modelo, color, cant_puertas, cant_pasajeros, precio, tipo_caja)
                        camioneta.agregar_vehiculo(camioneta)
                    else:
                        print("El tipo de vehiculo ingresado no es correcto")

                elif opcion_gestion_vehiculos == 'b':
                    # Eliminar vehículo
                    tipo_vehiculo = input("Ingrese el tipo de vehículo a eliminar (auto o camioneta): ")
                    
                    if tipo_vehiculo == "auto":
                        modelo = input("Ingrese el modelo del auto que quiere eliminar: ")
                        auto.eliminar_vehiculo(modelo)
                    elif tipo_vehiculo == "camioneta":
                        modelo = input("Ingrese el modelo de la camioneta que quiere eliminar: ")
                        camioneta.eliminar_vehiculo(modelo)
                    else:
                        print("El tipo de vehiculo ingresado no es correcto")

                elif opcion_gestion_vehiculos == 'c':
                    # Listar vehiculos
                    auto.listar_vehiculos()

                elif opcion_gestion_vehiculos == 'd':
                    # Volver al Menú Principal
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")



        elif opcion_principal == '3':
            while True:
                opcion_gestion_grupos = menu_gestionar_grupos()

                if opcion_gestion_grupos == 'a':
                    # Agregar Grupo
                    id_grupo = input("Ingrese el ID del grupo: ")
                    nombre_grupo = input("Ingrese el nombre del grupo: ")
                    fecha_inicio = input("Ingrese la fecha de inicio del grupo: ")
                    fecha_cierre = input("Ingrese la fecha de cierre del grupo: ")
                    tipo_vehiculo = input("Qué tipo de vehículo desea ingresar? (auto/camioneta): ")
                    if tipo_vehiculo == "auto":
                        id_vehiculo_grupo = input("Ingrese el ID del auto que agregara al grupo: ")
                        vehiculo_encontrado = None
                        for vehiculo in auto.lista_vehiculos:
                            if vehiculo.id_vehiculo == id_vehiculo_grupo:
                                vehiculo_encontrado = f'{vehiculo.marca}, {vehiculo.modelo}'
                                break
                        if vehiculo_encontrado: 
                            grupo = Grupo(id_grupo, nombre_grupo, fecha_inicio, fecha_cierre, vehiculo_encontrado)
                            grupo.agregar_grupo(grupo)
                        else:
                            print("ID inexistente, intente nuevamente")
                    elif tipo_vehiculo == "camioneta":
                        id_vehiculo_grupo = input("Ingrese el ID de la camioneta que agregara al grupo: ")
                        vehiculo_encontrado = None
                        for vehiculo in camioneta.lista_vehiculos:
                            if vehiculo.id_vehiculo == id_vehiculo_grupo:
                                vehiculo_encontrado = f'{vehiculo.marca}, {vehiculo.modelo}'
                                break
                        if vehiculo_encontrado: 
                            grupo = Grupo(id_grupo, nombre_grupo, fecha_inicio, fecha_cierre, vehiculo_encontrado)
                            grupo.agregar_grupo(grupo)
                        else:
                            print("ID inexistente, intente nuevamente")
                    else:
                        print("El tipo de vehiculo ingresado no es correcto")

                elif opcion_gestion_grupos == 'b':
                    # Modificar Grupo
                    id_grupo = input("Ingrese el ID del grupo a modificar: ")
                    nuevo_nombre_grupo = input("Ingrese el nuevo nombre del grupo: ")
                    grupo.modificar_grupo(id_grupo, nuevo_nombre_grupo)

                elif opcion_gestion_grupos == 'c':
                    # Eliminar Grupo
                    id_grupo = input("Ingrese el ID del grupo a eliminar: ")
                    grupo.eliminar_grupo(id_grupo)

                elif opcion_gestion_grupos == 'd':
                    # Agregar Cliente a Grupo
                    id_grupo = input("Ingrese el ID del grupo al que desea agregar un cliente: ")
                    dni_cliente = input("Ingrese el DNI del cliente a agregar: ")
                    cliente_encontrado = None
                    for cliente in cliente.lista_clientes:
                        if cliente.dni == dni_cliente:
                            cliente_encontrado = f'{cliente.dni}, {cliente.nombre}, {cliente.apellido}'
                            break
                    if cliente_encontrado: 
                        grupo.agregar_cliente(id_grupo, dni_cliente)
                    else:
                        print("DNI inexistente, intente nuevamente")


                elif opcion_gestion_grupos == 'e':
                    # Eliminar Cliente de Grupo
                    id_grupo = input("Ingrese el ID del grupo que desea gestionar: ")
                    dni_cliente = input("Ingrese el DNI del cliente a eliminar: ")
                    cliente_encontrado = None
                    for cliente in cliente.lista_clientes:
                        if cliente.dni == dni_cliente:
                            cliente_encontrado = f'{cliente.dni}, {cliente.nombre}, {cliente.apellido}'
                            break
                    if cliente_encontrado: 
                        grupo.eliminar_cliente(id_grupo, dni_cliente)
                    else:
                        print("DNI inexistente, intente nuevamente")
                    

                elif opcion_gestion_grupos == 'f':
                    # # Mostrar Grupos
                    grupo.listar_grupos()

                elif opcion_gestion_grupos == 'g':
                    # Volver al Menú Principal
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")



        elif opcion_principal == '4':
            # Cuota
            print("Cuota")
            break

        elif opcion_principal == '5':
            # Adjudicación
            print("Adjudicación")
            break

        elif opcion_principal == '6':
            # Salir
            print("Gracias por usar el plan de ahorro!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


main()