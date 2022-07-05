from urllib import request
from datetime import date
import os

def newFoulder(category):
    #Corroboro que la carpeta exista y si no la creamos
    
    if not(os.path.isdir(category)):
        os.mkdir(category)

def monthName(num):
    if num == 1:
        month = 'Enero'
    elif num == 2:
        month = 'Febrero'
    elif num == 3:
        month = 'Marzo'
    elif num == 4:
        month= 'Abril'
    elif num == 5:
        month= 'Mayo'
    elif num == 6:
        month = 'Junio'
    elif num == 7:
        month = 'Julio'
    elif num == 8:
        month = 'Augosto'
    elif num == 9:
        month= 'Septiembre'
    elif num == 10:
        month= 'Octubre'
    elif num == 11:
        month= 'Noviembre'
    elif num == 12:
        month= 'Diciembre'
    return month

def completeNum(num):
    if num<10:
        return "0"+ str(num)
    else:
        return str(num)

def downloadFile(urlFile, category):
    #le doy el formato solicitado
    dt = date.today()
    #creo la carpeta correspondiente
    nameLocation = category + "\\" + str(dt.year) + "-" + monthName(dt.month)
    print(os.getcwd())
    locationFile = os.getcwd() + "\\" + nameLocation + "\\" + category + "-" + completeNum(dt.day) + "-" + completeNum(dt.month) + "-" + str(dt.year) + ".csv"
    nameFile = category + "-" + completeNum(dt.day) + "-" + completeNum(dt.month) + "-" + str(dt.year) + ".csv"
    print(nameFile)
    print(urlFile)
    if not(os.path.isdir(nameLocation)):
        os.mkdir(nameLocation)
    
    #bajo el archivo
    try:
        request.urlretrieve("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv","verga.csv")


    except Exception:
        #urlFile = (input("Se ha producido un error, introduzca la URL correcta: "))
        #hacer una función para cambiar la URL
        #downloadFile(urlFile, category)
        print("Se ha producido un error.")

#datos importantes

categorys = {"Museos": 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv',"Salas de Cine" : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv',"Bibliotecas Populares" : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'}

#Creación de carpetas
for category in categorys:
    newFoulder(category)

for category in categorys:
    downloadFile(categorys[category],category)