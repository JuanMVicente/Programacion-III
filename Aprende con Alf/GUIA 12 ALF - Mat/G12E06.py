'''Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos de una empresa por meses y devuelva un diagrama de líneas con dos líneas, una para los ingresos y otra para los gastos. El diagrama debe tener una leyenda identificando la línea de los ingresos y la de los gastos, un título con el nombre “Evolución de ingresos y gastos” y el eje y debe empezar en 0.'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}
    df = pd.DataFrame(datos)
    diagrama_linea(df, "Evolución de ingresos y gastos")


def diagrama_linea(serie, titulo):
    fig, ax = plt.subplots()
    ax.plot(serie['Mes'],serie['Ventas'], color = 'tab:red')
    ax.plot(serie['Mes'],serie['Gastos'], color = 'tab:green')
    ax.set_ylim([0, max(serie['Gastos'].max(), serie['Ventas'].max()) + 5000])
    ax.set_title(titulo)
    plt.show()


if __name__ == "__main__":
    main()