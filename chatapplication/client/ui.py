import threading

def start_ui(client_socket):
    """Start the user interface for sending and receiving messages."""
    # Thread to receive messages
    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                print(f"\n{message}")
            except:
                print("Disconnected from the server.")
                client_socket.close()
                break

    # Start the thread
    threading.Thread(target=receive_messages, daemon=True).start()

    # Sending messages
    while True:
        try:
            message = input("You: ")
            client_socket.send(message.encode('utf-8'))
        except:
            print("Connection closed.")
            client_socket.close()
            break
