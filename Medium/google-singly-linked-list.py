'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
'''
class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        
        current = self.head
        while current.next is not None: # Compares whether the next element exists
            current = current.next
        current.next = Node(value) # Add at de final linked list

    '''
    I need to create this function because the address of two linked list is different.
    This method returns only those elements present in linked list.
    '''
    def returnArrayOfLinkedList(self):
        array_returns = list()
    
        current = self.head
        array_returns.append(current.item)
        while current is not None: # Only interative
            array_returns.append(current.item)
            current = current.next
        return array_returns

def removeKlast(linkedList, k):
    newLinkedList = LinkedList()
    p1 = linkedList.head

    newLinkedList.append(p1.item) # Add head to new Linked list
    for _ in range(k):
        p1 = p1.next
        newLinkedList.append(p1.item)

    p1 = p1.next # Jump kth last element
    while p1.next is not None:
        p1 = p1.next
        newLinkedList.append(p1.item)
    return newLinkedList

myLinkedList = LinkedList()
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList = removeKlast(myLinkedList, 2)

mylinkedListAssert = LinkedList()
mylinkedListAssert.append(1)
mylinkedListAssert.append(2)
mylinkedListAssert.append(3)
mylinkedListAssert.append(5)

assert myLinkedList.returnArrayOfLinkedList() == mylinkedListAssert.returnArrayOfLinkedList()

# Complexity
# O(n)