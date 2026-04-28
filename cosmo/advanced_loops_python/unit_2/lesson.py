def func(string):
    words = string.split()
    oddChar = []

    for word in words:
        if len(word) % 2 == 0:
            oddChar += [word[i] for i in range(len(word)) if i % 2 != 0]

    result = "".join(oddChar)
    return result


def solution(sentence):
    words = sentence.split()
    result = ""

    for word in words:
        if len(word) % 2 == 0:
            #steps through odds
            for i in range(1, len(word), 2):
                result += word[i]
        
    return result


print(func("Python is a high-level programming language.")) # yhnsihlvl
print(solution("Python is a high-level programming language.")) # yhnsihlvl