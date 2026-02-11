import random

def juego_adivina_numero():
    print("🎮 Bienvenido al juego Adivina el Número")
    print("Estoy pensando en un número entre 1 y 10.")

    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False

    while not adivinado:
        intento = int(input("Ingresa tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"🎉 ¡Correcto! Adivinaste en {intentos} intentos.")
            adivinado = True

juego_adivina_numero()
