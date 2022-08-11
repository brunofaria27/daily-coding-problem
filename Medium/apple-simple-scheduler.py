'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import time

def test_function():
    return "I'm a very good programmer."

def scheduler(function, time_wait):
    time.sleep(time_wait/1000) # Time in milliseconds
    return function()

assert scheduler(test_function, 10000) == "I'm a very good programmer."