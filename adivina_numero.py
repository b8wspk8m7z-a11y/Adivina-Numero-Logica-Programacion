import random  # Importamos la librería para generar números aleatorios

def juego_adivina_numero():
    print("🎮 Bienvenido al juego Adivina el Número")
    print("Estoy pensando en un número entre 1 y 10.")

    # Genera un número aleatorio entre 1 y 10
    numero_secreto = random.randint(1, 10)

    # Inicializamos el contador de intentos
    intentos = 0

    # Variable booleana para controlar el ciclo
    adivinado = False

    # Ciclo repetitivo que se ejecuta hasta que el usuario adivine
    while not adivinado:
        intento = int(input("Ingresa tu número: "))
        intentos += 1  # Aumenta el contador en cada intento

        # Estructura condicional para comparar el número ingresado
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"🎉 ¡Correcto! Adivinaste en {intentos} intentos.")
            adivinado = True  # Cambia el estado para salir del ciclo

# Llamamos a la función principal del juego
juego_adivina_numero()

