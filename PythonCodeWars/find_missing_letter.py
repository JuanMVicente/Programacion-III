def find_missing_letter(chars):
    i=1
    while i< chars.__len__():
        if ord(chars[i-1]) + 1 == ord(chars[i]):
            i+=1
        else:
            return chr(ord(chars[i-1])+1)
    pass



print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))
print(ord('a'))
print(chr(97))