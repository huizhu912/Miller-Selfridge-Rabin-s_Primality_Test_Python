import MillerRabin
import SieveOfEratosthenes

def compare(N):
    global i, listMiller, listSieve, d 

    for item in N: 
        i = 2
        listMiller = []
        listSieve = []
        d = []
        print("N = ", item)
        SieveOfEratosthenes.SieveOfEratosthenes1(item)
        listSieve = SieveOfEratosthenes.list
        print("Sieve Of Eratosthenes: PI(", item, ") = ", len(listSieve))

        while i <= item:
            if i == 2:
                listMiller.append(i)
                i = i + 1
            elif (i > 1) & (i % 2 != 0): 
                MillerRabin.MillerRabin1(i, 2)
                if MillerRabin.result == True:
                    listMiller.append(i)
                i = i + 2
        print("Miller-Selfridge-Rabin: PI(", item, ") = ", len(listMiller))

        for v in listMiller:
            if (v not in listSieve):
                d.append(v)
        print("probable primes which are composites: ", d)
        factorize(d)
        print("\n")

def factorize(pseudoprimelist):
    global f, k, fvalue, temp
    f = {}
    fvalue = []
    for k in pseudoprimelist:
        for i in listSieve:
            if (i < k) & (k % i == 0):
                fvalue.append(i)
            elif (i > k):
                break
        temp = {str(k):fvalue}
        f.update(temp)
        fvalue = []
        temp.clear()
    for key, value in f.items():
        print(key, "is defactorized as" , value)

N = [10, 100, 1000, 10000]		
compare(N)


    