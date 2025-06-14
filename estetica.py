from agregar_turno import agregar_turno
import json
import os
from datetime import datetime, timedelta

# Menú principal para el sistema de gestión de estética

def agendar_cita():
    print("Función agendar_cita (a implementar)")

def cancelar_cita():
    print("Función cancelar_cita (a implementar)")

def consultar_disponibilidad():
    print("Función consultar_disponibilidad (a implementar)")

def salir():
    print("¡Hasta luego!")

Menu_inicial = """
Bienvenido al sistema de gestión de estética
Por favor, seleccione una opción:
1. Agendar cita
2. Cancelar cita
3. Consultar disponibilidad
4. Salir
"""

def menu():
    while True:
        print("1. Agregar turno")
        print("2. Otra opción")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_turno()
        elif opcion == "2":
            # Aquí puedes agregar la lógica para otra opción
            pass
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_turno():
    print("=== Agregar Turno ===")
    nombre = input("Ingrese el nombre del cliente: ")
    
    categorias = {
        "Cabello": [
            "Corte de cabello",
            "Tinte de cabello",
            "Peinado",
            "Tratamiento capilar"
        ],
        "Uñas": [
            "Manicura",
            "Pedicura"
        ],
        "Facial": [
            "Masaje facial",
            "Limpieza facial",
            "Maquillaje"
        ],
        "Depilación": [
            "Depilación con cera",
            "Depilación con hilo"
        ]
    }
    
    print("Categorías de servicios:")
    categorias_lista = list(categorias.keys())
    for i, cat in enumerate(categorias_lista, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            opcion_cat = int(input("Seleccione el número de la categoría: "))
            if 1 <= opcion_cat <= len(categorias_lista):
                categoria_elegida = categorias_lista[opcion_cat - 1]
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    print(f"Servicios disponibles en {categoria_elegida}:")
    servicios = categorias[categoria_elegida]
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

    # Cargar turnos existentes
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

    # Ingreso y validación de hora
    while True:
        hora = input("Ingrese la hora del turno (HH:MM): ")
        try:
            hora_turno = datetime.strptime(hora, "%H:%M")
        except ValueError:
            print("Formato de hora incorrecto. Use HH:MM (ejemplo: 14:30)")
            continue

        # Verificar solapamiento en la misma categoría
        ocupado = False
        for c in clientes:
            if c.get("categoria") == categoria_elegida:
                if c.get("hora") == hora:
                    ocupado = True
                    break
        if ocupado:
            print("El horario está ocupado para esta categoría. Elija otro horario.")
        else:
            break

    turno = {
        "nombre": nombre,
        "categoria": categoria_elegida,
        "servicio": servicio_elegido,
        "hora": hora
    }

    clientes.append(turno)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)

    print(f"Turno agregado para {nombre} - Servicio: {servicio_elegido} - Hora: {hora}")

if __name__ == "__main__":
    menu()

