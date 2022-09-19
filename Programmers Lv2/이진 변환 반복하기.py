def solution(s):
    z_cnt = 0
    cnt = 0
    while True:
        s = list(s)
        cnt += 1
        length = 0
        for i in s:
            if i == "1":
                length += 1
            else:
                z_cnt += 1
        if length == 1:
            return [cnt, z_cnt]
        result = format(length, 'b')
        s = result
        