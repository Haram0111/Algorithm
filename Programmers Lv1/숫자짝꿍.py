def solution(X, Y):
    X_list = [0 for i in range(10)]
    Y_list = [0 for i in range(10)]
    answer = []
    
    for i in X:
        X_list[int(i)] += 1
    for i in Y:
        Y_list[int(i)] += 1
    for i in range(len(X_list)-1,-1,-1):
        number = min(X_list[i], Y_list[i])
        if i == 0 and answer == [] and number != 0:
            return "0"
        if number != 0:
            answer.append(str(i) * number)
    if answer:
        return ''.join(answer)
    return "-1"