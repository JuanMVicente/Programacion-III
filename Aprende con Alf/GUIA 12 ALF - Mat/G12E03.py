'''Escribir una función que reciba una serie de Pandas con las notas de los alumnos de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener el título “Distribución de notas”.'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    alumnos = [4,5,4,6,8,1,2,5,6,2,4,5,8,2,6,4,8,2,5,1,9,5]
    alumnos = pd.Series(alumnos)
    diagrama_cajas(alumnos)


def diagrama_cajas(alumnos): 
    fig, ax = plt.subplots()
    ax.boxplot(alumnos)
    ax.set_title("Distribución de notas") # loc='center', fontdict='arial'
    plt.show()


if __name__ == "__main__":
    main()