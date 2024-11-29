import multiprocessing

class IPCManager:
    def __init__(self):
        self.queue = multiprocessing.Queue()  # Message queue for IPC

    def send_message(self, message):
        """Send a message to the queue."""
        self.queue.put(message)

    def receive_message(self):
        """Retrieve a message from the queue."""
        if not self.queue.empty():
            return self.queue.get()
        return None
