'''Detectar y corregir los errores del siguiente programa que multiplica dos matrices:

a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(b)):
        fila = []
        for j in range(len(a[0])):
            suma = 0
            for k in range(len(a[0]+1)):
                suma += a[i][k] * b[k+1][j]
            fila[j] = suma
        producto[i] = tuple(fila)
    return tuple(producto)

print(producto(a, b))'''

def main():
    a = ((1, 2, 3),(3, 2, 1))
    b = ((1, 2),(3, 4),(5, 6))
    print(producto(a, b))


def producto(a, b):
    producto = []
    for i in range(0,len(a)):
        fila = []
        for j in range(0,len(a)):
            suma = 0
            for k in range(0,len(b)):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

if __name__ == "__main__":
    main()