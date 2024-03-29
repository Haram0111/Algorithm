from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while len(people) > 1:
        if people[0] + people[len(people)-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1
        else:
            people.pop()
            answer += 1
    if len(people) == 1:
        return answer + 1
    else:
        return answer