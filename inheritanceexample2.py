class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print("first name:"+self.fname+"lastname:"+self.lname)
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.gratuationyear=2012
p1=student("josna","amal")
print(p1.gratuationyear)
print(p1.printname())
