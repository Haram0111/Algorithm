N = int(input())
dic = {}
num_lst = []
for i in range(N):
    x, y = map(int,input().split(" "))
    dic[x,y] = 0
for i in dic:
    for j in dic:
        if i[0] > j[0] and i[1] > j[1]:
            dic[i] += 1
print(dic)
