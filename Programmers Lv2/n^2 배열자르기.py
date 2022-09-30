def solution(n, left, right):
    #arr = [[0 for i in range(n)] for j in range(n)]
    lst = []
    cnt = -1
    start_idx_x = left % n
    start_idx_y = left // n
    for i in range(right-left+1):
        if start_idx_x > n-1:
            start_idx_x = 0
            start_idx_y += 1
        if start_idx_x > start_idx_y:
            lst.append(start_idx_x+1)
        else:
            lst.append(start_idx_y+1)
        start_idx_x += 1    
    return lst