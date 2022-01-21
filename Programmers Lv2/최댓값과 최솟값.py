def solution(s):
    lst =[]
    s = s.split(" ")
    for i in s:
        lst.append(int(i))
    return f"{min(lst)} {max(lst)}"