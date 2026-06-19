import utils.mathHelpers as mth
import hashlib
import os
import random


def keygen (g,x,p):
    y = mth.modularExponentiation(g,x,p)

    publicKey = (p,g,y)
    privateKey = x

    print (f"y = {y}")
    print (f"public key = {publicKey}")
    print (f"private key = {privateKey}")

    return publicKey,privateKey


def signing (m,p,g,x):
    hashValue = int(hashlib.sha256(m.encode()).hexdigest()[:4], 16)
    hashValue = hashValue % p


    k = 2

    while True:
        k = random.randint(2, p-1)
        if mth.gcd(k, p-1) == 1:
            break

    

    a = mth.modularExponentiation(g,k,p)

    kInvers = mth.modInv(k,p-1)

    b = (kInvers * (hashValue - x * a )) % ( p - 1)

    signature = (a,b)

    print (f"k = {k}")
    print (f"a = {a}")
    print (f"b = {b}")
    print (f"hash value = {hashValue}")
    print (f"signature  = {signature}")
    return hashValue,signature


def verif (hashValue, signature, p, g, y):

    r,s = signature

    v1 = (mth.modularExponentiation(y, r, p) * mth.modularExponentiation(r, s, p)) % p

    v2 = mth.modularExponentiation(g, hashValue, p)

    print(f"V1 = {v1}")
    print(f"V2 = {v2}")
    print(f"V1 = V2 ? {v1==v2}")

def clear ():
    os.system('cls')


p = 1201
g = 137

while True:
    m = input("Masukkan pesan : ")

    while True:
        x = int(input(f"Masukkan private key x (2 <= x <= {p-2}) : "))
        if 1 < x < p - 1:
            break
        print(f"x harus memenuhi 1 < x < {p-1}")


    print()
    print("Proses Pembentukan Kunci")
    print("=" * 30)

    publicKey, privateKey = keygen(g, x, p)

    input("\nTekan Enter untuk Signing...")

    print()
    print("Proses Signing")
    print("=" * 30)

    hashValue, signature = signing(
        m,
        p,
        g,
        privateKey
    )

    input("\nTekan Enter untuk Verification...")

    print()
    print("Proses Verification")
    print("=" * 30)

    verif(
        hashValue,
        signature,
        p,
        g,
        publicKey[2]
    )

    confirmation = input(
        "\nTekan Enter untuk mengulang atau isi karakter untuk keluar : "
    )

    if confirmation != "":
        break

    clear()