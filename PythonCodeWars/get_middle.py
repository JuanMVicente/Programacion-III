'''You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.'''

def get_middle(s):
    resp = str(s)
    len = resp.__len__()
    if len % 2 == 0:
        return resp[int(len/2) - 1] +resp[int(len/2)]
    else:
        return resp[int(len/2)]




print(get_middle("testing"))