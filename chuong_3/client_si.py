import socket
import time
import random

HOST = 'locahost'
PORT = 12345
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST,PORT))

for i in range(10):
    temp = round(random.uniform(25.0,35.0), 2)
    message = f'Nhiệt độ: {temp} độ C'
    #Gửi dữ liệu đến sever
    client_socket.sendall(message.encode())
    print(f'[CLIENT] Gửi {message}')


    time.sleep(2)
client_socket.close()