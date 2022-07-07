
def main():
    # creacion del archivo
    f = open('E17/archivo.txt','w')
    f.write('primer ingreso\n')
    f.close()

    # Segundo ingreso y escritura
    f = open('E17/archivo.txt','a')
    f.write('segundo ingreso\n')
    f.close()

if __name__ == "__main__":
    main()
