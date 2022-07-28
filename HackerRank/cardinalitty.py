#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'cardinalitySort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY nums as parameter.
#
def cardinality(num):
    contador = 0
    while num / 2 >= 1:
        if num %2 == 1:
            contador += 1
        num = int(num/2)
    return contador
    
def cardinalitySort(nums):
    res = []
    for num in nums:
        i = 0
        while i < res.__len__() and cardinality(num)>cardinality(res[i]):
            i+=1
        while i < res.__len__() and cardinality(num)==cardinality(res[i]) and res[i]<num:
            i+=1
        res.insert(i,num)
    return res



nums = [1, 2, 3, 4, 5]
print(cardinalitySort(nums))