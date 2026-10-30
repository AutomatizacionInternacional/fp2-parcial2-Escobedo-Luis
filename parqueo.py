class Parqueo:
    """Agrupa vehículos que llegan ya creados (agregación)."""

    HORA_APERTURA = 6
    HORA_CIERRE = 22

    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.estacionados = []
        self.total_recaudado = 0

    def espacios_libres(self):
        return self.capacidad - len(self.estacionados)

    def buscar(self, placa):
        placa = placa.upper()
        for vehiculo in self.estacionados:
            if vehiculo.placa == placa:
                return vehiculo
        return None

    def _hora_valida(self, hora):
        return self.HORA_APERTURA <= hora <= self.HORA_CIERRE

    def registrar_entrada(self, vehiculo, hora):
        # Art. 1: capacidad
        if self.espacios_libres() <= 0:
            print("Entrada rechazada (Art. 1): el parqueo está lleno.")
            return False
        # Art. 2: horario
        if not self._hora_valida(hora):
            print("Entrada rechazada (Art. 2): se atiende de 6 a 22 horas.")
            return False
        # Art. 3: placa única
        if self.buscar(vehiculo.placa) is not None:
            print(f"Entrada rechazada (Art. 3): la placa {vehiculo.placa} ya está dentro.")
            return False

        vehiculo.hora_entrada = hora
        self.estacionados.append(vehiculo)
        print(f"Entrada registrada: {vehiculo.placa} a las {hora} horas.")
        return True

    def registrar_salida(self, placa, hora):
        vehiculo = self.buscar(placa)
        if vehiculo is None:
            print(f"Salida rechazada: la placa {placa.upper()} no está en el parqueo.")
            return 0
        # Art. 2: horario
        if not self._hora_valida(hora):
            print("Salida rechazada (Art. 2): se atiende de 6 a 22 horas.")
            return 0
        # Art. 4: nadie sale antes de la hora en que entró
        if hora < vehiculo.hora_entrada:
            print("Salida rechazada (Art. 4): no se puede salir antes de la hora de entrada.")
            return 0

        horas = hora - vehiculo.hora_entrada
        if horas < 1:
            horas = 1
        monto = vehiculo.calcular_tarifa(horas)
        self.total_recaudado += monto
        self.estacionados.remove(vehiculo)
        print(f"Salida registrada: {vehiculo.placa}, {horas} hora(s). Cobrar: Q{monto}")
        return monto

    def listar(self):
        if len(self.estacionados) == 0:
            print("No hay vehículos estacionados.")
            return
        for vehiculo in self.estacionados:
            print(f"{vehiculo.describir()} | entrada: {vehiculo.hora_entrada} horas")
