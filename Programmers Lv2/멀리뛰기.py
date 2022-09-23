def solution(n):
    lst = [1,2]
    if n >= 3:
        for i in range(n-2):
            lst.append(lst[-1]+lst[-2])
        return lst[-1] % 1234567
    else:
        return lst[n-1] % 1234567
