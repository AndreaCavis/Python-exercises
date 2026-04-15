# Q2. Consider a string, S, that is a series of characters, each followed by its frequency as an integer.
# The string is not compressed correctly, so there may be multiple occurrences of the same character.

# A properly compressed string will consist of one instance of each character in alphabetical order followed by the total count of that character within the string.

# eg: "a1f3d2a4s12"    output: "a5d2f3s12"

badCompressed = "a1c3b2a4"

def extractCharacters(badString):
    charMap = {}
    i=0
    while i < len(badString):
        if not badString[i].isdigit():
            key = badString[i]
            i+=1
            
            num = 0
            while i < len(badString) and badString[i].isdigit(): #out of bound
                num = num * 10 + int(badString[i])
                i+=1
            # if key in charMap: charMap[key] += num
            # else: charMap[key] = num
            charMap[key] = charMap.get(key, 0) + num
        else:
            i+=1
    return charMap
    
charTotal = extractCharacters(badCompressed)
sortedKeys = sorted(charTotal)

# answ = "".join(k + str(charTotal[k]) for k in sorted(charTotal))
answ = ""
for k in sortedKeys:
     answ += k + str(charTotal[k])

print(answ)