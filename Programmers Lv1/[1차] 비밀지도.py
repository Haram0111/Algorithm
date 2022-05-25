def solution(n, arr1, arr2):
    map1 = [[] for i in range(n)]
    for i in range(len(arr1)):
        a = format(arr1[i],"b")
        while len(a) < n:
            a = "0" + a
        for j in range(n):
            if a[j] == "0":
                map1[i].append(" ")
            elif a[j] == "1":
                map1[i].append("#")
    for i in range(len(arr2)):
        a = format(arr2[i],"b")
        while len(a) < n:
            a = "0" + a
        for j in range(n):
            if a[j] == "1":
                map1[i][j] = "#"
    for i in range(len(map1)):
        map1[i] = "".join(map1[i])
    return map1