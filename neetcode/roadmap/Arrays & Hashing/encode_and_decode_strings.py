'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150
'''

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for string in strs:
            # create a custom delimiter "--" to handle all cases.
            encoded_string += string + "-_-"
        # encoded_string = "{whatever content}--" the trailing -- will be handled in decode()
        return encoded_string

    
    def decode(self, s: str) -> list[str]:
        # the trailing -- creates an empty array value. Return the list without it
        decoded_list = s.split("-_-")
        return decoded_list[:-1]
    
# for the test suite see related file in folder


