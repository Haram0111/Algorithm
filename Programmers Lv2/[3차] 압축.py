from string import ascii_uppercase

def solution(msg):
    Alpa = list(ascii_uppercase)
    msg = list(msg)
    answer = []
    start = 0    
    while True:
        check = msg[start]
        cnt = 0
        while True:
            if check in Alpa:
                cnt += 1
                if start + cnt == len(msg):
                    answer.append(Alpa.index(check) + 1)
                    return answer
                check += msg[start + cnt] #KA                
            else:
                answer.append(Alpa.index(check[:-1]) + 1)
                Alpa.append(check) #KA를 Alpa에 추가
                start += cnt
                break
        if start == len(msg)-1:
            answer.append(Alpa.index(msg[start]) + 1)
            break
    return answer