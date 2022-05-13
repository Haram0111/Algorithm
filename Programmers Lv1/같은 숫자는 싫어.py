def solution(arr):
    answer = []
    start = arr[0]
    answer.append(arr[0])
    if len(arr) > 1:
        for i in range(1,len(arr)):
            if start != arr[i]:
                start = arr[i]
                answer.append(start)
    return answer