import utils.mathHelpers as mth
import hashlib
import os
import random


def keygen (g,p,x):

    y = mth.modularExponentiation(g,x,p)

    print(f"y = {y}")
    return y


def signing (m, g, p, q, x, k):

    h = int(hashlib.sha256(m.encode()).hexdigest(), 16)
    h = h % q

    r = mth.modularExponentiation(g,k,p)%q

    kInv = mth.modInv(k,q)

    s = (kInv * (h + x*r)) % q

    signature = (r,s)

    return signature


def verif (m, g, p, q, y, r, s):
    h = int(hashlib.sha256(m.encode()).hexdigest(), 16)
    h = h % q

    w = mth.modInv(s,q)

    u1 = (h*w)%q
    u2 = (r*w)% q

    v = ((mth.modularExponentiation(g,u1,p) * mth.modularExponentiation(y,u2,p))%p)%q

    print(f"w = {w}")
    print(f"u1 = {u1}")
    print(f"u2  = {u2}")
    print(f"v  = {v}")
    print(f"r  = {r}")
    print(f"Valid = {v == r}")

def clear ():
    os.system('cls')


while True:

    q = 999331
    p = 2038635241
    x = 123456
    g = 968811435
    k = 54321

    # g = pow(2,2040, p)
    # print(g)

    m = input("Masukkan nilai pesan (m) : ")
    print()
    print("="*30)
    print("PROSES PEMBENTUKAN KUNCI")
    print("="*30)
    y = keygen(g, p, x)
    print(f"Parameter p = {p}")
    print(f"Parameter q = {q}")
    print(f"Parameter g = {g}")
    print(f"Private Key (x) = {x}")
    print(f"Public Key  (y) = {y}")
    print()

    input("Tekan Enter untuk melanjutkan ke proses SIGN...")

    print()
    print("="*30)
    print("PROSES SIGNING")
    print("="*30)
    signature = signing(m, g, p, q, x, k)
    print(f"Signature (r, s) = {signature}")
    print()

    input("Tekan Enter untuk melanjutkan ke proses VERIFY...")

    print()
    print("="*30)
    print("PROSES VERIFICATION")
    print("="*30)
    verif(m, g, p, q, y, signature[0], signature[1])
    print()

    confirmation = input("Tekan Enter untuk ulang, atau isi dengan karakter apapun lalu Enter untuk keluar: ")

    if confirmation != "":
        break
        
    clear()