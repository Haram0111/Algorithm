from collections import deque

def solution(queue1, queue2):
    total_sum = (sum(queue1) + sum(queue2)) // 2 
    que1 = deque(queue1)
    que2 = deque(queue2)
    sum1, sum2 = sum(que1), sum(que2)
    cnt = 0
    if max(que1) > total_sum or max(que2) > total_sum:
        return -1
    for i in range(len(que1)*3):
        cnt += 1
        if sum1 > total_sum:
            temp = que1.popleft()            
            que2.append(temp)
            sum2 += temp
            sum1 -= temp
        elif sum2 > total_sum:
            temp = que2.popleft()            
            que1.append(temp)
            sum1 += temp
            sum2 -= temp
        elif sum1 == sum2:
            return cnt - 1
        if len(que1) == 0 or len(que2) == 0:
            return -1
    return -1