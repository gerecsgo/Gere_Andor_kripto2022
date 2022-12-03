
# A házinak az első két alpontját próbáltam megoldani 6 pontra. a 3-as alpont nincs meg.



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
    return z[0]*(2**7)+z[1]*(2**6)+z[2]*(2**5)+z[3]*(2**4)+z[4]*(2**3)+z[5]*(2**2)+z[6]*(2**1)+z[7]*(2**0)

def random_pakk():
    x = []
    for i in range(54):
        x.append(i+1)
    random.shuffle(x)
    return x

def solitaire(pakk):
    


def encode(arr, algoritmus, kulcs):
    encoded = []
    for c in arr:
        rand = blum(kulcs)
        encoded.append(c^rand)
        kulcs = rand
    return encoded

def decode(arr, algoritmus, kulcs):
    decoded = []
    for c in arr:
        rand = blum(kulcs)
        decoded.append(c^rand)
        kulcs = rand
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

    print("SOLITAIRE")
    encoded = encode(arr, solitaire, solitaire_kulcs)
    decoded = decode(encoded, solitaire, solitaire_kulcs)
    print("EREDETI:")
    print(arr)
    print("ENCODEOLT:")
    print(encoded)
    print("DECODEOLT:")
    print(decoded)

    # print(blum(36))

    #pakk = random_pakk()
    #solitaire(pakk)

if __name__ == "__main__": main()
    