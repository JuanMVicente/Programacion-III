'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.'''

import pandas as pd


def main():
    serie = pd.Series({2010:100, 2011:200, 2012: 300, 2013:100, 2011:200, 2014: 300, 2015:100, 2016:200, 2017: 300, 2018:100, 2019:200, 2020: 300, 2021:100, 2022:200})
    print('Ventas:\n',serie,'\n')
    
    anio_inicio = int(input('Desde que año desea visualizar: '))
    anio_fin = int(input('Hasta que año desea visualizar: '))
    
    serie = serie[serie.keys()>=anio_inicio]
    serie = serie[serie.keys()<=anio_fin]
    print('Ventas con filtro\n', serie,'\n')
   
    print('Ventas con descuento\n', serie *0.9,'\n')

    

if __name__ == "__main__":
    main()