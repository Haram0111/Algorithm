N = int(input())

answer = 0
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)
    answer += a
# print(answer)
lst.sort(reverse=True)
# print(lst)
for i in range(1,len(lst)//3 + 1):
    answer -= lst[i*3 - 1]
print(answer)