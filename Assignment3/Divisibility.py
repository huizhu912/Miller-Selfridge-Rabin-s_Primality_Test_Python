from math import *

def Divisibility1 (n):
    global isprime 
    isprime = True
    j = 2
    if (type(n) is int) & (n > 1) & (n % 2 != 0):
        while j <= sqrt(n):
            if n % j == 0:
                isprime = False
                break
            j = j + 1
    elif (type(n) is int) & (n > 1) & (n != 2) & (n % 2 == 0):
        isprime = False
    return isprime
