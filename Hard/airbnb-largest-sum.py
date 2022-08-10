'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
'''
def largest_sum(lst):
  if len(lst) <= 2:
    return max(0, max(lst))
  second = lst[0]
  first = max(second, lst[1])
  for i in range(2, len(lst)):
    current = max(first, second + lst[i])
    second = first
    first = current
  return first

list_int = [2, 4, 6, 2, 5]
assert(largest_sum(list_int) == 13)
list_int = [5, 1, 1, 5]
assert(largest_sum(list_int) == 10)

# Complexity Analysis
# Space Complexity: O(n)
# Time Complexity: O(n)