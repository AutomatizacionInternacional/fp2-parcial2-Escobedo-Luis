from vehiculo import Vehiculo


class Carro(Vehiculo):
    def __init__(self, placa, color, dueno, puertas):
        super().__init__(placa, color, dueno)
        self.puertas = puertas

    def calcular_tarifa(self, horas):
        # Art. 5: Q10 por hora, máximo Q60 por visita
        return min(10 * horas, 60)

    def describir(self):
        return f"Carro | {super().describir()} | {self.puertas} puertas"
