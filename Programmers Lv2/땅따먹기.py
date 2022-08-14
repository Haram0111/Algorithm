land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
sum_lst = []

for i in range(len(land[0])): #1,2,3,5 반복
    pre_index = i
    sum = land[0][i]
    for j in range(1,len(land)): #행 반복
        if land[j].index(max(land[j])) == pre_index: #현재 1이면 index 1이 되면 안됨
            for n in land[j]:
                if n < max(land[j]):
                    second = min(land[j])
                    if n > second:
                        second = n
            sum += second
            pre_index = land[j].index(second)
            print(f"{sum},{pre_index}")
        else:
            sum += max(land[j])
            pre_index = land[j].index(max(land[j]))
            print(f"{sum},{pre_index}")
    print(f"{i} 번째 입니다.")
    sum_lst.append(sum)
print(max(sum_lst))