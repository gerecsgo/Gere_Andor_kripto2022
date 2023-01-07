import copy
import random

import utils
import numpy as np

# KNAPSACK

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def generate_private_key(n=8):
    w = []
    w.append(random.randint(2,10))
    total = w[0]
    for i in range(1,n):
       gen = random.randint(total+1, 2*total)
       w.append(gen)
       total += gen

    total_all = sum(w)
    q = random.randint(total_all+1, 2*total_all)
    
    r = random.randint(2, q-1)
    while(not is_coprime(q,r)):
        r = random.randint(2, q-1)
    
    w_tuple = tuple(w)

    return (w_tuple,q,r)
        
def create_public_key(private_key):
    w = private_key[0]
    q = private_key[1]
    r = private_key[2]
    n = len(w)
    beta = []
    for i in range(n):
        beta.append((r*w[i])%q)

    beta_tuple = tuple(beta)

    return beta_tuple

def encrypt_mh(message, public_key):
    b = public_key
    encrypted = []
    for ch in message:
        sum = 0
        ascii = ord(ch)
        a = bin(ascii)[2:].zfill(8)
        for i in range(len(a)):
            sum += (int(a[i]) * b[i])
        encrypted.append(sum)

    return encrypted

def decrypt_mh(message, private_key):
    w = np.array(private_key[0])
    w_reverse = np.flip(w)
    q = private_key[1]
    r = private_key[2]
    s = utils.modinv(r, q)

    decrypted = ""
    for num in message:
        cI = (num*s)%q     
        w_is = []
        for i in range(len(w_reverse)):
            if((w_reverse[i] <= cI) and ((cI - w_reverse[i]) >= 0)):
                cI -= w_reverse[i]
                w_is.append(i)
                if(cI == 0):
                    break
        m = 0
        for w_i in w_is:
            m += 2**(8-(8-w_i))
        decrypted += chr(m)
    return decrypted



# SOLITAIRE
FEHER = 54
FEKETE = 53
UTOLSO = 53
ELSO = 0

def feher_pozicio(pakk):
    poz = 0
    for i in range(len(pakk)):
        if(pakk[i] == 54):
            poz = i
            break
    return poz

def fekete_pozicio(pakk):
    poz = 0
    for i in range(len(pakk)):
        if(pakk[i] == 53):
            poz = i
            break
    return poz

def rotate(l, n):
    return l[n:] + l[:n]

def solitaire(pakk):
    kell_ismetelni = 1
    while(kell_ismetelni == 1):
        feher_poz = feher_pozicio(pakk)
        
        # a lepes
        if(feher_poz == UTOLSO):
            pakk.pop(feher_poz)
            pakk.insert(1,FEHER)
        else:
            pakk.pop(feher_poz)
            pakk.insert(feher_poz+1, FEHER)

        # b lepes
        fekete_poz = fekete_pozicio(pakk)
        if(fekete_poz == UTOLSO):
            pakk.pop(fekete_poz)
            pakk.insert(2,FEKETE)
        elif(fekete_poz == UTOLSO-1):
                pakk.pop(fekete_poz)
                pakk.insert(1,FEKETE)
        else:
            pakk.pop(fekete_poz)
            pakk.insert(fekete_poz+2, FEKETE)           


        # c lepes
        cserelt_pakk = []
        fekete_poz = fekete_pozicio(pakk)
        feher_poz = feher_pozicio(pakk)
       # print(pakk)
        if(fekete_poz < feher_poz):
            cserelt_pakk.extend(pakk[(feher_poz+1):(len(pakk))])
            cserelt_pakk.extend(pakk[fekete_poz:(feher_poz+1)])
            cserelt_pakk.extend(pakk[0:fekete_poz])
        else:
            cserelt_pakk.extend(pakk[(fekete_poz+1):(len(pakk))])
            cserelt_pakk.extend(pakk[feher_poz:(fekete_poz+1)])
            cserelt_pakk.extend(pakk[0:feher_poz])       
        #print(cserelt_pakk)

        # d lepes
       #print(pakk)
        szamertek = cserelt_pakk[UTOLSO]
        #print(cserelt_pakk)

       # print(szamertek)
        ujracserelt_pakk = []
        ujracserelt_pakk.extend(cserelt_pakk[(szamertek):UTOLSO-1])
        ujracserelt_pakk.extend(cserelt_pakk[0:(szamertek+1)])
        ujracserelt_pakk.append(cserelt_pakk[UTOLSO])

        #print(ujracserelt_pakk)

        # e lepes
        szamertek = ujracserelt_pakk[ELSO]
        if(szamertek == 53 or szamertek == 54):
            kell_ismetelni = 1
            pakk = copy.deepcopy(ujracserelt_pakk)
        else:
            kivalasztott = ujracserelt_pakk[szamertek]
            #print(len(ujracserelt_pakk))
            return (kivalasztott, ujracserelt_pakk)

def encode_solitaire(text, kulcs):
    arr = []
    for i in range(len(text)):
        arr.append(ord(text[i]))

    encoded = []
    for c in arr:
        k = solitaire(kulcs)
        rand = k[0]
        encoded.append(c^rand)
        kulcs = k[1]

    encoded_text = ""
    for i in range(len(encoded)):
        encoded_text += chr(encoded[i])  

    return encoded_text

def decode_solitaire(text, kulcs):
    arr = []
    for i in range(len(text)):
        arr.append(ord(text[i]))

    decoded = []
    for c in arr:
        k = solitaire(kulcs)
        rand = k[0]
        decoded.append(c^rand)
        kulcs = k[1]

    decoded_text = ""
    for i in range(len(decoded)):
        decoded_text += chr(decoded[i])  

    return decoded_text

