#Write a Python program to find the list in a list of lists whose sum of elements is the highest

mylist = [[1, 2, 3], [852, 985, 836], [10000, 2000, 30], [100, -200, 300], [500, 600, 700]]
#using max function

print(max(mylist))

#using for loop

highest_sum = 0
highest_list = None
for x in mylist:
    current_sum = sum(x)
    if current_sum > highest_sum:
        highest_sum = current_sum
        highest_list = x
print(highest_list)
