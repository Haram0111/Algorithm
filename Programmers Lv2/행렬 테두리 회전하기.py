def solution(rows, columns, queries):
    hp = []
    answer = []
    for i in range(rows):
        lst = []
        for j in range(columns):
            lst.append(i * columns + j + 1)
        answer.append(lst)
    for i in queries:
        ly, lx = i[0]-1, i[1]-1
        ry, rx = i[2]-1, i[3]-1
        init = answer[ly][lx]
        a = init
        print(ly, lx, ry, rx) # 2 2 5 4 >> 1 1 4 3
        for j in range(ly,ry):
            answer[j][lx] = answer[j+1][lx]
            a = min(a, answer[j][lx])
        for j in range(lx,rx):
            answer[ry][j] = answer[ry][j+1]
            a = min(a, answer[ry][j])
        for j in range(ry,ly,-1):
            answer[j][rx] = answer[j-1][rx]
            a = min(a, answer[j][rx])
        for j in range(rx,lx,-1):
            answer[ly][j] = answer[ly][j-1]
            a = min(a, answer[ly][j])
        answer[ly][lx+1] = init
        hp.append(a)
    return hp
    