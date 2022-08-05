def solution(people, limit):
    people.sort()
    answer = 1
    weight = 0
    for i in range(len(people)):
        if people[i] > limit // 2:
            answer += len(people) - i
            print(weight, answer, people[i], i)
            return answer
        else:
            if weight + people[i] > limit:
                weight = people[i]
                answer += 1
            else:
                weight += people[i]
            print(weight, answer)