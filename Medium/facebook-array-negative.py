'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''
def trapped_water(arr):
    n = len(arr)
    left, right = 0, n-1
    left_max, right_max = 0, 0
    total_water = 0
    
    while left < right:
        if arr[left] < arr[right]:
            if arr[left] > left_max:
                left_max = arr[left]
            else:
                total_water += left_max - arr[left]
            left += 1
        else:
            if arr[right] > right_max:
                right_max = arr[right]
            else:
                total_water += right_max - arr[right]
            right -= 1
    
    return total_water

assert trapped_water([2, 1, 2]) == 1
assert trapped_water([3, 0, 1, 3, 0, 5]) == 8
assert trapped_water([0, 0, 0, 0, 0]) == 0

# Complexity
# O(n)