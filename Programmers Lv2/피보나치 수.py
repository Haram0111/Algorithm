def solution(n):
    F = [0,1]
    for i in range(n-1):
        num1 = F[-2]
        num2 = F[-1]
        num3 = num1 + num2 
        F.append(num3)
    return F[-1]%1234567