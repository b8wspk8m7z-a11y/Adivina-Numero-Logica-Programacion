import random

# Proyecto Autónomo - Lógica de Programación
# Juego: Adivina el Número

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Bienvenido al juego Adivina el Número")
print("El sistema ha generado un número entre 1 y 100.")

while not adivinado:
    try:
        numero_usuario = int(input("Ingresa un número: "))
        intentos += 1

        if numero_usuario > numero_secreto:
            print("El número secreto es menor.")
        elif numero_usuario < numero_secreto:
            print("El número secreto es mayor.")
        else:
            adivinado = True
            print("¡Felicidades! Adivinaste el número.")
            print("Intentos realizados:", intentos)

    except ValueError:
        print("Error: debes ingresar un número válido.")
