f = input("Fecha de su nacimiento en formato dd/mm/aaaa: ")
print ("Usted nació el día " + str(f[:2]) + " del mes " + str(f[3:5]) + " en el año " + str(f[6:]) + ".")

d = int(f[:2])
m = int(f[3:5])
a = int(f[6:])

print('Día ', d)
print('Mes ', m)
print('Año ', a)