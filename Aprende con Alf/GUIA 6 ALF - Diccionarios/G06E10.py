choice = 0
clients = {}
while choice != "6":
    if choice == "1":
        nif = input("Nro Cliente: ")
        name = input("Nombre: ")
        direccion = input("Dirección: ")
        mail = input("Mail: ")
        tel = input("Teléfono: ")
        vip = input("Preferente S/N: ")
        client = {"Name": name, "Direccion": direccion, "Mail": mail, "Telefono": tel, "VIP": vip=="S"}
        clients[nif] = client
    if choice == "2":
        nif = input("Nro de cliente que desea elimininar? ")
        if nif in clients:
            del clients[nif]
        else:
            print("No existe cliente con este Nro")
    if choice == "3":
        nif = input("Nro de cliente que desea mostrar? ")
        if nif in clients:
            print('Nro Cliente:', nif)
            for key, value in clients[nif].items():
                print(key.title() + ':', value)
        else:
            print("No existe cliente con este Nro")
    if choice == "4":
        print("Lista de clientes: ")
        for key, value in clients.items():
            print(key, value["Name"])
    if choice == "5":
        print("Lista de clientes preferentes: ")
        for key, value in clients.items():
            if value["VIP"]:
                print(key, value["Name"])
    choice = input("Opciones:\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción: ")