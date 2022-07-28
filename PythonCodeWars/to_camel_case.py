def to_camel_case(text):

    i = 0
    while i<text.__len__() and text[i] != "-" and text[i] != "_":
        i+=1

    if i == 0:
        return ""

    elif text[i] == "_":
        list = text.split("-").split("_")
        cad = list[0].lower()
        for i in range(1,list.__len__()):
            cad = cad + list[i].capitalize()
        return cad
    elif text[i] == "-":
        list = text.split("_").split("-")
        for i in range(0,list.__len__()):
            cad = cad + list[i].capitalize()
        return cad
    else:
        return text


print(to_camel_case("the_stealth-warrior"))
print(to_camel_case("The-Stealth-Warrior"))