import copy
import random

import sys
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9000
chat = (host, port)
s.connect(chat)

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

def encode(text, kulcs):
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

def decode(text, kulcs):
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

def teszt():
    solitaire_kulcs = [28, 15, 20, 30, 7, 9, 12, 49, 40, 6, 19, 48, 33, 34, 31, 27, 18, 38, 10, 46, 1, 14, 23, 39, 53, 29, 37, 54, 3, 22, 21, 51, 8, 45, 16, 44, 11, 17, 5, 26, 42, 2, 36, 24, 52, 47, 35, 25, 4, 50, 32, 43, 13, 41]
    text = 'Nem bank es nem hitelezok vagyunk. Mi egy penzugyi szolgaltatasokat es termekeket osszehasonlito oldal vagyunk'
    encoded = encode(text, copy.deepcopy(solitaire_kulcs))
    decoded = decode(encoded, copy.deepcopy(solitaire_kulcs))
    print("Encodeolt szoveg:")
    print(encoded)
    print("Decodeolt szoveg:")
    print(decoded)


def receive():
    while True:
        response = s.recv(2048).decode()
        print(response)
        if(response == 'Kileptel a chatbol'):
            sys.exit()
            break

def sendmsg():
    while True:
        type = input('public/private/users/logout/register\n')
        if(type == 'register'):
            msg = 'register'
        elif(type == 'public'):
            msg = str(0) + input('Ird be a szervernek kuldott uzenetet: ')
        elif(type == 'private'):
            msg = str(1) + input('Ird be a kliensnek kuldott uzenetet: ')
        elif(type == 'users'):
            msg = 'users'
        else:
            msg = 'logout'
        s.send(msg.encode())

sendmessage = threading.Thread(target = sendmsg)
sendmessage.daemon = True
sendmessage.start()

receivemsg = threading.Thread(target = receive)
receivemsg.start()
receivemsg.join()
s.close()
