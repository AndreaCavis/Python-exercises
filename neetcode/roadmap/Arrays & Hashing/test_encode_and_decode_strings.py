from encode_and_decode_strings import Solution

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