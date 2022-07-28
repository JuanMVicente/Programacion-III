def wave(people):
    list = []

    for i in range(0,people.__len__()):
        res = ""
        if people[i] != " ":
            for j in range(0,people.__len__()):
                if i==j:
                    res += people[i].upper()
                else:
                    res += people[j]
            list.append(res)
    return list
    


print(wave("hello"))