import math


def operaciones():
    while True:
        try:
            cantidad = int(input("Ingrese el número de operaciones a realizar: "))
            break
        except ValueError:
            print("Ingrese solo números")

    if opción == 1:
        contador = 0
        for _ in range(cantidad):
            while True:
                try:
                    valor = float(input("Ingrese el valor númerico: "))
                    break
                except ValueError:
                    print("Ingrese solo números")
            contador += valor
        print(f"El valor de la suma es de: {contador:.1f}")

    elif opción == 2:
        contador = 1
        for _ in range(cantidad):
            while True:
                try:
                    valor = float(input("Ingrese el valor númerico: "))
                    break
                except ValueError:
                    print("Ingrese solo números")
            contador *= valor
        print(f"El valor de la multiplicación es de: {contador:.1f}")

    elif opción == 3:
        for _ in range(cantidad):
            while True:
                try:
                    dividendo = float(input("Ingrese el dividendo: "))
                    divisor = float(input("Ingrese el divisor: "))
                    break
                except ValueError:
                    print("Ingrese solo números")
            if divisor == 0:
                print("El divisor no puede ser igual a 0")
            else:
                resultado = dividendo / divisor
                print(f"El valor de la división es de: {resultado:.3f}")

    elif opción == 4:
        for _ in range(cantidad):
            while True:
                try:
                    base = float(input("Ingrese la base: "))
                    exponente = float(input("Ingrese el exponente: "))
                    break
                except ValueError:
                    print("Ingrese solo números")
            resultado = base**exponente
            print(f"El valor de la potencia es de: {resultado:.1f}")

    elif opción == 5:
        for _ in range(cantidad):
            while True:
                try:
                    indice = float(input("Ingrese el índice de la raíz: "))
                    radicando = float(input("Ingrese el radicando de la raíz: "))
                    break
                except ValueError:
                    print("Ingrese solo números")
            resultado = radicando ** (1 / indice)
            print(f"El valor de la raíz es de: {resultado:.1f}")

    elif opción == 6:
        for _ in range(cantidad):
            while True:
                try:
                    argumento = float(input("Ingrese el argumento del logaritmo: "))
                    base = float(input("Ingrese la base del logaritmo: "))
                    break
                except ValueError:
                    print("Ingrese solo números")
            resultado = math.log(argumento, base)
            print(f"El valor del logaritmo es de: {resultado:.1f}")

    else:
        print("Operación no valida")
        print("Ingrese solo números enteros entre el 1 y el 6")
        exit()


name = input("Ingrese su nombre: ")
print(f"Bienvenido/a {name} a tu calculadora")

menu_operaciones = [
    "1. Suma y/o Resta",
    "2. Multiplicación",
    "3. División",
    "4. Potenciación",
    "5. Raíz",
    "6. Logaritmo",
]
print("Las operaciones disponibles son:")
for lista in menu_operaciones:
    print(lista)

while True:
    try:
        opción = int(input("Escoja el número de la operación deseada: "))
        break
    except ValueError:
        print("Ingrese solo números")

operaciones()
