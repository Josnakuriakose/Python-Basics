class Baseclass:
    def __init__(self):
        print("base init")
    def set_name(self, name):
        self.name = name
        print("baseclass setname")


class Subclass(Baseclass):
    def __init__(self):
        super().__init__()
        print("sub init")
    def set_name(self,name):
        super().set_name(name)
        print("subclass setname")
    def welcome(self):
        print("welcome")
    def display_name(self):
        print("name:"+self.name)

#x = Baseclass()
y = Subclass()



y.welcome()
y.set_name("josna")
y.display_name()