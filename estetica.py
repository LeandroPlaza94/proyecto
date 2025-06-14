from agregar_turno import agregar_turno

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
            # Lógica para otra opción
            pass
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()

