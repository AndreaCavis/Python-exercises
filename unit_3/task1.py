def solution(numbers):
    result = []
    n = len(numbers)
    obstacle_indices = find_obstacles(numbers)
    j = 0

    for i in range(n):
        if j < len(obstacle_indices):
            if i < obstacle_indices[j]:
                result.append(obstacle_indices[j])
            else:
                result.append(-1)
                if j < len(obstacle_indices):
                    j += 1
        else:
            result.append(numbers[i])
            
    return result
    

def find_obstacles(numbers):
    obstacles = []
    for i in range(len(numbers)):
        if numbers[i] < 0:
            obstacles.append(i)
    return obstacles


# output [2, 2, -1, 1, 2].
print(solution([3, 2, -3, 1, 2]))
#  output  [1, 2, 4, 4, -1, 8, 8, 8, -1, 4]
print(solution([1, 2, 3, 2, -3, 5, 2, 7, -1, 4]))







