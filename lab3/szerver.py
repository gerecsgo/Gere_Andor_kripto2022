
import socket
import threading
import crypto

host = '127.0.0.1'
port = 9000

chat = (host, port)
username = ''
users = ''
ind = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(chat)
s.listen()
print("A szerver elindult.")

clients = []
usernames = []

def checkUser(usernm):
    for i in usernames:
        if i == usernm:
            return False
    return True

def receive(conn,addr):
    global username
    global index
    global users
    try:
        while True:
            msg = conn.recv(2048).decode()
            msg_split = msg.split(' ')
            if(msg == 'register'):
                print('register parancs meghivva egy kliens altal.')
                resp = 'Meghivtad a register parancsot.'
                conn.send(resp.encode())
            elif(msg == 'join'):
                clients.append(conn)
                print(addr)
    finally:
        conn.close()

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target = receive, args=(conn,addr))
    thread.start()
