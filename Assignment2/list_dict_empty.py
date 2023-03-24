#Write a Python program to check if all dictionaries in a list are empty or not.

list1 = [{"name": "josna"}, {"company": "panasa"}, {"aaa": "aaa"}]
list=[{}, {"name": "josna"}, {}]
list2 = [{}, {}, {}]
count = 0
for x in list2:
    if not x:
        count = count+1

if count == len(list2):
     print("empty")
else:
     print("not empty")


