from os import *
from sys import *
from collections import *
from math import *

def isReflectionEqual(s):
    mirror = []
    i = str()
    if isinstance(s, str):
        letters = ['B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'N', 'L', 'P', 'Q', 'R', 'S', 'Z']
        for i in s:
            if i in letters:
                mirror.append(i)
            else:
                continue
        if len(mirror) > 0:
            print("NO")
        else:
            print("YES")
    else:
        print("false")

while True:
    try:
        case = input("Enter Number of cases: ")
        tests = int(case)
        break
    except ValueError:
        print("It's not a Number")


for j in range(tests):
    s = input("Enter String: ")
    isReflectionEqual(s)