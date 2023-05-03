N, M = map(int,input().split(" ")) #N은 폴더 개수, M은 파일 개수
dic = {'main' : []}
for i in range(N+M):
    route1, route2, C = input().split(" ")
    if C == '1':
        dic[route2] = []
        dic[route1].append(route2)
    else:
        dic[route1].append(route2)
    print(dic)
K = int(input()) #A -> B의 경로가 주어짐
for i in range(K):
    move, to = input().split(" ")
    move = move.split("/")[1]
    to = to.split("/")[1]
    for i in range(len(dic[move])):
        if dic[move][i] not in dic[to]:
            dic[to].append(dic[move][i])
    print(dic)
Q = int(input()) #쿼리 개수
for i in range(Q):
    route = input().split("/")[-1]
    kind, count = 0, 0
    for i in dic[route]:
        print(i)

