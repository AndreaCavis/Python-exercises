def solution(board, obstacle):
    moves = []
    n = len(board)
    
    for i in range(n):
        move = 0
        position = i
        
        if board[position] == obstacle:
            moves.append(-1)
            continue
        # THIS WORKS
        while position < n:
            next_position = position + board[position]
            
            if next_position >= n:
                moves.append(move + 1)
                position += board[position]
                continue
            else:
                if board[next_position] == obstacle:
                    moves.append(-1)
                    break
                position += board[position]
                move += 1

    return moves

#  output: [3, -1, 3, 1, 2, 2, 1]
print(solution([5, 3, 2, 6, 2, 1, 7], 3))


