import socket
import threading
import time

# Server configuration for testing
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Start a mock server for testing
def start_mock_server():
    def handle_client(client_socket):
        while True:
            try:
                # Receive messages from the client
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Mock Server Received: {message}")
                    # Echo the message back to the client
                    client_socket.send(f"Echo: {message}".encode('utf-8'))
                else:
                    break
            except:
                break
        client_socket.close()

    mock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mock_server.bind((SERVER_HOST, SERVER_PORT))
    mock_server.listen(1)
    print("Mock server started for testing.")
    
    while True:
        client_socket, addr = mock_server.accept()
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

# Test the client
def test_client():
    # Start the mock server in a separate thread
    server_thread = threading.Thread(target=start_mock_server, daemon=True)
    server_thread.start()

    time.sleep(1)  # Give the server some time to start

    # Create a client and connect to the mock server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    try:
        # Test sending a message
        test_message = "Hello, Server!"
        client.send(test_message.encode('utf-8'))
        print(f"Client Sent: {test_message}")

        # Test receiving a response
        response = client.recv(1024).decode('utf-8')
        print(f"Client Received: {response}")

        # Assert the response matches the expected echo
        assert response == f"Echo: {test_message}", "Test failed: Response mismatch"
        print("Test passed: Message sent and received successfully.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    test_client()
