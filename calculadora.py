 """
def sumar(a, b):
    return a + b

 """
def restar(a, b):
    return a - b

 """
def multiplicar(a, b):
    return a * b

 """
def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

"""
def mostrar_menu():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

 """
def calculadora():
    while True:
         """
        mostrar_menu()

        """
        opcion = input("Selecciona una opción (1/2/3/4/5): ")

        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break   """

         """
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, introduce números válidos.")
            continue  """

        """
        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"El resultado de {num1} + {num2} es: {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"El resultado de {num1} - {num2} es: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"El resultado de {num1} * {num2} es: {resultado}")
        elif opcion == '4':
            resultado = dividir(num1, num2)
            print(f"El resultado de {num1} / {num2} es: {resultado}")
        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 5.")

 """
calculadora()



