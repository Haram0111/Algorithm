from itertools import permutations

def check(x):
    for i in range(2,x//2 + 1):
        if x % i == 0:
            return 0
    return 1

def solution(numbers):
    cnt = 0
    for i in range(1,len(numbers)+1):
        a = list(set(permutations(numbers, i)))
        for j in range(len(a)):
            a[j] = list(a[j])
            a[j] = ''.join(a[j])
            if int(a[j]) >= 2 and a[j][0] != '0':
                if check(int(a[j])) == 1:
                    cnt += 1
    return cnt