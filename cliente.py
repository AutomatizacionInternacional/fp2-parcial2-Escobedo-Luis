class Cliente:
    """Dueño de un vehículo. Llega ya creado al vehículo (asociación)."""

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def describir(self):
        return f"{self.nombre} ({self.telefono})"
