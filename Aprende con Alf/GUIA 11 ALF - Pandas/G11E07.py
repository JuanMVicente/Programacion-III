'''El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

Generar un DataFrame con los datos del fichero.
Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
Mostrar por pantalla los datos del pasajero con identificador 148.
Mostrar por pantalla las filas pares del DataFrame.
Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
Eliminar del DataFrame los pasajeros con edad desconocida.
Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.'''

from itertools import count
import pandas as pd


def main():
    df = pd.read_csv('titanic.csv', sep=',', decimal='.', index_col=0)
    print('########## Ejercicio 2 ##########')
    print(df.info())
    print(df.head(10))
    print(df.tail(10))
    print('########## Ejercicio 3 ##########')
    print(df.loc[148])
    print('########## Ejercicio 4 ##########')
    print(df.iloc[range(1,df.shape[0],2)])
    print('########## Ejercicio 5 ##########')
    print(df[df['Pclass']==1]['Name'].sort_values())
    print('########## Ejercicio 6 ##########')
    print(df['Survived'].value_counts()/df['Survived'].count() * 100)
    print('########## Ejercicio 7 ##########')
    print(df.groupby('Pclass')['Survived'].value_counts(normalize=True))
    print('########## Ejercicio 8 ##########')
    df2 = df.dropna(subset=['Age'])
    print(df2)
    print('########## Ejercicio 8 ##########')
    print(df2.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])
    print('########## Ejercicio 9 ##########')
    df2['Menor'] = df2['Age'] < 18
    print(df2)
    print('########## Ejercicio 10 ##########')
    print(df2.groupby(['Pclass','Menor'])['Survived'].value_counts(normalize=True))

if __name__ == "__main__":
    main()