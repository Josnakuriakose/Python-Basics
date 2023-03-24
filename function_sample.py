def hello(name):
    print("hello"+name)
hello("josna")
def my_function(fstname,lstname):
    print(fstname+lstname)
my_function("josna"," kuriakose")
def my_functions(*kid):
    print("the youngest child is  " +kid[2])
my_functions("aaa","rrr","ddd")
def method(food):
    for x in food:
        print(x)
items=["rice","fish","meat"]
method(items)
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
