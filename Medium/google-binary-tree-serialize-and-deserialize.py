'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
'''
class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right
        
def serialize(node):
    if node is None:
        return '-1'
    return f'{node.val} {serialize(node.left)} {serialize(node.right)}'

def deserialize(string):
    array_val = iter(string.split()) # Transform to list_iterator
    def deserialize_rec():
        val = next(array_val) # Get next position in list_iterator each recursive call
        if val == '-1':
            return '-1'
        node = Node(val)
        node.left = deserialize_rec()
        node.right = deserialize_rec()
        return node
    return deserialize_rec()

# Binary Tree
node = Node('root', 
            Node('left', 
                Node('left.left'), 
                Node('left.right')
            ), 
            Node('right', 
                Node('right.left'), 
                Node('right.right')
            )
)

# Testing code
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).right.left.val == 'right.left'
assert deserialize(serialize(node)).right.val == 'right'
assert deserialize(serialize(node)).left.left.left == '-1'
assert deserialize(serialize(node)).left.right.val == 'left.right'
assert deserialize(serialize(node)).right.right.left == '-1'

# Complexity Analysis
# Space Complexity: O(n)
# Time Complexity: O(n)
