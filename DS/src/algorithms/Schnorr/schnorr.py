import utils.mathHelpers as mth
import hashlib
import os


def keygen (g,x,p):
    y = mth.modularExponentiation(g,x,p)
    print(y)

    y = mth.modInv(y,p)
    publicKey = (p,g,y)
    privateKey = x

    print (f"y = {y}")
    print (f"public key = {publicKey}")
    print (f"private key = {privateKey}")

    return publicKey,privateKey


def signing (m,g,k,p,x):

    r = mth.modularExponentiation(g,k,p)

    m_concat_r = f"{m}{r}"
    hashValue = int(hashlib.sha1(m_concat_r.encode()).hexdigest()[:4], 16)
    hashValue = hashValue % q

    s = (k+x*hashValue) % q

    signature = (hashValue,s)

    print (f"signature  = {signature}")
    return signature


def verif (m,e,s,g,p,y):
    rv = (mth.modularExponentiation(g,s,p) * mth.modularExponentiation(y,e,p)) % p

    m_concat_rv = f"{m}{rv}"
    hashValue = int(hashlib.sha1(m_concat_rv.encode()).hexdigest()[:4], 16)
    ev = hashValue % q

    print (f"h1 = {rv}")
    print (f"h2 = {ev}")
    print (f"ev = e ? {ev==e}")

def clear ():
    os.system('cls')


p = 1109
q = 277
g = 13
x = 140
k = 131

m = "Kriptografi mantap_18"

publicKey, privateKey = keygen(g,x,p)
signature = signing(m,g,k,p,x)
verif(m,signature[0],signature[1],g,p,publicKey[2])



# while True:
#     m = input("Masukkan nilai m : ")
#     p = 100003
#     q = 123457
#     e = int(input("masukkan nilai e(relatif prima) : "))

#     phiN = (p-1)* (q-1)
#     while True:
#         if mth.gcd(e, phiN) != 1:
#             print(f"{e} tidak relatif prima terhadap φ(n) = {phiN}")
#             e = int(input("masukkan nilai e(relatif prima) : "))
#         else:
#             break 
#     print()
#     print("="*30)
#     print()
#     print("proses pembentukan key : ")
#     n,phiN,d,publicKey,privateKey = keygen(p,q,e)
#     print()

#     input("tekan enter untuk melanjutkan proses sign !")

#     print()
#     print("="*30)
#     print()
#     print("proses sign : ")
#     hashValue, signature =  signing(m,n,d)
#     print()

#     input("tekan enter untuk melanjutkan proses verify !")

#     print()
#     print("="*30)
#     print()
#     print("proses verify : ")
#     verif(hashValue)

#     confirmation = input("tekan enter untuk kembali atau isi dengan char untuk mengakhiri")

#     if confirmation != "":
#         break
#     clear()