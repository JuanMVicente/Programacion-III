
def narcissistic( value ):
    acumulador = 0
    numero = value
    list = []
    while(numero/10 > 0.09):
        list.append(numero%10)
        numero = int(numero / 10)
        numero
    
    for num in list:
        acumulador += num ** list.__len__()
    
    if(acumulador == value):
        return True
    return False


print(narcissistic(153))

print(narcissistic(1938))

print(narcissistic(7))

print(narcissistic(371))
