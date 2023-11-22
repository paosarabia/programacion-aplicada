def registrar_pago_cuota(self):
  if self.cuotas_pagadas < 8:  # Verificar que el cliente no haya pagado todas las cuotas
    self.cuotas_pagadas += 1
    print(f"Se registró el pago de la cuota {self.cuotas_pagadas}.")
  if self.cuotas_pagadas == 8:  # Si se completan las 8 cuotas, gestionar adjudicación
    self.gestionar_adjudicacion()