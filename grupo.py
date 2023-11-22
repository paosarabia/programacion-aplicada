class Grupo:
    lista_grupos=[]
    
    def __init__(self, id_grupo, nombre, fecha_inicio, fecha_cierre, vehiculo):
        self.id_grupo = id_grupo
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_cierre = fecha_cierre
        self.vehiculo = vehiculo
        self.clientes = []

    def agregar_grupo (self, nuevo_grupo):
        self.lista_grupos.append(nuevo_grupo)  

    def modificar_grupo (self, id_grupo, nuevo_nombre_grupo):
        grupo_encontrado = None
        for grupo in self.lista_grupos:
            if grupo.id_grupo == id_grupo:
                grupo_encontrado = grupo
                break
        if grupo_encontrado:       
            grupo.nombre = nuevo_nombre_grupo
        else:
            print("ID inexistente, intente nuevamente")
            

    def eliminar_grupo (self, id_grupo):
        grupo_encontrado = None
        for grupo in self.lista_grupos:
            if grupo.id_grupo == id_grupo:
                grupo_encontrado = grupo
                break

        if grupo_encontrado:
            confirmacion = input(f"Está seguro de eliminar el grupo {grupo_encontrado.nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                self.lista_grupos.remove(grupo_encontrado)
                print(f"El grupo {grupo_encontrado.nombre} fue eliminado con éxito")
            else:
                print("Operación cancelada.")
        else:
            print(f"No se encontró ningun grupo con ID {id_grupo}")

    def agregar_cliente(self, id_grupo, dni_cliente):
        grupo_encontrado = None
        for grupo in self.lista_grupos:
            if grupo.id_grupo == id_grupo:
                grupo_encontrado = grupo
                break
        
        if grupo_encontrado:
            if len(grupo.clientes) < 5:
                grupo.clientes.append(dni_cliente)
            else:
                print("No se puede agregar más clientes a este grupo. Límite alcanzado.")
        else:
            print("Grupo inexistente, intente nuevamente")

    def eliminar_cliente (self, id_grupo, dni_cliente):
        grupo_encontrado = None
        for grupo in self.lista_grupos:
            if grupo.id_grupo == id_grupo:
                grupo_encontrado = grupo
                break
        
        if grupo_encontrado:
            cliente_encontrado = None
            for cliente in grupo.clientes:
                if cliente.dni == dni_cliente:
                    cliente_encontrado = cliente
                    break
            if cliente_encontrado:
                confirmacion = input(f"Está seguro de eliminar a {dni_cliente} de {grupo_encontrado.nombre}? (s/n): ")
                if confirmacion.lower() == 's':
                    grupo.clientes.remove(dni_cliente)
                    print(f"El cliente {dni_cliente} ha sido eliminado de {grupo_encontrado.nombre}")
                else:
                    print("Operación cancelada.")
            else:
                print("Cliente inexistente, intente nuevamente")
        else:
            print("Grupo inexistente, intente nuevamente")
    
    def listar_grupos(self):
        for grupo in self.lista_grupos:
            print(f"Grupo: {grupo.nombre} ({grupo.fecha_inicio} - {grupo.fecha_cierre}) - Vehículo: {grupo.vehiculo} - Clientes: {grupo.clientes}")

