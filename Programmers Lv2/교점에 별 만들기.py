def solution(line):
    list2_ = []
    for i in range(len(line)):
        for j in range(i,len(line)):
            if line[i][0] * line[j][1] - line[i][1]*line[j][0] != 0:
                x = (line[i][1]*line[j][2] - line[i][2]*line[j][1]) / (line[i][0] * line[j][1] - line[i][1]*line[j][0])
                y = (line[i][2]*line[j][0] - line[i][0]*line[j][2]) / (line[i][0] * line[j][1] - line[i][1]*line[j][0])
                if int(x) == x and int(y) == y:
                    list2_.append((int(x),int(y)))
    answer = list(set(list2_))

    max_x = -500
    min_x = 500
    max_y = -500
    min_y = 500
    
    for i in range(len(answer)):
        if min_x > answer[i][0]:
            min_x = answer[i][0]
        if max_x < answer[i][0]:
            max_x = answer[i][0]
        if min_y > answer[i][1]:
            min_y = answer[i][1]
        if max_y < answer[i][1]:
            max_y = answer[i][1]
    
    dot_x = 0
    dot_y = 0
    
    if min_x == max_x:
        dot_x = 1
    else:
        dot_x = abs(min_x) + abs(max_x) + 1
        
    if min_y == max_y:
        dot_y = 1
    else:
        dot_y = abs(min_y) + abs(max_y) + 1
        
    dot_answer = [ ["." for x in range(dot_x)] for y in range(dot_y)]
    ans = []
    if dot_y == 1: 
        for i in range(len(answer)):
            dot_answer[0][answer[i][0]+max_y] = '*'
        for i in range(len(dot_answer)):
            ans.append("".join(dot_answer[i]))
    else:
        for i in range(len(answer)):
            dot_answer[-(answer[i][1]+min_x)][-(answer[i][0]-max_y)] = '*'
        for i in range(len(dot_answer)):
            ans.append(''.join(dot_answer[i]))
    return ans
