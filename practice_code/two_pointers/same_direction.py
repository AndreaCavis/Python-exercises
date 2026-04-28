'''
REMOVE DUPLICATES (SAME DIRECTION) - The goal is to remove duplicates in a SORTED array in place, directly modifying the input array
                                     such that all unique elements appear at the front of the array.

solution = the key here is the same, the array is SORTED. 
            SLOW and FAST start next to each other. If num[slow] == num[fast] (i.e. duplicates), FAST moves forward.
            if num[slow] != num[fast], SLOW moves forward and the value at FAST is copied to SLOW.
            This cycle repeats unutil FAST is done traversing the array. The result will be that all values up to SLOW are unique.
'''

def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow, fast = 0, 1

    while fast < len(arr):
        if arr[slow] == arr[fast]:
            fast += 1
        else:
            slow += 1
            arr[slow] = arr[fast]

    return arr[:slow + 1]


print(remove_duplicates([1, 1, 2, 2, 3])) # [1,2,3]
print(remove_duplicates([1, 1, 1, 2, 2, 3, 3, 4, 5]))
