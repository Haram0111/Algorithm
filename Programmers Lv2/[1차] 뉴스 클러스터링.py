from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    lst1 = []
    lst2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a = str1[i] + str1[i+1]
            lst1.append(a)
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b = str2[i] + str2[i+1]
            lst2.append(b)
            
    Counter1 = Counter(lst1)
    Counter2 = Counter(lst2)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)