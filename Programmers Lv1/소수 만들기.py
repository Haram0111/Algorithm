def solution(nums):
    cnt = 0
    lst = []
    for i in nums:
        for j in nums[nums.index(i)+1:]:
            for k in nums[nums.index(j)+1:]:
                num = i+j+k         
                if lst.count(num) == 0:
                    lst.append(num)
    for l in lst:
        div_cnt = 0
        for m in range(1,l+1):
            if l % m == 0:
                div_cnt += 1
        if div_cnt == 2: 
            cnt += 1
    return cnt
#미해결