def solution(number, k):
    length = len(number) #초기 길이
    answer = '' #정답
    cnt,idx,i = 0,0,0
    if length -k ==1:   return max(number)
    while i <= length and cnt <= k:
        if length - k == len(answer): #99988112(8), 3, 99988(5) 최적으로 구할 수 있음 112를 안돌아도됨
            break
        temp = number[i:i+k-cnt+1]
        try:    idx = temp.index('9')
        except: idx = temp.index(max(temp))
        if idx == 0: #해당 수가 젤 큰수라면
            answer += number[i] #정답에 넣어줌
            i += 1
        else:
            if cnt + idx <= k:
                cnt += idx #해당 숫자를 넘어가고
                i += idx
            else:   cnt+=1
    return answer + number[i+1:]