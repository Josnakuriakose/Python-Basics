class person:
    def __init__(self,fstname,lstname):
        self.fstname=fstname
        self.lstname=lstname
    def printname(self):
        print(self.fstname,self.lstname)
p1=person("josna","kuriakose")
p1.printname()
class hello(person):
    pass
x=hello("amal","thomas")
x.printname()