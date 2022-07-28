def rgb(r, g, b):


    
    cad1 = str(hex(hexaAux(r)))[2:].upper()
    if cad1.__len__() == 1:
        cad1 = "0" + cad1

    cad2 = str(hex(hexaAux(g)))[2:].upper()
    if cad2.__len__() == 1:
        cad2 = "0" + cad2

    cad3 = str(hex(hexaAux(b)))[2:].upper()
    if cad3.__len__() == 1:
        cad3 = "0" + cad3


    return cad1 + cad2 + cad3


def hexaAux(x):
    if x>255:
        return 255
    elif x<0:
        return 0
    else:
        return x

print(rgb(0,0,0))
print(rgb(-20,275,125))
print(str(hexaAux(-20)))
print(str(hex(-20)))
print(str(hexaAux(275)))
print(str(hex(275)))