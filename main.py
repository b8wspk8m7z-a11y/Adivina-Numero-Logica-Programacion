from funciones import *

historial_partidas = []

def jugar():
    numero_secreto = generar_numero(1, 10)
    intentos = 0
    adivinado = False
    historial_intentos = []

    print("\n🎮 Nueva partida iniciada")
    
    while not adivinado:
        intento = pedir_numero()
        intentos += 1
        historial_intentos.append(intento)

        resultado = evaluar_intento(intento, numero_secreto)
        mostrar_mensaje(resultado)

        if resultado == "correcto":
            adivinado = True
            historial_partidas.append(intentos)
            print(f"Adivinaste en {intentos} intentos.")
            print("Intentos realizados:", historial_intentos)

def mostrar_estadisticas():
    if historial_partidas:
        print("\n📊 Estadísticas")
        print("Partidas jugadas:", len(historial_partidas))
        print("Intentos por partida:", historial_partidas)
        print("Mejor partida:", min(historial_partidas))
    else:
        print("No hay partidas registradas.")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Jugar")
        print("2. Ver estadísticas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            print("Gracias por jugar.")
            break
        else:
            print("Opción inválida.")

menu()