class First:
    def display(self):
        print("first")

class Second:
    def display(self):
        print("second")

class Third(First,Second):
    def display_third(self):
        print("Third")

x=Third()
x.display()
x.display_third()
print(Third.mro())