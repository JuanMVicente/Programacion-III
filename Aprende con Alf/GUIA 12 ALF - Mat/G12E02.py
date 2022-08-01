'''Escribir una función que reciba una diccionario con las notas de las asignaturas de un curso y una cadena con el nombre de un color y devuelva un diagrama de barras de las notas en el color dado.'''

import matplotlib.pyplot as plt


def main():
    alumnos = {'Juan':9,'Pablo':10,'Pedro':7,'Bianca':8,'Luis':4}
    color = 'red'
    diagrama_barras(alumnos, color)

    
def diagrama_barras(diccionario, color):
    fig, ax = plt.subplots()
    ax.bar(diccionario.keys(),diccionario.values(), color=color)
    plt.show()


if __name__ == "__main__":
    main()