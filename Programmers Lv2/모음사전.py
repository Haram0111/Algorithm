def solution(word):
    wordlist = ['A','E','I','O','U']
    answer = 0
    #5자리 숫자의 경우 1*5*5*5*5 = 625
    #4자리 > 1*5*5*5 = 125
    #3자리 > 1*5*5 = 25
    #2자리 > 1*5 = 5 >> 780
    #1자리 > 1
    #즉 앞자리 A일때 780개를 가진다
    #E는 782번째(1번은 A이므로 1+780)
    #E의 마지막 사전이 782+780이므로 1562이므로 I는 1563이다
    scorelist = [781,156,31,6,1]
    for i in range(len(word)):
        if word[i] == 'A':
            answer += 1
        else:
            answer += wordlist.index(word[i])*scorelist[i] + 1
    return answer