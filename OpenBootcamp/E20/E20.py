from functools import reduce

def main():
    lista = [0,1,2,3,4,5,6,7,8,9]
    impares = filter(lambda x: x % 2 == 1, lista)
    suma = reduce(lambda x,y: x + y, impares)
    print(suma)


if __name__ == "__main__":
    main()