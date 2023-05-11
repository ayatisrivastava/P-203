import socket
from threading import Thread
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '192.168.0.158'
port = 8000
server.bind((ip_address, port))
server.listen()
clients = []
list_clients = []
nicknames = []
print("Server is running.")
while True:
    conn, addr = server.accept()
    list_clients.append(conn)
    print(addr[0]+"connected")
    new_thread = Thread(target=clientthread, args=(conn, addr))
    new_thread.start()
def clientthread(conn, addr):
    conn.sent("Welcome to this Chat Room".encode('UTF-8'))
    while True:
        try:
            message = conn.recv(2048).decode('UTF-8')
            if message:
                print(message)
                broadcast(mesaage, conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message.encode('utf-8')) 
            except: remove(clients) 
def remove(connection): 
     if connection in list_of_clients: 
        list_of_clients.remove(connection)
def remove_nickname(nickname): 
    if nickname in nicknames: 
        nicknames.remove(nickname) 
while True: 
    conn, addr = server.accept() 
    conn.send('NICKNAME'.encode('utf-8')) 
    nickname = conn.recv(2048).decode('utf-8') 
    list_of_clients.append(conn) 
    nicknames.append(nickname) 
    message = "{} joined!".format(nickname) 
    print(message) 
    broadcast(message, conn) 
    new_thread = Thread(target= clientthread,args=(conn, nickname)) 
    new_thread.start()