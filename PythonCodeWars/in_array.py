def in_array(array1, array2):
    res = []
    for palabra in array1:
        i=0
        while (i < array2.__len__()  and array2[i].find(palabra) == -1):
            i+=1
        if i<array2.__len__() and (res.__contains__(palabra) == False):
            res.append(palabra)
    
    return sorted(res)


a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1,a2))

a1 = ["arp", "mice", "bull"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1,a2))

'''def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})'''