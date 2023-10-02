#트리를 잘 알고있냐? 에 대한 문제로 위에서 아래로 가야하고, 겹치는 부분이 없어야한다.
#자식은 n개를 가질 수 있지만 부모는 항상 1명을 가져야한다.
#그렇다면 자식을 list에 넣는것이 아닌 부모를 list에 넣어 길이가 1이 아니라면 삭제 시켜보자

cnt = 0

while True:
    tree = True
    parent, child = map(int,input().split())
    if parent == -1 and child == -1:
        break
    board = {}
    board[child] = []
    board[child].append(parent)
    print(board)
    while True:
        parent, child = map(int,input().split())
        if child == 0 and parent == 0:
            cnt += 1
            break
        if child not in board:
            board[child] = []
        board[child].append(parent)
        print(board)
    for i in board:
        if len(board[i]) != 1:
            tree = False
            break
    if tree == False:
        print(f"Case {cnt} is not a tree")
    else:
        print(f"Case {cnt} is a tree")