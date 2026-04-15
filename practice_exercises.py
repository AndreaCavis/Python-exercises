def reversed_triple_chars(s: str) -> str:
    # TODO: Implement the function that reform the string as described above
    result = ""
    n = len(s)

    for i in range(0, n, 3):
        if (n - i) < 3:
            result += s[i:]
        else:
            result += s[i:i+3][::-1]
    
    return result

print(reversed_triple_chars("abcdefghijk"))

# ----------------------------------------------------------------------------------

def organiseArray(nums):
    mid = len(nums) // 2

    if len(nums) % 2 == 1:
        left = mid-1
        right = mid+1
        result = [nums[mid]]
    else:
        left = mid-1
        right = mid
        result = []

    while left >= 0 and right < len(nums):r
        result.append(nums[left])
        result.append(nums[right])
        left -= 1
        right += 1

    return result

nums = [1,2,3,4,5,6]

print(organiseArray(nums))

# ----------------------------------------------------------------------------------

def unusual_traversal(array):
    n = len(array)
    mid = n // 2
    
    result = [array[mid]]
    
    left = mid - 1
    right = mid + 1
    
    while left >= 0 or right < n:
        
        # Take up to 2 from the left
        if left >= 1:
            result.append(array[left - 1])
            result.append(array[left])
            left -= 2
        elif left == 0:
            result.append(array[left])
            left -= 1
        
        # Take up to 2 from the right
        if right <= n - 2:
            result.append(array[right])
            result.append(array[right + 1])
            right += 2
        elif right == n - 1:
            result.append(array[right])
            right += 1
    
    return result

print(unusual_traversal([1, 2, 3, 4, 5, 6, 7]))
print(unusual_traversal([1, 2, 3, 4, 5]))

# ----------------------------------------------------------------------------------

def count_letters(string):
    n = len(string)
    begin, end = 0,0
    count = 0
    result = []

    while end < n:
        previousCh = string[begin]
        currentCh = string[end]

        if not string[end].isalpha() and not string[end].isdigit():
            end += 1
            continue
        
        if currentCh == previousCh:
            count += 1
            end += 1
        else:
            result.append((previousCh, count))
            count = 0
            begin = end

        if end == n:
            result.append((currentCh, 1))
            end += 1

    return result

print(count_letters("aaabb44cccaae"))

# ---------------------- alternative version ----------------

def encode_rle(s):
    # TODO: implement
    encodedString = ""
    currentCh = None
    count = 0
    
    for ch in s:
        if ch.isdigit() or ch.isalpha():
            if ch == currentCh:
                count += 1
            else:
                if currentCh is not None:
                    encodedString += currentCh + str(count)
                currentCh = ch
                count = 1
    
    if currentCh is not None:
        encodedString += currentCh + str(count)
        
    return encodedString

print(encode_rle("aaabbb"))

# ----------------------------------------------------------------------------------

def solution(s):
    # TODO: Implement the solution here
    words = s.split()
    shiftedWords = ["".join(shift_char(word, 1)) for word in words]
    result = " ".join(shiftedWords)
    return result

def shift_char(word, step):
    n = len(word)
    shiftedWord = ""
    for i in range(n):
        shiftedWord += word[0+(i-step)%n] 
    return shiftedWord
    
print(solution("abc 123 def ghi"))

# ----------------------------------------------------------------------------------

def solution(input_str):
    # TODO: implement the string transformation function
    words = input_str.split()
    shiftedWords = ["".join(shift_letters(word)) for word in words]
    result = shiftedWords[-1]

    if len(shiftedWords) == 1:
        return result
    else:
        result += " " + " ".join(shiftedWords[0:-1])

    return result


def shift_letters(word):
    a,z = ord("a"), ord("z")
    A, Z = ord("A"), ord("Z")
    result = ""

    for char in word:
        ch = ord(char)
        if "A" <= char <= "Z":
            result += chr(Z-ch+A)
        elif "a" <= char <= "z":
            result += chr(z-ch+a)
        
    return result

print(solution("An apple a day keeps the doctor away"))

# ----------------------------------------------------------------------------------

def solution(input_str):
    # TODO: implement the function
    words = input_str.split()
    capitalisedWords = ["".join(capitalise_first_letter(word)) for word in words]
    result = " ".join(capitalisedWords)
    
    return result



def capitalise_first_letter(word):
    n = len(word)
    result = ""
    
    for i in range(n):
        if i == 0:
            result += word[i].upper()
        else:
            result += word[i].lower()
    
    return result


print(solution("SoME rAndoM _TeXT"))
    

# ----------------------------------------------------------------------------------

