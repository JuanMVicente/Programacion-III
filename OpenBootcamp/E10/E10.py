
import math


def areaTriangulo(altura,base):
    return base * altura / 2


def areaCirculo(radio):
    return math.pi * (radio ** 2)


print(areaTriangulo(4,2))
print(areaCirculo(2))      