'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
'''
def giveNewArray(list_integer):
    new_list = list()
    for i in range(0, len(list_integer)): # Get de position of number
        acumulator = 1 # Empty Acumulator
        for j in range(0, len(list_integer)):
            if i != j:
                acumulator *= list_integer[j]
        new_list.append(acumulator)
    return new_list

# Testing coding using assert in Python
array = [1, 2, 3, 4, 5]
assert giveNewArray(array) == [120, 60, 40, 30, 24]

array = [-1, 1, 0, -3, 3]
assert giveNewArray(array) == [0, 0, 9, 0, 0]

array = [90, 80, 2, 30]
assert giveNewArray(array) == [4800, 5400, 216000, 14400]

# Complexity Analysis
# Space Complexity: O(n)
# Time Complexity: O(n^2)