def solution(s):
    # TODO: Implement the function that could solve the task
    words = s.split("-")
    swappedWords = ["".join(swap_char(word)) for word in words]
    result = "-".join(swappedWords)
    return result
    
    
def swap_char(word):
    swapped = ""
    num = ""
    nums = []
    
    for char in word:
        if char.isalpha():
            swapped += str(1 + (ord(char) - ord("a")) % 26)
        if char.isdigit():
            num += char
            
    if num:
        nums.append(int(num))
        
    for num in nums:
        swapped += chr(ord("a") + (num - 1) % 26)
    return swapped

# ----------------------------------------------------------------------------------

def solution(s):
    # TODO: implement
    words = s.split()
    stringNumbers = ["".join(find_number(word)) for word in words]
    numbers = [int(x) for x in stringNumbers if x != "0"]
    result = sum(numbers)
    return result


def find_number(word):
    digit = ""
    for char in word:
        if char.isdigit():
            digit += char    
    return digit if digit else "0"


print(solution("joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"))

# ----------------------------------------------------------------------------------

def solution(input_string):

    shiftedWords = []
    digit = ""
    for char in input_string:
        if char.isdigit():
            digit += char
            skipNext = True
        elif digit and char.isalpha():
            shiftedWords.append(char + digit)
            digit = ""
            skipNext = False
        elif digit and skipNext:
            continue
        else:
            shiftedWords.append(char)
            
    if digit:
        shiftedWords.append(digit)       

    result = "".join(shiftedWords)

    return result


print(solution("I have 2 apples and 5! oranges and 3 grapefruits."))

# ----------------------------------------------------------------------------------

def add_seconds_to_times(timePoints, seconds):
    formattedTimes = []
    for timePoint in timePoints:
        timeParts = [int(part) for part in timePoint.split(":")]
        secondsSinceStart = timeParts[0] * 3600 + timeParts[1] * 60 + timeParts[2]
        totalSeconds = (secondsSinceStart + seconds) % (24 * 3600)
        hour, remainder = divmod(totalSeconds, 3600)
        minute, second = divmod(remainder, 60)
        print(hour, minute, second)
        formattedTimes.append(f"{hour:02d}:{minute:02d}:{second:02d}") 
    return formattedTimes


timePoints = ['10:00:00', '23:30:00']
added_seconds = 3600


print(add_seconds_to_times(timePoints, added_seconds))

# ----------------------------------------------------------------------------------

def time_period_length(time_period):
    times = [time.strip() for time in time_period.split("-")]
    totalSeconds = []

    for time in times:
        timeParts = [int(part) for part in time.split(":")]
        totalSecond = timeParts[0] * 3600 + timeParts[1] * 60
        totalSeconds.append(totalSecond)
    
    differenceSeconds = totalSeconds[1] - totalSeconds[0]
    minutes = differenceSeconds // 60
    return print(minutes)

time_period_length("12:15:30 - 14:00:00")  # should return 105

# ----------------------------------------------------------------------------------

