import time

class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
        self.timestamp = time.time()

    def display(self):
        print(f"[{self.sender}]: {self.text}")

class Conversation:
    def __init__(self, title):
        self.title = title
        self.messages = []

    def send_message(self, sender, text):
        self.messages.append(Message(sender, text))

    def print_history(self):
        print(f"--- {self.title} ---")
        for msg in self.messages:
            msg.display()

    def delete(self):
        self.messages.clear()

    def get_message_count(self):
        return len(self.messages)

    def forward_message(self, target, message_index):
        if 0 <= message_index < len(self.messages):
            original = self.messages[message_index]
            target.send_message(original.sender, original.text)

if __name__ == "__main__":
    team_chat = Conversation("Team Discussion")
    project_chat = Conversation("Project Alpha")

    team_chat.send_message("Alice", "Hey team, standup in 5 minutes")
    team_chat.send_message("Bob", "Got it, joining now")
    team_chat.send_message("Alice", "Don't forget to update your tasks")

    project_chat.send_message("Charlie", "Deployment is scheduled for Friday")

    print("Before deletion:")
    team_chat.print_history()
    print(f"Project chat has {project_chat.get_message_count()} messages\n")

    team_chat.forward_message(project_chat, 2)
    print("After forwarding:")
    project_chat.print_history()

    team_chat.delete()
    print("\nAfter deleting team chat:")
    print(f"Team chat has {team_chat.get_message_count()} messages")
    print(f"Project chat still has {project_chat.get_message_count()} messages")