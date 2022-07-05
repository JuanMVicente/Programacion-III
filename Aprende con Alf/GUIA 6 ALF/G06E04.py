m = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
f = input("Escriba una fecha en formato (dd/mm/aaaa): ")
f = f.split("/")
print(f[0] + " de " + m[int(f[1])] + " de " + f[2])