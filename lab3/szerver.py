
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
public_keys = []

def receive(conn,addr):
    global username
    global index
    global users
    try:
        while True:
            msg = conn.recv(2048).decode()
            msg_split = msg.split('$$')

            if(msg_split[0] == 'register'):
                found = 0
                for key in public_keys:
                    if(key[0] == addr[1]):
                        key[1] = msg_split[1]
                        found = 1
                        break
                if(not found):
                    public_keys.append([addr[1], msg_split[1]])

                print('Register parancs meghivva egy kliens altal. Uj kulcs elmentve.')
                resp = 'Meghivtad a register parancsot, sikeresen kicserelted a privat kulcsod!'
                conn.send(resp.encode())
            elif(msg == 'join'):
                clients.append(conn)
                print('Uj kliens csatlakozott a szerverre. Cime:')
                print(addr)
            elif(msg == 'clients'):
                print('Clients parancs meghivva egy kliens altal. Valasz elkuldve.')
                joined_clients = []
                for c in public_keys:
                    joined_clients.append(c[0])
                resp = str(joined_clients)
                conn.send(resp.encode())
            elif(msg_split[0] == 'getkey'):
                print(public_keys)
                print(msg_split[1])
                print('Getkey parancs meghivva egy kliens altal. Valasz elkuldve.')
                resp = 'Az adott kliens kulcsat nem talaltuk meg!'
                for key in public_keys:
                    if(str(key[0]) == str(msg_split[1])):
                        resp = "A lekert kulcs: "+str(key[1])
                conn.send(resp.encode())
    finally:
        conn.close()

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target = receive, args=(conn,addr))
    thread.start()
