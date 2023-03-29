import socket
import threading


host = "127.0.0.1"
port = 44444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients  = []
nickNames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:

        try:

            message = client.recv(1024)
            broadcast(message)

        except:

            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickName = nickNames[index]
            broadcast(f"{nickName} left the chat!".encode("ascii"))
            nickNames.remove(nickName)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send("nickName".encode("ascii"))
        nickName = client.recv(1024).decode("ascii")
        nickNames.append(nickName)
        clients.append(client)
        # clients_id.append(client_id)
        # client_id += 1

        print(f"Client's NickName: {nickName}!")
        broadcast(f"{nickName} joined the chat!".encode("ascii"))
        client.send("Connected to the server!".encode("ascii"))


        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listening...")
receive()

