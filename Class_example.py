class Cars:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour
    def start(self):
        print(self.name+" engine started")
car1 = Cars("maruti", 10000, "Red")
car2 = Cars("Nissan",20000,"white")
car2.colour="yellow"
print(car1.name,car1.price,car1.colour)
print(car2.name,car2.price,car2.colour)
car1.start()
f=open("sample.txt","w")
f.close()
