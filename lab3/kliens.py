import copy
import random

import sys
import socket
import threading
import utils
import numpy as np
import crypto


solitaire_kulcs = np.random.permutation([28, 15, 20, 30, 7, 9, 12, 49, 40, 6, 19, 48, 33, 34, 31, 27, 18, 38, 10, 46, 1, 14, 23, 39, 53, 29, 37, 54, 3, 22, 21, 51, 8, 45, 16, 44, 11, 17, 5, 26, 42, 2, 36, 24, 52, 47, 35, 25, 4, 50, 32, 43, 13, 41])

# SZERVER CSATLAKOZAS
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9000
chat = (host, port)
s.connect(chat)
msg = 'join'
s.send(msg.encode())
print("Csatlakoztal a szerverhez.")
# KLIENS SOCKET FUGGVENYEK
def receive():
    while True:
        response = s.recv(2048).decode()
        print(response)
        if(response == 'Kileptel a chatbol'):
            sys.exit()
            break

def sendmsg():
    while True:
        type = input('Ird be a parancsot: register/clients/getkey/sendkey\n')
        if(type == 'register'):
            msg = 'register'+ '$$' + input('Ird be a public kulcsot, amivel regisztralni szeretnel: ')
            s.send(msg.encode())
        if(type == 'getkey'):
            msg = 'getkey' + '$$' + input('Ird be a klienst, akinek el akarod kerni a kulcsat: ')
            s.send(msg.encode())
        if(type == 'clients'):
            msg = 'clients'
            s.send(msg.encode()) 
        if(type == 'sendkey'):
            public_key = input('Ird be a kliens publikus kulcsat, akinek el akarod kuldeni a chat felkerest: ')
            msg = 'getkey' + '$$' + public_key + '$$' + crypto.encrypt_mh(str(solitaire_kulcs), public_key)
            s.send(msg.encode())      
        #elif(type == 'public'):
        #    msg = str(0) + input('Ird be a szervernek kuldott uzenetet: ')
        #elif(type == 'private'):
        #    msg = str(1) + input('Ird be a kliensnek kuldott uzenetet: ')
        #elif(type == 'users'):
        #    msg = 'users'
        #elif(type == 'logout'):
        #    msg = 'logout'
       


# MAIN
private_key = crypto.generate_private_key()
print("A privat kulcsod:")
print(private_key)
public_key = crypto.create_public_key(private_key)
print("A publikus kulcsod:")
print(public_key)

sendmessage = threading.Thread(target = sendmsg)
sendmessage.daemon = True
sendmessage.start()

receivemsg = threading.Thread(target = receive)
receivemsg.start()
receivemsg.join()
s.close()
