def solution(survey, choices):
    answer = ''
    score = [3,2,1,0,1,2,3]
    arry = ['R','T','C','F','J','M','A','N']
    lst = [0,0,0,0,0,0,0,0]
    for i in range(len(survey)):
        a = list(survey[i])
        if choices[i] > 3:
            lst[arry.index(a[1])] += score[choices[i]-1]
        else:
            lst[arry.index(a[0])] += score[choices[i]-1]
    for i in range(4):
        if lst[2*i] >= lst[2*i + 1]:
            answer += arry[2*i]
        else:
            answer += arry[2*i+1]
    return answer