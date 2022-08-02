'''Escribir una función que reciba una serie de Pandas con el número de ventas de un producto por años y una cadena con el tipo de gráfico a generar (lineas, barras, sectores, areas) y devuelva un diagrama del tipo indicado con la evolución de las ventas por años y con el título “Evolución del número de ventas”.'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    ventas = {2018:220,2019:250,2020:230,2021:265}
    serie = pd.Series(ventas)
    tipo = input('Elije tipo de Grafico (lineas/barras/sectores/areas): ')
    grafica(serie, tipo)


def grafica(serie,tipo):
    titulo = 'Evolución del número de ventas'
    if tipo.lower() == "lineas":
        diagrama_linea(serie, titulo)
    elif tipo.lower() == "barras":
        diagrama_barras(serie, titulo)
    elif tipo.lower() == "sectores":
        diagrama_sectores(serie, titulo)
    elif tipo.lower() == "areas":
        diagrama_areas(serie, titulo)


def diagrama_barras(serie, titulo):
    fig, ax = plt.subplots()
    ax.bar(list(serie.keys()),serie.tolist(), color='blue')
    plt.show()


def diagrama_linea(serie, titulo):
    fig, ax = plt.subplots()
    ax.plot(list(serie.keys()),serie.tolist())
    ax.set_title(titulo)
    plt.show()


def diagrama_sectores(serie, titulo): 
    fig, ax = plt.subplots()
    ax.pie(serie, labels=list(serie.keys()))
    ax.set_title(titulo)
    plt.show()


def diagrama_areas(serie, titulo): 
    fig, ax = plt.subplots()
    ax.fill_between(list(serie.keys()),serie.tolist())
    ax.set_title(titulo)
    plt.show()


if __name__ == "__main__":
    main()  