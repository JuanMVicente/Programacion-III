'''Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:

1- Generar un DataFrame con los datos de los cuatro ficheros.
2- Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
3- Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
4- Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
5- Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.
6- Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
7- Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
8- Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
9- Mostrar un resumen descriptivo para cada contaminante por distritos.
10- Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
11- Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
12- Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.'''

import pandas as pd
import numpy as np
import datetime as dt


def main():
    archivos = {'emisiones_2016':'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2016.csv',
                'emisiones_2017':'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2017.csv',
                'emisiones_2018':'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2018.csv',
                'emisiones_2019':'https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/emisiones-2019.csv'}
    emisiones = generar_df(archivos)
    print('########## Ejercicio 1 ##########')
    print(emisiones)
    print(emisiones.describe())

    print('########## Ejercicio 2 ##########')
    emisiones = eliminar_df(emisiones)
    # forma distinta de filtrar un dataframe
    '''columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']
    columnas.extend([col for col in emisiones if col.startswith('D')])
    emisiones = emisiones[columnas]'''
    print(emisiones)

    print('########## Ejercicio 3 ##########')
    emisiones = emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
    print(emisiones)

    print('########## Ejercicio 4 ##########')
    emisiones = fecha(emisiones)
    print(emisiones)

    print('########## Ejercicio 5 ##########')
    emisiones = emisiones.drop(emisiones[np.isnat(emisiones.FECHA)].index)
    emisiones = emisiones.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])
    print(emisiones)

    print('########## Ejercicio 6 ##########')
    estaciones = emisiones.ESTACION.unique()
    print('Estaciones:', estaciones)
    contaminantes = emisiones.MAGNITUD.unique()
    print('Contaminantes:', contaminantes)

    print('########## Ejercicio 7 ##########')
    print(filtro_estacion_contaminantes_fechas(emisiones, 56, 8, dt.datetime.strptime('2018/10/25', '%Y/%m/%d'), dt.datetime.strptime('2019/02/12', '%Y/%m/%d')))

    print('########## Ejercicio 8 ##########')
    print(emisiones.groupby('MAGNITUD').VALOR.describe())

    print('########## Ejercicio 9 ##########')
    emisiones.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()

    print('########## Ejercicio 10 ##########')
    print('Resumen Dióxido de Nitrógeno en Plaza Elíptica:\n', resumen(emisiones, 56, 8),'\n', sep='')

    print('########## Ejercicio 11 ##########')
    print(evolucion_mensual(emisiones, 8, 2019))


    
def generar_df(archivos):
    df = pd.DataFrame()
    for archivo in archivos:
        df_aux = pd.read_csv(archivos[archivo], sep=';')
        # df_aux['AÑO'] = int(archivo[-4:])
        df = pd.concat([df,df_aux])
    return df


def eliminar_df(emisiones):
    eliminar = ['PROVINCIA','MUNICIPIO','PUNTO_MUESTREO']
    for i in range(1,32):
        if i<10:
            cad = "V0" + str(i)
        else:
            cad = "V" + str(i)  
        eliminar.append(cad)
    for columna in eliminar:
        del emisiones[columna]
    return emisiones


def fecha(emisiones):
    # emisiones['DIA'] = emisiones.DIA.str.strip('D')
    emisiones['FECHA'] = emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.DIA.str.strip('D')
    emisiones['FECHA'] = pd.to_datetime(emisiones.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')
    return emisiones

def filtro_estacion_contaminantes_fechas(emisiones, estacion,contaminante,fecha_inicio,fecha_fin):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante) & (emisiones.FECHA >= fecha_inicio) & (emisiones.FECHA <= fecha_fin)].sort_values('FECHA').VALOR

def resumen(emisiones, estacion, contaminante):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)].VALOR.describe()

def evolucion_mensual(emisiones, contaminante, año):
    return emisiones[(emisiones.MAGNITUD == contaminante) & (emisiones.ANO == año)].groupby(['ESTACION', 'MES']).VALOR.mean().unstack('MES')

if __name__ == "__main__":
    main()