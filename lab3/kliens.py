import copy
import random

import sys
import socket
import threading
import utils
import numpy as np
import crypto

# SZERVER CSATLAKOZAS
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '127.0.0.1'
# port = 9000
# chat = (host, port)
# s.connect(chat)
# msg = 'join'
# s.send(msg.encode())


# TESZTFUGGVENYEK
def teszt():
    solitaire_kulcs = [28, 15, 20, 30, 7, 9, 12, 49, 40, 6, 19, 48, 33, 34, 31, 27, 18, 38, 10, 46, 1, 14, 23, 39, 53, 29, 37, 54, 3, 22, 21, 51, 8, 45, 16, 44, 11, 17, 5, 26, 42, 2, 36, 24, 52, 47, 35, 25, 4, 50, 32, 43, 13, 41]
    text = 'Ez volna az uzenete(#@)($)(!@#$)(U)(#UR)('
    encoded = crypto.encode_solitaire(text, copy.deepcopy(solitaire_kulcs))
    decoded = crypto.decode_solitaire(encoded, copy.deepcopy(solitaire_kulcs))
    print("Encodeolt szoveg:")
    print(encoded)
    print("Decodeolt szoveg:")
    print(decoded)

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
        type = input('public/private/users/logout/register\n')
        if(type == 'register'):
            msg = 'register'
        elif(type == 'public'):
            msg = str(0) + input('Ird be a szervernek kuldott uzenetet: ')
        elif(type == 'private'):
            msg = str(1) + input('Ird be a kliensnek kuldott uzenetet: ')
        elif(type == 'users'):
            msg = 'users'
        elif(type == 'logout'):
            msg = 'logout'
        s.send(msg.encode())

def main():
    private_key = crypto.generate_private_key()
    print("Private key")
    print(private_key)
    public_key = crypto.create_public_key(private_key)
    print("Public key")
    print(public_key)
    encrypted = crypto.encrypt_mh('SZEVASZTOK ! Ember vafojsog39025i320',public_key)
    print("Encrypted text")
    print(encrypted)
    decrypted = crypto.decrypt_mh(encrypted, private_key)
    print("Decrypted text")
    print(decrypted)

if __name__ == "__main__": main()

# sendmessage = threading.Thread(target = sendmsg)
# sendmessage.daemon = True
# sendmessage.start()

# receivemsg = threading.Thread(target = receive)
# receivemsg.start()
# receivemsg.join()
# s.close()
