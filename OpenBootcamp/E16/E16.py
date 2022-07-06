import time

def main():
    print(esHora())

def esHora():
    horaSalida = 19
    if time.localtime().tm_hour >= 19:
        return "Es hora de salir"
    else:
        return tiempoRestante()


def tiempoRestante():
    horasRestantes = 19 - time.localtime().tm_hour
    minutosRestantes = 60 - time.localtime().tm_min
    return f"Faltan {horasRestantes} horas y {minutosRestantes} minutos para la salida"


if __name__ == "__main__":
    main()