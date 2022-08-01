'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    serie = {2010:100, 2011:120, 2012: 130, 2013:133, 2011:125, 2014: 122, 2015:135, 2016:140, 2017: 137, 2018:142, 2019:145, 2020: 141, 2021:155, 2022:151}
    diagrama_linea(serie)
    

def diagrama_linea(serie):
    fig, ax = plt.subplots()
    ax.plot(serie.keys(),serie.values())
    plt.show()


if __name__ == "__main__":
    main()