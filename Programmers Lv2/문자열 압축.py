from math import gcd

def solution(s):
    min_len = len(s)
    for i in range(1,len(s)//2+1): #문자를 끊는 개수 1~문자길이//2
        st = ''
        cnt = 1
        for j in range(len(s)//i): #실제로 문자를 끊어서 개수세기
            if s[j*i:i*j+i] != s[(j+1)*i:i*(j+1)+i]:
                if cnt == 1:
                    st += s[j*i:i*j+i]
                    cnt = 1
                    if len(s[j*i:i*j+i]) != len(s[(j+1)*i:i*(j+1)+i]):
                        st += s[(j+1)*i:i*(j+1)+i]
                else:
                    st += str(cnt) + s[j*i:i*j+i]
                    cnt = 1
                    if len(s[j*i:i*j+i]) != len(s[(j+1)*i:i*(j+1)+i]):
                        st += s[(j+1)*i:i*(j+1)+i]
            elif s[j*i:i*j+i] == s[(j+1)*i:i*(j+1)+i]:
                cnt += 1
        min_len = min(min_len,len(st))
    return min_len