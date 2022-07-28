nombre = input("Nombre: ")
edad = input("Edad: ")
dire = input("Dirección: ")
tele = input("Teléfono: ")
datos = {"Nombre": nombre, "Edad": edad, "Dirección": dire, "Teléfono": tele}
print(str(datos["Nombre"])+ " tiene " + str(datos["Edad"]) + " años, vive en " + str(datos["Dirección"]) + " y su número de teléfono es " + str(datos["Teléfono"])+ ".")