class Message:
    def __init__(self, content, author, timestamp):
        self.content = content
        self.author = author
        self.timestamp = timestamp

class User:
    def __init__(self, name):
        self.name = name
        self.followers = []
        self.following = []
        self.messages = []

    def follow(self, user):
        if user != self and user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def send_message(self, content, timestamp):
        message = Message(content, self.name, timestamp)
        self.messages.append(message)