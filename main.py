from cliente import Cliente
from moto import Moto
from carro import Carro
from pickup import Pickup
from parqueo import Parqueo


def mostrar_menu(parqueo):
    print()
    print(f"═══ {parqueo.nombre} ═══")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Ver vehículos estacionados")
    print("4. Buscar vehículo por placa")
    print("5. Ver resumen del día")
    print("6. Salir")


def opcion_entrada(parqueo):
    tipo = input("Tipo (M = moto, C = carro, P = pickup): ").strip().upper()
    placa = input("Placa: ").strip()
    color = input("Color: ").strip()
    dato = input("Dato propio (cilindrada / puertas / carga en toneladas): ").strip()
    nombre = input("Nombre del dueño: ").strip()
    telefono = input("Teléfono: ").strip()
    hora = input("Hora de entrada: ").strip()

    if tipo not in ("M", "C", "P"):
        print("Tipo no válido: use M, C o P.")
        return
    if placa == "":
        print("La placa no puede estar vacía.")
        return
    if not dato.isdigit():
        print("El dato propio debe ser un número entero.")
        return
    if not hora.isdigit():
        print("La hora debe ser un número entero.")
        return

    cliente = Cliente(nombre, telefono)
    if tipo == "M":
        vehiculo = Moto(placa, color, cliente, int(dato))
    elif tipo == "C":
        vehiculo = Carro(placa, color, cliente, int(dato))
    else:
        vehiculo = Pickup(placa, color, cliente, int(dato))
    parqueo.registrar_entrada(vehiculo, int(hora))


def opcion_salida(parqueo):
    placa = input("Placa: ").strip()
    hora = input("Hora de salida: ").strip()
    if not hora.isdigit():
        print("La hora debe ser un número entero.")
        return
    parqueo.registrar_salida(placa, int(hora))


def opcion_buscar(parqueo):
    placa = input("Placa: ").strip()
    vehiculo = parqueo.buscar(placa)
    if vehiculo is None:
        print(f"El vehículo con placa {placa.upper()} no está en el parqueo.")
    else:
        print(vehiculo.describir())


def opcion_resumen(parqueo):
    print(f"Espacios libres: {parqueo.espacios_libres()} de {parqueo.capacidad}")
    print(f"Total recaudado: Q{parqueo.total_recaudado}")


def main():
    parqueo = Parqueo("El Obelisco", 6)
    try:
        while True:
            mostrar_menu(parqueo)
            opcion = input("Elige una opción: ").strip()
            if opcion == "1":
                opcion_entrada(parqueo)
            elif opcion == "2":
                opcion_salida(parqueo)
            elif opcion == "3":
                parqueo.listar()
            elif opcion == "4":
                opcion_buscar(parqueo)
            elif opcion == "5":
                opcion_resumen(parqueo)
            elif opcion == "6":
                print("Hasta luego.")
                break
            else:
                print("Opción no válida: elija un número del 1 al 6.")
    except EOFError:
        print("\nFin de la entrada.")


if __name__ == "__main__":
    main()
