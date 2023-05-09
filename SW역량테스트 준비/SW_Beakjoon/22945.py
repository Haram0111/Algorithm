N = int(input())
lst = list(map(int,input().split(" ")))
answer = 0
start = 0
end = len(lst) - 1
while start <= end:
    answer = max(answer, (end-start-1) * min(lst[start], lst[end]))
    if lst[start] > lst[end]:
        end -= 1
    else:
        start += 1
print(answer)
#최댓값이 나오려면 min이 크거나 사이에 있는 값이 많아야한다
#사이에 있는 값이 많아야한다 = end와 Start사이에 거리가 멀수록 좋다
#min 값이 클수록 좋다 = 둘 다 움직일 수 있다면 둘 중에 작은게 움직이는게 좋지 않을까? -> 계속해서 이동!