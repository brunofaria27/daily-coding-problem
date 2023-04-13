'''
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

import random

def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        # generate a random integer from 1 to 25 with uniform probability
        rand_int = (rand5() - 1) * 5 + rand5()
        # map the integer to a value from 1 to 7 with uniform probability
        if rand_int <= 21:
            return rand_int % 7 + 1
        
# Test case
for i in range(1000):
        rand_num = rand7()
        assert rand_num >= 1 and rand_num <= 7

# Complexity Analysis
# Time Complexity: O(1)