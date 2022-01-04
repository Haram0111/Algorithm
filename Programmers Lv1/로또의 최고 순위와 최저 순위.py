def solution(lottos, win_nums):
    answer = []
    zero_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
    price = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                price += 1
    price += zero_cnt
    for i in range(2):
        if price == 6:
            answer.append(1)
        elif price == 5:
            answer.append(2)
        elif price == 4:
            answer.append(3)
        elif price == 3:
            answer.append(4)
        elif price == 2:
            answer.append(5)
        else:
            answer.append(6)
        price -= zero_cnt
    return answer
    