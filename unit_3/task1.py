def solution(numbers):
    result = []
    n = len(numbers)

    for i in range(n):
        if numbers[i] < 0:
            result.append(-1)
            continue

        end_range = min(i + 1 + numbers[i], n)
        obstacle = None

        for j in range(i + 1, end_range):
            if numbers[j] < 0:
                obstacle = j
                break

        if obstacle is not None:
            result.append(obstacle)
        else:
            result.append(numbers[i])

               
    return result
    

# def find_obstacles(numbers):
#     obstacles = []
#     for i in range(len(numbers)):
#         if numbers[i] < 0:
#             obstacles.append(i)
#     return obstacles


# output [2, 2, -1, 1, 2].
print(solution([3, 2, -3, 1, 2]))
#  output  [1, 2, 4, 4, -1, 8, 8, 8, -1, 4]
print(solution([1, 2, 3, 2, -3, 5, 2, 7, -1, 4]))







