#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
def count_strings(list1):
    count=0
    for x in list1:
        if len(x)>=2 and x[0]==x[-1]:
            count += 1
    return count
strings = ['abca', 'yyzx', 'raaar', 'oello', 'bggc','aa']
count1 = count_strings(strings)
print("Number of strings with same first and last character:", count1)