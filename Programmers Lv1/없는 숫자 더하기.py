def solution(numbers):
    cnt = 0
    numbers.sort()
    for i in range(10):
        if i not in numbers:
            cnt += i
    return cnt