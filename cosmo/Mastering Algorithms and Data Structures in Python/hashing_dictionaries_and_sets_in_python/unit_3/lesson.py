# https://codesignal.com/learn/course/10/unit/3

''' Problem 1: Array Intersection

Our journey begins with the challenge of identifying the intersection of two arrays. 
In other words, we aim to pinpoint the elements that appear in both of the given lists. 
It's important to note that we're interested in locating unique common elements
- even if an element appears more than once in both lists,
it should only feature once in our output.

Problem Actualisation:
To elucidate how this problem might emerge in a real-world scenario, presume that you're managing a database for a marketing company. 
You have two customer lists, each obtained through various marketing strategies. 
Your task is to determine the customers that both strategies successfully targeted. 
Essentially, these are the common elements in your two lists.

Naive Approach:
Suppose you decide to resolve this problem in the most uncomplicated way possible: for each customer (or element) on the first list, 
you verify if they're also present on the second list. Once you identify a match, you must confirm that this customer hasn't previously been added to your output. 
Though this solution would, in the end, yield the correct list of shared customers, it would demand a lot of computational resources, 
as you would be operating at a time complexity of O(n^2) due to the nested lookups - far from ideal!

Efficient Approach Explanation:
Here, the unique functionality of Python's set data structure proves beneficial. A set in Python, as you may remember, is an unordered collection of unique objects, 
ensuring the absence of duplicate values. Furthermore, it allows us to perform several operations on such collections, such as:
- intersection (identifying common elements)
- union (combining all unique elements)
- difference (detecting unique items in a set).

Solution Building:
Let's decompose the solution to this problem:

Initially, we convert our lists into sets using Python's built-in function set(). The syntax looks like this: set1 = set(list1). 
What this operation accomplishes is iterate through list1, add each element to set1, and ensure that no duplicates are added.

In the next step, we find the intersection of our newly formed sets using the ampersand operator (&), akin to this: intersection = set1 & set2. 
This operation sifts through set1 and set2 and appends only the common elements to intersection.

Finally, we convert our set back into a list employing the list() function and sort it with the sorted() function before returning it: return sorted(list(intersection)).

The final code piece ends up looking like this: '''

def array_intersection(list1: list, list2: list) -> list :
    set1, set2 = set(list1), set(list2)
    intersection = set1 & set2
    return sorted(list(intersection))

def array_intersection_optimised(list1: list, list2: list) -> list :
    intersection = set(list1) & set(list2)
    return sorted(list(intersection))

# output: [0,20,40,60,80]
print(array_intersection([x for x in range(0,100,10) if x % 20 == 0], [x*10 for x in range(10)]))



''' Problem 2: Non-Repeating Elements

Our next issue is slightly more complex. We must determine all elements in a given list that appear only once,
meaning they don't have any duplicates in the same list. 

Problem Actualisation:
To illustrate how this problem might arise in real life, consider analyzing a company's sales transactions. 
Your aim is to identify the products sold exactly once over a specific period. These could potentially be underperforming products that need investigation.

Naive Approach:
A naive method to resolve this pitfall would involve iterating over the list and, for every item, checking if it occurs anywhere else in the list. 
This method is not efficient as it results in a time complexity of O(n^2).

Efficient Approach Explanation:
A more efficient approach would employ a Python set, a built-in data structure that holds an unordered collection of unique elements. 
Sets provide constant time complexity for the add, remove, and search operations, making this data structure suitable for our problem.

Solution Building:
Here's how you would tackle this predicament:

- First, we create two sets, one for keeping track of the elements we've seen and another for the elements that have repeated.
- Next, we return a list with the elements in the seen set but not in the repeated set.
- Consequently, our final solution would look as follows: '''

def non_repeating_elements(nums: list) -> list:
    seen, repeated = set(), set()
    # Create two sets
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    #  return a list with the elements in the seen set but not in the repeated set
    return list(seen - repeated)



''' Problem 3: Unique Elements

The third problem compels us to find elements unique to each of the two given lists, i.e. given two lists, list1 and list2, 
we need to find elements that exist only in list1 and elements that exist only in list2, respectively.

Such a task might be beneficial if you possess two lists of employees from different company departments
and you wish to identify the employees unique to each department. 

Naive Approach:
An unsophisticated solution might involve combining the two lists and then scrutinizing each element to ascertain if it exists in the other list. 
However, such an approach would also culminate in a high time complexity, O(len(list1) * O(len(list2)) in particular.

Efficient Approach Explanation:
We can leverage Python's set operation to solve this problem more efficiently. 
Here, we'll utilize set difference, which presents us with the elements in the first set but not the second.

Solution Building:
A solution would resemble this:

- Initially, convert our lists into sets
- Afterward, perform the difference operation. We use the minus sign (-) to ascertain the difference between two sets:
- Finally, convert the resulting sets back into sorted lists and return them as a tuple: '''

def unique_elements(list1: list, list2: list) -> tuple[list, list]:
    # Convert our lists into sets
    set1, set2 = set(list1), set(list2)
    # Perform the difference operation AND Convert the resulting sets back into sorted lists
    unique_to_1 = list(sorted(set1 - set2))
    unique_to_2 = list(sorted(set2 - set1))
    # Return the sorted lists as a tuple
    return (unique_to_1, unique_to_2)
    