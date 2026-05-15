def solution(arrayA, arrayB):
    idx_a, idx_b = 0, 0
    in_arrayA = True
    visited_arrayA = set()
    visited_arrayB = []

    while True:
        if in_arrayA:
            idx_b = arrayA[idx_a] - 1
        else:
            idx_a = arrayB[idx_b] - 1
            if idx_a in visited_arrayA:
                return visited_arrayB
            else:
                visited_arrayB.append(idx_b + 1)
                visited_arrayA.add(idx_a)

        in_arrayA = not in_arrayA


arrayA = [1, 3, 2, 5, 4]
arrayB = [5, 4, 3, 2, 1]

print(solution(arrayA, arrayB)) #  [1, 4, 3, 2, 5]