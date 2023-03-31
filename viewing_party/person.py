class Person:
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
