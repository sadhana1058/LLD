class Message:
    def __init__(self, author, content: str, timestamp: str):
        self.author = author
        self.content= content
        self.timestamp = timestamp

class User:
    def __init__(self, name: str):
        self.name = name
        self.followers = []
        self.following = []
        self.messages = []

    def follow(self, user): 
        # TODO: Add user to following, add self to user's followers
        # Guard against: self-follows, duplicates
        if user != self:
            self.following.append(user)
        
        user.followers.append(self)
        

    def send_message(self, content: str, timestamp: str):
        # TODO: Create Message and add to messages list
        message = Message(
            self.name,content,timestamp
        )
        self.messages.append(message)

if __name__ == "__main__":
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    alice.follow(bob)
    alice.follow(charlie)
    bob.follow(alice)

    alice.send_message("Hello world!", "10:00 AM")
    bob.send_message("Learning OOP!", "10:30 AM")

    print(f"{alice.name} is following:")
    for u in alice.following:
        print(f"  - {u.name}")

    print(f"{bob.name}'s followers:")
    for u in bob.followers:
        print(f"  - {u.name}")

    print(f"{alice.name}'s messages:")
    for m in alice.messages:
        print(f"  [{m.timestamp}] {m.content}")