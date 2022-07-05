# d = {}
# mas = "R"
# suma = 0
# cobro = 0
# while mas != "T":
#     if mas == "R":
#         fac = input("Nro factura: ")
#         costo = float(input("Monto: "))
#         d[fac] = costo
#         suma += costo
#     if mas == "P":
#         fac = input("Que factura paga? ")
#         costo = d.pop(fac, 0)
#         cobro += costo
#         suma -= costo
#     print("Se debe " + str(round(suma,2) + " y se cobró" + str(round(cobro,2) + ".")
#     mas = input("Registrar (R), Pagar (P) una factura o terminar: ")


invoices = {}
collected = 0
remains = 0
more = ''
while more != 'T':
    if more == 'A':
        key = input('Introduce el número de la factura: ')
        cost = float(input('Introduce el coste de la factura: '))
        invoices[key] = cost
        remains += cost
    if more == 'P':
        key = input('Introduce el número de la factura a pagar: ')
        cost = invoices.pop(key, 0)
        collected += cost
        remains -= cost
    print('Recaudado:', collected)
    print('Pendiente de cobro: ', remains)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')