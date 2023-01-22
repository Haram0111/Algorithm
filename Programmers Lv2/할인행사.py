def solution(want, number, discount):
    dic = {}
    answer = 0
    for i in range(len(discount)):
        for k in range(len(want)):
            dic[want[k]] = 0
        if i + 10 <= len(discount) - 1:
            for j in range(10):
                if discount[i+j] in dic:
                    dic[discount[i+j]] += 1
        else:
            for j in range(len(discount) - i):
                if discount[i+j] in dic:
                    dic[discount[i+j]] += 1
        result = list(dic.values())
        count = 0
        for m in range(len(number)):
            if number[m] == result[m]:
                count += 1
        if count == len(number):
            answer += 1
    return answer
            