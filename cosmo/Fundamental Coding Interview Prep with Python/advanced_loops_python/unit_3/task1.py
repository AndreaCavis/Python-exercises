'''
You are given an array of n integers, ranging from 1 to 100 inclusive.
Each integer represents a player's progress on a linear gameboard, indicating how many steps they can move to the right.
However, the course is fraught with challenges; there exist several obstacles, represented by negative integers.

Your task is to return a transformed array structuring the gameboard in a new way:
if an integer can lead the player to an obstacle on its right (within the range of its value), replace the number with the index of the obstacle.
If the number represents an obstacle (a negative integer), replace it with -1. If none of these conditions are met, retain the original integer.

Keep in mind, this task is an innovative take on our previous analysis lesson, implementing a "Move Until Obstacle" game.
Remember, your array will have no more than 500 elements, and the elements in the array range from -100 to 100, inclusive.
Good luck with your coding journey!

For instance, given an array [3, 2, -3, 1, 2], the output would be [2, 2, -1, 1, 2].

Here's how it works:

- Replace the first position with 2 because a player at the first position can move 3 steps but will hit the obstacle at the 2nd index.
- Replace the second position with 2 because a player at the second position can move 2 steps but will hit the obstacle at the 2nd index.
- Replace the negative number -3 at the third position with -1 because it represents an obstacle.
- Keep the number 1 at the fourth position as there are no obstacles in its range.
- Keep the number 2 at the fifth position as there are no further positions or obstacles to impact it.
'''

def solution(numbers):
    result = []
    n = len(numbers)
    
    # for loop not while because I needed to potentially update each value at a time
    for i in range(n):
        current_position = numbers[i]
        
        if current_position < 0:
            result.append(-1)
            continue
            
        start = i + 1
        finish = min(start + current_position, n)
        obstacle = None
        
        # check if steps from current_position land on obstacle
        for j in range(start, finish):
            if numbers[j] < 0:
                obstacle = j
                break
        #if they do, obstacle will be the index to replace the numbers[i] with  
        if obstacle is not None:
            result.append(obstacle)
        else:
            # steps don't land in obstacle, append current value
            result.append(current_position)
      
    return result


# output [2, 2, -1, 1, 2].
print(solution([3, 2, -3, 1, 2]))
#  output  [1, 2, 4, 4, -1, 8, 8, 8, -1, 4]
print(solution([1, 2, 3, 2, -3, 5, 2, 7, -1, 4]))







