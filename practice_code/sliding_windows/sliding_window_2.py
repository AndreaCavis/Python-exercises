'''
Given an array, find the maximum sum of k consecutive elements.
'''

def sliding_window(arr, k):
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]
    
    max_sum = window_sum
    n = len(arr)

    for i in range(k, n):
        window_sum -= arr[i-k]
        window_sum += arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


arr = [2, 5, 1, 8, 3]
k = 3
print(sliding_window(arr, k)) # 14