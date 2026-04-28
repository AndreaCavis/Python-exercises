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







