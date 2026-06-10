'''
In a unique town, there's a popular game that involves the town's houses and their numbers. What's special about this town is that each house is sequentially numbered from 1 to n. The game is played based on an interesting rule regarding these house numbers.

At each step of the game, every house number must "donate" one of its digits to the house on its right (or to the first house in the case of the last house). The particular digit to be transferred in each step is determined by the current game step: during the i-th step, the i-th digit from the right of each house number (1-indexed) is transferred. If a house number doesn't have the specified number of digits for a step, it doesn't donate any digit in that step.

During the transfer, the chosen digit is removed from its position in the donor house number and then added to the front (leftmost side) of the receiving house number. All numbers change simultaneously.

The function, house_game(houses), should simulate each step of the game, starting from transferring the rightmost (1st digit) and proceeding one digit position towards the left in each successive step, until there is no change in the house numbers from one step to the next. It should return the sequence of house numbers at the end.

It is guaranteed that there are at least two houses and there is no digit 0 in the numbers.

For instance, if houses = [123, 234, 345, 456], the function performs as follows:

Step 1 -> Transfer the 1st digit from the right (rightmost digit):

Before Transfer:

House 1: 123
House 2: 234
House 3: 345
House 4: 456
Digit Transfer:

Transfer '3' from House 1 to the front of House 2
Transfer '4' from House 2 to the front of House 3
Transfer '5' from House 3 to the front of House 4
Transfer '6' from House 4 to the front of House 1
After Transfer: [612, 323, 434, 545]

Step 2 -> Transfer the 2nd digit from the right:

Before Transfer:

House 1: 612
House 2: 323
House 3: 434
House 4: 545
Digit Transfer:

Transfer '1' from House 1 to the front of House 2
Transfer '2' from House 2 to the front of House 3
Transfer '3' from House 3 to the front of House 4
Transfer '4' from House 4 to the front of House 1
After Transfer: [462, 133, 244, 355]

Step 3 -> Transfer the 3rd digit from the right (leftmost digit):

Before Transfer: [462, 133, 244, 355]

After Transfer: [362, 433, 144, 255]

In Step 4, no further changes occur, so the final output is [362, 433, 144, 255].

This sequence of transformations leads to the final set of house numbers, [362, 433, 144, 255].
'''


def house_game(houses):
    # TODO: implement
    pass