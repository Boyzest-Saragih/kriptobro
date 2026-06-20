import utils.mathHelpers as mth
import hashlib
import os


def keygen (g,x,p,q):
    y = mth.modularExponentiation(g,x,p)
    print(y)

    y = mth.modInv(y,p)
    publicKey = (p,g,y)
    privateKey = x

    print (f"y = {y}")
    print (f"public key = {publicKey}")
    print (f"private key = {privateKey}")

    return publicKey,privateKey


def signing (m,g,k,p,q,x):

    r = mth.modularExponentiation(g,k,p)

    m_concat_r = f"{m}{r}"
    e = int(hashlib.sha256(m_concat_r.encode()).hexdigest(), 16)
    e = e % q

    s = (k+x*e) % q

    signature = (e,s)

    print (f"signature  = {signature}")
    return signature


def verif (m,e,s,g,p,q,y):
    rv = (mth.modularExponentiation(g,s,p) * mth.modularExponentiation(y,e,p)) % p

    m_concat_rv = f"{m}{rv}"
    ev = int(hashlib.sha256(m_concat_rv.encode()).hexdigest(), 16)
    ev = ev % q

    print(f"rv = {rv}")
    print(f"ev = {ev}")
    print(f"e  = {e}")
    print(f"Valid = {ev == e}")

def clear ():
    os.system('cls')


while True:
    p = 2038635241
    q = 999331
    g = 2

    h = 2

    g = pow(h, (p-1)//q, p)

    print(mth.isPrima(p))
    print(mth.isPrima(q))
    print(mth.isPrima(g))
    print(mth.modularExponentiation(g,q,p)==1)

    try:
        x = int(input(f"masukkan nilai x (bilangan acak yang lebih kecil dari {q}-1) : "))
        k = int(input(f"masukkan nilai k (acak yang kurang dari {q}-1) : "))
        m = input("Masukkan nilai m : ")

        if not (0 < k < q):
            print(f"Nilai k tidak valid. k harus memenuhi 0 < k < {q}")
            continue

        if not (0 < x < q):
            print(f"Nilai x tidak valid. x harus memenuhi 0 < x < {q}")
            continue
            
    except ValueError:
        print("Input error: Pastikan memasukkan angka yang benar.")
        continue



    print()
    print("="*30)
    print()
    print("proses pembentukan key : ")
    publicKey, privateKey = keygen(g, x, p, q)
    print()

    input("tekan enter untuk melanjutkan proses sign !")

    print()
    print("="*30)
    print()
    print("proses sign : ")
    signature = signing(m, g, k, p, q, x)
    print()

    input("tekan enter untuk melanjutkan proses verify !")

    print()
    print("="*30)
    print()
    print("proses verify : ")
    verif(m, signature[0], signature[1], g, p, q, publicKey[2])
    print()

    confirmation = input("tekan enter untuk kembali atau isi dengan char apapun untuk mengakhiri: ")

    if confirmation != "":
        break
        
    clear()