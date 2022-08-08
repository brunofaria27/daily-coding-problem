'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
def search_numbers(list_number, k):
    for i in range(0, len(list_number) - 1):
        for j in range(i + 1, len(list_number)):
            if list_number[i] + list_number[j] == k:
                return True
    return False

# Testing coding using assert in Python
list_numbers = [10, 20, 30, 40]
k = 60
assert search_numbers(list_numbers, k) == True

k = 80
assert search_numbers(list_numbers, k) == False

list_numbers = [0, 10, 5, 90, 87, 34]
k = 92
assert search_numbers(list_numbers, k) == True

k = 16
assert search_numbers(list_numbers, k) == False

# Complexity Analysis
# Space Complexity: O(1)
# Time Complexity: O(n^2)
