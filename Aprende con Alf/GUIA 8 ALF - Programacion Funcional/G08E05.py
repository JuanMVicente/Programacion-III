'''Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.'''

def fraseADiccionario(frase):
    palabras = frase.split()
    longitud = map(len, palabras)
    return dict(zip(palabras,longitud))

print(fraseADiccionario('estoy aprendiendo y estoy muy contento'))