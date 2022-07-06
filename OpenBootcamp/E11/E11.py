def esPrimo(x):
    primos = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    if x in primos:
        return True
    return False

def esPrimoIterativo(x):
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def esPrimoRecursivo(x, n=2):
    if n >= x:
        return True
    elif x % n != 0:
        return esPrimoRecursivo(x, n + 1)
    else:
        return False


print("Simple:", esPrimo(47),esPrimo(93))
print("Iterativo:", esPrimoIterativo(47),esPrimoIterativo(93))
print("Recursivo:", esPrimoRecursivo(47),esPrimoRecursivo(93))