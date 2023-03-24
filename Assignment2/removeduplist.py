#Write a Python program to remove duplicates from a list - Instead of creating a new list, try to find a solution within the list itself.
#using for loop
repeated_list = [1, 1, 2, 3, 4, 2, 3, 5, 6, 3, 2, 4, 5, 3, 4, 6, "aaaa", "aaaa"]

for x in set(repeated_list):
  for i in range(1, repeated_list.count(x)):
      repeated_list.remove(x)
print("Duplicate removed list: ", repeated_list)

#using set
my_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, "aaa", "aaa"]
print(list(set(my_list)))


