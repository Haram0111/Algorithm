def solution(x):
    a = list(str(x))
    a = sum(map(int, a))
    if x % a == 0:
        return True
    else:
        return False