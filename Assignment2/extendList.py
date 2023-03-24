#Write a Python program to extend a list without append.
#using Extend
list1 = ["apple", "banana", "kiwi"]
list2 = ["tomato", "potato", "brinjal"]
list1.extend(list2)
print(list1)

#using insert
list3 = ["apple", "banana", "mango"]
list3.insert(1, "kiwi")
print(list3)

#using +
my_list1 = ["aaa", "bbb", "ccc"]
my_list2 = [1, 2, 3]
my_list = my_list1+my_list2
print(my_list)
