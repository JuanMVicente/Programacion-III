import random
# https://docs.python.org/


def adivinaElNumero():
    
    print("##################################")
    print("      Bienvenido(a) al Juego")
    print("##################################")
    print("El objetivo es adivinar el número elegido por la computadora")
    x = int(input("Elija el valor máximo a predecir: "))

    numeroAleatorio = random.randint(1,x) # Numero aleatorio entre 1 y x inclusive

    prediccion = int(input(f"Elija un número entre uno y {x}: "))

    while prediccion != numeroAleatorio:
        if prediccion < numeroAleatorio:
            print("Este número es mas chico")
        else:
            print("Este número es mas grande")
        prediccion = int(input(f"Elija un número entre uno y {x}: ")) #f-string
    
    print(f"¡Felicitaciones! encontraste el número {numeroAleatorio}")



adivinaElNumero()
