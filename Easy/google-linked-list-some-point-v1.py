'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects
'''
def get_some_point(linked_list_one: list, linked_list_two: list) -> int:
    # Get size of the for interval
    if len(linked_list_one) > len(linked_list_two):
        size = len(linked_list_two)
    elif len(linked_list_one) < len(linked_list_two):
        size = len(linked_list_one)
    else: size = len(linked_list_one)
    # For in all points of array
    for i in range(0, size):
        if linked_list_one[i] == linked_list_two[i]:
            return linked_list_one[i]
    return 0


list1 = [3, 4, 5, 8]
list2 = [1, 3, 9, 8]
assert get_some_point(list1, list2) == 8
list1 = [3, 4, 5, 8, 10, 20, 30]
list2 = [1, 3, 9, 6, 10]
assert get_some_point(list1, list2) == 10
list1 = [3, 4, 5, 0]
list2 = [1, 3, 9, 8]
assert get_some_point(list1, list2) == 0