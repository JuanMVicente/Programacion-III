
import random
# https://docs.python.org/


def adivinaElNumeroComputadora(x):
    
    print("##################################")
    print("      Bienvenido(a) al Juego")
    print("##################################")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente encontrarlo.")

    limiteInferior = 1
    limiteSuperior = x

    respuesta = ""

    while respuesta != "C":
        # Generamos predicción de la computadora
        if limiteInferior != limiteSuperior:
            prediccion = random.randint(limiteInferior,limiteSuperior)
        else:
            prediccion = limiteInferior

        # Obtener respuesta del usuario

        respuesta = input(f"Mi prediccion es {prediccion}, Si es muy alta ingresa (A). Si es muy baja ingresa (B). Si es correcta ingresa (C): ").upper()

        if respuesta == "A":
            limiteSuperior = prediccion - 1
        elif respuesta == "B":
            limiteInferior = prediccion + 1
                
    print(f"La máquina a encontrado el número correctamente: {prediccion}")

adivinaElNumeroComputadora(10)
