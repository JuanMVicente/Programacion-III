
def consultaCliente(archivo, nombre):
    try:
        f = open(archivo,'r')
    except FileNotFoundError:
        return('El finchero listin.txt no Existe')
    else:
        # : Devuelve una lista de cadenas de caracteres donde cada cadena es una linea del fichero referenciado por fichero
        directorio = f.readlines()
        f.close()
        # genero un diccionario con nombre y telefono
        directorio = dict([tuple(linea.split(',')) for linea in directorio])
        if nombre in directorio:
            return directorio[nombre]
        else:
            return('No existe ese Cliente')

def aniadirCliente(archivo, nombre, telefono):
    try:
        f = open(archivo,'a')
    except FileNotFoundError:
        return('El finchero listin.txt no Existe')
    else:
        f.write(nombre + ',' + telefono +'\n')
        f.close()
        return ('El telefenofo se ha aniadido.\n')

def eliminaCliente(archivo, nombre):
    try:
        f = open(archivo,'a')
    except FileNotFoundError:
        return('El finchero listin.txt no Existe')
    else:
        # : Devuelve una lista de cadenas de caracteres donde cada cadena es una linea del fichero referenciado por fichero
        directorio = f.readlines()
        f.close()
        # genero un diccionario con nombre y telefono
        directorio = dict([tuple(linea.split(',')) for linea in directorio])
        if nombre in directorio:
            del directorio[nombre]
            f = open(archivo,'w')
            for nombre, telefono in directorio:
                f.write(nombre + ',' + telefono)
            f.close()
        else:
            return('No existe ese Cliente')

def crearDirectorio(archivo):
    import os
    if os.path.isfile(archivo):
        respuesta = input('El fichero ' + file + ' ya existe. ¿Desea vaciarlo (S/N)? ')
        if respuesta == 'N': 
            return 'No se ha creado el fichero porque ya existe.\n'
        else:
            f = open(archivo, 'w')
            f.close()
            return 'Se ha creado el fichero.\n'

def menu():
    



archivo = 'listin.txt'

