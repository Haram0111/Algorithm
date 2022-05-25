def solution(s):
    result = ""
    s = list(s)
    st = ["ze","on","tw","th","fo","fi","si","se","ei","ni"]
    num = ["0","1","2","3","4","5","6","7","8","9"]
    print(s)
    for i in range(len(s)-1):
        if s[i] in num:
            result += s[i]
        if s[i]+s[i+1] in st:
            result += num[st.index(s[i]+s[i+1])]
    if s[-1] in num:
        result += s[-1]
    return int(result)