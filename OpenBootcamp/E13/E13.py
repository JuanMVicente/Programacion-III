

class Vehiculo:
    color = None
    ruedas = 4
    puertas = None

    def __init__(self, color, puertas, ruedas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self, velocidad, cilindrada, color, puertas, ruedas = 4):
        super().__init__(color, puertas, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


c1 = Coche(120, 6,"rojo",5,4)
print(f"Coche 1:\nCilindrada: {c1.cilindrada}\nColor: {c1.color}\nPuertas: {c1.puertas}\nRuedas: {c1.ruedas}\nVelocidad: {c1.velocidad}")
print()
c2 = Coche(100, 4,"verde",4)
print(f"Coche 2:\nCilindrada: {c2.cilindrada}\nColor: {c2.color}\nPuertas: {c2.puertas}\nRuedas: {c2.ruedas}\nVelocidad: {c2.velocidad}")