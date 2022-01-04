def solution(n):
    answer = 0
    num_str = str(n)
    num_str.split()
    for i in range(len(num_str)):
        answer += int(num_str[i])
    return answer