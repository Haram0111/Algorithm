import string
def solution(new):

    lst = ["-","_","."]
    alpa = [i for i in string.ascii_lowercase]
    num = [str(i) for i in range(10)]
    
    new = new.lower() #1단계
    new = list(new)
    for i in range(len(new)):#2단계
        if new[i] not in lst and new[i] not in num and new[i] not in alpa:
            new[i] = ""
    new = "".join(new)
    new = list(new)
    #3단계
    for i in range(len(new)-1):
        if new[-i-1] == "." and new[-i-2] == ".":
            new[-i-1] = ""
    new = "".join(new)

    if new[0] == ".": #4단계
        new = new[1:]
    elif new[-1] == ".":
        new = new[:-1]
    if new == "": #5단계
        new += "a"
    if len(new) >= 16: #6단계
        new = new[:15]
    if new[-1] == ".": 
        new = new[:-1]
    if len(new) <= 2: #7단계
        while len(new) < 3:
            new += new[-1]
    return new