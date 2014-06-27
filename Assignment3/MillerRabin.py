def MillerRabin1(input, base):
    global n, result
    n = input
    A = base
    result = False
    k = 1
    q = int((n - 1) / pow(2, k))
    x = j = 0	
 
    if n == 2:
       result = True
       return result
    if (n > 1) & ((n % 2) != 0):
        while (q % 2) == 0:
            k = k + 1;
            q = int((n - 1) / pow(2, k))		
        if pow(A, q) % n == 1 % n:
            result = True
            return	result	
        else:
            for j in range(k):
                x = int(pow(2, j) * q)
                if (pow(A, x) % n) == ((n-1) % n):
                    result = True
                    return result

