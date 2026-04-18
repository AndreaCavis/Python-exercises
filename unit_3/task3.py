def solution(board, obstacle):
    moves = []
    n = len(board)
    
    for i in range(n):
        move = 0
        
        if board[i] == obstacle:
            moves.append(-1)
            continue
        
        while i < n:
            next_position = i + board[i]
            
            if next_position == obstacle:
                moves.append(-1)
                break
                # i += board[i]
                # continue
            
            if next_position > n:
                moves.append(move + 1)
                i += board[i]
                continue
            else:
                i += board[i]

            move += 1
    return moves


#  output: [3, -1, 3, 1, 2, 2, 1]
print(solution([5, 3, 2, 6, 2, 1, 7], 3))


