'''
Imagine a medieval tournament where knights participate in jousting matches.
The knights are arranged in a circular formation (represented as an array in your program),
and each knight is initially assigned strength, represented as integers from 1 to 100, determined randomly.

The game consists of rounds. On each round, each knight fights the knight on his right side
by subtracting the strength of his opponent from his own.
Since this is a circular game, the knight on the right side of the last knight in the array is the first knight.
Note that all matches are played in parallel, so the strengths are updated only after all matches are played. 
If after a match, a knight's strength becomes equal to or less than zero, symbolizing the knight's defeat, 
the knight is removed from the game in the next round.

The game continues until a situation develops in which no more moves can be made. 
This happens either when there is just one knight standing or all remaining knights have equal strength meaning no knight can win a match.

Given the list of knights' strengths in the initial order, your program should calculate the number of rounds in the tournament.
'''


def tournament(knights: list[int]) -> int:
    rounds = 0

    while True:
        n = len(knights)
        rounds += 1
        new_knights = []

        for i in range(n):
            damage = knights[(i + 1) % n] - knights[i]
            if knights[i] - damage > 0:
                new_knights.append(knights[i])
            
        if len(new_knights) <= 1:
            break

        knights = new_knights

    return rounds

# output: 3
print(tournament([100, 50, 30, 20]))


