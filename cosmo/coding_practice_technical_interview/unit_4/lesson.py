'''
Consider an array which symbolizes a dense forest; each index is either 1, indicating a tree, or 0, signifying a clear position.
Starting from a fixed initial index and given a specific direction, 
your objective is to ascertain the smallest possible jump size that enables traversal from the initial position to one of the ends of the array without hitting a tree.
Each move you make will be exactly the determined jump size in the given direction.

Keep these pointers in mind:

- The array of binary integers (0 and 1) depicts the forest.
- The journey will always commence from a 0 index.
- The direction is an integer. 1 implies jumping toward larger indices, while -1 denotes jumping toward smaller ones.
- In situations where there is no jump size that can avoid all trees, 
  return -1 to indicate the impossibility of traversal under these conditions.
- The ultimate objective? Identify the minimal jump size that ensures a smooth navigation through the entire forest without hitting a single tree.

------------------------------------------------------
Example

For the input values forest = [0, 1, 0, 0, 0, 0, 1, 1], start = 0, and direction = 1, the output should be 4.

- If you take the jump size equal to 1, you immediately step on a tree.
- If you choose 2, you step on a tree after three jumps at forest[6].
- If you choose 3, you again step on a tree at forest[6].
- For the jump size equal to 4, you first jump to the 4th position which is a valid position,
  then jump outside of the array, thereby traversing the forest without hitting a tree.
'''


# SOLUTION
def calculate_jump(forest, start,direction):
    jump = 1

    # direction * jump to handle positive AND negative directions
    while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
        pos = start
        # this is a WHILE/ELSE construct. Python "exclusive".
        # the else condition begins when the loop ends without break 
        while 0 <= pos < len(forest):
            if forest[pos] == 1:
                break
            pos += direction * jump
        else:
            return jump
    
        jump += 1
    return -1


# ------------------------- NAIVE SOLUTION -----------------------------------------

# This solution doesn't handle direction -1, therefore it is incomplete and wrong
def calculate_jump_naive(forest, start, direction):
    n = len(forest) - 1

    if forest[start] == 1:
        return -1

    for jump in range(1, n, direction):
        i = start
        while i < n:
            current_step = forest[i]
            if current_step == 1:
                break

            i += jump
            if i > n:
                return jump
    
    return -1


forest = [0, 1, 0, 0, 0, 0, 1, 1]
start = 0
direction = 1

print(calculate_jump_naive(forest, start, direction)) # output: 4
print(calculate_jump(forest, start, direction)) # output: 4