def evaluatePath(numbers):
    n = len(numbers)
    position, moves = 0, 0
    total_reversals = 2
    opposite_direction = False
    # "position < n" guards against index out of range
    while position < n:
        value = numbers[position]
        # if 0, game ends
        if value == 0:
            return (position, moves)
        
        if opposite_direction:
            value = -value

        next_position = position + value

        if next_position < 0 or next_position >= n:
            opposite_direction = not opposite_direction
            total_reversals -= 1
            # second touch of list border, game ends
            if total_reversals == 0:
                return (position, moves)
            continue
        else:
            position += value

        moves += 1

    return (position, moves)