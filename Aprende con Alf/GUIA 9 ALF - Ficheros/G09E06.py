'''Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''

import os


def consultaCliente(archivo, nombre):
    try:
        archivo = open(archivo,'r')
    except FileNotFoundError:
        return('El finchero listin.txt no Existe')
    else:
        # : Devuelve una lista de cadenas de caracteres donde cada cadena es una linea del fichero referenciado por fichero
        directorio = archivo.readlines()
        archivo.close()
        # genero un diccionario con nombre y telefono
        directorio = dict([tuple(linea.split(',')) for linea in directorio])
        if nombre in directorio:
            return directorio[nombre]
        else:
            return('No existe ese Cliente')


def aniadirCliente(archivo, nombre, telefono):
    try:
        archivo = open(archivo,'a')
    except FileNotFoundError:
        return('El finchero listin.txt no Existe')
    else:
        archivo.write(nombre + ',' + telefono +'\n')
        archivo.close()
        return ('El telefenofo se ha aniadido.\n')


def eliminaCliente(archivo, nombre):
    try:
        archivo = open(archivo,'a')
    except FileNotFoundError:
        return('El finchero listin.txt no Existe')
    else:
        # Devuelve una lista de cadenas de caracteres donde cada cadena es una linea del fichero referenciado por fichero
        directorio = archivo.readlines()
        archivo.close()
        # genero un diccionario con nombre y telefono
        directorio = dict([tuple(linea.split(',')) for linea in directorio])
        if nombre in directorio:
            del directorio[nombre]
            archivo = open(archivo,'w')
            for nombre, telefono in directorio:
                archivo.write(nombre + ',' + telefono)
            archivo.close()
            return ('Se ha borrado el Telefono solicitado\n')
        else:
            return(f'No existe el Cliente {nombre}')


def crearDirectorio(archivo):
    if os.path.isfile(archivo):
        respuesta = input('El archivo ' + archivo + ' ya existe. ¿Desea vaciarlo (S/N)? ')
        if respuesta == 'N': 
            return 'No se ha creado el fichero porque ya existe.\n'
    else:
        f = open(archivo, 'w')
        f.close()
        return 'Se ha creado el fichero.\n'


def menu():
    print('Gesión del listín telefónico')
    print('============================')
    print('1 - Consultar un teléfono')
    print('2 - Añadir un teléfono')
    print('3 - Eliminar un teléfono')
    print('4 - Crear el listín')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def directorio():
    archivo = 'listin.txt' 
    while True:
        opcion = menu()
        if opcion == '1':
            nombre = input('Introduce el nombre del cliente: ')
            print(consultaCliente(archivo, nombre))
        elif opcion == '2':
            nombre = input('Introduce el nombre del cliente: ')
            telf = input('Introduce el teléfono del cliente: ')
            print(aniadirCliente(archivo, nombre, telf))
        elif opcion == '3':
            name = input('Introduce el nombre del cliente: ')
            print(eliminaCliente(archivo, nombre))
        elif opcion == '4':
            print(crearDirectorio(archivo))
        else:
            break
    return


directorio()