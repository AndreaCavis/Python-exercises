'''
TWO SUM SORTED (OPPOSITE DIRECTION) - Given a sorted array and a target sum, return the indices of the two numbers that add up to the target sum.

solution = the key to the solution is that the array is SORTED, meaning that the LEFT pointer will start from small values and R from the big ones.
           in order to check how to move the pointers, you check the sum of the current values 
           (num[l] and num[r]) to establish which pointer should move:
           if sum > target, move r left.    if sum < target, move l right.    if sum == target, return the indices.
'''


