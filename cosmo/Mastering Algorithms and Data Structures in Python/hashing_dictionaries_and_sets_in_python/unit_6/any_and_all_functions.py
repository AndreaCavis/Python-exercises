''' any() and all() built-in python functions:

To find a nice example for any() and all() functions, let's start by refactoring 
password_strength_counter() from the related lesson: '''

def password_strenght_counter(password: str) -> dict[str, bool]:
    strength = {
        'length': False,
        'digit': False,
        'lowercase': False,
        'uppercase': False,
    }

    if len(password) > 8:
        strength['length'] = True

    for char in password:
        if char.isdigit():
            strength['digit'] = True
        if char.islower():
            strength['lowercase'] = True
        if char.isupper():
            strength['uppercase'] = True
        

    return strength

''' As you can see, the for loop iterates over each character and evaluates against the flags. 
Another approach could be using the any() function directly into the flag declaration as shown in the following function: '''

def pasdword_strength_counter_v2(password: str) -> dict[str, bool]:
    return {
        "length": len(password) > 8,
        "digit": any(char.isdigit() for char in password),
        "lowercase": any(char.islower() for char in password),
        "uppercase":any(char.isupper() for char in password),
    }

''' With this approach, each flag contains a generator expression that produces a series of booleans: '''

digit = [char.isdigit() for char in "abcd4"] # [False, False, False, False, True]
print(digit)

''' This is where any() comes in handy.

any() takes 1 iterable and returns:
- True if AT LEAST 1 item is truthy* (* see # comments at the end)
- False if ALL items are falsy* (or the iterable is EMPTY) 

So, following our digit example: '''

print(any(digit)) # output: True

''' The nice thing is that any() short-circuits: as soon as it finds a True, it stops iterating. '''


''' all()

There's also a companion function all() which returns True when ALL the items satisfy the condition:  '''

# setting up a list of bool based on the condition in list comprehension
nums = [x % 2 == 0 for x in range(0, 100, 2)]#
print(all(nums)) # output True


''' To Summarise:
- any() = "Does at least one item satisfy the condition?"
- all() = "Do all items satisfy the condition?"
'''

# * In Python, truthy and falsy describe how values behave when Python evaluates them in a Boolean context.
# Falsy values: False, None, 0, 0.0, 0j (complex zero), '', [], (), {}, set(), range(0)
# Truthy values: Most other values evaluate to True.
# You can check truthiness by using bool(): bool([]) False, bool(1) True, bool(0) False
# 
# Custom classes can control their truthiness by defining __bool()__ or __len()__.