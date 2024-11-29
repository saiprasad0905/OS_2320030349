from server.ipc_manager import IPCManager

def test_ipc_manager():
    ipc = IPCManager()
    test_message = "Hello, IPC!"
    
    ipc.send_message(test_message)
    received_message = ipc.receive_message()

    assert received_message == test_message, "Message failed in IPC mechanism"

if __name__ == "__main__":
    test_ipc_manager()
    print("IPC Manager test passed!")
