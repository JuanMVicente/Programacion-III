p = {}
mas = "s"
while mas == "s":
    clave = input("Que dato desear agregar? ")
    dato = input(clave + ": ")
    p[clave] = dato
    print(p)
    mas = input("Desea agregar más datos s/n?")


