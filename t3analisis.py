def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("Calculadora básica")
    print("Operaciones: suma, resta, multiplicacion, division")
    op = input("Elige una operación: ").strip().lower()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if op == "suma":
        print("Resultado:", sumar(a, b))
    elif op == "resta":
        print("Resultado:", restar(a, b))
    elif op == "multiplicacion":
        print("Resultado:", multiplicar(a, b))
    elif op == "division":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    calculadora()