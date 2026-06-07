'''
You are given a string s containing only uppercase letters, with its length n ranging from 1 to 100, inclusive. 
Your task involves series of sequential comparisons resulting in the removal of certain characters, following this process:

1. Form neighbouring pairs in the string sequentially (pair the first and second characters, the third and fourth, and so forth).
   If the string length is odd, keep the last character unpaired.
2. For each pair, compare the characters and remove the character that comes earlier in the lexicographical order.
   If they are the same, remove the first character in the pair.
3. These two steps define a round of operation. Perform these rounds until the string becomes empty.
4. If the string length after a round is 1, in the next round the last remaining character is removed and the process terminates.

Your task is to implement a Python function, solution(s), where s is the initial input string.
The function should follow the described process and return a list of the removed letters in the order of their removal.

Each character of the string is an uppercase letter from A to Z, inclusive.

As an example, if s = "BCAAB", the output should be ['B', 'A', 'A', 'B', 'C'].

The rounds would occur as follows:

- After the first round, the pairs are (B,C), (A,A), (B) and the resulting string is CAB with 'B' and 'A' being removed.
  The removed characters list becomes ['B', 'A'].
- After the second round, the pairs are (C,A) and (B), and the resulting string is CB with 'A' being removed.
  The removed characters list becomes ['B', 'A', 'A'].
- After the third round, B is removed and the string becomes C.
  The removed characters list becomes ['B', 'A', 'A', 'B'].
- After the fourth round, there are no pairs, and thus 'C' is removed, and the resulting string is empty. 
  The removed characters list becomes ['B', 'A', 'A', 'B', 'C'].
'''


def Mysolution(s: str) -> list[str]:
    # TODO: implement the solution here
    return [""]


def solution(s):
    n = len(s)
    neighbour_pairs = []
    i = 0

    while i < n:
        if n % 2 == 0:
            neighbour_pairs.append([s[i:i+2]])
        else:
            neighbour_pairs.append([s[i:i+2]])
        i += 2

    print(neighbour_pairs)
    pass

s = "BCAAB"
print(solution(s))