
myList = [1, 2, "aaa", 3, 4, 1, 2, "ccc", 3, "bbb", 4, 1, 3, 4, 1, "aaa", "bbb"]
i = 0
while i < len(myList):
    j = i + 1
    while j < len(myList):
        if myList[i] == myList[j]:

            del myList[j]
        else:
            j += 1
    i += 1
print(myList)
