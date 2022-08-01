'''Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.'''

from pydoc import describe
import pandas as pd


def main():
    alumnos = {'Juan':9,'Pablo':10,'Pedro':7,'Bianca':8,'Luis':4}
    alumnos = pd.Series(alumnos)

    resultado = {'minimo':alumnos.min(),'máximo':alumnos.max(),'media':alumnos.mean(),'desviación std':alumnos.std()}
    resultado = pd.Series(resultado)

    print(resultado)


if __name__ == "__main__":
    main()