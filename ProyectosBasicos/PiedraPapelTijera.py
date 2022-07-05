from operator import truediv
import random


def PiedraPapelTijera():

    print("##################################")
    print("      Bienvenido(a) al Juego")
    print("##################################")

    respuestaUsuario = input("Escoge una opcion:\n'pi' Piedra\n'pa'Papel\n'ti' Tijera\n").lower()

    eleccionComputadora = random.choice(['pi','pa','ti'])

    if respuestaUsuario == eleccionComputadora:
        return 'Empate'
    elif ganoUsuario(respuestaUsuario,eleccionComputadora):
        return 'Ganaste'
    return 'Perdiste' # los return anterior cierran la funcion
    

def ganoUsuario(jugador, computadora):
    if ((jugador == 'pi' and computadora == 'ti') or (jugador == 'pa' and computadora == 'pi') or (jugador == 'ti' and computadora == 'pa')):
        return True
    else: 
        return False


print(PiedraPapelTijera())