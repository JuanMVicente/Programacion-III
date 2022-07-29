'''El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.'''


def main():
    lista= procesa_archivo('calificaciones.csv')
    print("####### Ejercicio 1 ######")
    for diccionario in lista:
        print(diccionario)
    agrega_nota(lista)
    print("####### Ejercicio 2 ######")
    for diccionario in lista:
        print(diccionario['Apellidos'] + ' - ' + str(diccionario['NotaFinal']))
    aprobados, suspensos = califica(lista)
    print("####### Ejercicio 3 ######")
    for alumno in aprobados:
        print(alumno['Apellidos'])
    print("####### Ejercicio 3 ######")
    for alumno in suspensos:
        print(alumno['Apellidos'])

def procesa_archivo(nombre_archivo):
    archivo = open(nombre_archivo,'r',encoding='UTF8')
    datos = archivo.read().split('\n')
    archivo.close()
    # inicializado el diccionario
    lista = []

    # saco las claves del diccionario
    claves = datos.pop(0).split(';')
    datos.pop(len(datos)-1)

    # lleno la lista de diccionarios
    for linea in datos:
        diccionario_aux = {}
        linea = linea.split(';')
        diccionario_aux[claves[0]] = linea[0]
        diccionario_aux[claves[1]] = linea[1]
        diccionario_aux[claves[2]] = linea[2]
        for i in range(3,len(claves)):
            valor = linea[i].replace(',','.')
            if valor == '': valor = -1
            diccionario_aux[claves[i]] = float(valor)
        lista.append(diccionario_aux)
        lista.sort(key=lambda p: p['Apellidos'])
    return lista


def agrega_nota(lista):
    for persona in lista:
        if persona['Ordinario1'] == -1:
            nota = persona['Parcial1'] * 0.3
        else:
            nota = persona['Ordinario1'] * 0.3
        if persona['Ordinario2'] == -1:
            nota += persona['Parcial2'] * 0.3
        else:
            nota += persona['Ordinario2'] * 0.3
        if persona['OrdinarioPracticas'] == -1:
            nota += persona['Practicas'] * 0.4
        else:
            nota += persona['OrdinarioPracticas'] * 0.4
        
        persona['NotaFinal'] = nota
    return lista


def califica(alumnos):
    aprobados = []
    suspensos = []
    for persona in alumnos:
        asistencia = ""
        asistencia = persona['Asistencia']
        asistencia = int(asistencia.replace('%',''))

        cumple_asistencia = asistencia >= 75
        cumple_parcial1 = persona['Ordinario1'] >= 4 or (persona['Parcial1'] >= 4 and persona['Ordinario1'] == -1)
        cumple_parcial2 = persona['Ordinario2'] >= 4 or (persona['Parcial2'] >= 4 and persona['Ordinario2'] == -1)
        cumple_practica = persona['OrdinarioPracticas'] >= 4 or (persona['Practicas'] >= 4 and persona['OrdinarioPracticas'] == -1)
        cumple_nota_final = persona['NotaFinal'] >= 5


        if cumple_asistencia and cumple_parcial1 and cumple_parcial2 and cumple_practica and cumple_nota_final:
            aprobados.append(persona)
        else:
            suspensos.append(persona)
    return aprobados, suspensos


    

if __name__ == "__main__":
    main()