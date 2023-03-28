class Profile:
    year = 2020
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age+1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("year:"+str(Profile.year))
        print("Name:"+self.name)
        print("age:"+str(self.age))
        print(("place:"+self.place))

    @classmethod
    def add_year(cls):
        cls.year = cls.year+1

    @staticmethod
    def display_welcome():
        print("welcome")
Profile.display_welcome()
x = Profile("josna", 20, "kakkanad")
y = Profile("amal", 10, "kochi")
x.display()
y.display()
print("--------------------------------")
Profile.year=Profile.year+1
x.add_age()
y.add_age()

x.display()
y.display()

Profile.add_year()