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



'''
'''
