class User:
    def __init__(self, name):
        self.name = name
        self.groups = []
    def enroll(self, group):
        if group not in self.groups:
            self.groups.append(group)
            group.members.append(self)

class Group:
    def __init__(self, name):
        self.name = name
        self.members = []
    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)
            user.groups.append(self)
