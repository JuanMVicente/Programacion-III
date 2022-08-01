'''Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.'''

import pandas as pd


def main():
    datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}
    df = pd.DataFrame(datos)
    print(df)
    meses = ['Enero', 'Marzo']
    print('Balance:', balance(df, meses))


def balance(datos, meses):
    datos['Balance'] = datos.Ventas - datos.Gastos
    print(datos)
    return datos.set_index('Mes').loc[meses,'Balance'].sum()
        


if __name__ == "__main__":
    main()