import socket
import threading
from server.server import server

def test_server():
    # Start server in a thread
    def run_server():
        server.listen()

    threading.Thread(target=run_server, daemon=True).start()

    # Test connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))
    client.send("Test message".encode('utf-8'))

    client.close()
    print("Server test passed!")

if __name__ == "__main__":
    test_server()
