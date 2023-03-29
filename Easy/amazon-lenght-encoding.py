'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''
def encrypt(string: str) -> str:
    encrypted_string = ""
    count = 0

    prevs_char = string[0]
    for char in string:
        if prevs_char != char:
            encrypted_string += f'{count}{prevs_char}'
            count = 0
        count += 1
        prevs_char = char
    encrypted_string += f'{count}{prevs_char}' # This line is needed because the loop ends before adding the last element to the string.

    return encrypted_string

def decrypt(string_encrypted: str) -> str:
    decrypted_string = ""

    i = 0
    while i < len(string_encrypted):
        count = int(string_encrypted[i])
        char = string_encrypted[i + 1]
        decrypted_string += char * count
        i += 2
    return decrypted_string               

string = "AAAABBBCCDAA"
encrypted_string = "4A3B2C1D2A"
assert encrypt(string) == encrypted_string
assert decrypt(encrypted_string) == string

# Complexity Analysis
# Time Complexity: O(n) - where N is the number of chars in string