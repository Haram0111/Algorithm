# n = int(input())
# num = list(map(int,input().split()))
# num.sort()
# x = int(input()) #목표값

# count = 0
# interval_sum = 0
# end = 0

# for start in range(n):
#     while interval_sum < x and end < n:
#         interval_sum += 1
#         end += 1
#     if interval_sum == x:
#         count += 1
#     interval_sum -= num[start]

# print(count)
n = 9 # 데이터의 개수 N
m = 13 # 찾고자 하는 부분합 M
data = [5, 12, 7, 10, 9, 1, 2, 3, 11] # 전체 수열

count = 0
start = 0
end = 0

# start를 차례대로 증가시키며 반복
while start <= end:
    interval_sum = data[start] + data[end]
    # end를 가능한 만큼 이동시키기
    if interval_sum < m and start != end:
        end += 1
    elif interval_sum > m and start != end:
        start += 1
    # 부분합이 m일 때 카운트 증가
    elif interval_sum == m and start != end:
        count += 1
    else:
        start += 1
if data[start] + data[end] == m:
    count += 1

print(count)