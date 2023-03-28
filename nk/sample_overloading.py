class Sample:
    def set_name(self,name):
        self.name=name
    def __add__(self, other):
        name = self.name+" "+other.name
        return name

first_name = Sample()
second_name = Sample()

first_name.set_name("Josna")
second_name.set_name("kuriakose")
fullname=first_name+second_name
print(fullname)
