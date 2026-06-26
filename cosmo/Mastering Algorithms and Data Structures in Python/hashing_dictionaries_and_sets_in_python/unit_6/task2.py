'''
Alright, Space Voyager! Let's apply our knowledge to something a tad trickier - an array of passwords, each one a unique mystery to be solved. 
Imagine you're working as a security analyst, huh? Your mission, if you choose to accept it, is to create a program to evaluate the strength of multiple passwords.

You are to write a function that takes a list of passwords as input. Each password in the list will be a non-empty string. 
The function should output a list of dictionaries, with each dictionary corresponding to a password in the original list. 
Each dictionary will have five keys: 'length', 'digit', 'uppercase', 'lowercase', and 'special_char'. 
The value for each key will be a Boolean indicating whether the password meets a particular criterion: 
has at least 8 characters for 'length', contains a digit for 'digit', contains an uppercase letter for 'uppercase', 
contains a lowercase letter for 'lowercase', and contains a special character (one of "!@#$%^&*()-+") for 'special_char'.

Get ready to dive into the world of security analysis – this is where the real fun begins!
'''

def multi_password_strength_counter(passwords: list[str]) -> list[dict[str,bool]]:
    return [check_password_strength(pwd) for pwd in passwords]


def check_password_strength(password: str) -> dict[str, bool]:
    special_characters = "!@#$%^&*()-+"
    return {
        'length': len(password) >= 8, 
        'digit': any(char.isdigit() for char in password), 
        'lowercase': any(char.islower() for char in password),
        'uppercase': any(char.isupper() for char in password), 
        'special_char': any(char in special_characters for char in password),
    }


passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}


