'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''
def searchNumber(list_integers):
    list_integers.sort() # Order the list
    for i in range(0, len(list_integers)):
        if list_integers[i] < 0: i += 1 # Jump not positive integer
        try:
            if list_integers[i] + 1 != list_integers[i + 1] and list_integers[i] > 0:
                return list_integers[i] + 1
        except:
            if i == len(list_integers) - 1: return list_integers[i] + 1

list_integers = [3, 4, -1, 1]
assert searchNumber(list_integers) == 2
list_integers = [1, 2, 0]
assert searchNumber(list_integers) == 3
list_integers = [-5, -2, 0, 1, 2, 3, 5, 6, 7]
assert searchNumber(list_integers) == 4
list_integers = [7, 8, 9, 11, 12]
assert searchNumber(list_integers) == 10
list_integers = [1, 1, 0, -1, -2]
assert searchNumber(list_integers) == 2
list_integers = [2, 3, -7, 6, 8, 1, -10, 15]
assert searchNumber(list_integers) == 4

# Complexity Analysis
# Space Complexity: O(1)
# Time Complexity: O(n log n)
