# Convert a text number string into its digit representation.

print("PORCODIO")

numString = "one two double six triple four five"

textToNum = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

numArray = numString.split()
ans = ""
i = 0

while i < len(numArray):
    if numArray[i] == "double":
        ans += textToNum[numArray[i+1]] * 2
        i += 2
    elif numArray[i] == "triple":
        ans += textToNum[numArray[i+1]] * 3
        i += 2
    else:
        ans += textToNum[numArray[i]]
        i += 1
        
print(ans)
