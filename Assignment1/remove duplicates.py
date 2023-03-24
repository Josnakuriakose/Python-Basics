#Write a Python program to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))
mylist = [1, 2, 2, 3, 4, 4, 5,1,5]
newlist =remove_duplicates(mylist)
print("Original List:", mylist)
print("List with duplicates removed:", newlist)