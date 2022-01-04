def dfs(start,start_1):
    global o_cnt, v_cnt
    maplst[start][start_1] = 1 #현재 내가 있는 곳을 1로 바꾸겠다.
    for i in lst[start]: #내가 연결되어 있는 곳을 찾는거임
        for j in lst[i]:
            if maplst[i][j]==0: #어디로 가는지 정하는건데 0으로 가는거임 근데 이렇게 되면 횟수가 많아질 수 있음
                if maplst[i][j] == 'v':
                    v_cnt += 1
                    maplst[i][j] = 1
                elif maplst[i][j] == 'o':
                    o_cnt += 1
                    maplst[i][j] = 1
                else:
                    maplst[i][j] = 1         
                dfs(maplst[i][j])
#. = 빈필드 # 울타리 o 양 v 늑대
#R 가로 C 세로
#아침에 살아남은 양과 늑대를 순서대로 출력
R, C = map(int,input().split())
maplst = [[0]*C for _ in range(R)] #0과 1 방문list
lst = [] #입력 값
for i in range(R):
    a = input()
    lst.append(list(a))
for i in range(R):
    for j in range(C):
        if lst[i][j] == '#':
            maplst[i][j] = 1
ALL_v_cnt = 0
ALL_o_cnt = 0
o_cnt = 0
v_cnt = 0
dfs(0,0)