from itertools import combinations
N = int(input())
for i in range(N):
    left_num, right_num = map(int,input().split(" "))
    print(combinations(range(1,right_num),left_num))
