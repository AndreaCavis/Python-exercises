def solution(sentence, c):
    words = sentence.split()
    result = ""
    for word in words:
        if len(word) % 2 == 0:
            half_word = word[len(word) // 2:]

            for char in half_word:
                if char < c:
                    result += char
                
    return result