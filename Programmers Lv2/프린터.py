from collections import deque

def solution(priorities, location):
    cnt = 0
    priorities = deque(priorities)
    check = [False] * len(priorities)
    check[location] = True
    check = deque(check)
    while(True in check):
        first = max(priorities) #3
        minus = 0
        for i in range(len(priorities)):
            if priorities[i] != first: #제일 큰 숫자가 아닐 때
                priorities.append(priorities[i])
                check.append(check[i])
                minus += 1
            elif priorities[i] == first and check[i] == False: #제일 큰 숫자인데 location아닐 때
                cnt += 1
                minus += 1
                break
            elif priorities[i] == first and check[i] == True: #제일 큰 숫자이고 location 일치
                cnt += 1
                return cnt
        for i in range(minus):
            priorities.popleft()
            check.popleft()
