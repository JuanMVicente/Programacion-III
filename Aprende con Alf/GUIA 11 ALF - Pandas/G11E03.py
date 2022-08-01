'''Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.'''

import pandas as pd


def main():
    alumnos = {'Juan':9,'Pablo':10,'Pedro':7,'Bianca':8,'Luis':4}
    alumnos = pd.Series(alumnos)
    print('Alumnos\n',alumnos)
    print('Aprobados\n',aprobados(alumnos))


def aprobados(alumnos):
    return alumnos[alumnos >= 7].sort_values(ascending=False)

if __name__ == "__main__":
    main()