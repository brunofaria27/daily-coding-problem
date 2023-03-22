'''
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''
def processString(setWords: set, stringProcess: str) -> list:
    possibleReconstruction = list()
    comparableString = ""
    
    n = len(stringProcess)
    i = j = 0

    while j < n:
        if stringProcess[i:j + 1] in setWords:
            possibleReconstruction.append(stringProcess[i:j + 1])
            i = j + 1 # Update begin to last hit position in string
        else:
            if possibleReconstruction == [] and j == n - 1: # len not initialize in 0
                return None
        j += 1
    return possibleReconstruction

test1Words = {'quick', 'brown', 'the', 'fox'}
test1String = "thequickbrownfox"
assert processString(test1Words, test1String) == ['the', 'quick', 'brown', 'fox']

test2Words = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
test2String = "bedbathandbeyond"
assert processString(test2Words, test2String) == ['bedbath', 'and', 'beyond'] or ['bed', 'bath', 'and', 'beyond']

test3Words = {'bed', 'bath'}
test3String = "aksjhdbiadbasa"
assert processString(test3Words, test3String) == None

# Complexity
# Time: O(n) -> all chars in string