from os import *
from sys import *
from collections import *
from math import *

def convertSentence(s: str, n: int):
    # Write your code here.
    outputlist = []
    lower_case = s.lower()
    for char in lower_case:
        if char == 'a':
            outputlist.append(2)
        elif char == 'b':
            outputlist.append(22)
        elif char == 'c':
            outputlist.append(222)
        elif char == 'd':
            outputlist.append(3)
        elif char == 'e':
            outputlist.append(33)
        elif char == 'f':
            outputlist.append(333)
        elif char == 'g':
            outputlist.append(4)
        elif char == 'h':
            outputlist.append(44)
        elif char == 'i':
            outputlist.append(444)
        elif char == 'j':
            outputlist.append(5)
        elif char == 'k':
            outputlist.append(55)
        elif char == 'l':
            outputlist.append(555)
        elif char == 'm':
            outputlist.append(6)
        elif char == 'n':
            outputlist.append(6)
        elif char == 'o':
            outputlist.append(666)
        elif char == 'p':
            outputlist.append(7)
        elif char == 'q':
            outputlist.append(77)
        elif char == 'r':
            outputlist.append(777)
        elif char == 's':
            outputlist.append(7777)
        elif char == 't':
            outputlist.append(8)
        elif char == 'u':
            outputlist.append(88)
        elif char == 'v':
            outputlist.append(888)
        elif char == 'w':
            outputlist.append(9)
        elif char == 'x':
            outputlist.append(99)
        elif char == 'y':
            outputlist.append(999)
        elif char == 'z':
            outputlist.append(9999)
        else:
            return False
    display = ''.join(map(str, outputlist))
    print(display)


n = int(input())
s = input()
if len(s) > n:
    print("Error")
else:
    convertSentence(s, n)