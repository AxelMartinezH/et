import os 
os.system ("cls")

from datetime import date

def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    while cantidad < 1 or cantidad > 3:
        cantidad = int(input("Cantidad inválida. Ingrese la cantidad de entradas a comprar (1-3): "))
    print("""
    Platinum    (1 al 20)
    Gold        ( 21 al 50)
    Silver      (51 al 100)
    """)
    print("Ubicaciones disponibles:")
    for i in range(1, 101):
        if i <= 20:
            tipo = ""
        elif i <= 50:
            tipo = ""
        else:
            tipo = ""

        if i in asientos_vendidos:
            print(f"{i} ({tipo}):Vendido[X]", end="    ")
        else:
            print(f"{i} ({tipo}):Disponible", end="    ")

        if i % 10 == 0:
            print("\n")

    for _ in range(cantidad):
        asiento = int(input("Ingrese el número de asiento a comprar: "))
        while asiento in asientos_vendidos:
            print("Ubicación no disponible, elija otro asiento.")
            asiento = int(input("Ingrese el número de asiento a comprar: "))

        asientos_vendidos.append(asiento)
        run = input("Ingrese el RUN del asistente (sin puntos ni guiones): ")
        while not run.isdigit() or len(run) != 8:
            print("RUN inválido, ingrese solo números (8 dígitos).")
            run = input("Ingrese el RUN del asistente (sin puntos ni guiones): ")

        lista_asistentes.append((run, asiento))
        ventas_hoy.append((asiento, tipo))

    print("Operación realizada correctamente.")


def mostrar_ubicaciones_disponibles():
    print("Ubicaciones disponibles:")
    for i in range(1, 101):
        if i <= 20:
            tipo = "Platinum"
        elif i <= 50:
            tipo = "Gold"
        else:
            tipo = "Silver"

        if i in asientos_vendidos:
            print(f"Asiento{i} ({tipo}):Vendido[X]", end="    ")
        else:
            print(f"Asiento{i} ({tipo}):Disponible", end="    ")

        if i % 10 == 0:
            print("\n")


def ver_listado_asistentes():
    lista_asistentes.sort(key=lambda x: int(x[0]))
    print("Listado de asistentes:")
    for asistente in lista_asistentes:
        print(f"RUN: {asistente[0]}, Asiento: {asistente[1]}")


def mostrar_ganancias_totales():
    precios = {"Platinum": 120000, "Gold": 80000, "Silver": 50000}
    ganancias = {tipo: 0 for tipo in precios.keys()}
    total_ganancias = 0

    print("Tipo Entrada  Cantidad  Ganancias")
    print("-" * 30)
    for tipo in precios.keys():
        cantidad = asientos_vendidos.count(tipo)
        ganancia = precios[tipo] * cantidad
        ganancias[tipo] = ganancia
        print(f"{tipo:<13} {cantidad:>8} {ganancia:>10,}")
        total_ganancias += ganancia

    print("-" * 30)
    print(f"{'TOTAL':<13} {len(asientos_vendidos):>8} {total_ganancias:>10,}")

    total_ganancias_hoy = sum(precio * ventas_hoy.count((asiento, tipo)) for (asiento, tipo) in ventas_hoy for tipo, precio in precios.items())
    print(f"Ganancias totales de hoy ({date.today()}): {total_ganancias_hoy:,}")


def salir():
    import datetime
    fecha_actual = datetime.datetime.now()
    print("Saliendo del sistema...")
    print("Nombre del programador: Axel Martinez Hollander")
    print("Fecha actual:", fecha_actual.strftime("%Y-%m-%d %H:%M:%S"))



asientos_vendidos = []
lista_asistentes = []
ventas_hoy = []

while True:
    print("\n--- Menú ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            comprar_entradas()
        elif opcion == 2:
            mostrar_ubicaciones_disponibles()
        elif opcion == 3:
            ver_listado_asistentes()
        elif opcion == 4:
            mostrar_ganancias_totales()
        elif opcion == 5:
            salir()
        else:
            print("Opción inválida, seleccione una opción válida.")
    except ValueError:
        print("Opción inválida, seleccione una opción válida.")