N = int(input())
dic = {}
for i in range(N):
    num = list(map(int,input().split(" ")))
    count = len(num) // 2 - 1 #3
    dic[num[0]] = []
    for j in range(1,count+1): #1,2,3
        dic[num[0]].append([num[j*2-1], num[j*2]]) #연결노드, 가중치
    print(dic)
#dfs구현해서 갈때마다 가중치 더해주기