'''El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con : Empresa (nombre de la empresa), Apertura (precio de la acción a la apertura de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Cierre (precio de la acción al cierre de bolsa), Volumen (volumen al cierre de bolsa). Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales de las cotizaciones de cierre de cada banco.'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    archivo = 'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/matplotlib/bancos.csv'
    df = pd.read_csv(archivo, sep=',', decimal='.') # index_col=1
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    # print(datos)
    diagrama_linea(df)



def diagrama_linea(serie):
    fig, ax = plt.subplots()
    serie.groupby('Empresa').plot(x = 'Fecha', y = "Cierre", ax = ax)
    plt.title('Evolución de las cotizaciones (' + "Cierre" + ')')
    plt.legend(serie.groupby('Empresa').groups.keys())
    plt.show()


if __name__ == "__main__":
    main()