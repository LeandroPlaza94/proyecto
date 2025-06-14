import json
import os
from horarios import horario_disponible
from servicios import CATEGORIAS

def agregar_turno():
    print("=== Agregar Turno ===")
    nombre = input("Ingrese el nombre del cliente: ")
    
    print("Categorías de servicios:")
    categorias_lista = list(CATEGORIAS.keys())
    for i, cat in enumerate(categorias_lista, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            opcion_cat = int(input("Seleccione el número de la categoría: "))
            if 1 <= opcion_cat <= len(categorias_lista):
                categoria_elegida = categorias_lista[opcion_cat - 1]
                break
        except ValueError:
            pass
        print("Por favor, ingrese un número válido.")
    
    print(f"Servicios disponibles en {categoria_elegida}:")
    servicios = CATEGORIAS[categoria_elegida]
    for i, servicio in enumerate(servicios, 1):
        print(f"{i}. {servicio}")
    
    while True:
        try:
            opcion_serv = int(input("Seleccione el número del servicio: "))
            if 1 <= opcion_serv <= len(servicios):
                servicio_elegido = servicios[opcion_serv - 1]
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    archivo = "clientes.json"
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            clientes = json.load(f)
            if isinstance(clientes, dict):
                clientes = [clientes]
            elif not isinstance(clientes, list):
                clientes = []
    else:
        clientes = []

    # Solicitar fecha del turno ANTES de la hora
    while True:
        fecha = input("Ingrese la fecha del turno (YYYY-MM-DD): ")
        try:
            from datetime import datetime
            fecha_turno = datetime.strptime(fecha, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de fecha incorrecto. Use YYYY-MM-DD (ejemplo: 2024-06-15)")

    # Solicitar hora del turno y validar disponibilidad
    while True:
        hora = input("Ingrese la hora del turno (HH:MM): ")
        if not horario_disponible(clientes, categoria_elegida, hora, fecha):
            print("El horario está ocupado para esta categoría y fecha o el formato es incorrecto. Debe haber al menos 1 hora de diferencia.")
        else:
            break

    turno = {
        "nombre": nombre,
        "categoria": categoria_elegida,
        "servicio": servicio_elegido,
        "fecha": fecha,
        "hora": hora
    }

    clientes.append(turno)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)

    print(f"Turno agregado para {nombre} - Servicio: {servicio_elegido} - Fecha: {fecha} - Hora: {hora}")

if __name__ == "__main__":
    agregar_turno()