arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = 	[[3, 3], [3, 3]]
answer = []
for i in arr1:
    for j in i:
        for k in range(len(arr2[0])):
            print(k)
        print(j)
    print("------")
#    for j in range(len(arr1[i])):
#        for k in range(len(arr2[j])):
#            answer.append(arr1[i][j] * arr2[k][j])
print(answer)
#[[15, 15], [15, 15], [15, 15]]