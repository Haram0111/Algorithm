arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = 	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
lst = [[] for _ in range(len(arr1))]
for i in range(len(arr1)): #3번 줄반복
    for j in range(len(arr1[i])): #2번반복
        sum = 0
        for k in range(len(arr2[0])): #2번 반복
            a = arr1[i][k] * arr2[k][j]
            sum += a
        lst[i].append(sum)
print(lst)