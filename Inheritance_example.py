class Person:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
    def address(self):
        print(self.name,self.contact)
class Doctor(Person):
    pass
class Patient(Person):
    pass
doc1=Doctor("John",12345)
pat1=Patient("George",54321)
doc1.address()
pat1.address()