from os import *
from sys import *
from collections import *
from math import *

def findCelebrity(n, knows):
    stack = []
    for i in range(n):
        stack.append(i)
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if knows(a, b):
            stack.append(b)
        else:
            stack.append(a)
    if len(stack) == 0:
        return -1
    celeb = stack.pop()
    for i in range(n):
        if i != celeb:
            if not knows(i, celeb) or knows(celeb, i):
                return -1
    return celeb