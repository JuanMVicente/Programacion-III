d = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
m = input("Moneda: ")
print(d.get(m.title(), "La divisa no está."))