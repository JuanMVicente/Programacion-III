'''Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea 
(url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.'''
from urllib import request
from urllib.error import URLError

def leeArchivo(url, pais):
    try:
        archivo = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        # Genero una lista donde cada componente es una línea del archivo 
        contenido = archivo.read().decode('utf-8').split('\n')
        # divido la lista segun el espacio entre cada dato
        contenido = [i.split('\t') for i in contenido]
        # al primer valor lo cambio por solo el código del pais
        for i in contenido:
            i[0] = i[0].split(',')[-1]
        # cambio el contenido del primer dato de la primer fila
        contenido[0][0] = 'anio'
        #separo los contenidos cabecera y datos
        contenido = {i[0]:i[1:] for i in contenido}
        # genero el resultado esperado para la función
        resultado = {contenido['anio'][i]:contenido[pais][i] for i in range(len(contenido['anio']))}
        return resultado


url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true'

pais = input('Introduce un pais: ')
print('Producto Bruto per Capita de ', pais)
resultado = leeArchivo(url,pais)
resultado = resultado.items() # Devuelve un iterador sobre los pares clave‑valor de un diccionario
print ('Anio', '\t', 'PIB') #\t es una tabulación
for anio, pib in resultado:
    print(anio, '\t', pib)
