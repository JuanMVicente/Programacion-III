n = str(input("Nombre: "))
s = str(input("Hombre (H) / Mujer (M): "))
if (n[0].lower() < "n" and s.lower() == "m") or (n[0].lower() >= "n" and s.lower() == "h"):
    print("Grupo A")
else:
    print("Grupo B")