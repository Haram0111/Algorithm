def solution(s, n):
    low_sp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        if s[i].isupper() == True:
            st = s[i].lower()
            num = low_sp.index(st)
            num += n
            if num > 25:
                num -= 26
            s[i] = low_sp[num]
            s[i] = s[i].upper()
        elif s[i].isupper() == False:
            num = low_sp.index(s[i])
            num += n
            if num > 25:
                num -= 26
            s[i] = low_sp[num]
    s = "".join(s)
    return s
#97이 a