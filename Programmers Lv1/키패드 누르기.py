def solution(numbers, hand):
    answer = ''
    keypad = [1,2,3,4,5,6,7,8,9,10,11,12] #0을 11취급
    L , R = [3,0],[3,2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            a, b = 0, 0
            a = i // 3
            if i%3 == 1 or i%3 == 2:
                b = i%3 - 1
            if i%3 == 0:
                b = 2
                a -= 1
            L = [a,b]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            a, b = 0, 0
            a = i // 3
            if i%3 == 1 or i%3 == 2:
                b = i%3 - 1
            if i%3 == 0:
                b = 2
                a -= 1
            R = [a,b]
        else:
            if i == 0:
                i = 11
            a, b = 0, 0
            a = i // 3
            if i%3 == 1 or i%3 == 2:
                b = i%3 - 1
            if i%3 == 0:
                b = 2
                a -= 1 #(a,b)의 형태로 되어 있음
            if abs(a-R[0])+abs(b-R[1]) < abs(a-L[0])+abs(b-L[1]):
                R = [a,b]
                answer += 'R'
            elif abs(a-R[0])+abs(b-R[1]) > abs(a-L[0])+abs(b-L[1]):
                L = [a,b]
                answer += 'L'
            else:
                if hand == 'right':
                    R = [a,b]
                    answer += 'R'
                else:
                    L = [a,b]
                    answer += 'L'
    return answer