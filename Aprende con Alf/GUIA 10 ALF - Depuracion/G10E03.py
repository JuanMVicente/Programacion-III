'''Detectar y corregir los errores del siguiente programa que calcula el producto escalar de dos vectores:
u = (1, 2, 3)
v = (4, 5, 6)
def producto_escalar(u, v):
    for i in u:
        u[i+1] *= v[i+1]
    return sum(u)
print(producto_escalar(u, v))'''

def main():
    u = (1, 2, 3)
    v = (4, 5, 6)
    print(producto_escalar(u, v))


def producto_escalar(u, v):
    sum = 0
    for i in range(0,len(u)):
        sum += u[i] * v[i]
    return sum

if __name__ == "__main__":
    main()