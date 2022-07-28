p = float(input("Indicar puntuación anual: "))
if p < 0.4:
    print ("Nivel inaceptable, recibirá: " + str(p*2400) + " €.")
elif p < 0.6:
    print ("Nivel aceptable, recibirá: " + str(p*2400) + " €.")
else:
    print ("Nivel meritorio, recibirá: " + str(p*2400) + " €.")
