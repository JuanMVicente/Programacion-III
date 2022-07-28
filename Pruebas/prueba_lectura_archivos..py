file = open("Pruebas\prueba.csv", "w")
file.write("ejemplo1,01\n")
file.write("ejemplo2,02")
file.close()

file = open("Pruebas\prueba2.csv", "w")
file.write("ejemplo4,04\n")
file.write("ejemplo5,05")
file.close()


import csv

def genera_lista(categoria):
    with open(categoria,'r') as archivo:
        lector = csv.reader(archivo, delimiter=",")
        lista = []
        for linea in lector:
            fila = [linea[0], linea[1]]
            lista.append(fila)
    print(lista)
    return lista

def procesamiento():
    datos = {}
    categorys = {"Pruebas\prueba.csv", "Pruebas\prueba2.csv"}
    tabla = []
    for category in categorys:
        print(category)
        tabla.extend(genera_lista(category))
   
    print(tabla)

procesamiento()

