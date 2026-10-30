from vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, placa, color, dueno, cilindrada):
        super().__init__(placa, color, dueno)
        self.cilindrada = cilindrada

    def calcular_tarifa(self, horas):
        # Art. 5: Q5 por hora, sin tope
        return 5 * horas

    def describir(self):
        return f"Moto | {super().describir()} | {self.cilindrada} cc"
