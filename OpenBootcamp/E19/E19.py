
def main():
    cadena = input('Lista de paises separados por ",": ' )
    lista = cadena.split(',')
    lista = [pais.strip() for pais in lista]
    lista = sorted(lista)
    # print(lista)

    for i in range(0,lista.__len__()-1):
        print(lista[i] + ",", end=' ')
    print(lista[lista.__len__()-1])

if __name__ == "__main__":
    main()