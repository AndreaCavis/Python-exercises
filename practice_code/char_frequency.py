def count_chars(text):
    # words = text.split() is not needed
    char_frequency = {}

    for char in text:
            if char == " ":
                 continue
            else:
                 char = char.lower()
                 char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency

print(count_chars("Hello World"))


def count_max_char(word):
    char_frequency = {}

    for char in word:
        char_count = char_frequency.get(char, 0) + 1
        char_frequency[char] = char_count
    # valid syntax for returning the key with the highest value
    return max(char_frequency.keys(), key=char_frequency.get) # type: ignore

print(count_max_char("COBBBBBRA"))