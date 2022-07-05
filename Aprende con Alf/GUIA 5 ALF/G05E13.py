l = input("Escribe una muestra de nros separados por comas: ")
l = l.split(",")
for i in range(len(l)):
    l[i] = int(l[i])
suma = 0
sq = 0
for i in range(len(l)):
    suma += l[i]
    sq += l[i]**2
media = suma / len(l)
desvst = (sq/len(l)-media**2)**(1/2)
print('La media es ' +str(round(media,2)) + ', y la desviación típica es ' + str(round(desvst,2)) + ".")