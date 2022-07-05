p = input ("Cuantos euros sale (dos decimales): ")
print (str(p[:p.find(".")]) + " euros y " + str(p[p.find(".")+1:]) + " centimos.")