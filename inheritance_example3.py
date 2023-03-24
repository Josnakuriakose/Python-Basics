class person:
    def __init__(self,fname,lname):
        self.lname=lname
        self.fname=fname
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
    def welcome(self):
        print("welcome",self.fname,self.lname,"to the class of",self.graduationyear)
p=student("josna","amal",2008)
p.welcome()