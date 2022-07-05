dictionary = {}
words = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in words.split(','):
    key, value = i.split(':')
    dictionary[key] = value
phrase = input('Introduce una frase en español: ')
for i in phrase.split():
    if i in dictionary:
        print(dictionary[i], end=' ')
    else:
        print(i, end=' ')