list1=["apple","banana","grapes"]
print(list1)
print(len(list1))
list2=["abc",5,"dgh",True]
print(list2)
print(type(list1))
print(type(list2))
list3=list(("mango","lemon",6))
print(list3)
print(list1[2])
print(list3[-2])
print(list3[1:])
print(list3[:2])
if "apple" in list1:
    print("yes apple in list1")
mylist=["jobin","amal","chester"]
print(mylist)
mylist[0]="josna"
print(mylist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist1 = ["apple", "banana", "cherry"]

thislist1[1:2] = ["blackcurrant", "watermelon"]

print(thislist1)
mylist2=["aaa","bbb","ccc"]
mylist2[1:3]=["wwww"]
print(mylist2)
mylist3=["appple","banana","cucumber"]
mylist3.insert(2,"kiwi")
print(mylist3)
#append
mylist3.append("grapes")
print(mylist3)
list5=[1,2,3]
list6=[4,5,6]
list5.extend(list6)
print(list5)
