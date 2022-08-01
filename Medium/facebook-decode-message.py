'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
'''
# Create a map
def message_possibility(message_encoded):
    def decoded_message(message, k):
        if k == 0: return 1 # Empty String - Error
        if message.find("00") > 0: return 0 # Not valid entry - Error
        if message[0] == '0': return 0 # Not valid
        s = len(message) - k
        res = decoded_message(message, k - 1)
        # The condition verify if the two digits before k are in the interval
        if k >= 2 and int(message[s:s + 2]) < 27:
            res += decoded_message(message, k - 2)
        return res
    return decoded_message(message_encoded, len(message_encoded))

                        
# Testing coding using assert in Python
assert message_possibility('') == 1
assert message_possibility('1') == 1
assert message_possibility('111') == 3
assert message_possibility('1111') == 5
assert message_possibility('11161') == 5
assert message_possibility('12161') == 5
assert message_possibility('13161') == 4
assert message_possibility('0103001') == 0
assert message_possibility('0101') == 0
assert message_possibility('001') == 0
assert message_possibility('011010') == 0
