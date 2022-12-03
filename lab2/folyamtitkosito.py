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
    print(pakk)


def main():
    print(blum(36))
    #pakk = random_pakk()
    #solitaire(pakk)

if __name__ == "__main__": main()
    