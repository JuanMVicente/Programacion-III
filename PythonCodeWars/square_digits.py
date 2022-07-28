def square_digits(num):
    value = str(num)
    res = ""
    for i in value:
        res += str(int(i) ** 2)
    return int(res)

print(square_digits(9119))
print(square_digits(0))