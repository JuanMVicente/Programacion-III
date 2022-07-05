'''Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt 
la tabla de multiplicar de ese número, done n es el número introducido.'''

n = int(input('Escribe un número del 1 al 10: '))
nombreArchivo = 'tabla-'+str(n)+'.txt'
archivo = open(nombreArchivo,'w')
for i in range(1,11):
    #archivo.write(str(i) + ' x ' + str(n) + ' = ' + str(i*n) + '\n')
    archivo.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
archivo.close()


'''n = int(input('Introduce un numero entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()'''