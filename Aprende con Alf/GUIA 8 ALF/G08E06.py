'''Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.'''

def calificaciones(lista):
    l=[]
    for i in lista:
        if i>=7:
            l.append('promociona')
        elif i>=5:
            l.append('habilita')
        else:
            l.append('desaprueba')
    return l

laux=(5,6,8,2,4,7,8,9,6,3,2,5,7,5.5,7.2,5.1)

print(calificaciones(laux))