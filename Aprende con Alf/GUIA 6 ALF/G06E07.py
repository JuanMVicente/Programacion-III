a = {}
suma = 0
mas = "s"
while mas == "s":
    clave = input("Artículo: ")
    dato = int(input("Precio: "))
    a[clave] = dato
    mas = input("Desea agregar más datos s/n?")
    suma += dato
print(a)
print("Costo total " + str(suma))

# basket = {}
# more = 'Si'
# while more == 'Si':
#     item = input('Introduce un artículo: ')
#     price = float(input('Introduce el precio de ' + item + ': '))
#     basket[item] = price
#     more = input('¿Quieres añadir artículos a la lista (Si/No)? ')
# cost = 0
# print('Lista de la compra')
# for item, price in basket.items():
#     print(item, '\t', price)
#     cost += price
# print('Coste total: ', cost)