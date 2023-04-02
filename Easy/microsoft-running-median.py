'''
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''
def running_median(nums):
    sorted_nums = []
    for num in nums:
        sorted_nums.append(num)
        sorted_nums.sort()
        n = len(sorted_nums)
        if n % 2 == 0:
            median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
            print(median)
        else:
            median = sorted_nums[n//2]
            print(median)

nums = [2, 1, 5, 7, 2, 0, 5]
running_median(nums)

# Complexity Analysis
# Time Complexity: O(n log n)