# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


list1 = [1, 7,2, 3, 4, 5, 6,5,1,2]
list2=set(list1)
list3=list(list2)
print(list3)
print(list2)
f=filter(lambda x:x%2 ==0,list1)
print(list(f))