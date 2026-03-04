print("=== CALCULADORA ===")
print("Operaciones: + - * /")
print("Escribe 'salir' para cerrar")
print("===================")

while True:
    num1 = input("\nPrimer número: ")
    if num1.lower() == "salir":
        print("¡Hasta luego!")
        break

    num2 = input("Segundo número: ")
    if num2.lower() == "salir":
        print("¡Hasta luego!")
        break

    operacion = input("Operación (+, -, *, /): ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("⚠️  Error: ingresa solo números válidos")
        continue

    if operacion == "+":
        print("Resultado:", num1 + num2)
    elif operacion == "-":
        print("Resultado:", num1 - num2)
    elif operacion == "*":
        print("Resultado:", num1 * num2)
    elif operacion == "/":
        if num2 == 0:
            print("⚠️  Error: no se puede dividir entre 0")
        else:
            print("Resultado:", num1 / num2)
    else:
        print("⚠️  Operación no válida. Usa +, -, *, /")