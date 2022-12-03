
# A házinak az első két alpontját próbáltam megoldani 6 pontra. a 3-as alpont nincs meg.

import copy
import random

def blum(s):
    len = 8
    p = 5623
    q = 7639
    n = p*q
    x = []
    z = []
    x.append(s**2%n)
    for i in range(len):
        x.append(x[i]**2%n)
        z.append(x[i+1]%2)

    szam = z[0]*(2**7)+z[1]*(2**6)+z[2]*(2**5)+z[3]*(2**4)+z[4]*(2**3)+z[5]*(2**2)+z[6]*(2**1)+z[7]*(2**0)
    return (szam, szam)

def random_pakk():
    x = []
    for i in range(54):
        x.append(i+1)
    random.shuffle(x)
    return x

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

FEHER = 54
FEKETE = 53
UTOLSO = 53
ELSO = 0

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


def encode(arr, algoritmus, kulcs):
    encoded = []
    for c in arr:
        k = algoritmus(kulcs)
        rand = k[0]
        encoded.append(c^rand)
        kulcs = k[1]
    return encoded

def decode(arr, algoritmus, kulcs):
    decoded = []
    for c in arr:
        k = algoritmus(kulcs)
        rand = k[0]
        decoded.append(c^rand)
        kulcs = k[1]
    return decoded   

def main():
    arr = [12, 54, 65, 128, 64, 64, 23, 65, 88, 210, 255, 0, 233]
    blum_kulcs = 36
    solitaire_kulcs = [28, 15, 20, 30, 7, 9, 12, 49, 40, 6, 19, 48, 33, 34, 31, 27, 18, 38, 10, 46, 1, 14, 23, 39, 53, 29, 37, 54, 3, 22, 21, 51, 8, 45, 16, 44, 11, 17, 5, 26, 42, 2, 36, 24, 52, 47, 35, 25, 4, 50, 32, 43, 13, 41]

    print("BLUM BLUM SHUB")
    encoded = encode(arr, blum, blum_kulcs)
    decoded = decode(encoded, blum, blum_kulcs)
    print("EREDETI:")
    print(arr)
    print("ENCODEOLT:")
    print(encoded)
    print("DECODEOLT:")
    print(decoded)

    #print(solitaire(solitaire_kulcs))

    print("SOLITAIRE")
    encoded = encode(arr, solitaire, copy.deepcopy(solitaire_kulcs))
    decoded = decode(encoded, solitaire, copy.deepcopy(solitaire_kulcs))
    print("EREDETI:")
    print(arr)
    print("ENCODEOLT:")
    print(encoded)
    print("DECODEOLT:")
    print(decoded)

    
if __name__ == "__main__": main()
    