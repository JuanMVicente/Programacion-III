l = ["quimica", "fisica", "matemática", "lengua"]
for i in range(len(l)-1, -1, -1):
    nota = float(input("Nota en " + l[i] + ": "))
    if nota >= 7:
        l.pop(i)
print("Debe recuperar " + str(l))