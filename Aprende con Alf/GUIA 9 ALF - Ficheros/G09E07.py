'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.

Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.'''

def main():
    diccionario = procesa_archivo('cotizacion.csv')
    print(diccionario)
    genera_archivo(diccionario)
    

def procesa_archivo(archivo):
    archivo = open(archivo, 'r')
    datos = archivo.read().split('\n')
    archivo.close()
    '''for dato in datos:
        print(dato)
    print(datos)'''
    claves = datos.pop(0).split(';')

    # inicializado el diccionario
    diccionario = {}
    # inicializo las listas dentro del diccionario
    for clave in claves:
        diccionario[clave] = []
    # cargo los datos de cada linea
    for linea in datos:
        valores = linea.split(";")
        diccionario[claves[0]].append(valores[0])
        for i in range(1,len(valores)):
            valor = valores[i]
            valor = valor.replace('.', '')
            valor = float(valor.replace(',','.'))
            diccionario[claves[i]].append(valor)
    return diccionario

def genera_archivo(diccionario):
    # Se borran el vaor de los nombres del diccionario
    del(diccionario['Nombre'])

    # inicializamos el contenido a poner el fichero externo con los nombres de cada columna
    contenido = 'Columna;Minimo;Maximo;Media'

    # en las filas quedaran cada columna y en las columnas los valores calculados
    for clave in diccionario:

        contenido += '\n' + clave + ';' + str(min(diccionario[clave])).replace('.',',') + ';' + str(max(diccionario[clave])).replace('.',',') + ';' + str(sum(diccionario[clave])/len(diccionario[clave])).replace('.',',')

    file = open('cotizacion-analisis.csv',"w")
    file.write(contenido)
    file.close()
    return




if __name__ == "__main__":
    main()