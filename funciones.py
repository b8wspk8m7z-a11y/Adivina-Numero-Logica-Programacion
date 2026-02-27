import random

# Genera un número aleatorio dentro de un rango
def generar_numero(minimo, maximo):
    return random.randint(minimo, maximo)

# Pide al usuario un número validando que sea correcto
def pedir_numero():
    while True:
        try:
            numero = int(input("Ingresa tu número: "))
            return numero
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Evalúa si el intento es mayor, menor o correcto
def evaluar_intento(intento, numero_secreto):
    if intento < numero_secreto:
        return "mayor"
    elif intento > numero_secreto:
        return "menor"
    else:
        return "correcto"

# Muestra mensaje según el resultado
def mostrar_mensaje(resultado):
    if resultado == "mayor":
        print("El número es mayor.")
    elif resultado == "menor":
        print("El número es menor.")
    else:
        print("🎉 ¡Correcto!")