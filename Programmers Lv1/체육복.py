def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    check = ['F'] * len(reserve) #빌려준 사람의 list
    stu = ['T'] * n #모든학생이 옷을 가지고 있다고 가정
    for i in lost:
        stu[i-1] = 'F' #안가져온 학생은 T로 나타냄
    for i in lost: #여벌옷이 있는데 도난당하면 내 옷부터 챙김
        for j in range(len(reserve)):
            if i == reserve[j]:
                stu[i-1] = 'T'
                check[j] = 'T'
    for i in lost: #여벌옷있는데 도난안당하면 도와줄 수 있음
        for j in range(len(reserve)):
            if i - 1 == reserve[j] and check[j] == 'F' and stu[i-1] == 'F':
                check[j] = 'T'
                stu[i-1] = 'T'
            elif i + 1 == reserve[j] and check[j] == 'F' and stu[i-1] == 'F':
                check[j] = 'T'
                stu[i-1] = 'T'
    return stu.count('T')