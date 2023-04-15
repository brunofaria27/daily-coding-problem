'''
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
'''
def longest_palindromic_substring(s: str) -> str:
    if not s: return ""

    n = len(s)
    start, end = 0, 0

    for i in range(n):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)

        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start:end + 1]

def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

string = "aabcdcb"
assert longest_palindromic_substring(string) == "bcdcb"

string = "bananas"
assert longest_palindromic_substring(string) == "anana"

# Complexity Analysis
# Time Complexity: O(n)