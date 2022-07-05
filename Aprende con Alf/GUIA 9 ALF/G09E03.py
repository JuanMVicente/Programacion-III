'''Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de 
multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar 
un mensaje por pantalla informando de ello.'''
n = int(input('Numero n: '))
m = int(input('Numero m: '))

nombreArchivo = 'tabla-'+str(n)+'.txt'
try:
    archivo = open(nombreArchivo,'r')
except FileNotFoundError:
    #print('El finchero con el numero ' + str(n) + ' no Existe')
    print('El finchero con el numero' , n, 'no Existe')
else:
    lineas = archivo.readlines()
    print(lineas[m-1])