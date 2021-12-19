import socket
import threading

host = '127.0.0.1' #local
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # SİLİNEBİLİR
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} ayrildi!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
       
        client, address = server.accept()
        print("Ip ve Port {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

    
        print("Kullanici adi: {}".format(nickname))
        broadcast("{} katildi!".format(nickname).encode('ascii'))
        #print("{} portu ile katildi".port)
        client.send('Sunucuya katildi!'.encode('ascii'))

        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()