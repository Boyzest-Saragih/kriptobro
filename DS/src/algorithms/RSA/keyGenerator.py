import sys
import os

# Menambahkan path folder 'src' ke sistem path Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import utils.mathHelpers as mth

p, q = 61, 53

n = p* q

eulerTotient = (p-1)* (q-1)

e = 17
# verif
mth.gcd(e, eulerTotient)

d = mth.modInv(e,eulerTotient)

publicKey = [e,n]
privateKey = [d,n]

print(publicKey)