from agregar_turno import agregar_turno

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
        print(Menu_inicial)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_turno()
        elif opcion == "2":
            print("Función cancelar_cita (a implementar)")
        elif opcion == "3":
            print("Función consultar_disponibilidad (a implementar)")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

