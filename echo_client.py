import socket

HOST = "127.0.0.1"
PORT = 5050


message = input("Enter a message: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(message.encode())
    print("Reply:", client.recv(1024).decode())
