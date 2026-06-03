'''
You are given an array of n integers, where 1 <= n <= 500. The array represents a path through a dungeon.
Each value is a trap power in the range [-10^10, 10^10]. Positive values reduce your health, and negative values increase it.

You start at index 0 (the first element) and want to move to the right end of the array.
Choose a fixed step size x where 1 <= x <= n. You then visit indices 0, x, 2x, 3x, ... until the next step would go past the last index.
Each visited value is added to your total loss, and your health is updated as health -= value at each step.
If your health ever becomes 0 or less, that x is invalid.

Find the x that maximizes your remaining health.

--------------------------------------------------------
Example

Input:
- Array of trap powers: [0, 5, -2, 8, 3, 0, 10, 4, -1, 7]
- Initial health: 20

Example reasoning:
- x = 1 visits all indices; total loss is 34, so you loose all your health before finishing.
- x = 8 visits indices 0 and 8; total loss is -1, so remaining health is 21.
- x = 10 visits index 0 only; total loss is 0, so remaining health is 20.

The best choice is x = 8, because it leaves you with the most health.

Output:
- Optimal step size (x): 8
- Maximum remaining health: 21
'''


def solution(dungeon, health):
    # TODO: Implement the solution
    pass

