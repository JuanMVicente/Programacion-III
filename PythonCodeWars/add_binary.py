
from pickle import LONG

def add_binary(a,b):
    num = a+b
    bin =""
    while num / 2 > 0:
        bin = str(int(num%2)) + bin
        num = num/2
    
    if num == 0:
        return "0"
    return bin

print(add_binary(51,12))