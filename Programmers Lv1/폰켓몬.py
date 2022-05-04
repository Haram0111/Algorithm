def solution(nums):
    init = len(nums) // 2
    nums = set(nums)
    if init > len(nums):
        return len(nums)
    else:
        return init