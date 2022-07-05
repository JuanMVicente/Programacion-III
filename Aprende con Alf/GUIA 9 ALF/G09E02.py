'''Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de 
multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no 
existe debe mostrar un mensaje por pantalla informando de ello.'''

n = int(input('Escribe un número del 1 al 10: '))
nombreArchivo = 'tabla-'+str(n)+'.txt'
try:
    archivo = open(nombreArchivo,'r')
except FileNotFoundError:
    #print('El finchero con el numero ' + str(n) + ' no Existe')
    print('El finchero con el numero' , n, 'no Existe')
else:
    print(archivo.read())
