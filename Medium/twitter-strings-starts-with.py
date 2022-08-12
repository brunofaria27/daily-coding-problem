'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''
def get_words(query, strings):
    array_string = list()
    for i in strings:
        if i.startswith(query):
            array_string.append(i)
    return array_string

query = 'de'
list_querys = ['dog', 'deer', 'deal']
assert get_words(query, list_querys) == ['deer', 'deal']
query = 'ar'
list_querys = ['arvore', 'futebol', 'arte', 'array', 'galo', 'tearos']
assert get_words(query, list_querys) == ['arvore', 'arte', 'array']

# Complexity Analysis
# Space Complexity: O(n)
# Time Complexity: O(n)