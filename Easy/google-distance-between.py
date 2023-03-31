'''
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them.
'''
def subst(s: str, t: str) -> int:
    count_distance = 0
    max_tam = max(len(s), len(t))

    for i in range(0, max_tam):
        try:
            if s[i] != t[i]:
                count_distance += 1
        except IndexError:
            count_distance += 1
    return count_distance

assert subst("kitten", "sitting") == 3
assert subst("kitten", "kitten") == 0
assert subst("banana", "yyyyyyyyyy") == 10

# Complexity Analysis
# Time Complexity: O(n)

'''
Searching I found the solution using the Levenshtein distance:
- The Levenshtein distance (or Edit distance) is a way of quantifying how different two strings are from one another by counting the minimum number of operations required to transform one string into the other.
'''
def levenshteinDistance(s: str, t: str) -> int:
    m, n = len(s), len(t)

    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = i
    for j in range(1, n + 1):
        T[0][j] = j

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            T[i][j] = min(T[i - 1][j] + 1, T[i][j - 1] + 1, T[i - 1][j - 1] + cost)
    return T[m][n]

assert levenshteinDistance("kitten", "sitting") == 3
assert levenshteinDistance("kitten", "kitten") == 0
assert levenshteinDistance("banana", "yyyyyyyyyy") == 10

# Complexity Analysis
# Time Complexity: O(m * n)