nums = [1,2,7,6,4]
cnt = 0
lst = []
for i, j, k in nums:
    num = i+j+k            
    if lst.count(num) == 0: #중복체크
        lst.append(num)
    print(lst)
for l in lst:#나눌 숫자
    div_cnt = 0
    for m in range(1,len(lst)):#나누는 숫자
        if lst[l] % m == 0:
            div_cnt += 1
    if div_cnt == 1:
        cnt += 1
print(cnt)