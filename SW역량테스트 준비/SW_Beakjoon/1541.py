num = input()
num = num.split("-")

answer = []

for i in num:
    a = 0
    tmp = i.split("+")
    for j in tmp:
        a += int(j)
    answer.append(a)

n = answer[0]

for i in range(1,len(answer)):
    n -= answer[i]
print(n)