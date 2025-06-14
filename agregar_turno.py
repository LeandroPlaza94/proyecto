import json
import os

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
    
    hora = input("Ingrese la hora del turno: ")
    turno = {
        "nombre": nombre,
        "categoria": categoria_elegida,
        "servicio": servicio_elegido,
        "hora": hora
    }

    # Guardar en clientes.json
    archivo = "clientes.json"
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            try:
                clientes = json.load(f)
                if isinstance(clientes, dict):
                    clientes = [clientes]
                elif not isinstance(clientes, list):
                    clientes = []
            except json.JSONDecodeError:
                clientes = []
    else:
        clientes = []

    clientes.append(turno)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)

    print(f"Turno agregado para {nombre} - Servicio: {servicio_elegido} - Hora: {hora}")

if __name__ == "__main__":
    agregar_turno()