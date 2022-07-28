# edad =  int(input("Edad: "))
# ing = int(input("Ingresos mensuales: "))
# if edad > 16:
#     if ing >= 1000:
#         print("Tributas impuestos.")
#     else:
#         print("No tributas impuestos")
# else:
#     print("No tributas impuestos")

edad =  int(input("Edad: "))
ing = int(input("Ingresos mensuales: "))
if edad > 16 and ing >= 1000:
    print("Tributas impuestos.")
else:
    print("No tributas impuestos")