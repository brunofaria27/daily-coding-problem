'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.
'''
# Kadane's algorithm
def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

array = [34, -50, 42, 14, -5, 86]
assert max_subarray_sum(array) == 137

# Complexity Analysis
# Space Complexity: O(n)
# Time Complexity: O(n)