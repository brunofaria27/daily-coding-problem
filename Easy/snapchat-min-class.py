'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2
'''
def min_rooms(array):
    min_rooms = 0
    start_times = []
    end_times = []
    for i in range(0, len(array)):
        start_times[i].append(array[i][0])
        end_times[i].append(array[i][1])
    start_times.sort()
    end_times.sort()
    end_index = 0
    for i in range(1, len(array)):
        if start_times[i] < end_times[end_index]:
            min_rooms += 1
        else:
            end_index += 1
    return min_rooms

array = [(30, 75), (0, 50), (60, 150)]
assert min_rooms(array) == 2

# Complexity Analysis
# Space Complexity: O(n)
# Time Complexity: O(n)
