'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isUnival(tree):
    def unvalHelper(tree, key):
        if tree is None:
            return True
        if tree.key == key:
            if unvalHelper(tree.left, key) and unvalHelper(tree.right, key):
                return True
        return False
    return unvalHelper(tree, tree.key)

def countUnivalSubTrees(tree):
    if tree is None:
        return 0
    left_unival = countUnivalSubTrees(tree.left)
    right_unival = countUnivalSubTrees(tree.right)
    return 1 + left_unival + right_unival if isUnival(tree) else left_unival + right_unival

tree = Node(0)
assert countUnivalSubTrees(tree) == 1
tree = Node(0, Node(0), )
assert countUnivalSubTrees(tree) == 2
tree = Node(0, Node(0), Node(0), )
assert countUnivalSubTrees(tree) == 3
tree = Node(0, Node(0, Node(0), Node(1), ), Node(1, Node(1), Node(1), ),)
assert countUnivalSubTrees(tree) == 5