'''Understanding Hash Tables

As we delve into the world of hash tables, let's start by understanding their underlying structure. 
A hash table consists of an array (the actual table where data is stored), coupled with a hash function. 
The hash function plays a crucial role - it takes the keys as input and generates an index,
mapping keys to different slots or indices in the table.

Each index of the array holds a bucket that ultimately contains the key-value pair. The pairing of keys with values enhances the data retrieval process.
The efficiency of retrieving values depends on the hash function's ability to distribute data across the array uniformly.

You can also think of hash tables as hash sets storing tuples of (key, value), 
but this particular interface makes it less easy to use, so Python has a concept of dictionaries we will cover below.

Let's visualize this with a Python dictionary, which operates on the same principle. 
Suppose we have a dictionary containing student names as keys and their corresponding scores as values: '''

# A simple dictionary illustrating the principle of hashing
student_scores = { 'Tom': 85, 'Serena': 92, 'Alex': 78, 'Nina': 88 }

# printing the scores
for student, score in student_scores.items():
    print(f"{student}: {score}")

# Outputs:
# Tom: 85
# Serena: 92
# Alex: 78
# Nina: 88 

''' In this example, 'Tom', 'Serena', 'Alex', and 'Nina' are keys, while 85, 92, 78, and 88 are their associated values. 
Under the hood, the Python interpreter uses a hash function to assign each key-value pair to a unique address in memory. '''



'''Collision Handling in Hash Tables

There are instances when two different keys produce the same index after being processed through the hash function. 
This situation is known as a collision. When a collision occurs, 
we are faced with a dilemma - where do we store the new key-value pair since that index is already occupied?

Here are two common strategies to handle such scenarios:

1. Chaining: 
    In this method, each index (or bucket) in the array hosts a linked list of all key-value pairs that hash to the same index. 
    When a collision occurs, we simply go to the collided index and append the new key-value pair to the existing linked list.

2. Open Addressing: 
    Upon encountering a collision, the hash table searches for another free slot or index in the table (possibly the next available empty slot)
    and assigns that location to the new key-value pair. This approach requires a suitable probing strategy to ensure efficient use of table space. 
    
The image below provides a visual example of Chaining collision resolving method (// you'll have to imagine this one) 
John Smith and Sandra Dee have the same hash function result, so their entries are organized in a linked list in the corresponding bucket.

(basically 5 names are stored in different buckets, each index marked with an integer. Both John Smith and Sandra Dee share the index 152.
Therefore, when accessing 152, you'll find a linked list with both values, at least in this image example)
'''


'''Time and Space Complexity Analysis for Hash Tables

Hash tables are renowned for their efficiency and speed when it comes to data storage and retrieval. 
They boast constant time complexity O(1) for the operations on key-value pairs - insertion, deletion, and retrieval. 
This efficiency comes from a good hash function, which allows for keys to be uniformly distributed across the table 
and accessed directly via their indices, eliminating the need to scan through unnecessary slots.

Although hash tables generally perform robustly, situations may arise where frequent collisions occur. 
Such situations could deteriorate the table's efficiency and extend the time complexity to a worst-case scenario of O(n), 
where n is the number of keys hashing to the same index. '''


