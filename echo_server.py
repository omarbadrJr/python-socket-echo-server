import socket

HOST = "127.0.0.1"
PORT = 5050


def transform(message):
    command = message[0]
    text = message[1:]

    if command == "A":
        return "".join(sorted(text, reverse=True))
    if command == "C":
        return "".join(sorted(text))
    if command == "D":
        return text.upper()
    return message


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server is running on port {PORT}")

    while True:
        client, address = server.accept()
        with client:
            message = client.recv(1024).decode()
            reply = transform(message)
            client.sendall(reply.encode())
            print(f"{address}: {message} -> {reply}")
