'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:
string encode(vector<string> strs) {
    # // ... your code
    return encoded_string;
}

# Machine 2 (receiver) has the function:
vector<string> decode(string s) {
    # //... your code
    return strs;
}

# So Machine 1 does:
string encoded_string = encode(strs);

# and Machine 2 does:
vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example 1:
# Input:
dummy_input = ["Hello","World"]
# Output: ["Hello","World"]

Explanation:
# Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

# Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

------------------------------------------------------------------------
Example 2:
# Input: 
dummy_input = [""]
# Output: [""]

------------------------------------------------------------------------
Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
'''


# ------------- Naive Solution ------------------
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

    


# -------------------- Test Suite ---------------------------------
solution_test = Solution()

encode = solution_test.encode(["Hello", "World"])
encode2 = solution_test.encode([","])
encode3 = solution_test.encode([""])
encode4 = solution_test.encode(["0"])
encode5 = solution_test.encode(["", ""])
encode6 = solution_test.encode(["Cristo", "Cane"])
decode = solution_test.decode

print(encode)
print(decode(encode2))
print(decode(encode3))
print(decode(encode4))
print(decode(encode5))
print(decode(encode6))