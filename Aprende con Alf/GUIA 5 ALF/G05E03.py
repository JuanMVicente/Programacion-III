l = ["quimica", "fisica", "matemática"]
n = []
for i in l:
    nota = input("Nota en " + i + ": ")
    n.append(nota)
for i in range(len(l)):
    print("En " + l[i] + " has sacado " + n[i] + ".")