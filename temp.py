def replace_substring(text, old, new):
    oldText = text.split(old)
    newText = new.join(oldText)
    # replace() can be used as well, return text.replace(old, new)
    return newText


print(replace_substring("hello world, I love the world, amazing world", "world", "friend"))