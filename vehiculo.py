from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """Clase abstracta: nunca se crea un Vehiculo directamente."""

    def __init__(self, placa, color, dueno):
        self.placa = placa.upper()
        self.color = color
        self.dueno = dueno  # Cliente ya creado (asociación)
        self.hora_entrada = None

    @abstractmethod
    def calcular_tarifa(self, horas):
        pass

    def describir(self):
        return f"{self.placa}, color {self.color}, dueño: {self.dueno.describir()}"
