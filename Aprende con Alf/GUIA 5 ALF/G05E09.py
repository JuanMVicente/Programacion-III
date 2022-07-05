a = list(input("Escriba una palabra: "))
print("La cantidad de <a> es " + str(a.count("a")) + ".")
print("La cantidad de <e> es " + str(a.count("e")) + ".")
print("La cantidad de <i> es " + str(a.count("i")) + ".")
print("La cantidad de <o> es " + str(a.count("o")) + ".")
print("La cantidad de <u> es " + str(a.count("u")) + ".")

# Asi lo resuelve ALF
# word = input("Introduce una palabra: ")
# vocals = ['a', 'e', 'i', 'o', 'u']
# for vocal in vocals: 
#     times = 0
#     for letter in word: 
#         if letter == vocal:
#             times += 1
#     print("La vocal " + vocal + " aparece " + str(times) + " veces")