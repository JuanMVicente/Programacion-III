def roman_to_decimal(roman):
    romanos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    resultado = romanos[roman[0].upper()]
    for i in range(1,roman.__len__()):
        if roman[i].upper() =='M':
            resultado += 1000
            if roman[i-1].upper() =='C': 
                resultado -= 200
        else:
            if roman[i].upper() =='D':
                resultado += 500
                if roman[i-1].upper() =='C': 
                    resultado -= 200
            else:
                if roman[i].upper() =='C':
                    resultado += 100
                    if roman[i-1].upper() =='X': 
                        resultado -= 20
                else:
                    if roman[i].upper() =='L':
                        resultado += 50
                        if roman[i-1].upper() =='X': 
                            resultado -= 20
                    else:
                        if roman[i].upper() =='X':
                            resultado += 10
                            if roman[i-1].upper() =='I': 
                                resultado -= 2
                        else:
                            if roman[i].upper() =='V':
                                resultado += 5
                                if roman[i-1].upper() =='I': 
                                    resultado -= 2
                            else:
                                if roman[i].upper() =='I':
                                    resultado += 1
    return resultado


def sortRoman(names):
    pass

print(roman_to_decimal("XCII"))
print(roman_to_decimal("IX"))