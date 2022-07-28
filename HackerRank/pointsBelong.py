import math
import os
import random
import re
import sys

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):

    ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    bc = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    ac = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

    if ab >= bc + ac or bc >= ab + ac or ac >= ab + bc:
        return 0
    
    wp1 = ((x3 - x1) * (y1 + yp) +  (y3 - y1) * (xp - x1)) / ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x2 - x1))
    wp2 = (yp - y1 - wp1 * (y2 - y1)) / (y3 - y1)

    wq1 = ((x3 - x1) * (y1 + yq) +  (y3 - y1) * (xq - x1)) / ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x2 - x1))
    wq2 = (yp - y1 - wq1 * (y2 - y1)) / (y3 - y1)

    if wp1 >= 0 and wp2 >=0 and wp1 + wp2<=1:
        if wq1 >= 0 and wq2 >=0 and wq1 + wq2<=1:
            return 3
        else:
            return 1
    else:
        if wq1 >= 0 and wq2 >=0 and wq1 + wq2<=1:
            return 2
        else:
            return 4

print(pointsBelong(3,1,7,1,5,5,5,2,6,3))