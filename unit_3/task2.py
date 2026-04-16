# neater function but less efficient O(W * n^2)
def solution(sentence):
    words = [word.lower() for word in sentence.split()]
    result = ""
    
    for word in words:
        if len(word) % 2 != 0:
            # count goes through the entire word for each character, so it is O(n^2)
            char = max(word, key=word.count) 
            result += char

    return result

# more verbose but more efficient O(W * n)
def long_solution(sentence):
    words = [word.lower() for word in sentence.split()]
    result = ""
    
    for word in words:
        if len(word) % 2 != 0:
            max_occurence = 0
            recurring_chars = {}
    
            for i in range(len(word)):
                if word[i] in recurring_chars:
                    recurring_chars[word[i]] += 1
                else:
                    recurring_chars[word[i]] = 1
                
                if recurring_chars[word[i]] > max_occurence:
                        max_occurence = recurring_chars[word[i]]
                        
            for char in recurring_chars:
                if recurring_chars[char] == max_occurence:
                    result += char
                    break

    return result