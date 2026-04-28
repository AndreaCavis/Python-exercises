'''
TWO SUM SORTED (OPPOSITE DIRECTION) - Given a sorted array and a target sum, return the indices of the two numbers that add up to the target sum.

solution = the key to the solution is that the array is SORTED, meaning that the LEFT pointer will start from small values and R from the big ones.
           in order to check how to move the pointers, you check the sum of the current values 
           (num[l] and num[r]) to establish which pointer should move:
           if sum > target, move r left.    if sum < target, move l right.    if sum == target, return the indices.
'''

def two_pointers_opposite_direction(arr, target):
    left, right = 0, len(arr) - 1
    result = []

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            result.append(left)
            result.append(right)
            return result
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
    return [-1, -1] # no matches found

print(two_pointers_opposite_direction([1, 2, 3, 4, 6], 6)) # [1, 3]
print(two_pointers_opposite_direction([2, 3, 4, 5, 8, 11, 18], 8)) # [1, 3]
