class Vehiculo:
    marca = None
    modelo = None

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f'Vehiculo [Marca : {self.marca}, Modelo: {self.modelo}]'
