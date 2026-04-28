def solution(numbers, obstacle):
    position, moves= 0, 0

    while position < len(numbers):
       steps = numbers[position]
       if steps == obstacle:
           return position
       moves += 1
       position += steps

    return moves


numbers = [2, 3, 3, 4, 2, 4]
obstacle = 4
# output: 5
print(solution(numbers, obstacle))

numbers2 = [4, 1, 2, 2, 4, 2, 2]
obstacle2 = 2
# output: 2
print(solution(numbers2, obstacle2))