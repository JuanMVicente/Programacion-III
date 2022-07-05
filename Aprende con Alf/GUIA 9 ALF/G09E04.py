'''Escribir un programa que acceda a un fichero de internet mediante su url y muestre 
por pantalla el número de palabras que contiene.'''

def archivoPalabras(url):
    from urllib import request
    from urllib.error import URLError
    try:
        archivo = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = archivo.read()
        return len(contenido.split())

print(archivoPalabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(archivoPalabras('https://no-existe.txt'))