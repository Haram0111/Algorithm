N = input()
answer = False
length = len(N)
for i in range(int(N)):
    start = i
    sum = 0
    sum += i
    for j in range(length-1,-1,-1):
        sum += start // (pow(10,j))
        start = start - (start // (pow(10,j)))*pow(10,j)
    if sum == int(N):
        print(i)
        answer = True
        break

if answer == False:
    print("0")