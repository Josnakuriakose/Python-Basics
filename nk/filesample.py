file=open("example.py", "w")
content=file.write("print('hi'')")
file.close()
with open("multipleinheritance.py","r") as f:
    x=f.read()
print(x)