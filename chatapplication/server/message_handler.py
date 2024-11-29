class MessageHandler:
    def __init__(self):
        self.messages = []  # In-memory storage for messages

    def save_message(self, sender, message):
        """Save a message with the sender's details."""
        self.messages.append({'sender': sender, 'message': message})

    def get_all_messages(self):
        """Retrieve all stored messages."""
        return self.messages
