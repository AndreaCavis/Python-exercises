def solution(board, obstacle):
    moves = []
    n = len(board)
    
    for i in range(n):
        move = 0
        position = i
        
        if board[position] == obstacle:
            moves.append(-1)
            continue

        while position < n:
            move += 1
            next_position = position + board[position]
            
            if next_position >= n:
                moves.append(move)
                position += board[position]
                continue
            else:
                if board[next_position] == obstacle:
                    moves.append(-1)
                    break
                position += board[position]

    return moves



#  output: [3, -1, 3, 1, 2, 2, 1]
print(solution([5, 3, 2, 6, 2, 1, 7], 3))


