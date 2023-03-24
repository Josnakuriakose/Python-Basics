#Write a Python program to sum all the items in a list.
#using a loop
list1= [10, 20, 30, 40, 50]
sum1 = 0
for x in list1:
   sum1 = sum1+x
print("The sum of all items in the list is:", sum1)


# using the built-in sum() function
list2=[1,2,3,4,5]
total= sum(list2)
print("The sum of all items in the list is:", total)