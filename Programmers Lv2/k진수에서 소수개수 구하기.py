def Binary(num, k):
    result = ""
    while True:
        a = num % k
        num = num // k
        result += str(a)
        if num < k:
            break
    result += str(num)
    answer = result[::-1]
    return answer

def solution(n, k):
    cnt = 0
    result = Binary(n, k)
    result = result.split("0")
    for i in result:
        if i == '0' or i == "1":
            continue
        if len(i) == 0:
            continue
        prime=True
        for j in range(2,int(int(i)**0.5)+1): # 소수찾기
            if int(i)%j==0:
                prime=False
                break
        if prime:
            cnt+=1
    return cnt
    