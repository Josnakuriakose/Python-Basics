def highest_sum_list(lst):

    highest_sum = float('-inf')
    highest_list = None

    for x in lst:
          curr_sum = sum(x)

          if curr_sum > highest_sum:
            highest_sum = curr_sum
            highest_list = x

    return highest_list


my_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = highest_sum_list(my_list)
print(result)