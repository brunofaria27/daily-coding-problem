'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''
def staircase(n, X):
    if n == 0 or len(X) == 0:
        return 0
    elif n in X:
        return 1 + sum(staircase(n - x, X) for x in X if x < n)
    else:
        return sum(staircase(n - x, X) for x in X if x < n)

assert staircase(0, []) == 0
assert staircase(4, [1, 2]) == 5
assert staircase(5, [1, 3, 5]) == 5

# Complexity Analysis
# Space Complexity: O(n)
# Time Complexity: O(|X|^n)