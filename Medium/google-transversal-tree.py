'''
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
For example, given the following preorder traversal:
[a, b, d, e, c, f, g]

And the following inorder traversal:
[d, b, e, a, f, c, g]

You should return the following tree:
    a
   / \
  b   c
 / \ / \
d  e f  g
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not inorder: return None

    root_val = preorder.pop(0)
    root = Node(root_val)

    idx = inorder.index(root_val)

    root.left = build_tree(preorder, inorder[:idx])
    root.right = build_tree(preorder, inorder[idx + 1:])
    return root

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

root = build_tree(preorder, inorder)
print_tree(root)