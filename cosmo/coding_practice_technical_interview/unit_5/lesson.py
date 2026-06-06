'''
Picture a quaint, small town where every house is numbered sequentially from 1 to n. One day, a festive town event is held, and balloons are tied to each house.
The festivities do not end there. At the conclusion of the event, a fun game is played:
at each step of the game, each house sends half of its balloons to the neighboring house simultaneously 
(the neighbor on the right side, and for the last house, the neighbor is the first house). 
The game goes on until at some step there are no changes in the amount of balloons compared to the previous step.

The task is to create a Python function, solution(balloons), where balloons is a list representing the number of balloons at each house. 
The function should simulate this game and return the number of steps in the game.

For example, if balloons = [4, 1, 2], the output should be solution(balloons) = 3.
- After the first step, the list becomes [3, 3, 1]. 
  This is because the first house sends 2 balloons and gets 1, the second house sends nothing but gets 2, and the third house sends 1 but receives nothing.
Note that when the number of balloons x is odd, than the house sends (x - 1) / 2 balloons. 
- After the second step, the list becomes [2, 3, 2] and never changes after that.
- So after the third step, the process finishes.
'''

'''
new_balloon += curr_balloons
x % n new position
'''

'''
NOTE: array.copy() creates a new SHALLOW COPY of array. shallow copy means a new list object with same elements,
      whilst being different lists in memory. Shallow copy means that only the top-level is copied, so if the content
      of the top level are other inner lists, those will be affected by the change when they are applied directly to the content,
      e.g.: .append(), .extend(), .sort()

      A completely indipendent copy can be obtained through new_arr = copy.deepcopy(arr), however you must import copy   
'''


# NAIVE SOLUTION.
def solution(balloons: list) -> int:
    steps = 0
    while True:
        steps += 1
        # copy() is what I was trying to organise in my naive attempt without knowing about this built in function
        new_balloons = balloons.copy() # store updated balloon counts
        # TODO: share the balloons
        if new_balloons == balloons:
            break
        balloons = new_balloons

    return steps


balloons = [4, 1, 2]
print(solution(balloons)) # 3