def main():
    print("Calculadora Básica")
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Selección de operación
    opcion = input("Ingrese el número de la operación (1/2/3/4): ")

    # Ingreso de números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Ejecución de operación
    if opcion == '1':
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif opcion == '2':
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif opcion == '3':
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif opcion == '4':
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: División entre cero no permitida")
    else:
        print("Opción no válida")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
