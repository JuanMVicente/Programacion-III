def likes(names):  
    if names.__len__() == 0:
        return "no one likes this"
    elif names.__len__() == 1:
        return names[0] + " likes this"
    elif names.__len__() == 2:
        return names[0] + " and " + names[1] + " like this"
    elif names.__len__() == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + "like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(names.__len__()-2) + " others like this"





print(likes(['Alex', 'Jacob']))