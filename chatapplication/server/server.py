import socket
import threading
from ipc_manager import IPCManager

HOST = '127.0.0.1'
PORT = 5000

ipc = IPCManager()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            ipc.send_message(message)  # Add to the IPC queue
            print(f"Received: {message}")
        except:
            client_socket.close()
            break

def process_messages():
    while True:
        message = ipc.receive_message()
        if message:
            print(f"Processing message: {message}")
            # You can add message storage or routing logic here

# Start the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

# Start the message processing thread
threading.Thread(target=process_messages, daemon=True).start()

# Accept clients
while True:
    client_socket, addr = server.accept()
    print(f"Connected to {addr}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()
