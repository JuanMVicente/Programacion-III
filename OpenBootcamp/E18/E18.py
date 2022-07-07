import Vehiculo
import pickle

def main():
    # guardarVehiculo()
    v1 = leerVehiculo()
    print(str(v1))

def guardarVehiculo():
    v1 = Vehiculo.Vehiculo("BMW",2022)
    f = open('E18/vehiculo.bin', 'wb')
    pickle.dump(v1,f)
    f.close()


def leerVehiculo():
    f = open('E18/vehiculo.bin', 'rb')
    v = pickle.load(f)
    f.close()
    return v
    


if __name__ == "__main__":
    main()