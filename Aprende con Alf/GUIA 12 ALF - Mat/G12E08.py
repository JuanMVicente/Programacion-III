'''El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.

Diagrama de sectores con los fallecidos y supervivientes.
Histograma con las edades.
Diagrama de barras con el número de personas en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    archivo = 'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/matplotlib/titanic.csv'
    df = pd.read_csv(archivo, sep=',', decimal='.', index_col=0)
    print(df)
    diagrama_sectores(df,'Diagrama de Torta: Supervivientes vs fallecidos')
    # diagrama_histograma(df, 'Histograma Edades')
    # diagrama_barras_clase(df, 'Diag de Barras: Personas por Clase')
    # diagrama_barras_clase_supervivientes(df, 'Diag de Barras: Supervivienters por Clase')
    # diagrama_barras_clase_supervivientes_acumulados(df, 'Diag de Barras: Acumulado por clase')

def diagrama_sectores(df, titulo): 
    fig, ax = plt.subplots()
    df.Survived.value_counts().plot(kind = "pie", labels = ["Muertos", "Supervivientes"], title = titulo)
    plt.show()


def diagrama_histograma(df, titulo):
    fig, ax = plt.subplots()
    df.Age.plot(kind = "hist", title = titulo)
    plt.show()

def diagrama_barras_clase(df, titulo):
    # fig, ax = plt.subplots()
    # df.Pclass.value_counts().plot(kind = "bar", title = titulo)
    df.groupby("Pclass").size().plot(kind = "bar", title = titulo)
    plt.show()


def diagrama_barras_clase_supervivientes(df, titulo):
    df.groupby(["Pclass","Survived"]).size().unstack().plot(kind = "bar", title = titulo)
    plt.show()


def diagrama_barras_clase_supervivientes_acumulados(df, titulo):
    df.groupby(["Pclass","Survived"]).size().unstack().plot(kind = "bar", stacked = True, title = titulo)
    plt.show()


if __name__ == "__main__":
    main()