N = int(input())
mapping = []
cnt = 0
for i in range(N):
    x, y, d, g = map(int, input().split())
    mapping.append((x, y))
    lst = [d]
    for j in range(g):
        lst_copy = lst.copy()
        for k in range(len(lst_copy)):
            lst_copy[k] = (lst_copy[k] + 1) % 4
        lst_copy.reverse()
        lst += lst_copy
    for j in range(len(lst)):
        if lst[j] == 0:
            x += 1
        elif lst[j] == 1:
            y -= 1
        elif lst[j] == 2:
            x -= 1
        else:
            y += 1
        mapping.append((x, y))
#print(mapping) #모든 좌표 단계별 출력
mapping_set = list(set(mapping))
#print(mapping_set)
for i in range(len(mapping_set)):
    if (mapping_set[i][0], mapping_set[i][1]+1) in mapping_set and (mapping_set[i][0]+1, mapping_set[i][1]) in mapping_set and (mapping_set[i][0]+1, mapping_set[i][1]+1) in mapping_set:
        cnt += 1
print(cnt)