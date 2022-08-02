'''Escribir una función que reciba una serie de Pandas con el número de ventas de un producto durante los meses de un trimestre y un título y cree un diagrama de sectores con las ventas en formato png con el titulo dado. El diagrama debe guardarse en un fichero con formato png y el título dado.'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    ventas = {'Abril':250,'Mayo':230,'Junio':265}
    serie = pd.Series(ventas)
    titulo = "diagrama_ventas"
    diagrama_sectores(serie, titulo)
    serie.to_list()


def diagrama_sectores(serie, titulo): 
    fig, ax = plt.subplots()
    ax.pie(serie, labels=list(serie.keys()))
    ax.set_title(titulo)
    plt.savefig(titulo + '.png')


if __name__ == "__main__":
    main()  