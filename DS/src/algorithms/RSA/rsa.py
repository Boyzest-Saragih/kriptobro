import utils.mathHelpers as mth
import hashlib
import os


def keygen (p,q,e):
    n = p* q

    phiN = (p-1)* (q-1)

    d = mth.modInv(e,phiN)

    publicKey = (e,n)
    privateKey = (d,n)

    print (f"n = {n}")
    print (f"ϕ(n) = {phiN}")
    print (f"d = {d}")
    print (f"public key = {publicKey}")
    print (f"private key = {privateKey}")

    return n,phiN,d,publicKey,privateKey


def signing (m,n,d):
    hashValue = int(hashlib.sha256(m.encode()).hexdigest(), 16)
    hashValue = hashValue % n

    signature = mth.modularExponentiation(hashValue,d,n)

    print (f"hash value = {hashValue}")
    print (f"signature  = {signature}")
    return hashValue,signature


def verif (hashValue):
    h1 = hashValue

    h2 = mth.modularExponentiation(signature,e,n)

    print (f"h1 = {h1}")
    print (f"h2 = {h2}")
    print (f"h1 = h2 ? {h1==h2}")

def clear ():
    os.system('cls')


while True:
    m = input("Masukkan nilai m : ")
    p = 100003
    q = 123457
    e = int(input("masukkan nilai e(relatif prima) : "))

    phiN = (p-1)* (q-1)
    while True:
        if mth.gcd(e, phiN) != 1:
            print(f"{e} tidak relatif prima terhadap φ(n) = {phiN}")
            e = int(input("masukkan nilai e(relatif prima) (ex : 65537) : "))
        else:
            break 
    print()
    print("="*30)
    print()
    print("proses pembentukan key : ")
    n,phiN,d,publicKey,privateKey = keygen(p,q,e)
    print()

    input("tekan enter untuk melanjutkan proses sign !")

    print()
    print("="*30)
    print()
    print("proses sign : ")
    hashValue, signature =  signing(m,n,d)
    print()

    input("tekan enter untuk melanjutkan proses verify !")

    print()
    print("="*30)
    print()
    print("proses verify : ")
    verif(hashValue)

    confirmation = input("tekan enter untuk kembali atau isi dengan char untuk mengakhiri")

    if confirmation != "":
        break
    clear()