import socket
import threading

nickName = input("Please, Enter your nickName: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 44444))

def receive():
    while True:
        try:

            message = client.recv(1024).decode("ascii")
            if message == "nickName":
                client.send(nickName.encode("ascii"))
            else:
                print(message)

        except:
            print("There is an ERROR!")
            client.close()
            break


def write():
    while True:
        message = f'{nickName}: {input("")}'
        client.send(message.encode("ascii"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
