'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects
'''
class List:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

def get_intersection(linked_list1: list, linked_list2: list) -> int:
    pointer_one = linked_list1
    pointer_two = linked_list2

    while(pointer_one != pointer_two):
        if pointer_one == pointer_two:
            return pointer_one
        pointer_one = pointer_one.next
        pointer_two = pointer_two.next
    return pointer_one

# Equal node for return 
node_equal = List(10)

# First Linked List
linked_list1 = List(90)
linked_list1.next = node_equal
linked_list1.next.next = List(3)
linked_list1.next.next.next = List(1)

# Second Linked List
linked_list2 = List(80)
linked_list2.next = node_equal

assert get_intersection(linked_list1, linked_list2) == node_equal
