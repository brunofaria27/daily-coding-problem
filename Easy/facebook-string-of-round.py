'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''
def isBalanced(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char) # For each opening bracket, we push it onto the stack
        elif char in bracket_map.keys(): # For each closing bracket, we check if it matches the top of the stack
            print(str(bracket_map[char]))
            if not stack or bracket_map[char] != stack.pop():
                return False
    return not stack

s = "([])[]({})"
print(isBalanced(s))

# Complexity 
# O(n): where n is all chars in the string