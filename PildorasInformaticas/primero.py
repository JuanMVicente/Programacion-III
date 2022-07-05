saludo = "hola mundo"


print(saludo.upper())

edad = int(input("Edad?"))
print("Edad: ", edad)

if edad<18:
    print("es menor.")
elif edad<65:
    print("edad laboral.")
else:
    print("jubilado.")