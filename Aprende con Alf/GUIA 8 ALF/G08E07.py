'''Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas 
en mayúsculas y las calificaciones correspondientes a las notas.'''

def calificaciones(nota):
    if nota>=7:
           return 'promociona'
    elif nota>=5:
            return 'habilita'
    else:
            return 'desaprueba'


def nuevaLista(l2): 
    materias = map(str.upper, l2.keys())
    notas = map(calificaciones, l2.values())
    return dict(zip(materias, notas))

lAux={'Matematica':5.8, 'Lengua': 4, 'Fisica': 9, 'Historia':5,'Quimica':7}

print(nuevaLista(lAux))