def add_days(date, n):
    year, month, day = map(int, date.split("-"))

    # This approach is different from time changing into seconds due to leap years, instead
    # reduce n day by day and increase month and year. Second function to check leap_year
    while n > 0:
        DAYS_IN_MONTH = [0, 31, 29 if is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        day += 1
        n -= 1

        if day > DAYS_IN_MONTH[month]:
            day = 1
            month += 1

            if month > 12:
                month = 1
                year += 1


    return f"{year}-{month:02d}-{day:02d}"

# Second function: leap year is divisible by 4 but if is a century (divisible by 100)
# it is a leap century only if divisible by 400, therefore
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

date = '2099-12-31'
n = 50000

print(add_days(date, n))

# ----------------------------------------------------------------------------------

def solution(orig_string, substrs):
    result = []
    
    # zip() allows to create pairs between original string and substring
    for original, substring in zip(orig_string, substrs):
        # the string method find() allows to search for a substring in a string. 
        # It returns the lowest index at which substring appears, else -1
        startPosition = original.find(substring)
        matchIndices = []

        while startPosition != -1:
            matchIndices.append(str(startPosition))
            # find() can take a second argument for its starting index
            startPosition = original.find(substring, startPosition + 1)
    
        result.append(f"The substring '{substring}' was found in '{original}' at position(s) {', '.join(matchIndices)}.")  
    
    return "\n".join(result)

print(solution(["HelloWorld", "LearningPython", "GoForBroke", "BackToBasics"], ["loW", "ear", "o", "Ba"]))

# ----------------------------------------------------------------------------------

def replace_substring(text, old, new):
    oldText = text.split(old)
    newText = new.join(oldText)
    # replace() can be used as well, return text.replace(old, new)
    return newText


print(replace_substring("hello world, I love the world, amazing world", "world", "friend"))

# ----------------------------------------------------------------------------------

def solution(sentences, words):
    result = []
    for sentence, word in zip(sentences, words):
        sentence = sentence.replace(word, word[:][::-1])
        sentence = sentence.replace(word.capitalize(), word[:][::-1].capitalize())
        result.append(sentence)
    return result
    
    
print(solution(['this is a simple example.', 'the name is bond. James bond.', 'remove every single e'], ['simple', 'bond', 'e']))
print(solution(['lower case sentence', 'upper case Sentence', 'another Sentence here', 'final Sentence yay'], ['sentence', 'sentence', 'sentence', 'sentence']))

# ----------------------------------------------------------------------------------

def spot_swaps(source: str, target: str) -> list:
    result = []
    n = len(source)
    
    for i in range(n):
        if source[i] != target[i]:
            if i == n-1:
                continue
            elif source[i] == target[i+1] and source[i+1] == target[i]:
                result.append((i, source[i], target[i]))
    
    return result


print(spot_swaps("hello", "hlelo")) # [(1, 'e', 'l')]

print(spot_swaps("abcdef", "abcfed")) # []

print(spot_swaps("goodbye", "godobye")) # [(2, 'o', 'd')]

print(spot_swaps("firsttest", "firtestst")) # []

print(spot_swaps("pythonista", "pyhtonista")) # [(2, 't', 'h')]

print(spot_swaps("qwertyuiop", "qewrtyuiop")) # [(1, 'w', 'e')]

print(spot_swaps("hellothereworld", "helotlehreworld")) # [(6, 'h', 'e')]

# ----------------------------------------------------------------------------------

def spot_swaps(source: str, target: str) -> list:
    result = []
    n = len(source)
    
    if not n == len(target):
        return ["The words are not the same length."]
    
    for i in range(n):
        if i == n - 1:
            # out of range guard
            continue
        elif source[i] != target[i]:
            if source[i] == target[i+1] and source[i+1] == target[i]:
                result.append((i, source[i], target[i]))
    
    return result


print(spot_swaps("hello", "hlelo")) # [(1, 'e', 'l')]

print(spot_swaps("abcdef", "abcfed")) # []

print(spot_swaps("hellothereworld", "helotlehreworld")) # [(6, 'h', 'e')]

# ----------------------------------------------------------------------------------

def stringSearch(sourceArray, searchArray):
    result = []
    
    for i in sourceArray:
        for j in searchArray:
            indexSource, stringSource = (i[0], i[1])
            indexSearch, stringSearch = (j[0], j[1])
            
            if indexSource <= indexSearch and stringSearch.find(stringSource) != -1:
                result.append(i)
                break
            
    return result

print(stringSearch([(1, 'abc'), (2, 'def'), (3, 'ghi')], [(4, 'abcdefghi'), (5, 'defghiabc')]))
print(stringSearch([(1, 'var'), (2, 'ans'), (3, 'tes')], [(4, 'variant'), (5, 'answertest'), (6, 'tesla')]))
print(stringSearch([(1, 'ab'), (2, 'bc'), (3, 'cd')], [(4, 'abcd'), (5, 'bcda')]))

# ----------------------------------------------------------------------------------

# unit 2 ex 5
def solution(arr1, arr2):
    # TODO: Implement this function
    result = []
    for i in arr1:
        for j in arr2:
            if calculate_perfect_square((i + j)):
                result.append((i, j))
    return result
    

def calculate_perfect_square(num):
    # this math approach returns the original value only for perfect squares (else is 23.9999 etc)
    return True if int(num**0.5)**2 == num else False


print(solution([2,3,16], [1,9,10]))
# [(3, 1), (16, 9)]    
print(solution([0], [0]))
# [(0, 0)]
print(solution([4, 13, 23], [-4, -3, -24]))
# [(4, -4), (4, -3), (13, -4)]
print(solution([4, 13, 23], [-4, -3, -24]))
# [(4, -4), (4, -3), (13, -4)]  
print(solution([0, 1, 2, -100, 100], [-100, 100, 30, 0, -1, -2, -3]))
# [(0, 100), (0, 0), (1, 0), (1, -1), (2, -1), (2, -2), (-100, 100), (100, -100), (100, 0)
print(solution([100, 75, 36, 9, -25, -64, -100], [-1, 1, 24, 0, -1, -24]))
# [(100, 0), (36, 0), (9, 0)]
print(solution([],  [1, 2, 3, 4]))
# []
print(solution([1, 2, 3, 4], []))
# []
print(solution([], []))
# []

# ----------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------

