def to_camel_case(text):

    i = 0
    while i<text.__len__() and text[i] != "-" and text[i] != "_":
        i+=1

    if i == 0:
        return ""

    elif text[i] == "_":
        list = text.split("_")
        list = text.split("-")
        cad = list[0].lower()
        for i in range(1,list.__len__()):
            cad = cad + list[i].capitalize()
        return cad
    elif text[i] == "-":
        list = text.split("_")
        list = text.split("-")
        cad = ""
        for i in range(0,list.__len__()):
            cad = cad + list[i].capitalize()
        return cad
    else:
        return text