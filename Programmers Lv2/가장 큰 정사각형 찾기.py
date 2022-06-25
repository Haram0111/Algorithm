def solution(board):
    max = 0
    for i in range(1,len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                abx = min(board[i-1][j],board[i][j-1],board[i-1][j-1])
                board[i][j] += abx
                if board[i][j] > max:
                    max = board[i][j]
    if board[0][0] == 1 and max == 0:
        max = 1
            
    return max*max