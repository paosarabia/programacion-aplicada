class Plan:
  def __init__(self, nombre_plan, fecha_apertura, fecha_cierre):
    self.nombre_plan = nombre_plan
    self.fecha_apertura = fecha_apertura
    self.fecha_cierre = fecha_cierre
    self.grupos = []

  def agregar_grupo(self, grupo):
    self.grupos.append(grupo)