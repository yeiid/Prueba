tareas = []

def agregar_tarea():
    tarea = input("Ingrese una nueva tarea: ")
    tareas.append({"tarea": tarea, "completada": False})
    print("Tarea agregada.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "✔" if tarea["completada"] else "✘"
            print(f"{i}. {tarea['tarea']} [{estado}]")

def completar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea completada: ")) - 1
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    except (IndexError, ValueError):
        print("Número de tarea no válido.")

def main():
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            mostrar_tareas()
        elif opcion == '3':
            completar_tarea()
        elif opcion == '4':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
