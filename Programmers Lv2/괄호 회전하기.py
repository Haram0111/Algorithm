from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        s.append(s.popleft())
        cnt = 0
        Big = [0,0,0]
        Small = [0,0,0] #소문자가 ), }, ] 개수를 나타내고 소문자가 대문자보다 많아지면 안됨
        for j in s:
            if j == '[':
                Big[0] += 1
            elif j == '{':
                Big[1] += 1
            elif j == '(':
                Big[2] += 1
            elif j == ']':
                Small[0] += 1
                if Big[0] < Small[0]:
                    break
            elif j == '}':
                Small[1] += 1
                if Big[1] < Small[1]:
                    break
            elif j == ')':
                Small[2] += 1
                if Big[2] < Small[2]:
                    break
        for j, k in zip(Big, Small):
            if j !=0 and j == k:
                cnt += 1
            else:
                break
        if cnt == 3:
            answer += 1
    return answer