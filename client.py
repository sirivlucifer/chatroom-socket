import socket
import threading

nickname = input("Kullanici adinizi yaziniz: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #sock_stream tcp tanımlama
#AF_INET, IPv4 için İnternet adresi ailesidir. SOCK_STREAM, mesajlarımızı ağda taşımak için kullanılacak protokol olan TCP için soket tipidir.
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Error Hata Dikkat!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()