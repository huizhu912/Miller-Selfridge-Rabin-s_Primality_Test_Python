import Divisibility
from math import *

def SieveOfEratosthenes1(input):
    global list
    n = input
    x = 0
    list = [j for j in range(2, n + 1)]
    j = 1
    j = j + 1
    if (type(n) is int) & (n > 1):	
        while j <= sqrt(n):
            if Divisibility.Divisibility1(j) == True: #if j is a probable prime
                x = j + j
                crossOutChain(x, j, n)
            j = j + 1

def crossOutChain(x, j, n):
    while x <= n:
        if x in list:
            p = list.index(x)
            list.pop(p)
        x = x + j;	


        				

        
    
    		