money = 5000000 #백만원
lst = [31,59,90,120,151,181,212,243,273,304,334,365]
for i in range(365):
    if i in lst:
        money += 800000
add = money * 0.02
money += add
print(money, add)