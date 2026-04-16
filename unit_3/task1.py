def solution(sentence):
    words = sentence.split()
    result = ""
    
    for word in words:
        if len(word) % 2 != 0:
            for i in range(0, len(word), 2):
                result += word[i]
    
    return result[:][::-1]