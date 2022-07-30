'''Corregir los errores sintácticos del siguiente programa:

contraseña = input('Introduce la contraseña: ")
if contraseña in ['sesamo'):
  print('Pasa')
else
  print('No pasa')'''



def main():
    contrasena = input('Introduce la contraseña: ')
    if contrasena in 'sesamo':
        print('Pasa')
    else:
        print('No pasa')

if __name__ == "__main__":
    main()