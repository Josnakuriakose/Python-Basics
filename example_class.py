class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("amal",20)
print(p1.name)
print(p1.age)

class Persons:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Persons("John", 36)

print(p1)

class person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print("hello my name is "+self.name)
p2=person1("josna",10)
p2.myfun()
