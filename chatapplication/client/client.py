import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to the server. Type your messages below:")

while True:
    message = input("You: ")
    client.send(message.encode('utf-8'))
