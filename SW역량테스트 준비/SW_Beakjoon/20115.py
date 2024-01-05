N = int(input())
num = list(map(int,input().split(" ")))
answer = 0

num.sort()

for i in num:
    answer += i / 2
    #print(i / 2)
answer += num[-1] / 2
print(answer)