def modularExponentiation(base, exp, mod):
    return pow(base, exp, mod)


def gcd(a,b):
    while b !=0:
        temp = b
        b = a % b
        a = temp
    return a

def extendGcd (a,b):
    if b == 0:
        return a,1,0

    gcd, x1, y1 = extendGcd(b, a%b)
    x = y1 
    y = x1 -(a//b)*y1

    return gcd,x,y

def modInv (a,m):
    gcd, x, y = extendGcd(a,m)
    if gcd ==1:
        return x % m
    
    return "no invers"

def isPrima (n):
    if n % 2 != 0:
        return True
    else:
        return False
