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


# NAIVE SOLUTION.
def solution(balloons: list) -> int:
    n = len(balloons)
    steps = 0
    i, j = 0, n - 1
    
    balloons_record = dict()
    for i in range(n):
        balloons_record[i] = balloons[i]

    # curr_balloons = dict()
    while True:
        balloons_record = {x for x in curr_balloons} if steps > 0 else balloons_record
        curr_balloons = dict() if steps < 1 else curr_balloons
        for i in range(n):
            # original balloons
            # balloons_record[i] = balloons[i]
            
            balloon_received = balloons_record[i] // 2
            balloon_sent = balloons_record[(i+1)%n] // 2
            # current ballons step
            curr_balloons[(i+1)%n] = balloons_record[(i+1)%n] + balloon_received - balloon_sent
        
        steps += 1

        curr_balloons = sorted(curr_balloons.items(), key=lambda item: item[0])
        for i, j in zip(balloons_record, curr_balloons):
            old_step = balloons_record[i]
            new_step = curr_balloons[j]
            if old_step != new_step:
                break
            else:
                continue
        else:
            return steps

balloons = [4, 1, 2]
print(solution(balloons)) # 3