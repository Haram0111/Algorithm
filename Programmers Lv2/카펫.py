def solution(brown, yellow):
    answer = []
    for i in range(1,brown//2):
        part = brown
        part -= i * 2 #i가 가로 길이
        col = part // 2 #col이 가운데 세로 길이
        if i < col + 2:
            continue
        if (i-2) * col == yellow:
            answer.append(i)
            answer.append(col+2)
            return answer