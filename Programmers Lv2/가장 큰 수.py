def solution(numbers):
    numbers_str = [str(num) for num in numbers]                 #1. 사전 값으로 정렬하기
    numbers_str.sort(key=lambda num: num*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교

    return str(int(''.join(numbers_str)))